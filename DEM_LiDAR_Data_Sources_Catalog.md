# DEM / Elevation / LiDAR Data Sources Catalog

Compiled: 2026-03-31

---

## Global Datasets

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| **SRTM (NASA)** | https://www.earthdata.nasa.gov/data/instruments/srtm | Global (60N-60S) | DEM (DSM) | 1 arc-sec (~30m), 3 arc-sec (~90m) | Free | Yes (Earthdata API, OPeNDAP) | SRTMGL1 v003, SRTMGL3 | GeoTIFF/HGT; Earthdata login required; radar-derived; ~2000 vintage |
| **NASADEM** | https://www.earthdata.nasa.gov/about/competitive-programs/measures/new-nasa-digital-elevation-model | Global (60N-56S) | DEM (DSM) | 1 arc-sec (~30m) | Free | Yes (Earthdata API, OpenTopography REST) | NASADEM_HGT v001 | Reprocessed SRTM with ASTER/ICESat corrections; fewer voids; GeoTIFF |
| **ASTER GDEM v3** | https://lpdaac.usgs.gov/products/astgtmv003/ | Global (83N-83S) | DEM (DSM) | 1 arc-sec (~30m) | Free | Yes (AppEEARS, GEE, OpenTopoData) | ASTGTM v003 | COG + NetCDF4; stereo-optical derived; noisier than SRTM in flat terrain |
| **Copernicus DEM GLO-30** | https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM | Global | DSM | 1 arc-sec (~30m) | Free | Yes (OData, STAC, S3, Sentinel Hub, GEE) | COP-DEM GLO-30 | COG; TanDEM-X derived; best free global DSM; CC-BY-4.0; AWS open data |
| **Copernicus DEM GLO-90** | https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM | Global | DSM | 3 arc-sec (~90m) | Free | Yes (same as GLO-30) | COP-DEM GLO-90 | Full global coverage without restrictions |
| **ALOS World 3D (AW3D30)** | https://www.eorc.jaxa.jp/ALOS/en/dataset/aw3d30/ | Global | DSM | 1 arc-sec (~30m) | Free | Yes (GEE, OpenTopography) | AW3D30 v4.1 | Optical stereo (PRISM); registration required at JAXA; GeoTIFF |
| **TanDEM-X 90m** | https://download.geoservice.dlr.de/TDM90/ | Global | DEM (DSM) | 3 arc-sec (~90m) | Free (scientific) | No (HTTP download) | TDM90 | DLR; free for science only; commercial via Airbus WorldDEM; GeoTIFF |
| **TanDEM-X 12m** | https://tandemx-science.dlr.de | Global | DEM (DSM) | 0.4 arc-sec (~12m) | Proposal-based / Commercial | No (proposal form) | TDM DEM 12m | Best global SAR DEM; commercial rights with Airbus; proposal for research |
| **FABDEM** | https://data.bris.ac.uk/data/dataset/s5hqmjcdj8yo2ibzi9b4ew3sn | Global | DTM (bare earth) | 1 arc-sec (~30m) | Free (non-commercial) | Yes (GEE, Fathom API) | FABDEM v1-2 | Copernicus GLO-30 with forests+buildings removed; CC-BY-NC-SA 4.0 |
| **MERIT DEM** | https://hydro.iis.u-tokyo.ac.jp/~yamadai/MERIT_DEM/ | Global (90N-60S) | DTM | 3 arc-sec (~90m) | Free | Yes (GEE) | MERIT DEM v1.0.3 | Multi-error-removed SRTM+AW3D; best for hydrology; EGM96 geoid |
| **ArcticDEM** | https://www.pgc.umn.edu/data/arcticdem/ | Arctic (>60N) | DSM | 2m (strips), 10m/32m (mosaic) | Free (2m restricted to research) | Yes (STAC, AWS S3) | ArcticDEM Release 7 | Stereo satellite imagery; multitemporal; GeoTIFF; PGC |
| **EarthDEM** | https://www.pgc.umn.edu/data/earthdem/ | Global (60N-60S) | DSM | 2m (strips), 10m/32m (mosaic) | Restricted (US govt-funded) | Yes (NASA CSDA) | EarthDEM | Stereo satellite; limited public access; full access via NASA CSDA |
| **GMTED2010** | https://www.usgs.gov/coastal-changes-and-impacts/gmted2010 | Global | DEM | 7.5 arc-sec (~250m) | Free | Yes (GEE) | GMTED2010 | USGS; multi-source; coarse but consistent global baseline |
| **ETOPO1** | https://www.ngdc.noaa.gov/mgg/global/ | Global (land+ocean) | DEM + bathymetry | 1 arc-min (~1.8km) | Free | Yes (GEE, NOAA API) | ETOPO 2022 | NOAA; includes ocean bathymetry; useful for large-scale studies |
| **OpenTopography** | https://opentopography.org/ | Global (aggregator) | LiDAR point clouds, DEM, DSM, DTM | Variable (sub-meter to 30m) | Free | Yes (REST API, S3) | SRTM, NASADEM, COP-DEM, AW3D, 500+ LiDAR datasets | NSF-funded; API key for global rasters; LAS/LAZ + GeoTIFF; best single portal |
| **Google Earth Engine** | https://developers.google.com/earth-engine/datasets/tags/elevation | Global (aggregator) | DEM, DSM, DTM | Variable | Free (non-commercial) | Yes (Python/JS API) | SRTM, ASTER, COP-DEM, AW3D, MERIT, NASADEM, AHN, etc. | Cloud processing; no download needed; commercial requires fee |
| **Microsoft Planetary Computer** | https://planetarycomputer.microsoft.com/ | Global (aggregator) | DEM, DSM | Variable | Free | Yes (STAC API) | COP-DEM GLO-30/90, ALOS DEM, NASADEM | Azure-hosted; COG; STAC compliant; Python/pystac |
| **AWS Open Data** | https://registry.opendata.aws/ | Global (aggregator) | DEM, DSM, LiDAR | Variable | Free (some requester-pays) | Yes (S3) | COP-DEM, ArcticDEM, USGS 3DEP LiDAR, AHN | S3 buckets; COG; bulk access |

---

## European Datasets

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| **Copernicus EEA-10** | https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM | Europe (EEA39) | DSM | ~10m | Restricted (public authorities) | Yes (OData) | COP-DEM EEA-10 | TanDEM-X derived; not publicly downloadable; restricted access |
| **EU-DEM v1.1** | https://www.eea.europa.eu/data-and-maps/data/copernicus-land-monitoring-service-eu-dem | Europe (EEA39) | DSM | 25m | Free (discontinued) | No | EU-DEM v1.1 | SRTM+ASTER hybrid; archived; contact service desk for access |
| **Sonny's LiDAR DTMs** | https://sonny.4lima.de/ | Europe (multi-country) | DTM | 1 arc-sec (~25m) | Free | No (HTTP) | DTMs for AT, CH, DE, IT, SI, ES, NO, FI, SE, etc. | CC-BY-4.0; LiDAR-derived; excellent community resource; HGT format |
| **OpenDEM** | https://www.opendem.info/ | Europe | DTM, DSM | Variable | Free | No | European national DEMs aggregated | Portal linking to national open DEM sources |
| **EuroGeographics EuroDEM** | https://www.mapsforeurope.org/datasets/euro-dem | Europe | DEM | Variable | Commercial | No | EuroDEM | Pan-European; not free; from national mapping agencies |

---

## National Datasets (Europe)

| Platform | URL | Country | Data Type | Resolution | Cost | API | Notes |
|---|---|---|---|---|---|---|---|
| **UK Environment Agency LiDAR** | https://environment.data.gov.uk/ | UK (England) | DTM, DSM, LiDAR point cloud | 1m, 2m | Free | Yes (WMS, WFS) | OGL license; LAZ point clouds; GeoTIFF rasters; quarterly updates |
| **Netherlands AHN4** | https://www.ahn.nl/ | Netherlands | DTM, DSM, LiDAR point cloud | 0.5m (raster), 10+ pts/m2 (point cloud) | Free | Yes (GEE, PDOK WMS/WCS, S3) | CC-0; nationwide; LAZ format; also on OpenTopography |
| **Finland NLS Laser Scanning** | https://www.maanmittauslaitos.fi/en/maps-and-spatial-data/datasets-and-interfaces/product-descriptions/laser-scanning-data | Finland | LiDAR point cloud, DTM | 2m (raster), 0.5-5 pts/m2 | Free | Yes (WMS, download service) | LAZ format; NLS MapSite download; new 5 pts/m2 survey ongoing |
| **Norway NDH (hoydedata.no)** | https://hoydedata.no/LaserInnsyn/ | Norway | DTM, DSM, LiDAR point cloud | 1m | Free | Yes (WMS, seamless server) | CC-BY-4.0; Kartverket; most of Norway covered |
| **Sweden Lantmateriet** | https://www.lantmateriet.se/en/geodata/our-products/product-list/elevation-model-download/ | Sweden | DTM, LiDAR point cloud | 1m (raster), 0.5-2 pts/m2 | Free | Yes (download service) | Open data; NH (0.5 pts/m2) and Forest (1-2 pts/m2) datasets |
| **Germany DGM** | https://www.opendem.info/opendtm_de.html | Germany | DTM | 1m (DGM1), 5m (DGM5) | Free (varies by state) | Yes (WMS) | Federal states publish independently; all open since June 2024 |
| **France RGE ALTI** | https://geoservices.ign.fr/ | France | DTM | 1m, 5m | Free | Yes (WMS, WCS, GEE) | IGN; LiDAR or photogrammetric; GeoTIFF; open license |
| **Spain PNOA-LiDAR** | https://centrodedescargas.cnig.es/ | Spain | DTM, LiDAR point cloud | 5m (DTM05), 0.5-4 pts/m2 | Free | Yes (WMS, WMTS) | IGN/CNIG; 3rd coverage ongoing; LAZ; ETRS89 |
| **Italy TINITALY** | https://tinitaly.pi.ingv.it/ | Italy | DTM | 10m | Free | Yes (GEE) | INGV; CC-BY-4.0; v1.1 (2023); GeoTIFF; UTM WGS84 zone 32 |
| **Austria Geoland** | https://www.data.gv.at/ | Austria | DTM | 1m, 10m | Free | Yes (WMS) | LiDAR-derived; federal states data; open data portal |
| **Slovenia ARSO LiDAR** | http://gis.arso.gov.si/evode/profile.aspx?id=atlas_voda_Lidar@Arso | Slovenia | DTM, DSM, LiDAR point cloud | 1m (raster), 2-5 pts/m2 | Free | Yes (WMS) | Fully open; ASC + LAZ; QGIS plugin available |
| **Poland ISOK** | https://www.geoportal.gov.pl/en/data/lidar-measurements-lidar/ | Poland | DTM, DSM, LiDAR point cloud | 1m (raster), 4-20 pts/m2 | Free | Yes (WMS, WFS) | Open since 2018; LAZ; GUGiK geoportal |
| **Czech Republic DMR 5G** | https://geoportal.cuzk.cz/ | Czech Republic | DTM | ~5m grid | Free | Yes (WMS, ArcGIS ImageServer) | CUZK; LiDAR 2009-2013; 0.18m accuracy (open terrain) |
| **Slovakia ALS/DMR** | https://www.geoportal.sk/en/zbgis/als/ | Slovakia | DTM, DSM, LiDAR point cloud | 1m, 5m | Free | Yes (WMS) | UGKK; 2nd cycle ongoing (DMR 6.0); download limits apply |
| **Romania ANCPI** | https://geoportal.ancpi.ro/ | Romania | DTM | 5m, 10m | Free (limited) | Yes (WMS) | OGL-ROU; partial LiDAR coverage; request-based for point clouds |

---

## Hungary / Central Europe Specific

| Platform | URL | Country | Data Type | Resolution | Cost | API | Notes |
|---|---|---|---|---|---|---|---|
| **HUNDEM-5 (FOMI)** | https://en.foldhivatal.hu/ | Hungary | DTM | 5m | Commercial / request-based | No | FOMI (now Lechner Tudaskozpont); Baltic height system; EOV projection; ~15 GB; not openly downloadable |
| **EnviMAP (Envirosense)** | https://envirosense.hu/en/featured_item/elevation-data/ | Hungary | DTM, DSM, LiDAR point cloud | Sub-meter to 5m | Commercial | No | Covers ~75% of Hungary (~70,000 km2); private provider |
| **Copernicus GLO-30 (for Hungary)** | https://dataspace.copernicus.eu/ | Hungary (via global) | DSM | 30m | Free | Yes | Best free option for Hungary; ~30m resolution |
| **Sonny's DTM Hungary** | https://sonny.4lima.de/ | Hungary (partial) | DTM | ~25m | Free | No | Derived from available LiDAR; CC-BY-4.0; check availability |

---

## USA (Reference)

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| **USGS 3DEP / National Map** | https://www.usgs.gov/3d-elevation-program | USA | DTM, DSM, LiDAR point cloud | 1m (DEM), variable pts/m2 (LiDAR) | Free | Yes (REST, WMS, AWS S3) | 3DEP 1m DEM, LiDAR point clouds | No account required; Entwine Point Tiles on AWS; LAZ; GeoTIFF; GEE |

---

## Summary Statistics

| Metric | Count |
|---|---|
| Global DEM/DSM datasets | 17 |
| European pan-continental datasets | 5 |
| National European LiDAR/DEM programs | 15 |
| Hungary-specific sources | 4 |
| Free datasets | ~35 |
| Commercial/restricted datasets | ~5 |
| Platforms with API support | ~30 |

---

## Recommended Priority for Central European Work

1. **Copernicus GLO-30** -- best free global DSM, 30m, immediate download
2. **FABDEM** -- bare-earth corrected version of GLO-30, 30m
3. **TanDEM-X 90m** -- free for science, excellent quality
4. **SRTM / NASADEM** -- well-established baseline, 30m
5. **National LiDAR** (SK, CZ, SI, AT, PL) -- sub-meter where available
6. **HUNDEM-5** -- 5m DTM for Hungary but requires purchase/request from FOMI/Lechner
7. **OpenTopography** -- single portal aggregating many of the above

---

Sources:
- [NASA Earthdata SRTM](https://www.earthdata.nasa.gov/data/instruments/srtm)
- [ASTER GDEM v3](https://lpdaac.usgs.gov/products/astgtmv003/)
- [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM)
- [ALOS AW3D30](https://www.eorc.jaxa.jp/ALOS/en/dataset/aw3d30/)
- [TanDEM-X 90m](https://download.geoservice.dlr.de/TDM90/)
- [OpenTopography](https://opentopography.org/)
- [USGS 3DEP](https://www.usgs.gov/3d-elevation-program)
- [UK Environment Agency LiDAR](https://environment.data.gov.uk/)
- [Netherlands AHN](https://www.ahn.nl/)
- [Finland NLS](https://www.maanmittauslaitos.fi/en/maps-and-spatial-data/datasets-and-interfaces/product-descriptions/laser-scanning-data)
- [Norway hoydedata](https://hoydedata.no/LaserInnsyn/)
- [Sweden Lantmateriet](https://www.lantmateriet.se/en/geodata/our-products/product-list/elevation-model-download/)
- [Spain CNIG](https://centrodedescargas.cnig.es/)
- [Italy TINITALY](https://tinitaly.pi.ingv.it/)
- [Austria data.gv.at](https://www.data.gv.at/)
- [Slovenia ARSO LiDAR](http://gis.arso.gov.si/evode/profile.aspx?id=atlas_voda_Lidar@Arso)
- [Poland Geoportal](https://www.geoportal.gov.pl/en/data/lidar-measurements-lidar/)
- [Czech Republic CUZK](https://geoportal.cuzk.cz/)
- [Slovakia Geoportal](https://www.geoportal.sk/en/zbgis/als/)
- [Romania ANCPI](https://geoportal.ancpi.ro/)
- [FABDEM Bristol](https://data.bris.ac.uk/data/dataset/s5hqmjcdj8yo2ibzi9b4ew3sn)
- [MERIT DEM](https://hydro.iis.u-tokyo.ac.jp/~yamadai/MERIT_DEM/)
- [ArcticDEM PGC](https://www.pgc.umn.edu/data/arcticdem/)
- [EarthDEM PGC](https://www.pgc.umn.edu/data/earthdem/)
- [Sonny's LiDAR DTMs](https://sonny.4lima.de/)
- [OpenDEM](https://www.opendem.info/)
- [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com/)
- [Google Earth Engine Elevation Catalog](https://developers.google.com/earth-engine/datasets/tags/elevation)
- [AWS Open Data Registry](https://registry.opendata.aws/)
- [Germany OpenDTM-DE](https://www.opendem.info/opendtm_de.html)
- [France RGE ALTI on GEE](https://gee-community-catalog.org/projects/france5m/)
- [FOMI Hungary](https://en.foldhivatal.hu/)
- [JRC LiDAR in Europe Report](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC126223/jrc126223_jrc126223_lidaropensourcedata.pdf)
