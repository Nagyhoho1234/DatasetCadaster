"""
Dataset Cadaster QGIS Plugin
Browse 388+ geospatial data sources and add WMS/WFS layers to your project.
"""


def classFactory(iface):
    """Load the DatasetCadasterPlugin class.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    from .plugin import DatasetCadasterPlugin
    return DatasetCadasterPlugin(iface)
