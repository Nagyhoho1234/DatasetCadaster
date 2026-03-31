# Ocean, Marine, and Bathymetry Data Sources

## Global Bathymetry and Topography

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Notes |
|---|---|---|---|---|---|---|---|
| GEBCO | gebco.net | Global | Bathymetry grid | 15 arc-sec (~450m) | Free | WMS / WCS | GEBCO_2023 grid; TID grid for source info |
| NOAA ETOPO | ncei.noaa.gov | Global | Combined bathymetry + topography | 15/30/60 arc-sec | Free | THREDDS | ETOPO 2022; ice surface and bedrock versions |
| SRTM15+ Scripps | topex.ucsd.edu | Global | Bathymetry from altimetry + soundings | 15 arc-sec | Free | No | Sandwell & Smith gravity-derived |
| IBCAO | ibcao.org | Arctic | Arctic bathymetry | 500m | Free | No | International Bathymetric Chart of the Arctic Ocean |
| IBCSO | ibcso.org | Antarctic | Antarctic bathymetry | 500m | Free | No | International Bathymetric Chart of the Southern Ocean |

## European Marine Data

| Platform | URL | Scope | Data Type | Resolution | Temporal | Cost | API | Notes |
|---|---|---|---|---|---|---|---|---|
| EMODnet Bathymetry | emodnet.ec.europa.eu | Europe | Bathymetric DTM | ~115m (1/16 arc-min) | 2018-present | Free | WMS / WFS / ERDDAP | Composite from national hydrographic surveys |
| EMODnet Chemistry | emodnet.ec.europa.eu | Europe | Marine contaminants, nutrients | Station-level | 1900s-present | Free | WMS / WFS / ERDDAP | Aggregated in-situ chemistry |
| EMODnet Physics | emodnet.ec.europa.eu | Europe | T, S, waves, currents, sea level | Station-level + grid | Real-time + historical | Free | ERDDAP | In-situ and model data |
| EMODnet Biology | emodnet.ec.europa.eu | Europe | Marine species occurrences | Station-level | 1900s-present | Free | WFS / WMS | Integrated from OBIS and national sources |
| EMODnet Geology | emodnet.ec.europa.eu | Europe | Seabed substrate, geomorphology | Varies | Various | Free | WMS / WFS | Seabed substrate maps, events |
| EMODnet Seabed Habitats | emodnet.ec.europa.eu | Europe | Habitat maps | Varies | Various | Free | WFS / WMS | EUSeaMap broad-scale habitat map |
| EMODnet Human Activities | emodnet.ec.europa.eu | Europe | Maritime uses | Varies | Various | Free | WMS / WFS | Cables, pipelines, wind farms, shipping |
| SeaDataNet | seadatanet.org | Europe | Aggregated ocean observations | Station-level | 1900s-present | Free | CDI search | Pan-European ocean data infrastructure |

## Global Ocean Models and Reanalysis

| Platform | URL | Scope | Data Type | Resolution | Temporal | Cost | API | Notes |
|---|---|---|---|---|---|---|---|---|
| Copernicus Marine CMEMS | marine.copernicus.eu | Global + EU seas | SST, currents, salinity, bio, waves | 0.083° (global) to 0.028° (regional) | 1993-present + forecast | Free | Python API / OPeNDAP | Core service; ~200 products |
| CMEMS Med MFC | marine.copernicus.eu | Mediterranean | Physics + biogeochemistry | 0.042° (~4km) | 1987-present | Free | Python API / OPeNDAP | Mediterranean Monitoring and Forecasting Centre |
| CMEMS Baltic MFC | marine.copernicus.eu | Baltic Sea | Physics + biogeochemistry | ~1 nmi | 1993-present | Free | Python API / OPeNDAP | Baltic monitoring and forecasting |
| CMEMS Black Sea MFC | marine.copernicus.eu | Black Sea | Physics + biogeochemistry | 0.028° (~3km) | 1993-present | Free | Python API / OPeNDAP | Black Sea monitoring and forecasting |
| ERA5 Waves via CDS | cds.climate.copernicus.eu | Global | Wave height, period, direction | 0.5° | 1940-present | Free | CDS API | ECMWF wave reanalysis |

## Global Ocean Observations

| Platform | URL | Scope | Data Type | Resolution | Temporal | Cost | API | Notes |
|---|---|---|---|---|---|---|---|---|
| NOAA NCEI Ocean | ncei.noaa.gov | Global | In-situ ocean data archive | Station-level | 1770s-present | Free | ERDDAP / THREDDS | World's largest ocean data archive |
| NASA PO.DAAC | podaac.jpl.nasa.gov | Global | Sea level, SST, salinity, currents | Varies (satellite) | 1978-present | Free | CMR API / OPeNDAP | Physical oceanography satellite products |
| NASA Ocean Color | oceancolor.gsfc.nasa.gov | Global | Chlorophyll-a, water optics | 1-4 km | 1997-present | Free | OPeNDAP | MODIS, VIIRS, PACE ocean color |
| SeaBASS | seabass.gsfc.nasa.gov | Global | In-situ ocean color observations | Station-level | 1990s-present | Free | Search API | Validation data for satellite products |
| Argo | argo.ucsd.edu | Global | T/S profiles to 2000m (6000m deep) | Float-level (~4000 active) | 2000-present | Free | ERDDAP | Autonomous profiling floats |
| Euro-Argo / Coriolis | euro-argo.eu / coriolis.eu.org | Europe + Global | T/S/bio profiles | Float-level | 2000-present | Free | ERDDAP | European Argo contribution |
| WOD World Ocean Database | ncei.noaa.gov | Global | Historical ocean profiles | Station-level | 1770s-present | Free | WODselect | Largest uniformly formatted ocean profile database |
| PANGAEA | pangaea.de | Global | Earth science data archive | Varies | Various | Free | REST / OAI-PMH | Data publisher; DOI for each dataset |
| BODC | bodc.ac.uk | UK / Global | Marine data archive | Station-level | 1900s-present | Free | ERDDAP | British Oceanographic Data Centre |
| IFREMER | ifremer.fr | Europe / Global | Multi-disciplinary marine | Varies | Various | Free | ERDDAP / Sextant | French oceanographic institute |

## Satellite Altimetry and Sea Level

| Platform | URL | Scope | Data Type | Resolution | Temporal | Cost | API | Notes |
|---|---|---|---|---|---|---|---|---|
| AVISO+ | aviso.altimetry.fr | Global | Sea level anomaly, currents | 0.25° (gridded) | 1993-present | Free | FTP / OPeNDAP | Multi-mission altimetry products |
| PSMSL | psmsl.org | Global | Tide gauge monthly means | Station-level (~1500 stations) | 1807-present | Free | No | Permanent Service for Mean Sea Level |
| IOC Sea Level Monitoring | ioc-sealevelmonitoring.org | Global | Real-time tide gauge | Station-level | Real-time | Free | JSON API | UNESCO/IOC real-time monitoring |
| GESLA | gesla.org | Global | High-frequency tide gauge | Station-level (~5000 records) | Various | Free | No | Global Extreme Sea Level Analysis |
| EUMETSAT OSI SAF | osi-saf.eumetsat.int | Global | Sea ice concentration, SST, flux | Varies | 1978-present | Free | No | Operational sea ice and SST products |

## Waves

| Platform | URL | Scope | Data Type | Resolution | Temporal | Cost | API | Notes |
|---|---|---|---|---|---|---|---|---|
| CDIP | cdip.ucsd.edu | US coastal | Wave buoy data | Station-level | 1975-present | Free | THREDDS | Coastal Data Information Program |

## Marine Biology and Ecology

| Platform | URL | Scope | Data Type | Resolution | Temporal | Cost | API | Notes |
|---|---|---|---|---|---|---|---|---|
| OBIS | obis.org | Global | Marine species occurrences | Station-level | 1800s-present | Free | REST API | Ocean Biodiversity Information System; 100M+ records |
| ICES | ices.dk/data | NE Atlantic | Fish surveys, ocean data | Station/haul level | 1900s-present | Free | DATRAS web services | DATRAS trawl surveys; advisory data |
| WDPA Marine | protectedplanet.net | Global | Marine Protected Areas | Polygon | 1900s-present | Free | REST API | UN Environment WCMC maintained |
| Natura 2000 Marine | ec.europa.eu/environment/nature | Europe | Marine Natura 2000 sites | Polygon | 1992-present | Free | WFS | Habitats + Birds Directive sites |

## Ocean Carbon and Chemistry

| Platform | URL | Scope | Data Type | Resolution | Temporal | Cost | API | Notes |
|---|---|---|---|---|---|---|---|---|
| SOCAT | socat.info | Global | Surface ocean CO2 (fCO2) | Ship track | 1957-present | Free | ERDDAP | Community quality-controlled dataset |
| GLODAP | glodap.info | Global | Deep ocean carbon chemistry | Station-level | 1972-present | Free | No | Internally consistent bottle data |

## Coastal

| Platform | URL | Scope | Data Type | Resolution | Temporal | Cost | API | Notes |
|---|---|---|---|---|---|---|---|---|
| NOAA Digital Coast | coast.noaa.gov | US coastal | Lidar, land cover, imagery | Varies | Various | Free | REST | US coastal geospatial data |
| Eurosion | eurosion.org | Europe | Coastal erosion data | Varies | ~2004 | Free | No | European coastal erosion assessment |

## Maritime Activity

| Platform | URL | Scope | Data Type | Resolution | Temporal | Cost | API | Notes |
|---|---|---|---|---|---|---|---|---|
| MarineTraffic | marinetraffic.com | Global | AIS vessel tracking | Ship-level | Real-time + historical | Freemium | REST API | Free basic; commercial for full API |
| Global Fishing Watch | globalfishingwatch.org | Global | Fishing vessel activity | Ship-level | 2012-present | Free, CC-BY-NC | REST / BigQuery | AIS-based fishing detection |

## Regional Services

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Notes |
|---|---|---|---|---|---|---|---|
| BSH | bsh.de | Germany / North+Baltic Sea | Hydrographic, tides, currents | Varies | Various | Free | WMS | German Federal Maritime and Hydrographic Agency |
| HELCOM | helcom.fi | Baltic Sea | Environmental data | Varies | Various | Free | No | Baltic Marine Environment Protection Commission |
| OSPAR | ospar.org | NE Atlantic | Environmental assessments | Varies | Various | Free | No | NE Atlantic marine environment convention |

## Federated Discovery

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Notes |
|---|---|---|---|---|---|---|---|
| OceanInfoHub | oceaninfohub.org | Global | Federated search across repositories | Varies | Free | SPARQL | UNESCO/IOC; links to source data |
