# GIS Data Cost & Structure Estimator — Tool Design Document

**Date:** 2026-03-31
**Purpose:** Design specification for a web-based tool that helps researchers estimate costs and plan data structures for GIS/remote sensing projects.

---

## 1. Market Gap Analysis

### 1.1 What Exists Today

| Tool | What it does | What it does NOT do |
|------|-------------|---------------------|
| **SkyFi** (skyfi.com) | Instant per-km² pricing for specific satellite orders (optical & SAR). Draw AOI, pick sensor, get price. | No project-level budgeting; no free-data recommendations; no data structure advice |
| **SkyWatch EarthCache** | API-based satellite data procurement starting at $10/km² | Commercial data only; no planning or advisory component |
| **Ongeo Intelligence** | Draw AOI, search archives, see per-image prices | Archive search only; no project planning |
| **SpyMeSat** | Mobile-first satellite image purchasing from $9.99 | Single-image purchase; no workflow planning |
| **Planet Pricing Page** | Subscription-based pricing (opaque; "contact sales") | No self-service cost estimation |
| **Airbus OneAtlas** | Archive browsing + tasking for Pleiades/SPOT | Requires account; no comparison with free alternatives |
| **Google Earth Engine Pricing** | EECU-hour based compute pricing | Only GEE costs; no data acquisition cost estimation |

### 1.2 The Gap

**No tool currently exists that:**
1. Takes a project description (domain, area, resolution, timeframe) as input
2. Recommends BOTH free and commercial data sources matched to the use case
3. Estimates total project cost (data + storage + processing)
4. Recommends data formats, projections, and processing pipelines
5. Lives as a free, open, citeable resource on a researcher's website

This is the gap we fill. Every existing tool is a sales funnel for a specific data vendor. Our tool is vendor-neutral and researcher-oriented.

---

## 2. Tool Name Candidates

| Name | Pros | Cons |
|------|------|------|
| **GeoDataPlanner** | Clear, descriptive | Generic |
| **EO Budget Calculator** | Precise for the EO community | Excludes non-EO GIS data |
| **DataScout** | Catchy, action-oriented | Too vague |
| **GeoDataCost** | Direct, SEO-friendly | Sounds like a price-comparison site |
| **The GIS Data Advisor** | Implies recommendation, not just pricing | Long |
| **SpatialBudget** | Clean, professional | May confuse with financial GIS |
| **GeoEstimator** | Short, memorable, clear | Slightly generic |

**Recommended name:** **GeoEstimator** — with subtitle: *"Plan your geospatial data needs, estimate costs, and find the right sources."*

Alternative: **EO Data Planner** if the audience is specifically the Earth observation community.

---

## 3. Feature Specification

### 3.1 Input Wizard — "What Do You Need?"

#### Step 1: Domain Selection

The user selects their application domain. This drives downstream recommendations.

| Domain | Typical data needs | Key sensors |
|--------|-------------------|-------------|
| **Agriculture / Precision Farming** | NDVI time series, soil moisture, weather | Sentinel-2, PlanetScope, MODIS, ERA5 |
| **Urban Planning** | Building footprints, land use, DSM | Pleiades Neo, WorldView, OpenStreetMap |
| **Flood Risk / Hydrology** | DEM, rainfall, river gauge, SAR for flood extent | Copernicus DEM, Sentinel-1, ERA5, local gauges |
| **Ecology / Biodiversity** | Land cover, habitat maps, phenology | Sentinel-2, Landsat, MODIS, GBIF |
| **Geology / Mining** | DEM, geological maps, hyperspectral, geophysics | ASTER, Sentinel-2 SWIR, national geological surveys |
| **Climate Analysis** | Temperature, precipitation, reanalysis grids | ERA5, CHIRPS, CRU, CMIP6 |
| **Forestry** | Canopy height, biomass, deforestation | Sentinel-1/2, GEDI, Global Forest Watch |
| **Disaster Response** | Rapid SAR, optical before/after | Sentinel-1, Copernicus EMS, ICEYE, Capella |
| **Coastal / Marine** | Bathymetry, SST, chlorophyll, shoreline change | Sentinel-2/3, Landsat, GEBCO |
| **Cultural Heritage / Archaeology** | High-res optical, DEM, LiDAR derivatives | Pleiades, drone LiDAR, national LiDAR |
| **General / Custom** | User specifies manually | — |

#### Step 2: Area of Interest

- **Quick selection:** Dropdown of countries/regions with pre-computed areas
- **Draw polygon:** Leaflet.js map with drawing tools; area auto-calculated in km²
- **Manual entry:** Type area in km² or hectares
- **Bounding box:** Enter NW and SE corner coordinates

Output: Area in km², centroid coordinates, UTM zone (for projection recommendation).

#### Step 3: Requirements Specification

**Spatial Resolution**

| Level | Resolution | Typical sensors | Cost class |
|-------|-----------|----------------|------------|
| Rough (landscape) | 250 m – 1 km | MODIS, VIIRS, ERA5 | Free |
| Medium (regional) | 10 – 30 m | Sentinel-2, Landsat 8/9 | Free |
| High (local) | 1 – 5 m | SPOT 6/7, RapidEye | €3–8 /km² |
| Very high (site) | 0.3 – 1 m | Pleiades, WorldView, SkySat | €8–30 /km² |
| Ultra high (object) | < 0.3 m | Pleiades Neo, WorldView-3 | €18–100 /km² |

**Temporal Frequency**

| Level | Frequency | Typical source | Notes |
|-------|-----------|---------------|-------|
| One-time snapshot | Single acquisition | Any | Cheapest option |
| Seasonal (4×/year) | Quarterly | Sentinel-2, Landsat | Free if 10-30m is sufficient |
| Monthly | 12×/year | Sentinel-2 (free), PlanetScope (commercial) | Free at 10m; ~$3-5/km²/month at 3m |
| Weekly | ~52×/year | PlanetScope, SkySat | Subscription required |
| Daily | 365×/year | PlanetScope, MODIS (250m) | PlanetScope subscription or MODIS (free, coarse) |
| Near real-time | Hours | Sentinel-1 (6-day), GOES (minutes, 1km) | SAR for all-weather; GOES for atmosphere only |

**Historical Depth**

| Depth | Available sources |
|-------|------------------|
| Current only | All sources |
| 5 years (2021–2026) | Sentinel-2, Landsat 8/9, PlanetScope |
| 10 years (2016–2026) | Sentinel-2 (from 2015), Landsat 8 (from 2013) |
| 20 years (2006–2026) | Landsat 7 (from 1999), MODIS (from 2000), ASTER |
| 30+ years (1990s–) | Landsat 5 (from 1984), AVHRR |
| 40+ years | Landsat MSS (from 1972, 60m), KH spy satellite declassified |

**Data Types Needed** (multi-select checkboxes)

- [ ] Optical imagery (visible + NIR)
- [ ] SAR (radar) imagery
- [ ] Digital Elevation Model (DEM/DSM/DTM)
- [ ] Climate / meteorological data
- [ ] Soil data
- [ ] Hydrology / water data
- [ ] Land use / land cover maps
- [ ] Administrative boundaries
- [ ] Geological maps
- [ ] LiDAR point clouds
- [ ] Hyperspectral imagery
- [ ] Population / demographic data

### 3.2 Output Panel — "Here's What We Recommend"

The output is organized into tabs/sections:

#### Tab 1: Recommended Free Data Sources

A table matched to the user's inputs:

| Data type | Source | Resolution | Temporal | Coverage | Access |
|-----------|--------|-----------|----------|----------|--------|
| Optical | Sentinel-2 L2A | 10 m | 5-day revisit | Global (land) | Copernicus Open Access Hub |
| Optical | Landsat 8/9 | 30 m | 8-day revisit | Global | USGS EarthExplorer |
| SAR | Sentinel-1C | 5–40 m | 6-day revisit | Global | Copernicus Hub |
| DEM | Copernicus GLO-30 | 30 m | Static (2021) | Global | Copernicus DEM |
| DEM | SRTM v3 | 30 m | Static (2000) | ±60° latitude | USGS |
| Climate | ERA5 | 31 km | Hourly, 1940–present | Global | Copernicus CDS |
| Soil | SoilGrids | 250 m | Static | Global | ISRIC |
| LULC | ESA WorldCover | 10 m | 2020, 2021 | Global | ESA |
| LULC | CORINE | 100 m | 2000–2018 | Europe | Copernicus |
| Population | WorldPop | 100 m | Annual | Global | WorldPop |
| Boundaries | GADM | Vector | Static | Global | gadm.org |
| Geology | OneGeology | Varies | Static | Global (patchy) | onegeology.org |

*Only rows matching the user's selected data types are shown.*

#### Tab 2: Commercial Alternatives (with estimated costs)

| Data type | Provider | Resolution | Price/km² (archive) | Price/km² (tasking) | Min order | Notes |
|-----------|----------|-----------|--------------------|--------------------|-----------|-------|
| Optical VHR | Maxar (WorldView) | 30–50 cm | $15–25 | $40–60 | 25 km² | Best archive depth |
| Optical VHR | Airbus Pleiades Neo | 30 cm | €18 | €25–40 | 25 km² (tasking) | Best European coverage |
| Optical VHR | Airbus Pleiades | 50 cm | €3.80–8 | €10–15 | None (archive) | Good budget VHR |
| Optical VHR | Planet SkySat | 50 cm | ~$8 | ~$12 | 5 km² | Via SkyFi |
| Optical HR | Planet PlanetScope | 3 m | Subscription | Subscription | Area-based | Daily global; contact sales |
| Optical HR | SPOT 6/7 | 1.5 m | €2.80 | €5–8 | 250 km² | Large area, lower res |
| SAR | ICEYE | 25 cm–1 m | ~$15–50 | ~$30–100 | 100 km² | X-band; 25cm spotlight |
| SAR | Capella Space | 50 cm | ~$15–30 | ~$30–60 | Scene-based | X-band; all-weather |
| SAR | Umbra | 1 m | ~$15 | ~$25 | 100 km² (10×10) | Budget SAR option |
| DEM | Airbus WorldDEM | 12 m | ~€5–10 | N/A | 100 km² | TanDEM-X derived |
| LiDAR | Airborne survey | 0.5–2 m | $500–2000 | Custom | Project-based | Requires flight planning |
| LiDAR | Drone survey | 2–5 cm | $200–800 | Custom | Per-day | < 5 km² practical |

#### Tab 3: Cost Breakdown Calculator

The tool computes an itemized estimate based on user inputs:

```
PROJECT COST ESTIMATE
=====================

Project: Monitoring 10,000 ha farmland for 5 years
Area: 100 km²
Period: 2026–2031

DATA ACQUISITION
─────────────────────────────────────────────────────────
Sentinel-2 imagery (10m, free)              €0
  └ ~60 scenes/year × 5 years = 300 scenes
Landsat 8/9 (30m, free, backup)             €0
ERA5 climate data (free)                    €0
Copernicus DEM GLO-30 (free)                €0

Option: PlanetScope 3m daily
  └ Annual subscription for 100 km²         ~€5,000/year
  └ 5-year total                            ~€25,000

Option: Pleiades 50cm (2 snapshots/year)
  └ 100 km² × €3.80 × 10 acquisitions      €3,800

STORAGE
─────────────────────────────────────────────────────────
Sentinel-2 tiles (100km² AOI)
  └ ~500 MB per tile × 300 tiles            ~150 GB
ERA5 climate grids                          ~2 GB
DEM                                         ~0.1 GB
Total raw storage                           ~152 GB
With processed derivatives (×2)             ~304 GB

PROCESSING
─────────────────────────────────────────────────────────
Google Earth Engine (free tier)              €0
  └ For academic/non-commercial use
OR
GEE Commercial
  └ Batch EECU: ~50 hrs × €0.40            ~€20
  └ Platform fee (Basic)                    ~€100/month

LOCAL PROCESSING
  └ QGIS (free)                              €0
  └ Cloud VM (optional): 100 hrs × €0.50   ~€50

─────────────────────────────────────────────────────────
TOTAL (free-data route):                     €0 – €50
TOTAL (with PlanetScope):                    ~€25,050
TOTAL (with Pleiades snapshots):             ~€3,850
```

#### Tab 4: Data Format & Projection Recommendations

Based on the AOI centroid, the tool recommends:

| Parameter | Recommendation | Rationale |
|-----------|---------------|-----------|
| **Coordinate system** | Auto-detected UTM zone (e.g., EPSG:32633 for Hungary) | Best metric accuracy for local analysis |
| **National projection** | EOV (EPSG:23700) for Hungary, Lambert-93 for France, etc. | Matches national datasets |
| **Raster format** | Cloud-Optimized GeoTIFF (COG) | Best interoperability; works with QGIS, GEE, Python |
| **Vector format** | GeoPackage (.gpkg) | Replaces shapefile; no file-size limits; single file |
| **Naming convention** | `{source}_{date}_{band}_{resolution}.tif` | Enables automated processing |
| **Folder structure** | `/raw/{source}/`, `/processed/`, `/derived/`, `/metadata/` | Keeps project organized |
| **Metadata standard** | ISO 19115 / STAC catalog | Machine-readable, searchable |

#### Tab 5: Data Gap Analysis

For each user-selected data type, flag what is NOT available for free:

| Need | Free option | Gap | Commercial solution |
|------|------------|-----|---------------------|
| Optical < 5m resolution | None | No free VHR optical | Pleiades archive from €3.80/km² |
| SAR < 5m resolution | None (Sentinel-1 is 5–40m) | No free high-res SAR | ICEYE, Capella, Umbra |
| Daily optical at 3m | None | PlanetScope is subscription | Planet Explorer subscription |
| DEM < 10m resolution | Country-specific LiDAR | Patchy global coverage | Airbus WorldDEM (12m), custom LiDAR |
| Historical data pre-1984 | None (Landsat MSS starts 1972 at 60m) | Very limited pre-satellite era | Aerial photo archives (national) |
| Real-time SAR | None | No free real-time SAR | ICEYE Rapid Tasking |

### 3.3 Example Budgets — Pre-built Scenarios

These are clickable presets that auto-fill the wizard:

#### Scenario 1: "Monitoring 10,000 ha Farmland for 5 Years"

- **Domain:** Agriculture
- **Area:** 100 km²
- **Resolution:** Medium (10m optical) + seasonal VHR snapshots
- **Temporal:** Weekly (vegetation season), monthly (off-season)
- **Data types:** Optical, climate, soil, DEM

| Component | Free route | Budget route | Premium route |
|-----------|-----------|-------------|---------------|
| Satellite imagery | Sentinel-2 (free) | + Pleiades 2×/yr (€760) | + PlanetScope daily (€5k/yr) |
| Climate data | ERA5 (free) | ERA5 (free) | ERA5 + local stations |
| DEM | Copernicus 30m (free) | + national LiDAR (free in many EU countries) | Drone LiDAR (€5k) |
| Processing | QGIS + GEE free | QGIS + GEE free | GEE commercial (€1.2k/yr) |
| Storage | 150 GB local | 300 GB local | 1 TB cloud (€300/yr) |
| **5-year total** | **~€0** | **~€4,500** | **~€35,000** |

#### Scenario 2: "Urban Heat Island Study for a European City"

- **Domain:** Urban planning / Climate
- **Area:** 500 km² (metro area)
- **Resolution:** High (thermal 100m from Landsat; 10m optical)
- **Temporal:** Summer months, 3-5 years
- **Data types:** Optical, thermal IR, DEM, land cover, population

| Component | Cost |
|-----------|------|
| Landsat 8/9 thermal (100m) | Free |
| Sentinel-2 optical (10m) | Free |
| ESA WorldCover land use | Free |
| Copernicus DEM | Free |
| WorldPop population | Free |
| ECOSTRESS thermal (70m, ISS) | Free |
| Optional: Aerial thermal survey | €10,000–30,000 |
| Processing (GEE free tier) | Free |
| **Total (remote sensing only)** | **€0** |
| **Total (with aerial thermal)** | **€10,000–30,000** |

#### Scenario 3: "Watershed Flood Risk Assessment"

- **Domain:** Hydrology / Flood risk
- **Area:** 2,000 km² (catchment)
- **Resolution:** Medium DEM (30m) or high DEM (5-12m)
- **Temporal:** Historical rainfall + SAR for flood mapping
- **Data types:** DEM, SAR, rainfall, river network, soil, land cover

| Component | Cost |
|-----------|------|
| Copernicus DEM GLO-30 | Free |
| Sentinel-1 SAR (flood extent) | Free |
| ERA5 precipitation | Free |
| CORINE / WorldCover land use | Free |
| EU-DEM (25m, Europe) | Free |
| SoilGrids | Free |
| Optional: Airbus WorldDEM (12m) | 2,000 km² × €5 = €10,000 |
| Optional: National LiDAR DEM | Free (varies by country) |
| HEC-RAS / LISFLOOD modeling | Free (open source) |
| **Total (free route)** | **€0** |
| **Total (with commercial DEM)** | **~€10,000** |

#### Scenario 4: "National-Scale Land Cover Change (Hungary)"

- **Domain:** Ecology / Land use
- **Area:** 93,000 km²
- **Resolution:** Medium (10-30m)
- **Temporal:** 1990, 2000, 2006, 2012, 2018, 2024
- **Data types:** Optical, land cover maps

| Component | Cost |
|-----------|------|
| CORINE Land Cover (all epochs) | Free |
| Landsat 5/7/8/9 archive | Free |
| Sentinel-2 (2015–present) | Free |
| ESA WorldCover 2020/2021 | Free |
| Dynamic World (Google, 10m) | Free |
| Processing via GEE | Free (academic) |
| Storage: ~2 TB | Local disk or cloud (~€50/yr) |
| **Total** | **€0–50** |

#### Scenario 5: "Geological Survey for Mining Exploration"

- **Domain:** Geology / Mining
- **Area:** 5,000 km² (concession area)
- **Resolution:** High (optical), medium (hyperspectral)
- **Temporal:** One-time + historical comparison
- **Data types:** Optical VHR, DEM, hyperspectral, geological maps, geophysics

| Component | Cost |
|-----------|------|
| ASTER VNIR+SWIR+TIR (15-90m) | Free |
| Sentinel-2 SWIR bands (20m) | Free |
| Landsat 8/9 (30m) | Free |
| Copernicus DEM (30m) | Free |
| National geological maps | Free (varies) |
| Optional: Pleiades Neo 30cm | 5,000 km² × €18 = €90,000 |
| Optional: WorldView-3 SWIR | 5,000 km² × €25 = €125,000 |
| Optional: Airborne hyperspectral | €50,000–200,000 |
| Optional: Airborne geophysics | €100,000–500,000 |
| **Total (free route)** | **€0** |
| **Total (with VHR optical)** | **€90,000–125,000** |
| **Total (full commercial survey)** | **€250,000–800,000** |

---

## 4. Pricing Data Reference Table (for internal calculation engine)

### 4.1 Commercial Optical Imagery (per km², archive pricing)

| Provider | Product | Resolution | Archive $/km² | Tasking $/km² | Min order |
|----------|---------|-----------|---------------|---------------|-----------|
| Maxar | WorldView-2/3 | 30–50 cm | $15–25 | $40–60 | 25 km² |
| Airbus | Pleiades Neo | 30 cm | €18 | €25–40 | 25 km² |
| Airbus | Pleiades 1A/1B | 50 cm | €3.80–8 | €10–15 | None |
| Airbus | SPOT 6/7 | 1.5 m | €2.80 | €5–8 | 250 km² |
| Planet | SkySat | 50 cm | ~$8 | ~$12 | 5 km² |
| Planet | PlanetScope | 3 m | Subscription | Subscription | Area-based |
| SkyFi | Multi-source VHR | 30–50 cm | $8–22.50 | $12–30 | 5 km² |
| SkyFi | Ultra-high | 7.5–10 cm | $100 | N/A | 1 km² |
| SI Imaging | KOMPSAT-3/3A | 40–70 cm | ~$8–12 | ~$15 | 25 km² |

### 4.2 Commercial SAR Imagery (per km²)

| Provider | Resolution | Archive $/km² | Tasking $/km² | Min order |
|----------|-----------|---------------|---------------|-----------|
| ICEYE | 25 cm (spotlight) | ~$30–50 | ~$50–100 | 100 km² |
| ICEYE | 1 m (stripmap) | ~$10–20 | ~$25–40 | 100 km² |
| Capella Space | 50 cm | ~$15–30 | ~$30–60 | Scene-based |
| Umbra | 1 m | ~$15 | ~$25 | 100 km² |

### 4.3 DEM Products

| Product | Resolution | Coverage | Cost |
|---------|-----------|----------|------|
| SRTM v3 | 30 m | ±60° latitude | Free |
| Copernicus GLO-30 | 30 m | Global | Free |
| NASADEM | 30 m | ±60° latitude | Free |
| ALOS World 3D | 30 m | Global | Free |
| ASTER GDEM v3 | 30 m | ±83° latitude | Free |
| EU-DEM v1.1 | 25 m | Europe | Free |
| Airbus WorldDEM | 12 m | Global | ~€5–10/km² |
| Airbus WorldDEM Neo | 5 m | On request | ~€15–25/km² |
| National LiDAR DEMs | 0.5–2 m | Country-specific | Free in many EU states |

### 4.4 Climate & Environmental Data

| Product | Resolution | Temporal | Cost |
|---------|-----------|----------|------|
| ERA5 | 31 km (~0.25°) | Hourly, 1940–present | Free |
| ERA5-Land | 9 km (~0.1°) | Hourly, 1950–present | Free |
| CHIRPS (rainfall) | 5 km | Daily, 1981–present | Free |
| CRU TS | 50 km (0.5°) | Monthly, 1901–present | Free |
| SoilGrids | 250 m | Static | Free |
| ISRIC soil data | Various | Static | Free |
| MODIS LST | 1 km | Daily | Free |
| ESA CCI soil moisture | 25 km | Daily, 1978–present | Free |

### 4.5 Storage Size Estimates

| Data source | Size per scene/tile | Coverage per scene |
|-------------|--------------------|--------------------|
| Sentinel-2 L2A | ~500 MB per 100×100 km tile | 100 × 100 km |
| Landsat 8/9 | ~920 MB compressed, 1.6 GB uncompressed | 185 × 180 km |
| Sentinel-1 GRD | ~1.5 GB | 250 × 250 km (IW mode) |
| MODIS | ~50 MB per tile | 10° × 10° |
| ERA5 (single variable, global) | ~50 MB per time step | Global |
| Copernicus DEM 30m | ~40 MB per 1° × 1° tile | 1° × 1° |
| Pleiades (50cm, pansharpened) | ~1.5 GB per 100 km² | ~20 × 5 km strip |

### 4.6 Processing Cost Estimates

| Platform | Pricing model | Approximate cost |
|----------|--------------|-----------------|
| Google Earth Engine (academic) | Free | $0 |
| Google Earth Engine (commercial) | EECU-hours | $0.40/batch-hr, $1.33/online-hr |
| GEE Basic plan | Monthly subscription | ~$100/month + overages |
| GEE Professional plan | Monthly subscription | ~$500/month + overages |
| AWS EC2 (r5.xlarge) | On-demand | ~$0.25/hour |
| Microsoft Planetary Computer | Free (with Hub) | $0 |
| Local QGIS / Python | Free software | $0 (hardware cost only) |

---

## 5. Formulas for the Cost Engine

### 5.1 Data Acquisition Cost

```
IF resolution_needed <= 10m AND source is Sentinel/Landsat:
    acquisition_cost = 0

IF resolution_needed < 10m:
    acquisition_cost = area_km2 × price_per_km2 × n_acquisitions

    WHERE price_per_km2 = lookup(provider, resolution, archive_vs_tasking)
    AND   n_acquisitions = temporal_frequency × years

    IF acquisition_cost < minimum_order_value:
        acquisition_cost = minimum_order_value
```

### 5.2 Storage Estimate

```
# For raster imagery
bytes_per_pixel = bit_depth / 8  (typically 2 bytes for 16-bit)
pixels_per_km2 = (1000 / resolution_m)²
scene_size_bytes = area_km2 × pixels_per_km2 × bytes_per_pixel × n_bands

total_storage = scene_size_bytes × n_acquisitions × processing_multiplier
WHERE processing_multiplier = 2.5  (raw + processed + derivatives)
```

### 5.3 Number of Scenes Estimate

```
# Sentinel-2
scenes_per_year = (365 / 5) × cloud_free_fraction
WHERE cloud_free_fraction ≈ 0.3 (Central Europe) to 0.8 (arid regions)

tiles_needed = CEIL(area_km2 / 10000)  # 100×100 km tiles

# Landsat
scenes_per_year = (365 / 16) × cloud_free_fraction × path_row_count
```

### 5.4 Quick Cost Formula (for back-of-envelope display)

```
total_project_cost ≈ data_cost + storage_cost + processing_cost

WHERE:
  data_cost = 0 (if free sources suffice)
            = area_km2 × price_per_km2 × n_acquisitions (if commercial)

  storage_cost = total_GB × $0.023/GB/month × months  (AWS S3 standard)
               = 0 (if local storage)

  processing_cost = 0 (if GEE academic or local QGIS)
                  = eecu_hours × $0.40 (if GEE commercial batch)
```

---

## 6. What Would Make This Tool Stand Out

### 6.1 Features That Make Researchers Bookmark It

1. **Vendor-neutral honesty.** The tool recommends free data first, commercial only when genuinely needed. No existing tool does this because they all sell data.

2. **Domain-specific presets.** Clicking "Flood Risk Assessment" auto-configures sensible defaults. No existing tool translates domain knowledge into data requirements.

3. **The "Can I do this for free?" answer.** For many research projects, the answer is yes. The tool makes this explicit and shows exactly how.

4. **Regional awareness.** For a Hungarian AOI, it recommends EOV projection (EPSG:23700), knows that FÖMI provides free LiDAR, and links to the relevant national data portals. For France, it recommends Lambert-93 and points to IGN data.

5. **Shareable project specifications.** The output generates a URL-encoded project spec that can be shared with collaborators or included in grant proposals. Example: `geoestimator.com/?domain=flood&area=2000&res=10m&temporal=monthly&years=5`

6. **Grant budget generator.** Export the cost estimate as a formatted table suitable for pasting into a funding application.

### 6.2 Making It Citeable

- Assign a DOI via Zenodo for the tool (not just the paper)
- Include a "How to cite" box: *"Surname, N. (2026). GeoEstimator: A Decision Support Tool for Geospatial Data Planning and Cost Estimation. https://doi.org/10.5281/zenodo.XXXXXXX"*
- Publish a companion methods paper describing the pricing model and decision logic
- Version the tool explicitly (v1.0, v1.1, etc.) so citations remain valid

### 6.3 Keeping It Maintainable

| Challenge | Solution |
|-----------|----------|
| Prices change | Store pricing in a single JSON file (`pricing.json`); update annually; show "Last updated" date prominently |
| New satellites launch | Maintain a `satellites.json` catalog; add entries without code changes |
| Free data sources appear/disappear | Linked to the Dataset Cadaster catalogs (see Section 8); one source of truth |
| Tool becomes stale | Add a "Report outdated info" button; crowdsource corrections |
| Provider URLs break | Use DOI/persistent identifiers where possible; link to search pages rather than deep links |

**Minimum maintenance commitment:** Update `pricing.json` once per year (takes ~2 hours). Major satellite launches warrant an immediate update.

---

## 7. Mockup Description — User Journey

### Screen 1: Landing Page

```
┌─────────────────────────────────────────────────────────────┐
│  GeoEstimator                                                │
│  Plan your geospatial data needs. Estimate costs.            │
│  Find the right sources.                                     │
│                                                              │
│  [Start Planning →]     [Browse Example Budgets]             │
│                                                              │
│  ── or try a quick example ──                                │
│  🌾 Farm monitoring  🏙️ Urban heat  🌊 Flood risk            │
│  🌍 Land cover change  ⛏️ Mining exploration                  │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐     │
│  │  "I saved 3 days of proposal writing. This tool     │     │
│  │   told me exactly what data I needed and what it     │     │
│  │   would cost."  — Researcher, University of Vienna  │     │
│  └─────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────┘
```

### Screen 2: Domain Selection (Step 1 of 3)

```
┌─────────────────────────────────────────────────────────────┐
│  Step 1 of 3: What is your project about?                    │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │  Agriculture  │  │ Urban Plan.  │  │  Flood Risk  │       │
│  │  & Farming    │  │ & Land Use   │  │  & Hydrology │       │
│  └──────────────┘  └──────────────┘  └──────────────┘       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │  Ecology &   │  │  Geology &   │  │   Climate    │       │
│  │  Biodiversity│  │   Mining     │  │   Analysis   │       │
│  └──────────────┘  └──────────────┘  └──────────────┘       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │  Forestry    │  │  Disaster    │  │  Coastal &   │       │
│  │              │  │  Response    │  │   Marine     │       │
│  └──────────────┘  └──────────────┘  └──────────────┘       │
│  ┌──────────────┐                                            │
│  │  Custom /    │                                            │
│  │  Other       │                                            │
│  └──────────────┘                                            │
│                                          [Next →]            │
└─────────────────────────────────────────────────────────────┘
```

### Screen 3: Area of Interest (Step 2 of 3)

```
┌─────────────────────────────────────────────────────────────┐
│  Step 2 of 3: Where is your area of interest?                │
│                                                              │
│  ┌────────────────────────────────────────────────┐          │
│  │                                                │          │
│  │         [Interactive Leaflet Map]               │          │
│  │         Draw polygon / rectangle                │          │
│  │         or search for a place                   │          │
│  │                                                │          │
│  │  📍 Search: [Budapest, Hungary          ]      │          │
│  └────────────────────────────────────────────────┘          │
│                                                              │
│  Or select a country: [Hungary              ▼]               │
│  Or enter area manually: [___100___] km²                     │
│                                                              │
│  Detected: Area = 100 km²                                    │
│            Centroid: 47.5°N, 19.1°E                          │
│            UTM Zone: 34N (EPSG:32634)                        │
│            National CRS: EOV (EPSG:23700)                    │
│                                                              │
│                              [← Back]  [Next →]             │
└─────────────────────────────────────────────────────────────┘
```

### Screen 4: Requirements (Step 3 of 3)

```
┌─────────────────────────────────────────────────────────────┐
│  Step 3 of 3: What do you need?                              │
│                                                              │
│  Spatial resolution:                                         │
│  ○ Rough (250m–1km)  ● Medium (10–30m)                      │
│  ○ High (1–5m)       ○ Very high (<1m)                      │
│                                                              │
│  How often:                                                  │
│  ○ One-time  ○ Seasonal  ● Monthly  ○ Weekly  ○ Daily       │
│                                                              │
│  How far back:                                               │
│  ○ Current only  ● 5 years  ○ 10 years  ○ 30+ years        │
│                                                              │
│  Data types needed:                                          │
│  ☑ Optical imagery     ☐ SAR imagery                        │
│  ☑ DEM                 ☑ Climate / weather                  │
│  ☑ Soil data           ☐ Hydrology                          │
│  ☐ Land cover maps     ☐ Admin boundaries                   │
│  ☐ Geological maps     ☐ LiDAR                              │
│  ☐ Hyperspectral       ☐ Population                         │
│                                                              │
│                              [← Back]  [Get Estimate →]     │
└─────────────────────────────────────────────────────────────┘
```

### Screen 5: Results Dashboard

```
┌─────────────────────────────────────────────────────────────┐
│  Your Data Plan                                              │
│  Agriculture | 100 km² near Budapest | 10m | Monthly | 5yr  │
│                                                              │
│  [Free Sources] [Commercial Options] [Cost Breakdown]        │
│  [Data Formats] [Gap Analysis] [Export for Grant]            │
│                                                              │
│  ── QUICK SUMMARY ──────────────────────────────────────     │
│  ✓ This project can be done ENTIRELY with free data          │
│    if 10m resolution is sufficient.                          │
│  △ Commercial data recommended only if you need              │
│    sub-5m resolution (add €3,800–25,000).                    │
│                                                              │
│  ── FREE SOURCES MATCHED ───────────────────────────────     │
│  ┌─────────────┬──────────┬──────────┬─────────────────┐    │
│  │ Data Type   │ Source   │ Res.     │ Access Link      │    │
│  ├─────────────┼──────────┼──────────┼─────────────────┤    │
│  │ Optical     │ Sent.-2  │ 10 m     │ [Copernicus Hub] │    │
│  │ Optical     │ Landsat 9│ 30 m     │ [EarthExplorer]  │    │
│  │ DEM         │ Cop.DEM  │ 30 m     │ [Copernicus]     │    │
│  │ Climate     │ ERA5     │ 31 km    │ [CDS]            │    │
│  │ Soil        │ SoilGrids│ 250 m    │ [ISRIC]          │    │
│  └─────────────┴──────────┴──────────┴─────────────────┘    │
│                                                              │
│  [📋 Copy to clipboard]  [📄 Export PDF]  [🔗 Share link]    │
└─────────────────────────────────────────────────────────────┘
```

---

## 8. Integration with the Dataset Cadaster

The GeoEstimator tool is the **interactive front-end** to the Dataset Cadaster catalog files. Here is how they connect:

### 8.1 Architecture

```
Dataset Cadaster (.md files)          GeoEstimator (web tool)
─────────────────────────────         ──────────────────────────
satellite_climate_soil_gaps.md   →    datasets.json (parsed)
DEM_LiDAR_Data_Sources.md       →       ↓
LULC_Data_Catalog.md             →    Recommendation engine
geology_geophysics_catalog.md    →    matches user needs to
air_quality_atmospheric.md       →    catalog entries
ocean_marine_bathymetry.md       →       ↓
admin_boundaries_cadastral.md    →    Results displayed in UI
population_urban_built.md        →
```

### 8.2 Data Flow

1. Each Dataset Cadaster `.md` file is parsed into a structured `datasets.json` containing:
   - Dataset name, provider, URL
   - Spatial resolution, temporal resolution, coverage
   - Cost (free / price per unit)
   - Data types / tags
   - Format, projection, access method

2. The GeoEstimator's recommendation engine queries `datasets.json` filtered by:
   - Data type matching (user selected → catalog tags)
   - Resolution compatibility (user needs ≤ dataset resolution)
   - Coverage check (AOI within dataset coverage)
   - Temporal compatibility (dataset period ≥ user's historical depth)

3. Results link back to the full catalog entry for detailed metadata.

### 8.3 Mutual Benefits

| Cadaster benefits from GeoEstimator | GeoEstimator benefits from Cadaster |
|-------------------------------------|-------------------------------------|
| Interactive discovery layer; people find datasets they didn't know existed | Comprehensive, curated dataset database; no need to build from scratch |
| Increased traffic and citations | Automatic updates when catalog is maintained |
| User feedback reveals catalog gaps | Domain-specific knowledge encoded in catalog structure |

---

## 9. Technical Implementation

### 9.1 Can It Be Static JavaScript?

**Yes.** The core tool can be entirely client-side:

| Component | Technology | Backend needed? |
|-----------|-----------|----------------|
| Wizard UI | HTML + CSS + vanilla JS (or Vue.js/Svelte) | No |
| Map / AOI drawing | Leaflet.js + Leaflet.Draw | No |
| Area calculation | Turf.js (client-side geospatial) | No |
| Pricing engine | JSON lookup + JS math | No |
| UTM zone detection | Simple formula from longitude | No |
| Results display | HTML tables + CSS | No |
| PDF export | jsPDF or html2canvas | No |
| Share links | URL query parameters | No |

**No backend is required.** This can be hosted as a static site on GitHub Pages, Netlify, or any web host.

### 9.2 Recommended Tech Stack

```
Framework:     Vanilla JS or Svelte (small bundle, fast)
Map:           Leaflet.js 1.9+ with Leaflet.Draw
Geospatial:    Turf.js (area calculation, centroid, UTM zone)
Styling:       Tailwind CSS or simple custom CSS
Data:          datasets.json + pricing.json (static files)
Build:         Vite (if using Svelte) or none (if vanilla)
Hosting:       GitHub Pages (free, version-controlled)
Analytics:     Plausible or Umami (privacy-friendly)
```

### 9.3 File Structure

```
geoestimator/
├── index.html
├── css/
│   └── style.css
├── js/
│   ├── app.js              # Main wizard logic
│   ├── map.js              # Leaflet map + drawing
│   ├── estimator.js        # Cost calculation engine
│   ├── recommendations.js  # Dataset matching logic
│   └── export.js           # PDF/clipboard export
├── data/
│   ├── datasets.json       # Parsed from Dataset Cadaster
│   ├── pricing.json        # Commercial pricing lookup
│   ├── domains.json        # Domain → default data types mapping
│   ├── projections.json    # Country → recommended CRS mapping
│   └── scenarios.json      # Pre-built example budgets
├── assets/
│   └── icons/              # Domain icons
└── README.md
```

### 9.4 Key JSON Structures

**pricing.json** (excerpt):
```json
{
  "last_updated": "2026-03-01",
  "optical": [
    {
      "provider": "Maxar",
      "product": "WorldView Archive",
      "resolution_m": 0.3,
      "price_per_km2_archive_usd": 20,
      "price_per_km2_tasking_usd": 50,
      "min_order_km2": 25,
      "currency": "USD"
    },
    {
      "provider": "Airbus",
      "product": "Pleiades Archive",
      "resolution_m": 0.5,
      "price_per_km2_archive_eur": 3.80,
      "price_per_km2_tasking_eur": 12,
      "min_order_km2": 0,
      "currency": "EUR"
    }
  ],
  "sar": [...],
  "dem": [...],
  "free_sources": [
    {
      "name": "Sentinel-2 L2A",
      "type": "optical",
      "resolution_m": 10,
      "revisit_days": 5,
      "archive_start": "2015-06-23",
      "coverage": "global_land",
      "access_url": "https://dataspace.copernicus.eu/",
      "file_size_mb_per_tile": 500,
      "tile_size_km": 100
    }
  ]
}
```

**domains.json** (excerpt):
```json
{
  "agriculture": {
    "label": "Agriculture & Farming",
    "default_data_types": ["optical", "climate", "soil", "dem"],
    "recommended_resolution": "medium",
    "recommended_temporal": "monthly",
    "key_indices": ["NDVI", "NDWI", "EVI"],
    "suggested_tools": ["Google Earth Engine", "QGIS", "Sen2Agri"],
    "typical_area_km2": [10, 1000]
  },
  "flood_risk": {
    "label": "Flood Risk & Hydrology",
    "default_data_types": ["dem", "sar", "climate", "lulc", "soil", "hydrology"],
    "recommended_resolution": "medium",
    "recommended_temporal": "event_based",
    "key_indices": ["TWI", "SPI", "CN"],
    "suggested_tools": ["HEC-RAS", "LISFLOOD", "QGIS", "Google Earth Engine"],
    "typical_area_km2": [100, 10000]
  }
}
```

### 9.5 Development Estimate

| Phase | Effort | Description |
|-------|--------|-------------|
| Phase 1: Core wizard + free data recommendations | 3–5 days | Static HTML/JS, 3-step wizard, free source matching |
| Phase 2: Commercial pricing + cost calculator | 2–3 days | pricing.json, cost formulas, output tables |
| Phase 3: Map integration + AOI drawing | 2 days | Leaflet.js, Turf.js area calculation |
| Phase 4: Example scenarios + export features | 1–2 days | Pre-built scenarios, PDF/clipboard export |
| Phase 5: Dataset Cadaster integration | 1–2 days | Parse .md catalogs to datasets.json |
| Phase 6: Polish + deploy | 1 day | Responsive design, GitHub Pages, analytics |
| **Total** | **10–15 days** | One developer, part-time |

---

## 10. Summary and Next Steps

### What makes this tool unique in the market

1. **It is the only vendor-neutral GIS data planning tool.** Every existing tool (SkyFi, SkyWatch, Ongeo) is a storefront. GeoEstimator is an advisor.
2. **It translates domain questions ("I study floods") into data specifications ("You need SAR + DEM + rainfall").** No existing tool does this.
3. **It answers the #1 question new researchers ask:** "Can I do this for free?" with a concrete yes/no and specific data sources.
4. **It produces grant-ready budget tables.** This alone makes it worth bookmarking.
5. **It connects to a living dataset catalog** (the Dataset Cadaster), making it a discovery tool, not just a calculator.

### Recommended next steps

1. **Build Phase 1** (wizard + free data recommendations) as a proof of concept
2. **Parse existing Dataset Cadaster .md files** into `datasets.json`
3. **Compile `pricing.json`** from the pricing data in this report
4. **Deploy on GitHub Pages** as a subdirectory of the Dataset Cadaster repository
5. **Get feedback** from 3–5 researchers before building the commercial pricing features
6. **Register a DOI** via Zenodo once the tool reaches v1.0

---

## Sources

- [Ongeo Intelligence — Satellite Image Cost & Pricing Guide 2025](https://ongeo-intelligence.com/blog/satellite-imagery-pricing-guide)
- [SkyFi Pricing](https://skyfi.com/en/pricing)
- [SkyFi 2025 Pricing PDF](https://skyfi.com/files/SkyFi_Pricing_2025.pdf)
- [SkyWatch EarthCache Pricing](https://skywatch.com/earthcache/pricing/)
- [SkyWatch — Satellite Imagery Pricing Factors & Cost Guide](https://skywatch.com/satellite-imagery-pricing-what-you-need-to-know/)
- [LAND INFO — Satellite Imagery Pricing](https://landinfo.com/satellite-imagery-pricing/)
- [Apollo Mapping — Simplified Maxar Pricing](https://apollomapping.com/blog/simplified-maxar-pricing-unveiled-in-december)
- [Geoimage — New Pricing on Maxar Satellite Data](https://geoimage.com.au/news/all-new-pricing-maxar-satellite-data)
- [Geoawesome — Demystifying Satellite Data Pricing](https://geoawesome.com/demystifying-satellite-data-pricing-a-comprehensive-guide/)
- [Nimbo — Satellite Imagery Pricing: Rethinking How We Buy EO Data](https://nimbo.earth/stories/satellite-imagery-pricing/)
- [Planet Pricing](https://www.planet.com/pricing/)
- [Airbus — Pleiades Neo](https://space-solutions.airbus.com/imagery/our-optical-and-radar-satellite-imagery/pleiades-neo/)
- [Airbus — Satellite Tasking](https://space-solutions.airbus.com/imagery/how-to-order-imagery-and-data/one-tasking/)
- [Apollo Mapping — Pleiades Neo](https://apollomapping.com/pleiades-neo-satellite)
- [SpyMeSat Pricing](https://www.spymesat.com/pricing.html)
- [Google Earth Engine Pricing](https://cloud.google.com/earth-engine/pricing)
- [GEE Cost Controls](https://developers.google.com/earth-engine/guides/cost_controls)
- [USGS — Landsat File Sizes](https://www.usgs.gov/faqs/what-are-landsat-collection-1-level-1-data-product-file-sizes)
- [Sentinel-2 Wikipedia](https://en.wikipedia.org/wiki/Sentinel-2)
- [EOS — Spatial Resolution in Remote Sensing](https://eos.com/blog/spatial-resolution/)
- [EOS — Free Satellite Imagery Sources](https://eos.com/blog/free-satellite-imagery-sources/)
- [Off-Nadir Delta — DEM Comparison](https://offnadir-delta.com/blog/digital-elevation-models-dem-comparison)
- [Off-Nadir Delta — SAR vs Optical](https://offnadir-delta.com/blog/sar-vs-optical-when-to-use-which)
- [ESA — Newcomers Earth Observation Guide](https://business.esa.int/newcomers-earth-observation-guide)
- [NASA Earthdata — EO Data Basics](https://www.earthdata.nasa.gov/learn/earth-observation-data-basics)
- [Think Onward — Satellite Imagery 101](https://thinkonward.com/resources/content-hub/satellite-imagery-101-your-intro-guide-to-choosing-the-right-data)
- [UP42 — Guide to Buying Satellite Imagery](https://up42.com/blog/a-definitive-guide-to-buying-and-using-satellite-imagery)
- [Adam Keith — The Problem of EO Data Pricing](https://medium.com/@adamkeithspace/the-problem-of-eo-data-pricing-58d96ab7e29d)
- [GeoNetwork OpenSource](https://geonetwork-opensource.org/)
- [Penn State GEOG 871 — Cost Management](https://www.e-education.psu.edu/geog871/l6_p3.html)
- [GIS Geography — 15 Free Satellite Imagery Sources](https://gisgeography.com/free-satellite-imagery-data-list/)
- [Robin Wilson — Free GIS Datasets](https://freegisdata.rtwilson.com/)
- [XR Tech Group — Satellite Imagery Pricing Guide 2026](https://xrtechgroup.com/what-is-satellite-imagery-pricing/)
