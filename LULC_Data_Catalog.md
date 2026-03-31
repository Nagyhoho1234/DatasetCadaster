# Land Use and Land Cover (LULC) Dataset Catalog

Compiled: 2026-03-31

---

## Summary Table

| # | Platform | URL | Scope | Data Type | Spatial Res. | Temporal Res. | Cost | API | Key Datasets | Notes |
|---|----------|-----|-------|-----------|-------------|---------------|------|-----|--------------|-------|
| 1 | **CORINE Land Cover (CLC)** | [land.copernicus.eu](https://land.copernicus.eu/en/products/corine-land-cover) | Europe (EEA39) | Vector + 100m raster, change maps | 100m raster; MMU 25 ha (vector) | 6-year cycle (1990, 2000, 2006, 2012, 2018; 2024 in production) | Free | Yes (WMS, WCS, CLMS API, OData) | CLC status layers, CLC change layers | 44 classes. GeoPackage/GeoTIFF. Open Copernicus license. Also on Google Earth Engine. |
| 2 | **CLCplus Backbone** | [land.copernicus.eu](https://land.copernicus.eu/en/products/clc-backbone) | Europe | Raster | 10m | 2-3 year cycle (2018, 2021, 2023) | Free | Yes (WMS, WEkEO, CDSE) | CLCplus Backbone status layers | 11 basic LC classes from Sentinel-2. Requires WEkEO login. OA >90%. |
| 3 | **ESA WorldCover** | [esa-worldcover.org](https://esa-worldcover.org/en/data-access) | Global | Raster | 10m | 2020, 2021 | Free | Yes (AWS S3, GEE, Terrascope) | WorldCover v100 (2020), v200 (2021) | 11 classes. COG tiles 3x3 deg. CC-BY 4.0. Also on Zenodo. |
| 4 | **ESA CCI Land Cover** | [climate.esa.int](https://climate.esa.int/en/projects/land-cover/data/) | Global | Raster, time series | 300m | Annual (1992-2022) | Free | Yes (CDS API, WMS) | Annual LC maps v2.0.7 (1992-2015), v2.1.1 (2016+) | 22 classes (UN-LCCS). NetCDF4 / GeoTIFF. Part of ESA Climate Change Initiative. |
| 5 | **Copernicus Global Land Cover (CGLS-LC100)** | [land.copernicus.eu](https://land.copernicus.eu/en/products/global-dynamic-land-cover) | Global | Raster + fractional cover | 100m | Annual (2015-2019) | Free | Yes (GEE, CDSE, OData) | LC100 Collection 3 (2015-2019) | 23 classes from PROBA-V. Includes discrete + fractional cover layers. |
| 6 | **MODIS Land Cover (MCD12Q1)** | [earthdata.nasa.gov](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mcd12q1-061) | Global | Raster, time series | 500m | Annual (2001-2024) | Free | Yes (AppEEARS, GEE, LAADS DAAC) | MCD12Q1 v6.1 | 5 classification schemes (IGBP, UMD, LAI, BGC, PFT). HDF5. Note: reduced accuracy post-2020 due to unfunded training updates. |
| 7 | **GlobeLand30** | [globallandcover.com](http://www.globallandcover.com/home_en.html) | Global | Raster | 30m | 2000, 2010, 2020 | Free (registration required) | No | GlobeLand30 status layers | 10 classes. GeoTIFF. Developed by NGCC (China). Login approval required. |
| 8 | **GLAD GLCLUC** | [glad.umd.edu](https://glad.umd.edu/dataset/GLCLUC2020) | Global | Raster, change maps | 30m | 2000, 2005, 2010, 2015, 2020 | Free | Yes (GEE) | Global Land Cover and Land Use Change 2000-2020 v2 | Forest, cropland, built-up, water, snow/ice. CC-BY. 10x10 deg tiles. UInt8. |
| 9 | **Dynamic World (Google)** | [dynamicworld.app](https://dynamicworld.app/) | Global | Raster, near-real-time | 10m | Per Sentinel-2 image (2015-present) | Free | Yes (GEE API) | Dynamic World V1 | 9 classes + probability bands. Near-real-time. Sentinel-2 based. CC-BY 4.0. |
| 10 | **Esri Land Cover** | [livingatlas.arcgis.com](https://livingatlas.arcgis.com/landcoverexplorer/) | Global | Raster, time series | 10m | Annual (2017-2024) | Free | Yes (ArcGIS REST, GEE) | Sentinel-2 10m LULC time series v3 | 9-10 classes. Impact Observatory deep learning model. ~75% global accuracy. Accessible via ArcGIS Living Atlas. |
| 11 | **GLC_FCS30D** | [zenodo.org](https://doi.org/10.5281/zenodo.12779975) | Global | Raster, time series, change | 30m | 1985-2022 (5-yr before 2000, annual after) | Free | Yes (GEE) | GLC_FCS30D v1 | 35 fine LC subcategories. Landsat-based. OA 80.88%. Continuous change detection. |
| 12 | **GLC_FCS10** | [zenodo.org](https://doi.org/10.5281/zenodo.14729665) | Global | Raster | 10m | 2023 | Free | Yes (GEE) | GLC_FCS10 2023 | 30 fine LC types. Sentinel-1+2 based. OA 83.16%. Published 2025. |
| 13 | **FROM-GLC** | [data.starcloud.pcl.ac.cn](http://data.starcloud.pcl.ac.cn/) | Global | Raster | 10m / 30m | 2010, 2015, 2017 | Free | No | FROM-GLC10, FROM-GLC30, FROM-GLC Plus | Tsinghua University. Migrated to StarCloud platform. 10 classes. |
| 14 | **GLC-SHARE (FAO)** | [data.apps.fao.org](https://data.apps.fao.org/catalog/dataset/global-land-cover-share-database) | Global | Raster (fractional) | ~1 km (30 arc-sec) | Single epoch (~2014) | Free | No | GLC-SHARE v1.0 | 11 classes as % cover per pixel. GeoTIFF. Synthesis of best-available national datasets. |
| 15 | **EarthEnv Consensus LC** | [earthenv.org](https://www.earthenv.org/landcover) | Global | Raster (fractional) | ~1 km (30 arc-sec) | Single epoch (~2005) | Free | Yes (GEE) | Consensus Land Cover | 12 classes. Integrates GlobCover, MODIS, GLC2000, DISCover. Full + reduced versions. CC0. |
| 16 | **Copernicus Urban Atlas** | [land.copernicus.eu](https://land.copernicus.eu/en/products/urban-atlas) | Europe (FUA cities) | Vector, change maps | MMU 0.25 ha (urban), 1 ha (rural) | 3-6 yr cycle (2006, 2012, 2018, 2021) | Free | Yes (WMS, CDSE) | Urban Atlas status + change layers | ~800 FUAs. 17+ urban LC classes. Based on 2-4m satellite imagery. Very high detail. |
| 17 | **Copernicus Riparian Zones** | [land.copernicus.eu](https://land.copernicus.eu/en/products/riparian-zones) | Europe (rivers Strahler 2-8) | Vector + raster | Scale 1:10,000 | 6-yr cycle (2012, 2018) | Free | Yes (WMS, CLMS API) | RZ LCLU status + change layers | Detailed LCLU for riparian corridors. SHP/GeoTIFF. |
| 18 | **Copernicus Coastal Zones** | [land.copernicus.eu](https://land.copernicus.eu/en/products/coastal-zones) | Europe (10 km from coast) | Vector + raster | Scale 1:10,000 | 6-yr cycle (2012, 2018) | Free | Yes (WMS, CLMS API) | CZ LCLU status + change layers | Detailed LCLU for 10 km coastal strips. SHP/GeoTIFF. |
| 19 | **NLCD (US)** | [mrlc.gov](https://www.mrlc.gov/data) | USA (CONUS, AK, HI) | Raster, time series, change | 30m | Annual (1985-2024); legacy: 2001-2021 snapshots | Free | Yes (WMS) | Annual NLCD CU v1.1, Impervious Surface, Tree Canopy, Rangeland | 16 Anderson-based classes. Landsat-derived. GeoTIFF. |
| 20 | **S2GLC** | [s2glc.cbk.waw.pl](https://s2glc.cbk.waw.pl/) | Europe | Raster | 10m | 2017 | Free | Yes (WMS via CREODIAS) | S2GLC 2017 Land Cover Map of Europe | 13 classes. OA 86%. Single GeoTIFF mosaic ~8 GB. ESA-funded. |
| 21 | **LUCAS Survey** | [ec.europa.eu/eurostat](https://ec.europa.eu/eurostat/web/lucas) | EU | Point survey (in-situ) | Point-based (~1.1M points) | 3-yr cycle (2006, 2009, 2012, 2015, 2018, 2022, 2025) | Free | No (bulk CSV/microdata download) | LUCAS microdata, topsoil data (ESDAC) | In-situ field survey. Photos + LC/LU classification. Ideal for training/validation. Panel component added 2025. |
| 22 | **HILDA+** | [doi.pangaea.de](https://doi.org/10.1594/PANGAEA.974335) | Global | Raster, time series | 1 km | Annual (1960-2020; extended 1899-2019 in NetCDF) | Free | No | HILDA+ v2.0 | 6 generic LU classes. Reconstruction-based. GeoTIFF + NetCDF. CC-BY 4.0. |
| 23 | **HYDE** | [pbl.nl](https://www.pbl.nl/en/hyde-history-database-of-the-global-environment) | Global | Raster, time series | 5 arc-min (~10 km) | 10,000 BCE - 2023 CE (variable steps) | Free | No | HYDE v3.3 | Cropland, pasture, population, built-up. ESRI ASCII grid. Utrecht Univ. / PBL. Deep historical coverage. |
| 24 | **OpenLandMap** | [openlandmap.org](https://openlandmap.org/) | Global | Raster, multi-theme | 30m - 1 km (varies) | Varies by layer | Free | Yes (REST API, STAC, GEE) | Land cover, soil, climate, vegetation layers | Aggregator platform. COGs on S3. OpenGeoHub Foundation. |
| 25 | **MapBiomas** | [mapbiomas.org](https://brasil.mapbiomas.org/en/downloads/) | South America, Indonesia | Raster, time series, change | 30m | Annual (1985-present) | Free | Yes (GEE) | Annual LC maps per biome/country | 20+ classes. Landsat-based. Also fire, deforestation, water, mining alerts. CC-BY-SA. |
| 26 | **Copernicus Data Space Ecosystem** | [dataspace.copernicus.eu](https://dataspace.copernicus.eu/) | Global/Europe | Multi-format | Varies | Varies | Free | Yes (STAC, openEO, OGC WMS/WCS, Sentinel Hub) | All Copernicus + CLMS products | Central hub for all Copernicus data. Browser, APIs, Jupyter. Migration completing 2025. |
| 27 | **Geo-harmonizer / ODSE** | [opendatascience.eu](https://opendatascience.eu/) | Europe | Raster | 30m | Annual (2000-2019) | Free | No (COG download) | Annual LC maps 33 CLC-compatible classes | EML-based. Czech Technical Univ. Project closed; data archived on maps.opendatascience.eu. Succeeded by Open Earth Monitor. |

---

## Detailed Platform Notes

### API Protocol Summary

| Platform | WMS | WCS | STAC | REST | GEE | S3/COG | Other |
|----------|-----|-----|------|------|-----|--------|-------|
| CORINE / CLMS products | Y | Y | Y | Y (CLMS API) | Y | - | OData |
| ESA WorldCover | - | - | - | - | Y | Y (AWS) | Zenodo |
| ESA CCI LC | Y | - | - | Y (CDS API) | Y | - | - |
| CGLS-LC100 | - | - | - | Y (OData) | Y | - | CDSE |
| MODIS MCD12Q1 | - | - | - | Y (AppEEARS) | Y | - | LAADS DAAC |
| Dynamic World | - | - | - | - | Y | - | - |
| Esri LC | - | - | - | Y (ArcGIS REST) | Y | - | Living Atlas |
| OpenLandMap | - | - | Y | Y | Y | Y | - |
| NLCD | Y | - | - | - | Y | - | mrlc.gov viewer |
| Copernicus Data Space | Y | Y | Y | Y | - | - | openEO, Sentinel Hub |

### National / Regional Datasets for Central/Eastern Europe

Most Central and Eastern European countries (Hungary, Czechia, Poland, Slovakia, Romania, etc.) rely on:

1. **CORINE Land Cover** -- pan-European coverage since 1990, consistent across all EEA member states
2. **CLCplus Backbone** -- 10m upgrade for Europe
3. **Urban Atlas** -- detailed LULC for functional urban areas
4. **LUCAS survey** -- in-situ validation points
5. **Geo-harmonizer / ODSE** -- annual 30m maps 2000-2019 for continental Europe
6. **S2GLC** -- 10m European map for 2017
7. **Historical Carpathian Dataset** -- 91,310 points across 7 countries (1819-1980), available at [tandfonline.com](https://www.tandfonline.com/doi/full/10.1080/17445647.2018.1502099)

No standalone national LULC portals were identified for Hungary, Czechia, or Poland beyond what is provided through Copernicus/EEA programs.

### Historical Land Use Datasets

| Dataset | Period | Resolution | Scope | Classes |
|---------|--------|-----------|-------|---------|
| HYDE v3.3 | 10,000 BCE - 2023 CE | 5 arc-min (~10 km) | Global | Cropland, pasture, population, built-up |
| HILDA+ v2.0 | 1899/1960 - 2020 | 1 km | Global | 6 generic LU types |
| Historical Carpathian | 1819 - 1980 | Point-based | Central Europe | Multiple LU classes |
| GLC_FCS30D | 1985 - 2022 | 30m | Global | 35 fine LC types |
| NLCD Annual | 1985 - 2024 | 30m | USA | 16 classes |

### License Summary

All datasets listed above are **free and open access**. Most use CC-BY 4.0 or equivalent open licenses. GlobeLand30 requires registration and administrator approval but is free for research. The Copernicus datasets follow the Copernicus data policy (full, open, free access). LUCAS microdata is available under Eurostat's open data policy.

---

Sources:
- [CORINE Land Cover - Copernicus](https://land.copernicus.eu/en/products/corine-land-cover)
- [CLCplus Backbone - Copernicus](https://land.copernicus.eu/en/products/clc-backbone)
- [ESA WorldCover](https://esa-worldcover.org/en/data-access)
- [ESA CCI Land Cover](https://climate.esa.int/en/projects/land-cover/data/)
- [Copernicus Global Dynamic Land Cover](https://land.copernicus.eu/en/products/global-dynamic-land-cover)
- [MODIS MCD12Q1 - NASA Earthdata](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mcd12q1-061)
- [GlobeLand30](http://www.globallandcover.com/home_en.html)
- [GLAD GLCLUC 2020](https://glad.umd.edu/dataset/GLCLUC2020)
- [Dynamic World](https://dynamicworld.app/)
- [Esri Land Cover Explorer](https://livingatlas.arcgis.com/landcoverexplorer/)
- [GLC_FCS30D - ESSD](https://essd.copernicus.org/articles/16/1353/2024/)
- [GLC_FCS10 - ESSD](https://essd.copernicus.org/articles/17/4039/2025/)
- [FROM-GLC - StarCloud](http://data.starcloud.pcl.ac.cn/)
- [GLC-SHARE - FAO](https://data.apps.fao.org/catalog/dataset/global-land-cover-share-database)
- [EarthEnv Consensus Land Cover](https://www.earthenv.org/landcover)
- [Urban Atlas - Copernicus](https://land.copernicus.eu/en/products/urban-atlas)
- [Riparian Zones - Copernicus](https://land.copernicus.eu/en/products/riparian-zones)
- [Coastal Zones - Copernicus](https://land.copernicus.eu/en/products/coastal-zones)
- [NLCD - MRLC](https://www.mrlc.gov/data)
- [S2GLC](https://s2glc.cbk.waw.pl/)
- [LUCAS - Eurostat](https://ec.europa.eu/eurostat/web/lucas)
- [HILDA+ - PANGAEA](https://doi.org/10.1594/PANGAEA.974335)
- [HYDE - PBL](https://www.pbl.nl/en/hyde-history-database-of-the-global-environment)
- [OpenLandMap](https://openlandmap.org/)
- [MapBiomas](https://brasil.mapbiomas.org/en/downloads/)
- [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/)
- [Open Data Science Europe](https://opendatascience.eu/)
- [CLMS API Documentation](https://eea.github.io/clms-api-docs/download.html)
