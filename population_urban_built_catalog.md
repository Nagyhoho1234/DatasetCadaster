# Population, Urban, and Built Environment Data Sources

## Global Population Grids

| Platform | URL | Scope | Data Type | Resolution | Temporal | Cost | API | Notes |
|---|---|---|---|---|---|---|---|---|
| GHSL GHS-POP | ghsl.jrc.ec.europa.eu | Global | Population grid | 100m / 1km | 1975-2030 (5yr epochs) | Free | No (bulk download) | GeoTIFF; JRC Multitemporal |
| WorldPop | worldpop.org | Global | Population grid | 100m | 2000-2020 | Free | REST API | Age/sex disaggregated available |
| GPW v4 SEDAC | sedac.ciesin.columbia.edu | Global | Population grid | 1km (~30 arc-sec) | 2000-2020 | Free | No | Census-based; Earthdata login required |
| LandScan Global | landscan.ornl.gov | Global | Ambient population grid | 1km (~30 arc-sec) | 2000-present | Free since 2022 | No | Models ambient (daytime) population |
| Meta/Facebook HRSL | data.humdata.org (HDX) | Global | High-res pop grid | 30m | ~2018-2020 | Free | No | AI building detection + census redistribution |
| Kontur Population | kontur.io | Global | H3 hexagon population | H3 resolution 8 | 2020+ | Free via HDX | No | H3 hexagonal grid aggregation |
| UN World Urbanization Prospects | population.un.org/wup | Global | Urban/rural population (tabular) | Country/city level | 1950-2050 | Free | REST API | Projections and estimates |
| Eurostat Population Grids GEOSTAT | ec.europa.eu/eurostat | Europe | Census pop grid | 1km | 2006, 2011, 2021 | Free | GISCO REST | ETRS89-LAEA 1km grid |
| KSH / TEIR | ksh.hu, teir.hu | Hungary | Settlement-level census | Settlement | Decennial + annual | Free | Partial API | Hungarian Central Statistics Office |

## Building Footprints and Urban Extent

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Notes |
|---|---|---|---|---|---|---|---|
| Microsoft Building Footprints | github.com/microsoft/GlobalMLBuildingFootprints | Global | 800M+ building polygons | Building-level | Free, ODbL | PMTiles / Planetary Computer | AI-derived from satellite imagery |
| Google Open Buildings | sites.research.google/open-buildings | Africa, Asia, Latin America | 1.8B building polygons | Building-level | Free, CC-BY 4.0 | GEE / BigQuery | AI-derived, confidence scores |
| Overture Maps | overturemaps.org | Global | Merged building footprints | Building-level | Free, CDLA | S3/Azure bulk | Merges MS/Google/OSM buildings; GeoParquet |
| GHSL GHS-BUILT-S | ghsl.jrc.ec.europa.eu | Global | Built-up surface fraction | 10m / 100m / 1km | Free | No (bulk) | GeoTIFF; 1975-2030 epochs |
| GHSL GHS-BUILT-H | ghsl.jrc.ec.europa.eu | Global | Building height | 100m | Free | No (bulk) | GeoTIFF; estimated building heights |
| WSF World Settlement Footprint | geoservice.dlr.de | Global | Settlement extent | 10m | Free | WMS / WFS | DLR; Sentinel-1/2 derived |
| GUF Global Urban Footprint | DLR | Global | Urban extent | 12m | Free for science | No | TanDEM-X derived; application required |
| ESM European Settlement Map | ghsl.jrc.ec.europa.eu/esm.php | Europe | Built-up map | 2.5m | Free | No (bulk) | High-resolution built-up from VHR imagery |
| HBASE NASA SEDAC | sedac.ciesin.columbia.edu | Global | Built-up binary mask | 30m | Free | No | Landsat-derived built-up presence |

## Urban and Settlement Classification

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Notes |
|---|---|---|---|---|---|---|---|
| GHSL GHS-SMOD | ghsl.jrc.ec.europa.eu | Global | Settlement model / DEGURBA | 1km | Free | No (bulk) | Urban centre / cluster / rural classification |
| DEGURBA Grid JRC | ghsl.jrc.ec.europa.eu/degurba.php | Global | Settlement classification | 1km | Free | No | Degree of urbanisation grid |
| Urban Atlas Copernicus | land.copernicus.eu/local/urban-atlas | Europe | Urban land use/land cover | 10m (urban) / 2.5m (SL) | Free | No | ~800 Functional Urban Areas; 2006/2012/2018 |
| UCDB Urban Centre Database | ghsl.jrc.ec.europa.eu | Global | Urban centre attributes | City-level (~10k cities) | Free | No | 70+ attributes per city (pop, GDP, climate) |
| CORINE Land Cover (urban classes) | land.copernicus.eu | Europe | Land cover classes 111-142 | 100m | Free | No | Urban fabric, industrial, transport, green urban |
| Copernicus Imperviousness HRL | land.copernicus.eu | Europe | Impervious surface density | 10m (2018) / 20m (earlier) | Free | WMS | 0-100% imperviousness; change layers available |

## Nighttime Lights

| Platform | URL | Scope | Data Type | Resolution | Temporal | Cost | API | Notes |
|---|---|---|---|---|---|---|---|---|
| VIIRS Black Marble VNP46 | blackmarble.gsfc.nasa.gov | Global | Nighttime lights radiance | 500m | 2012-present | Free | LAADS API | Daily/monthly/annual composites |
| DMSP-OLS | eogdata.mines.edu | Global | Nighttime lights DN | 1km (~30 arc-sec) | 1992-2013 | Free | No | Historical archive; 6-bit DN values |
| EOG Annual VNL Composites | eogdata.mines.edu/products/vnl | Global | Annual VIIRS nightlights | 500m (~15 arc-sec) | 2012-present | Free | No | Stray-light corrected annual composites |

## Roads and Infrastructure

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Notes |
|---|---|---|---|---|---|---|---|
| GRIP Global Roads | globio.info | Global | Road network | Line features (21M km) | Free | No | 5 road types; derived from multiple sources |

## Composite Indices

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Notes |
|---|---|---|---|---|---|---|---|
| Human Modification Index SEDAC | sedac.ciesin.columbia.edu | Global | Human modification degree | 1km | Free | No | Composite of settlement, agriculture, energy, transport |
