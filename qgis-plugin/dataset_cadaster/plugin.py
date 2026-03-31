"""
Dataset Cadaster QGIS Plugin - Main plugin class.
"""

import os
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction


class DatasetCadasterPlugin:
    """Main plugin class that integrates with the QGIS interface."""

    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        self.action = None
        self.dialog = None

    def initGui(self):
        """Called when the plugin is loaded into QGIS."""
        icon_path = os.path.join(self.plugin_dir, "icon.png")
        if not os.path.exists(icon_path):
            icon_path = os.path.join(self.plugin_dir, "icon.svg")

        icon = QIcon(icon_path)
        self.action = QAction(icon, "Dataset Cadaster", self.iface.mainWindow())
        self.action.setStatusTip("Browse geospatial data sources and add WMS/WFS layers")
        self.action.triggered.connect(self.run)

        # Add to Web menu and toolbar
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToWebMenu("Dataset Cadaster", self.action)

    def unload(self):
        """Called when the plugin is unloaded from QGIS."""
        self.iface.removePluginWebMenu("Dataset Cadaster", self.action)
        self.iface.removeToolBarIcon(self.action)
        if self.dialog is not None:
            self.dialog.close()
            self.dialog = None

    def run(self):
        """Open the Dataset Cadaster dialog."""
        # Lazy import so the heavy dialog module loads only on first click
        from .dialog import DatasetCadasterDialog

        if self.dialog is None:
            self.dialog = DatasetCadasterDialog(self.iface, self.plugin_dir)
        self.dialog.show()
        self.dialog.raise_()
        self.dialog.activateWindow()
