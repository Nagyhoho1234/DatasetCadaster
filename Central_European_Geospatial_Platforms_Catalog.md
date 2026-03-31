# Central European Geospatial & Environmental Data Platforms Catalog

*Compiled: 2026-03-31*

---

## HUNGARY

### National Mapping & Geoportals

| Platform | URL | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|
| Lechner Tudaskozpont (Geoshop) | https://geoshop.hu/ | Mapping, orthofotos, DEM, DSM, cadastre | 20 cm ortho, 0.5-5 m DEM | Freemium (some free, most paid) | Yes - WMS/WMTS | Orthophotos (2000-present), DDM (Digital Terrain Model), DFM (Digital Surface Model), topographic maps, cadastral maps | EOV + WGS84. Since 2016: 3-year ortho cycle. 24/7 webshop. Hungarian/English |
| NTA (Nemzeti Terinformatikai Alapterkep) | https://nta.lechnerkozpont.hu/ | Unified base map service | Varies by layer | Free (gov), Freemium (commercial) | Yes - WMTS | Admin boundaries, buildings, transport, water, land cover, nature conservation - 400+ layers in 8 thematic groups | Free registration required. WMTS free for municipalities/state bodies |
| Fentrol.hu (Aerial Photo Archive) | https://www.fentrol.hu/ | Historical aerial photographs | Varies | Freemium | No (web viewer) | 272,000+ aerial photos from 1959-2008, continuously expanding | Former FOMI archive. ~10,000 new images/semester |
| Foldhivatal (Land Registry Portal) | https://foldhivatal.hu/ | Cadastral data | Parcel-level | Freemium | Yes - TAKARNET system | Cadastral maps, ownership data, land registry extracts | TAKARNET online since 2003. Registered users only for full access |

### Climate & Meteorology

| Platform | URL | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|
| HungaroMet / OMSZ (odp.met.hu) | https://odp.met.hu/ | Meteorological, climate | Station-based + gridded | Free | Partial (FTP/HTTP download, API coming via RODEO project) | Synoptic obs, climate normals, radar, model forecasts, HuClim database | CC-BY-SA license. Open since 2021-01-01. CSV/NetCDF formats |
| NATer (Nat. Adaptation GeoInfo System) | https://nater.mbfsz.gov.hu/ | Climate adaptation, vulnerability | Settlement/district/county | Free | No (web viewer) | Climate projections, demographics, ecosystem services, heat wave data, forestry, energy | Now operated by HungaroMet. Map viewer at map.hugeo.hu/nater/ |

### Geology & Mining

| Platform | URL | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|
| MBFSZ/SZTFH Map Server | https://map.mbfsz.gov.hu/ | Geological, geothermal, hydrogeological | 1:100k - 1:500k | Free | Yes - WMS/WFS, REST API | Geological maps, borehole data, geothermal isotherms (OGRe platform), mineral resources, seismicity | OGC-compliant. INSPIRE metadata at geonetwork.geoservices.hu |
| SZTFH INSPIRE Catalogue | https://geonetwork.geoservices.hu/geonetwork/ | Metadata catalogue | N/A | Free | Yes - CSW | INSPIRE-compliant metadata for all MBFSZ/SZTFH datasets | Standard INSPIRE discovery service |

### Hydrology & Water Management

| Platform | URL | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|
| OVF / vizugy.hu | https://www.vizugy.hu/ | Hydrological | Station-based | Free | Partial (data download) | Real-time water levels, discharge, water temperature, precipitation | Operational data from surface water + groundwater stations |
| OVF Open Data (data.vizugy.hu) | https://data.vizugy.hu/ | Hydrological archives | Station-based | Free | Yes (data download service) | Historical water level, discharge, water temp, precipitation from monitoring network | Open since 2024-07-15. No restrictions |
| Vizeink.hu (WFD portal) | https://vizeink.hu/ | Water Framework Directive | Catchment-level | Free | No | River basin management plans, water body boundaries, water source protection areas | GIS shapefiles downloadable. EU WFD compliance portal |
| Geoportal Vizugy | https://geoportal.vizugy.hu/ | Water resource protection maps | Regional | Free | WMS | Water resource protection country map, flood risk maps | Web GIS viewer |

### Agriculture

| Platform | URL | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|
| MePAR (Agri Parcel ID System) | https://mepar.hu/ | Agricultural parcels (LPIS) | Physical block level | Freemium | Limited (web viewer) | Physical blocks, ineligible areas, erosion risk, flood risk, slope >17% areas | Portal at mepar.mvh.allamkincstar.gov.hu. Official EU subsidy reference system. Thematic layers purchasable |

### Forestry

| Platform | URL | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|
| Erdoterkep (NEBIH) | https://erdoterkep.nebih.gov.hu/ | Forestry parcels | Parcel-level | Free | No (web viewer) | Forest parcel boundaries, species, age, management data | Daily updates. Operated by NEBIH (food chain safety) |
| E-forest (SoE-ERTI) | http://eforest.hu/ | Forestry climate indices | Regional | Free | No | Monthly temperatures, precipitation, frost days, Ellenberg index, growth indicators | Research-oriented portal |

### Nature Conservation

| Platform | URL | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|
| TIR (Termeszetvedelmi Info Rendszer) | https://web.okir.hu/hu/tir | Protected areas, nature conservation | Site-level | Free | No (web viewer) | National parks, Natura 2000, protected species occurrences, ecotourism info | Part of OKIR (National Environmental Information System) |

### Soil

| Platform | URL | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|
| AGROTOPO Database | Via EJP Soil catalogue | Soil maps | 1:100,000 | Free | Limited (WMS from some providers) | Soil type, organic matter, soil value number (talajertekszam) | Created 1991, MTA Institute for Soil Sciences. DXF/MapInfo/ArcMAP formats |
| DOSoReMI | Research portal | Digital soil mapping | Varies | Free (research) | Under development | Renewed soil spatial data infrastructure for Hungary | Next-generation soil data system |

### Utilities & Infrastructure

| Platform | URL | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|
| e-Kozmu | https://ekozmu.e-epites.hu/ | Utility networks | Network-level | Free (viewing) | Yes - WFS (for providers) | Electricity, gas, water, drainage, telecom, district heating from ~900 providers | Distributed system querying providers in real-time. Registration required |

### Statistics & Census

| Platform | URL | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|
| KSH Regional Atlas / INSPIRE | https://www.ksh.hu/regionalatlas_inspire | Statistical, demographic | 1 km grid, settlement, county | Free | Yes (API for High-Value Datasets) | Census 2011/2022 grid maps, TIMEA thematic maps, demographic/economic data | EOV 1x1 km grid. CC-BY license. INSPIRE-compliant |

### Geodetic Networks

| Platform | URL | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|
| GNSSnet.hu (KGO Penc) | https://www.sgo-penc.hu/ | GNSS corrections, RINEX | cm-level positioning | Commercial (for real-time) | Yes (NTRIP for RTK) | 35 HU stations + 19 cross-border, RINEX for post-processing, real-time RTK corrections | 60-80 km station separation. Part of EUREF/IGS networks |

---

## AUSTRIA

| Platform | URL | Country | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| BEV (Bundesamt f. Eich- u. Vermessungswesen) | https://www.bev.gv.at/ | AT | Mapping, cadastre, geodesy | Varies | Freemium | Yes - WMS/WMTS | Cadastral maps, topographic maps, Austrian Map, geodetic data | Cadastre open data at kataster.bev.gv.at |
| basemap.at | https://basemap.at/ | AT | Base map tiles | Multi-scale | Free | Yes - WMTS/WMS | Orthophoto, standard map, terrain, overlay, surface | CC-BY 4.0 (OGD Austria). Cooperation of 9 provinces + BEV |
| BEV Data Catalogue | https://data.bev.gv.at/ | AT | Metadata + downloads | N/A | Yes - CSW | INSPIRE metadata, spatial datasets | INSPIRE-compliant discovery + download |
| GeoSphere Austria (ex-ZAMG + GBA) | https://data.hub.geosphere.at/ | AT | Meteorological, geological, geophysical | Station-based + mapped | Freemium | Yes - OGC services, REST API | Climate data, geological maps 1:50k (GeoFAST), geothermal, seismology, SKOS vocabularies | Merged 2023. CC-BY license. data.hub for downloads |
| GeoSphere GIS Portal | https://gis.geosphere.at/ | AT | Geological maps | 1:50,000 | Free | Yes - WMS | Geological maps, geothermal maps, mineral resources | Former GBA map server |
| eHYD | https://ehyd.gv.at/ | AT | Hydrological | Station-based | Free | No (web viewer + download) | Precip, runoff, groundwater from ~700 stations | Mobile WebApp available |
| eBOD (Digital Soil Map) | https://bodenkarte.at/ | AT | Agricultural soil | 1 km raster | Free | Yes - WMS | Soil types, soil forms, hydraulic properties | Operated by BFW/AGES. Parametrized evaluations per raster cell |
| BFW Service Portals | https://www.bfw.gv.at/en/services-products/service-portals/ | AT | Forestry | Varies | Free | Yes - WMS | Forest inventory, forest damage, soil maps | Austrian Federal Forest Research Centre |
| AGES BORIS (Soil Info System) | https://www.ages.at/ | AT | Soil contamination | Site-level | Restricted | No | Soil contamination data, background values | Cooperation between AGES, BFW, provinces |

---

## SLOVAKIA

| Platform | URL | Country | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| Geoportal SK (UGKK) | https://www.geoportal.sk/ | SK | National SDI, INSPIRE | Multi-scale | Free | Yes - WMS/WFS/ATOM | INSPIRE datasets, orthophotos, cadastre, topographic maps | INSPIRE-compliant. English available |
| ZBGIS | https://zbgis.skgeodesy.sk/ | SK | Base geographic data + cadastre | 1:10,000 | Free | Yes - WMS/REST | Topographic objects, cadastral maps, ownership data, address points | Publicly accessible cadastral map + ownership info |
| SHMU (Hydromet Institute) | https://www.shmu.sk/ | SK | Meteorological, hydrological, air quality | Station-based | Freemium | Limited | Weather obs, climate data, water levels, air quality monitoring | Since 1969. Under Ministry of Environment |
| SGIDS Geoportal (Geological Survey) | https://www.geology.sk/maps-and-data/geoportal-sguds/ | SK | Geological maps | 1:50,000 - 1:500,000 | Free | Yes - WMS | Geological maps, hydrogeological maps, mineral deposits, old mining works, landfills | GeoIS project outcome |
| VUPOP (Soil Research Institute) | https://www.vupop.sk/ | SK | Soil data | Varies | Free | Yes - WMS (ArcGIS REST) | Slovak soil register, BPEJ (bonified soil-ecological units), soil maps | Bratislava-based. podnemapy.sk portal |
| LPIS SK | Via podnemapy.sk | SK | Agricultural parcels | Parcel-level | Restricted | Limited | Reference plots, land use, subsidy applications | Accessible via VUPOP/LPIS portal |

---

## ROMANIA

| Platform | URL | Country | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| ANCPI Geoportal | https://geoportal.ancpi.ro/ | RO | Cadastre, topography | Parcel-level | Freemium | Yes - ArcGIS REST, WMS | Cadastral parcels, topographic maps, geodetic networks | Free registration for SHP/DXF/DGN/GDB downloads. INSPIRE-compliant |
| Geoportal.gov.ro | https://geoportal.gov.ro/ | RO | National SDI | Multi-scale | Free | Yes - WMS | INSPIRE datasets from multiple agencies | National INSPIRE node |
| ANM INSPIRE Catalogue | https://inspire.meteoromania.ro/geonetwork/ | RO | Meteorological | Station-based | Freemium | Yes - CSW, WMS | Station observations, WIGOS-registered station data, climate normals | INSPIRE-compliant metadata |
| IGR Geoportal (Geological Institute) | https://geoportal.igr.ro/ | RO | Geological maps | 1:200,000 | Free | Yes - WMS | Geological map 1:200k, mineral resources maps, geological cross-sections | Since 1906. INSPIRE view services |
| APIA LPIS | https://lpis.apia.org.ro/ | RO | Agricultural parcels | Parcel-level | Restricted | Limited | Physical blocks, land use, EFA layers (including forest edges) | Part of IACS. For subsidy management |
| ICPA (Soil Research) | https://www.icpa.ro/ | RO | Soil, land evaluation | Varies | Research access | Limited | Soil maps, land suitability, agrochemistry | Official land evaluation methodology since 1980s |

---

## SERBIA

| Platform | URL | Country | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| GeoSrbija | https://geosrbija.rs/ | RS | National SDI | Multi-scale | Free | Yes - WMS/WFS | 335+ datasets from 44+ institutions, address registry, admin boundaries | 10M+ requests/year. Open data portal integration |
| RGZ (Republic Geodetic Authority) | https://www.rgz.gov.rs/ | RS | Cadastre, topography | Parcel-level, 1:25k | Free | Yes - WMS | e-Cadastre (public access), topographic maps, address register, property valuation | All data free 24/7. No counter visits needed |
| RHMZ (Hydromet Service) | https://www.hidmet.gov.rs/ | RS | Meteorological, hydrological | Station-based | Freemium | Limited | Weather obs, climate data, water levels, discharge, air quality | Operational since Soviet era |
| SEPA Eco Register | http://www.ekoregistar.sepa.gov.rs/ | RS | Environmental | Site/regional | Free | Yes - WMS | Environmental monitoring, air/water quality, waste | Integrated with GeoSrbija |
| Open Data Portal | https://data.gov.rs/ | RS | Various | Varies | Free | Yes - CKAN API | Government open datasets including spatial data | Machine-readable formats |

---

## CROATIA

| Platform | URL | Country | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| DGU Geoportal | https://geoportal.dgu.hr/ | HR | National SDI, mapping | Multi-scale | Free | Yes - WMS/WMTS | Orthophoto (DOP5), Croatian Base Map (HOK 1:5000), topographic maps, cadastral maps | INSPIRE-compliant. 10,945 orthophoto sheets |
| DHMZ (Hydromet Service) | https://meteo.hr/ | HR | Meteorological, hydrological | Station-based | Freemium | Limited | Weather observations, climate data, water levels, air quality | Combined met + hydro service |
| HGI-CGS (Geological Survey) | https://www.hgi-cgs.hr/ | HR | Geological | 1:50,000 - 1:300,000 | Freemium | Yes - WMS | Geological maps, hydrogeological maps, mineral resources, geohazards | Archives from 19th century |
| HAOP (Nature Protection) | https://www.haop.hr/ | HR | Nature conservation | Site-level | Free | Yes - WMS | Natura 2000, protected areas, species data | INSPIRE environmental data |

---

## SLOVENIA

| Platform | URL | Country | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| E-prostor (GURS) | https://www.e-prostor.gov.si/ | SI | Geodesy, cadastre, topography | Parcel-level | Free | Yes - WMS/WFS | Cadastral maps, topographic data, geodetic points, address register | CC-BY 4.0. Full INSPIRE compliance |
| ARSO (Environment Agency) | https://www.arso.gov.si/ | SI | Met, hydro, environment | Station-based | Free | Yes - WMS, data download | Weather, water levels, air quality, LiDAR DEM | National met + hydro + environmental service combined |
| ARSO LiDAR / eVode | http://gis.arso.gov.si/evode/ | SI | LiDAR point clouds, DEM | 1 m DTM, 5-10 cm vertical accuracy | Free | Yes - WMS, direct download | Nationwide 1 m DTM, point clouds (LAZ), DSM | Public domain license. Entire country covered |
| GeoZS (Geological Survey) | https://www.geo-zs.si/ | SI | Geological | 1:50,000 - 1:250,000 | Free | Yes - WMS | Geological maps, hydrogeological maps, mineral resources, geohazards | INSPIRE, WFD, GMES compliant |
| Geopedia | https://www.geopedia.si/ | SI | Community + official spatial data | Multi-scale | Free | Yes - API | Cadastre overlay, land use, various thematic layers | Popular crowdsourced + official data platform |

---

## CZECH REPUBLIC

| Platform | URL | Country | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| CUZK Geoportal | https://geoportal.cuzk.cz/ | CZ | Mapping, cadastre, DEM | 0.18 m ortho, 1-5 m DEM | Free | Yes - WMS/WMTS/WFS/ATOM | ZABAGED (topo DB), orthophoto, cadastral maps, DEM (DMR 4G/5G), DSM, contour lines | CC-BY 4.0 since 2020. Full open data since 2023-07-01 |
| CGS (Czech Geological Survey) | https://cgs.gov.cz/ | CZ | Geological | 1:25,000 - 1:500,000 | Free | Yes - WMS/WFS, ATOM, REST | Geological maps, hydrogeological maps, soil maps, mineral resources, geohazards | Open data in GeoJSON (WGS84). INSPIRE ATOM feeds. MIcKA metadata catalogue |
| CHMI (Hydromet Institute) | https://www.chmi.cz/ | CZ | Meteorological, hydrological, air quality | Station-based | Freemium | Yes - ArcGIS Hub (open-data-chmi.hub.arcgis.com) | Climate data (Clidata), air quality (AQIS), surface water, groundwater monitoring | Since 1954. Under Min. of Environment |
| CENIA (Env. Info Agency) | https://cenia.gov.cz/ | CZ | Environmental | Varies | Free | Yes - WMS | Environmental information systems, mapping services | Min. of Environment subsidized org |
| LPIS CZ | https://eagri.cz/ssl/nosso/MZE/Plocha/ | CZ | Agricultural parcels | Parcel-level | Free (viewing) | Yes - WMS | Farmer blocks, land use, DPB (dily pudnich bloku) | Part of IACS system |

---

## POLAND

| Platform | URL | Country | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| Geoportal.gov.pl (GUGiK) | https://www.geoportal.gov.pl/ | PL | National SDI, mapping, DEM | 0.25 m ortho, 0.5-1 m DEM | Free | Yes - WMS/WMTS/WFS | BDOT10k (topo), BDOO (general), orthophoto, DEM, DSM, LiDAR, PRG (boundaries), PRNG (placenames), EGiB (cadastre) | GML/SHP/ASC/GeoTIFF. CC-BY or equivalent. Best LiDAR coverage in region |
| GUGiK INSPIRE Geoportal | https://www.gov.pl/web/gugik-en/geoportal-inspire | PL | INSPIRE datasets | Multi-scale | Free | Yes - WMS/WFS/ATOM | All INSPIRE annex themes from Polish sources | Full INSPIRE compliance |
| GUGiK LiDAR | https://www.geoportal.gov.pl/en/data/lidar-measurements-lidar/ | PL | LiDAR point clouds | 4-20 pts/m2 | Free | Yes - download service | Nationwide ALS coverage, classified point clouds | 20 pts/m2 in cities. LAZ format |
| IMGW-PIB | https://imgw.pl/ | PL | Meteorological, hydrological | Station-based | Free | Yes (danepubliczne.imgw.pl, R/Python packages) | Synoptic/climate station data, water levels, precipitation | Open data. R package (climate), Python package (imgw-data) |
| PIG-PIB (Geological Institute) | https://www.pgi.gov.pl/ | PL | Geological | 1:50,000 - 1:500,000 | Free | Yes - WMS, GeoLOG portal | CBDG (Central Geological DB), geological maps, boreholes, hydrogeology, mineral resources | GeoLOG at geolog.pgi.gov.pl |
| ARiMR Geoportal (LPIS) | https://geoportal.arimr.gov.pl/ | PL | Agricultural parcels | Parcel-level | Restricted | Yes - WMS (institutional) | LPIS reference plots, land use types, max qualified area | Access limited to institutions, research, EU bodies |
| Soil Science Society Geoportal | https://ptgleb.pl/en/geoportal-en/ | PL | Soil | Varies | Free | Yes - WMS | Soil maps, soil classification | Academic/research resource |

---

## CROSS-BORDER / PAN-EUROPEAN RESOURCES

| Platform | URL | Coverage | Data Type | Cost | API | Notes |
|---|---|---|---|---|---|---|
| INSPIRE Geoportal | https://inspire-geoportal.ec.europa.eu/ | EU-wide | All INSPIRE themes | Free | Yes - CSW/WMS | Central access to all national INSPIRE nodes |
| Copernicus Land Monitoring | https://land.copernicus.eu/ | EU-wide | Land cover/use, DEM | Free | Yes - WMS/WCS | EU-DEM 25m, CLC, HRL, Urban Atlas |
| European Soil Data Centre (ESDAC) | https://esdac.jrc.ec.europa.eu/ | EU-wide | Soil | 1 km - 250 m | Free (registration) | Yes - WMS | LUCAS, European Soil Database, erosion maps |
| EEA Datahub | https://www.eea.europa.eu/en/datahub | EU-wide | Environmental | Varies | Free | Yes - various | Air quality, water, biodiversity, climate |
| EUREF Permanent Network | https://www.epncb.oma.be/ | EU-wide | GNSS | cm-level | Free | Yes - RINEX download | European reference frame stations |

---

## SUMMARY TABLE - COVERAGE BY TOPIC

| Topic | HU | AT | SK | RO | RS | HR | SI | CZ | PL |
|---|---|---|---|---|---|---|---|---|---|
| National Geoportal / SDI | Lechner/NTA | BEV/basemap.at | Geoportal.sk | ANCPI/geoportal.gov.ro | GeoSrbija | DGU | E-prostor | CUZK | Geoportal.gov.pl |
| INSPIRE Node | Lechner | BEV | UGKK | ANCPI | GeoSrbija | DGU | GURS | CUZK | GUGiK |
| Geological Survey | MBFSZ/SZTFH | GeoSphere | SGIDS | IGR | Geoinstitut | HGI-CGS | GeoZS | CGS | PIG-PIB |
| Meteorological Service | HungaroMet | GeoSphere | SHMU | ANM | RHMZ | DHMZ | ARSO | CHMI | IMGW-PIB |
| Hydrological Service | OVF/vizugy.hu | eHYD | SHMU | ANM | RHMZ | DHMZ | ARSO | CHMI | IMGW-PIB |
| Environmental Agency | OKIR/TIR | Umweltbundesamt | SEA | ANPM | SEPA | HAOP | ARSO | CENIA | GDOS |
| Forestry DB | NEBIH erdoterkep | BFW | NLC | ICAS | Srbijasume | HGI | ZGS | UHUL | GDLP |
| LPIS / Agri Parcels | MePAR | INVEKOS/AMA | LPIS SK | APIA LPIS | LPIS RS | APPRRR | GERK | eAGRI LPIS | ARiMR |
| Cadastre Open Data | Foldhivatal | kataster.bev.gv.at | ZBGIS | ANCPI | RGZ e-Cadastre | DGU | E-prostor | CUZK | EGiB |
| DEM/LiDAR | Lechner (paid) | basemap.at | UGKK | ANCPI | RGZ | DGU | ARSO (1m free) | CUZK (free) | GUGiK (free, 4-20pt/m2) |
| Soil Database | AGROTOPO | eBOD/BORIS | VUPOP | ICPA | Inst. Soil Sci. | Pedology dept | ARSO | CGS | IUNG/PTGLEB |
| Nature Conservation | TIR | Umweltbundesamt | SOP SR | ANANP | ZZPS | HAOP | ARSO/ZRSVN | AOPK | GDOS |
| GNSS Network | GNSSnet.hu | APOS | SKPOS | ROMPOS | AGROS | CROPOS | SIGNAL | CZEPOS | ASG-EUPOS |

---

## OPEN DATA MATURITY RANKING (subjective assessment)

1. **Poland** - Best-in-class LiDAR (4-20 pts/m2 free), full topo/DEM/ortho open data, IMGW open met data
2. **Czech Republic** - Full open data since 2023 (ZABAGED, ortho, DEM, cadastre), CC-BY 4.0
3. **Austria** - basemap.at free, cadastre vector tiles open, GeoSphere data hub
4. **Slovenia** - Nationwide 1m LiDAR free (public domain), ARSO comprehensive
5. **Slovakia** - ZBGIS open, cadastre publicly viewable, geological survey open
6. **Hungary** - Improving (HungaroMet open since 2021, NTA free for gov, OVF open since 2024), but Lechner DEM/ortho still mostly paid
7. **Serbia** - GeoSrbija strong initiative, RGZ all data free, but coverage gaps
8. **Romania** - ANCPI improving, geological maps available, but many datasets still restricted
9. **Croatia** - DGU geoportal functional, but limited free downloads
