"""
Dataset Cadaster QGIS Plugin - Dialog with search, filter, and layer-add functionality.
"""

import json
import os
import webbrowser
from urllib.request import urlopen, Request
from urllib.error import URLError

from qgis.PyQt.QtCore import Qt, QThread, pyqtSignal, QUrl
from qgis.PyQt.QtGui import QFont, QColor, QDesktopServices
from qgis.PyQt.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDialog,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QSplitter,
    QTableWidget,
    QTableWidgetItem,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)
from qgis.core import QgsProject, QgsRasterLayer, QgsVectorLayer

from .resources import (
    CATEGORY_LABELS,
    DEFAULT_DATASETS_URL,
    WFS_ENDPOINTS,
    WMS_ENDPOINTS,
)


# ---------------------------------------------------------------------------
# Background fetcher
# ---------------------------------------------------------------------------
class DatasetFetcher(QThread):
    """Fetch datasets.json in a background thread."""

    finished = pyqtSignal(list)
    error = pyqtSignal(str)

    def __init__(self, url, parent=None):
        super().__init__(parent)
        self.url = url

    def run(self):
        try:
            req = Request(self.url, headers={"User-Agent": "QGIS-DatasetCadaster/1.0"})
            with urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            self.finished.emit(data)
        except Exception as exc:
            self.error.emit(str(exc))


# ---------------------------------------------------------------------------
# Main dialog
# ---------------------------------------------------------------------------
class DatasetCadasterDialog(QDialog):
    """Main browser dialog for the Dataset Cadaster plugin."""

    COLUMNS = ["Name", "Category", "Scope", "Cost", "API", "Resolution"]
    COL_NAME = 0
    COL_CATEGORY = 1
    COL_SCOPE = 2
    COL_COST = 3
    COL_API = 4
    COL_RESOLUTION = 5

    def __init__(self, iface, plugin_dir, parent=None):
        super().__init__(parent or iface.mainWindow())
        self.iface = iface
        self.plugin_dir = plugin_dir
        self.datasets = []          # full list
        self.filtered = []          # currently visible
        self.selected_dataset = None
        self.fetcher = None

        self.setWindowTitle("Dataset Cadaster")
        self.setMinimumSize(960, 640)
        self.resize(1100, 720)
        self._build_ui()
        self._load_data()

    # ------------------------------------------------------------------
    # UI construction
    # ------------------------------------------------------------------
    def _build_ui(self):
        root = QVBoxLayout(self)

        # --- top bar: search + refresh ---
        top = QHBoxLayout()
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search datasets by name, description, tags...")
        self.search_box.setClearButtonEnabled(True)
        self.search_box.textChanged.connect(self._apply_filters)
        top.addWidget(self.search_box, 1)

        self.btn_refresh = QPushButton("Refresh Data")
        self.btn_refresh.clicked.connect(self._fetch_remote)
        top.addWidget(self.btn_refresh)
        root.addLayout(top)

        # --- filter bar ---
        filt = QHBoxLayout()

        filt.addWidget(QLabel("Category:"))
        self.combo_category = QComboBox()
        self.combo_category.addItem("All", "")
        for key in sorted(CATEGORY_LABELS):
            self.combo_category.addItem(CATEGORY_LABELS[key], key)
        self.combo_category.currentIndexChanged.connect(self._apply_filters)
        filt.addWidget(self.combo_category)

        filt.addWidget(QLabel("Scope:"))
        self.combo_scope = QComboBox()
        for label, val in [("All", ""), ("Global", "global"), ("Europe", "europe"), ("National", "national")]:
            self.combo_scope.addItem(label, val)
        self.combo_scope.currentIndexChanged.connect(self._apply_filters)
        filt.addWidget(self.combo_scope)

        filt.addWidget(QLabel("Cost:"))
        self.combo_cost = QComboBox()
        for label, val in [("All", ""), ("Free", "free"), ("Freemium", "freemium"), ("Commercial", "commercial")]:
            self.combo_cost.addItem(label, val)
        self.combo_cost.currentIndexChanged.connect(self._apply_filters)
        filt.addWidget(self.combo_cost)

        self.chk_api = QCheckBox("API only")
        self.chk_api.stateChanged.connect(self._apply_filters)
        filt.addWidget(self.chk_api)

        self.lbl_count = QLabel("")
        self.lbl_count.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        filt.addWidget(self.lbl_count)

        root.addLayout(filt)

        # --- splitter: table + detail ---
        splitter = QSplitter(Qt.Vertical)

        # results table
        self.table = QTableWidget()
        self.table.setColumnCount(len(self.COLUMNS))
        self.table.setHorizontalHeaderLabels(self.COLUMNS)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.setSortingEnabled(True)
        header = self.table.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(self.COL_NAME, QHeaderView.Stretch)
        for c in range(1, len(self.COLUMNS)):
            header.setSectionResizeMode(c, QHeaderView.ResizeToContents)
        self.table.currentCellChanged.connect(self._on_selection_changed)
        splitter.addWidget(self.table)

        # detail panel
        detail_widget = QWidget()
        detail_layout = QVBoxLayout(detail_widget)
        detail_layout.setContentsMargins(4, 4, 4, 4)

        self.detail_browser = QTextBrowser()
        self.detail_browser.setOpenExternalLinks(True)
        self.detail_browser.setMinimumHeight(120)
        detail_layout.addWidget(self.detail_browser)

        # action buttons
        btn_bar = QHBoxLayout()
        self.btn_open = QPushButton("Open in Browser")
        self.btn_open.clicked.connect(self._open_in_browser)
        btn_bar.addWidget(self.btn_open)

        self.btn_wms = QPushButton("Add WMS Layer")
        self.btn_wms.clicked.connect(self._add_wms)
        btn_bar.addWidget(self.btn_wms)

        self.btn_wfs = QPushButton("Add WFS Layer")
        self.btn_wfs.clicked.connect(self._add_wfs)
        btn_bar.addWidget(self.btn_wfs)

        self.btn_copy = QPushButton("Copy URL")
        self.btn_copy.clicked.connect(self._copy_url)
        btn_bar.addWidget(self.btn_copy)

        btn_bar.addStretch()
        detail_layout.addLayout(btn_bar)
        splitter.addWidget(detail_widget)

        splitter.setStretchFactor(0, 3)
        splitter.setStretchFactor(1, 1)
        root.addWidget(splitter)

        self._update_buttons()

    # ------------------------------------------------------------------
    # Data loading
    # ------------------------------------------------------------------
    def _cache_path(self):
        return os.path.join(self.plugin_dir, "datasets_cache.json")

    def _load_data(self):
        """Load from local cache first, then attempt remote fetch."""
        cache = self._cache_path()
        if os.path.exists(cache):
            try:
                with open(cache, "r", encoding="utf-8") as f:
                    self.datasets = json.load(f)
                self._apply_filters()
                return
            except Exception:
                pass

        # Try the bundled datasets.json shipped alongside the plugin
        bundled = os.path.join(self.plugin_dir, "datasets.json")
        if os.path.exists(bundled):
            try:
                with open(bundled, "r", encoding="utf-8") as f:
                    self.datasets = json.load(f)
                self._apply_filters()
                return
            except Exception:
                pass

        # Nothing local -- fetch from remote
        self._fetch_remote()

    def _fetch_remote(self):
        self.btn_refresh.setEnabled(False)
        self.btn_refresh.setText("Fetching...")
        self.fetcher = DatasetFetcher(DEFAULT_DATASETS_URL, self)
        self.fetcher.finished.connect(self._on_fetch_finished)
        self.fetcher.error.connect(self._on_fetch_error)
        self.fetcher.start()

    def _on_fetch_finished(self, data):
        self.datasets = data
        # save cache
        try:
            with open(self._cache_path(), "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False)
        except Exception:
            pass
        self._apply_filters()
        self.btn_refresh.setEnabled(True)
        self.btn_refresh.setText("Refresh Data")
        self.iface.messageBar().pushSuccess(
            "Dataset Cadaster", f"Loaded {len(data)} datasets from remote."
        )

    def _on_fetch_error(self, msg):
        self.btn_refresh.setEnabled(True)
        self.btn_refresh.setText("Refresh Data")
        if not self.datasets:
            QMessageBox.warning(
                self,
                "Dataset Cadaster",
                f"Could not fetch datasets and no local cache found.\n\n{msg}\n\n"
                "Copy datasets.json into the plugin directory or check the URL.",
            )
        else:
            self.iface.messageBar().pushWarning(
                "Dataset Cadaster", f"Remote fetch failed (using cache): {msg}"
            )

    # ------------------------------------------------------------------
    # Filtering
    # ------------------------------------------------------------------
    def _apply_filters(self):
        query = self.search_box.text().strip().lower()
        cat = self.combo_category.currentData()
        scope = self.combo_scope.currentData()
        cost = self.combo_cost.currentData()
        api_only = self.chk_api.isChecked()

        results = []
        for ds in self.datasets:
            if cat and ds.get("category", "") != cat:
                continue
            if scope and ds.get("scope", "") != scope:
                continue
            if cost and ds.get("cost", "") != cost:
                continue
            if api_only and not ds.get("apiSupport", False):
                continue
            if query:
                searchable = " ".join([
                    ds.get("name", ""),
                    ds.get("description", ""),
                    ds.get("category", ""),
                    ds.get("operator", ""),
                    " ".join(ds.get("tags", [])),
                ]).lower()
                if not all(tok in searchable for tok in query.split()):
                    continue
            results.append(ds)

        self.filtered = results
        self._populate_table()

    def _populate_table(self):
        self.table.setSortingEnabled(False)
        self.table.setRowCount(len(self.filtered))
        for row, ds in enumerate(self.filtered):
            self.table.setItem(row, self.COL_NAME, QTableWidgetItem(ds.get("name", "")))
            cat_key = ds.get("category", "")
            self.table.setItem(row, self.COL_CATEGORY, QTableWidgetItem(CATEGORY_LABELS.get(cat_key, cat_key)))
            self.table.setItem(row, self.COL_SCOPE, QTableWidgetItem((ds.get("scope") or "").title()))
            self.table.setItem(row, self.COL_COST, QTableWidgetItem((ds.get("cost") or "").title()))
            api_text = ds.get("apiProtocol", "") if ds.get("apiSupport") else ""
            self.table.setItem(row, self.COL_API, QTableWidgetItem(api_text or ("Yes" if ds.get("apiSupport") else "")))
            self.table.setItem(row, self.COL_RESOLUTION, QTableWidgetItem(ds.get("spatialResolution", "")))
        self.table.setSortingEnabled(True)
        self.lbl_count.setText(f"{len(self.filtered)} / {len(self.datasets)} datasets")
        self._update_detail(None)

    # ------------------------------------------------------------------
    # Selection & detail
    # ------------------------------------------------------------------
    def _on_selection_changed(self, row, col, prev_row, prev_col):
        if 0 <= row < len(self.filtered):
            # We need to map from the visual (sorted) row to the dataset.
            name_item = self.table.item(row, self.COL_NAME)
            if name_item:
                name = name_item.text()
                ds = next((d for d in self.filtered if d.get("name") == name), None)
                self._update_detail(ds)
        else:
            self._update_detail(None)

    def _update_detail(self, ds):
        self.selected_dataset = ds
        self._update_buttons()
        if ds is None:
            self.detail_browser.setHtml("<i>Select a dataset to see details.</i>")
            return

        ds_id = ds.get("id", "")
        has_wms = ds_id in WMS_ENDPOINTS
        has_wfs = ds_id in WFS_ENDPOINTS

        tags_html = " ".join(
            f'<span style="background:#e8f4f8;padding:1px 6px;border-radius:3px;font-size:11px;">{t}</span>'
            for t in ds.get("tags", [])
        )

        service_badges = ""
        if has_wms:
            service_badges += ' <span style="background:#27ae60;color:white;padding:2px 6px;border-radius:3px;font-size:11px;font-weight:bold;">WMS</span>'
        if has_wfs:
            service_badges += ' <span style="background:#2980b9;color:white;padding:2px 6px;border-radius:3px;font-size:11px;font-weight:bold;">WFS</span>'

        html = f"""
        <h3 style="margin:2px 0;">{ds.get('name', '')}{service_badges}</h3>
        <p style="margin:2px 0;">{ds.get('description', '')}</p>
        <table style="font-size:12px;">
        <tr><td><b>Operator:</b></td><td>{ds.get('operator', 'N/A')}</td>
            <td style="padding-left:20px;"><b>License:</b></td><td>{ds.get('license', 'N/A')}</td></tr>
        <tr><td><b>Data type:</b></td><td>{ds.get('dataType', 'N/A')}</td>
            <td style="padding-left:20px;"><b>Formats:</b></td><td>{ds.get('formats', 'N/A')}</td></tr>
        <tr><td><b>Spatial res.:</b></td><td>{ds.get('spatialResolution', 'N/A')}</td>
            <td style="padding-left:20px;"><b>Temporal res.:</b></td><td>{ds.get('temporalResolution', 'N/A')}</td></tr>
        <tr><td><b>Coverage:</b></td><td>{ds.get('temporalCoverage', 'N/A')}</td>
            <td style="padding-left:20px;"><b>Country:</b></td><td>{ds.get('country') or 'N/A'}</td></tr>
        </table>
        <p style="margin:4px 0;">URL: <a href="{ds.get('url', '')}">{ds.get('url', '')}</a></p>
        <p style="margin:2px 0;">{tags_html}</p>
        """
        self.detail_browser.setHtml(html)

    def _update_buttons(self):
        has_sel = self.selected_dataset is not None
        self.btn_open.setEnabled(has_sel)
        self.btn_copy.setEnabled(has_sel)

        ds_id = self.selected_dataset.get("id", "") if has_sel else ""
        self.btn_wms.setEnabled(ds_id in WMS_ENDPOINTS)
        self.btn_wfs.setEnabled(ds_id in WFS_ENDPOINTS)

    # ------------------------------------------------------------------
    # Actions
    # ------------------------------------------------------------------
    def _open_in_browser(self):
        if self.selected_dataset:
            url = self.selected_dataset.get("url", "")
            if url:
                QDesktopServices.openUrl(QUrl(url))

    def _copy_url(self):
        if self.selected_dataset:
            url = self.selected_dataset.get("url", "")
            if url:
                QApplication.clipboard().setText(url)
                self.iface.messageBar().pushInfo("Dataset Cadaster", f"URL copied: {url}")

    def _add_wms(self):
        if not self.selected_dataset:
            return
        ds_id = self.selected_dataset.get("id", "")
        wms_url = WMS_ENDPOINTS.get(ds_id)
        if not wms_url:
            QMessageBox.information(self, "Dataset Cadaster", "No known WMS endpoint for this dataset.")
            return
        name = self.selected_dataset.get("name", ds_id)
        uri = f"url={wms_url}&layers=&styles=&format=image/png&crs=EPSG:4326"
        layer = QgsRasterLayer(uri, name, "wms")
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
            self.iface.messageBar().pushSuccess("Dataset Cadaster", f"WMS layer added: {name}")
        else:
            QMessageBox.warning(
                self,
                "Dataset Cadaster",
                f"Could not create a valid WMS layer from:\n{wms_url}\n\n"
                "The service may require additional parameters (layer name, API key, etc.). "
                "You can try connecting manually via the QGIS Data Source Manager.",
            )

    def _add_wfs(self):
        if not self.selected_dataset:
            return
        ds_id = self.selected_dataset.get("id", "")
        wfs_url = WFS_ENDPOINTS.get(ds_id)
        if not wfs_url:
            QMessageBox.information(self, "Dataset Cadaster", "No known WFS endpoint for this dataset.")
            return
        name = self.selected_dataset.get("name", ds_id)
        uri = f"url={wfs_url}&version=2.0.0"
        layer = QgsVectorLayer(uri, name, "WFS")
        if layer.isValid():
            QgsProject.instance().addMapLayer(layer)
            self.iface.messageBar().pushSuccess("Dataset Cadaster", f"WFS layer added: {name}")
        else:
            QMessageBox.warning(
                self,
                "Dataset Cadaster",
                f"Could not create a valid WFS layer from:\n{wfs_url}\n\n"
                "The service may require a specific layer/typename parameter. "
                "You can try connecting manually via the QGIS Data Source Manager.",
            )
