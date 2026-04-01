"""
Resource constants for the Dataset Cadaster plugin.
"""

# Default URL to fetch datasets.json from GitHub
DEFAULT_DATASETS_URL = (
    "https://raw.githubusercontent.com/dataset-cadaster/DatasetCadaster/main/datasets.json"
)

# Known WMS endpoints mapped by dataset ID
WMS_ENDPOINTS = {
    "copernicus-dem-30": "https://copernicus-dem-30m.s3.eu-central-1.amazonaws.com",
    "corine-land-cover": "https://image.discomap.eea.europa.eu/arcgis/services/Corine/CLC2018_WM/MapServer/WMSServer",
    "sentinel-2-ab": "https://services.sentinel-hub.com/ogc/wms/",
    "eurostat-gisco": "https://gisco-services.ec.europa.eu/distribution/v2/nuts/geojson/",
    "copernicus-imperviousness-hrl": "https://image.discomap.eea.europa.eu/arcgis/services/GioLand/HRL_Imperviousness_Density_2018/MapServer/WMSServer",
    "eea-air-quality-portal": "https://discomap.eea.europa.eu/map/fme/AirQualityExport.htm",
    "natura-2000-marine": "https://bio.discomap.eea.europa.eu/arcgis/services/Natura2000/Natura2000End2021_Bioregion/MapServer/WMSServer",
    "gebco": "https://www.gebco.net/data_and_products/gebco_web_services/web_map_service/mapserv",
    "emodnet-bathymetry": "https://ows.emodnet-bathymetry.eu/wms",
    "emodnet-biology": "https://geo.vliz.be/geoserver/Emodnetbio/wms",
    "isric-soilgrids": "https://maps.isric.org/mapserv?map=/map/soilgrids.map",
    "ghsl-ghs-pop": "https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/",
    "urban-atlas-copernicus": "https://image.discomap.eea.europa.eu/arcgis/services/UrbanAtlas/UA2018/MapServer/WMSServer",
    "osm-overpass": "https://overpass-api.de/api/interpreter",
    "esa-worldcover": "https://services.terrascope.be/wms/v2",
    "egms": "https://egms.land.copernicus.eu/",
    "copernicus-marine-cmems": "https://nrt.cmems-du.eu/thredds/wms/",
    "one-geology": "https://onegeology-geonetwork.brgm.fr/geonetwork/srv/eng/csw",
}

# Known WFS endpoints mapped by dataset ID
WFS_ENDPOINTS = {
    "emodnet-bathymetry": "https://ows.emodnet-bathymetry.eu/wfs",
    "emodnet-biology": "https://geo.vliz.be/geoserver/Emodnetbio/wfs",
    "eurostat-gisco": "https://gisco-services.ec.europa.eu/distribution/v2/nuts/geojson/",
    "natura-2000-marine": "https://bio.discomap.eea.europa.eu/arcgis/services/Natura2000/Natura2000End2021_Bioregion/MapServer/WFSServer",
    "isric-soilgrids": "https://maps.isric.org/mapserv?map=/map/soilgrids.map",
    "urban-atlas-copernicus": "https://image.discomap.eea.europa.eu/arcgis/services/UrbanAtlas/UA2018/MapServer/WFSServer",
}

# Category display names
CATEGORY_LABELS = {
    "admin-boundaries": "Admin Boundaries",
    "air-quality": "Air Quality",
    "biosphere-ecology": "Biosphere & Ecology",
    "climate-weather": "Climate & Weather",
    "data-platform": "Data Platforms",
    "dem-elevation": "DEM & Elevation",
    "geodesy-insar": "Geodesy & InSAR",
    "geology-geophysics": "Geology & Geophysics",
    "hydrology": "Hydrology",
    "land-use-land-cover": "Land Use / Land Cover",
    "ocean-marine": "Ocean & Marine",
    "population-urban": "Population & Urban",
    "satellite-eo": "Satellite & EO",
    "soil": "Soil",
}
