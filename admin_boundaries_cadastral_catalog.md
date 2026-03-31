# Administrative Boundaries, Cadastral, and Base Map Data Sources

## Global

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| GADM | gadm.org | Global | Admin boundaries levels 0-5 | Country to sub-municipal | Free (academic); commercial license needed | No | Admin polygons all countries | GeoPackage/SHP/KMZ formats |
| Natural Earth | naturalearthdata.com | Global | Admin + physical + cultural | 1:10m / 1:50m / 1:110m | Free, public domain | No | Countries, states, coastlines, rivers, lakes | SHP format |
| geoBoundaries | geoboundaries.org | Global | Admin boundaries levels 0-5 | Country to sub-municipal | Free, CC-BY 4.0 | REST API (api.geoboundaries.org) | Standardized admin boundaries | GeoJSON format |
| UN SALB | salb.un.org | Global | Admin boundaries levels 0-2 | Country to district | Free | No | UN-endorsed admin boundaries | SHP format |
| DIVA-GIS | diva-gis.org/gdata | Global | Country datasets | Varies | Free | No | Admin, roads, elevation, population | Older data, not regularly updated |
| HDX / OCHA | data.humdata.org | Global | Humanitarian data | Varies | Free | CKAN API | COD admin boundaries, population | Focus on humanitarian contexts |
| MapCruzin | mapcruzin.com | Global | Aggregated geospatial data | Varies | Free | No | Admin, roads, land use | Some datasets outdated |
| OSM Geofabrik | download.geofabrik.de | Global | Street-level vector data | Street level | Free, ODbL | Bulk download | Roads, buildings, admin, POIs | PBF/SHP formats |
| OSM BBBike | extract.bbbike.org | Global | Custom OSM extracts | Street level | Free | No (web tool) | Custom area extracts | Multiple output formats |
| OSM Overpass API | overpass-api.de | Global | Real-time OSM queries | Street level | Free | Overpass QL API | Any OSM feature via query | Rate-limited; real-time data |
| GeoNames | geonames.org | Global | 12M+ place names | Point locations | Free, CC-BY 4.0 | REST API | Place names, postal codes, elevations | 30k requests/day free tier |
| WMO OSCAR | oscar.wmo.int | Global | Weather station network | Station locations | Free | REST API | Station metadata, capabilities | Observing Systems Capability Analysis |
| Overture Maps | overturemaps.org | Global | Buildings, places, transport, admin | Building-level | Free, CDLA | S3/Azure bulk | Buildings, places, transport, admin divisions | GeoParquet format |
| OpenAddresses | openaddresses.io | Global (partial) | Address points | Address level | Free | No | Addresses with coordinates | Coverage varies by country |
| Who's on First | whosonfirst.org | Global | Place gazetteer | Multi-scale | Free, CC-BY 4.0 | REST API | Hierarchical place data | Mapzen-originated project |
| FAO GAUL | data.apps.fao.org | Global | Admin boundaries levels 0-2 | Country to district | Free | WMS | Global admin unit layers | UN-FAO maintained |
| H3 Uber | h3geo.org | Global | Hexagonal grid system | Multi-resolution (0-15) | Free, Apache 2.0 | Library (not web API) | Hierarchical hexagonal index | Grid system, not data per se |

## European

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| Eurostat GISCO | ec.europa.eu/eurostat/web/gisco | Europe | Statistical boundaries + grids | NUTS 0-3, LAU, communes | Free | REST / WMS / WFS | NUTS, LAU, communes, grids, coastlines | SHP/GeoJSON/TopoJSON formats |
| INSPIRE Geoportal | inspire-geoportal.ec.europa.eu | Europe | 34 INSPIRE themes | Varies by provider | Free (mostly) | WMS / WFS / ATOM | Cadastral parcels, addresses, hydro, transport | Federated across member states |
| EuroGeographics | eurogeographics.org | Europe | Reference mapping | 1:100k to 1:1M | Commercial (EuroGlobalMap open) | WMS | EuroBoundaryMap, EuroRegionalMap, EuroGlobalMap | National mapping agencies consortium |
| EEA Reference Grids | eea.europa.eu | Europe | ETRS89-LAEA grids | 1km / 10km / 100km | Free | No | Reference grids for reporting | SHP format |

## National - Hungary

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| Lechner Tudaszkozpont | lfrankl.lechnerkozpont.hu | Hungary | Cadastral, topo, ortho | Parcel to 1:100k | Freemium | WMS / WFS | Cadastral map, topographic maps, orthophotos | Core Hungarian geospatial hub |
| NATer | map.mbfsz.gov.hu/nater | Hungary | Environmental, geological | Varies | Free | WMS | Soil, geology, groundwater, climate risk | National Environmental Information System |
| e-kozmu | e-kozmu.hu | Hungary | Utility cadastre | Utility level | Regulated | Regulated API | Water, gas, electric, telecom networks | Access regulated by law |
| KSH | ksh.hu/stadat + teir.hu | Hungary | Statistical boundaries | Settlement level | Free | Partial API | Census tracts, settlement boundaries | TEIR for spatial statistics |
| Geoshop Lechner | geoshop.lfrankl.hu | Hungary | Cadastral detail | Parcel level | Commercial | No | Detailed cadastral parcel data | Paid downloads |

## National - Other Countries

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| Netherlands PDOK | pdok.nl | Netherlands | All reference data | Parcel level | Free | WMS / WFS / WCS / OGC API | BAG, BRT, cadastral parcels, AHN | Comprehensive Dutch SDI |
| France Cadastre | cadastre.gouv.fr + data.gouv.fr | France | Cadastral parcels | Parcel level | Free | WMS / WFS | Cadastral parcels, Plan Cadastral Informatise | Open data since 2017 |
| Germany BKG | gdz.bkg.bund.de | Germany | Admin, topo, geodetic | Varies | Free | WMS / WFS | VG250 admin, Digital Landscape Model | Federal Agency for Cartography |
| Austria basemap.at | basemap.at + data.gv.at | Austria | Reference maps | Multi-scale | Free, CC-BY 4.0 | WMTS | Basemap, orthophotos, surface model | Open Government Data |
| Czech Republic CUZK | cuzk.cz | Czech Republic | Cadastral, topo | Parcel level | Free viewing / paid bulk | WMS / WFS | RUIAN, cadastral maps, ZABAGED | Czech Office for Surveying |
| Spain INSPIRE Cadastre | sedecatastro.gob.es | Spain | Cadastral parcels | Parcel level | Free | WMS / WFS / ATOM | Cadastral parcels, buildings | INSPIRE-compliant |
| Poland GUGiK | mapy.geoportal.gov.pl | Poland | Cadastral, topo, ortho | Parcel level | Free | WMS / WFS / WMTS | EGiB cadastre, BDOT topography, orthophotos | Geoportal.gov.pl |
| Romania ANCPI | geoportal.ancpi.ro | Romania | Cadastral | Parcel level | Partial | WMS | Cadastral maps, INSPIRE parcels | Ongoing digitization |
| Slovakia UGKK | geoportal.sk | Slovakia | ZBGIS cadastral, topo | Parcel level | Free viewing | WMS / WFS | ZBGIS, cadastral portal | Slovak Geodesy Authority |
| Croatia DGU | geoportal.dgu.hr | Croatia | Cadastral, topo | Parcel level | Free viewing | WMS | Digital cadastral map, topographic data | State Geodetic Administration |
| Switzerland swisstopo | swisstopo.admin.ch | Switzerland | All reference data | Multi-scale | Free since 2021 | REST / WMS / WMTS | swissBUILDINGS3D, swissTLM3D, ALTI3D | Comprehensive open geodata |
| UK OS Data Hub | osdatahub.os.uk | UK | Admin, topo | Multi-scale | Freemium | REST / WMS / WFS | OS MasterMap, Boundary-Line, OpenMap Local | Free tier with limits |
| Finland NLS | maanmittauslaitos.fi | Finland | Topo, cadastral | Multi-scale | Free, CC-BY 4.0 | WMS / WFS / OGC API | Topographic database, cadastral index map | National Land Survey |
| Sweden Lantmateriet | lantmateriet.se | Sweden | Cadastral, topo | Parcel level | Free / paid | WMS / WFS | Fastighetskartan, property register | Lantmateriet open data |
| Norway Geonorge | geonorge.no | Norway | All reference data | Multi-scale | Free, CC-BY 4.0 | WMS / WFS / WCS / OGC API | N50 topo, cadastral, admin boundaries | National geoportal |

## Place Names and Grid Systems

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| OpenGeoDB | opengeodb.org | DACH | Postal codes, place names | Postal code level | Free | No | DE/AT/CH postal code polygons | MySQL dump format |
| Eurostat NUTS/LAU | ec.europa.eu/eurostat/web/nuts | Europe | Statistical regions | NUTS 0-3, LAU | Free | REST | NUTS classification, LAU correspondences | Updated every 3 years |
| ISO 3166 | iso.org | Global | Country/subdivision codes | Country + subdivision | Free list / paid full | No | ISO 3166-1 (countries), 3166-2 (subdivisions) | Standard country codes |
| EEA ETRS89-LAEA Grid | eea.europa.eu | Europe | Reference grid | 1km / 10km / 100km | Free | No | Standard European reporting grid | SHP format, EPSG:3035 |
