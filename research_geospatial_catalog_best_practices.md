# Geospatial / Environmental Dataset Catalog: Best Practices Research Report

*Compiled 2026-03-31*

---

## 1. Academic / Research Dataset Portals

### 1.1 Robin Wilson's Free GIS Data List
- **URL**: https://freegisdata.rtwilson.com/
- **Creator**: Dr Robin Wilson (individual researcher)
- **Presentation**: Single long page with categorized links. No cards or grid -- just a structured list with hyperlinked dataset names and 1-2 sentence descriptions per entry.
- **Organization**: Three top-level groups:
  - *Physical Geography* (11 subcategories: elevation, weather/climate, hydrology, land cover, ecology, natural disasters, etc.)
  - *Human Geography* (11 subcategories: administrative boundaries, population, buildings/roads/POI, transport, etc.)
  - *Country-Specific* (60+ regions, alphabetical)
- **Navigation**: Dropdown menus for section jumping. No full-text search -- author explicitly recommends browser Ctrl+F.
- **Metadata shown**: Brief description, sometimes resolution/format/temporal coverage, notes on registration requirements.
- **Tech stack**: Static HTML, Bootstrap CSS, Matomo analytics. No database, no JavaScript framework.
- **Strengths**:
  - Extremely fast to load and search (no JS overhead)
  - 500+ datasets, well-maintained (last updated July 2025)
  - Concise expert-written descriptions add genuine value over raw link dumps
  - Low maintenance burden (just HTML)
- **Weaknesses**:
  - No filtering, sorting, or faceted search
  - No spatial preview or coverage maps
  - No structured metadata (resolution, temporal range, file size, API availability)
  - Relies entirely on manual curation for updates

### 1.2 Awesome GEE Community Catalog
- **URL**: https://gee-community-catalog.org/
- **Creator**: Samapriya Roy (individual researcher, unfunded open-source project)
- **Presentation**: Documentation-style site with hierarchical navigation. Each dataset gets its own page with detailed description, code snippets, and preview images.
- **Organization**: Thematic categories:
  - Population & Socioeconomic
  - Geophysical, Biological & Biogeochemical
  - Elevation and Bathymetry
  - Soil Properties
  - Land Use / Land Cover (global + regional)
  - Hydrology, Oceans and Shorelines
  - Agriculture, Vegetation and Forestry
  - Weather and Climate
  - Fire Monitoring
  - Biodiversity, Ecosystems & Habitat
  - Utilities, Assets and Amenities
  - Analysis Ready Data
  - Global Events
- **Key UI/UX features**:
  - AI-powered search ("Ask AI" floating button)
  - Community chat integration (floating button with randomized Google-palette colors)
  - Tutorials, changelog, publications sections
  - Rotating promotional banner (12-second cycle)
  - Insider/premium datasets section
  - Table of contents sidebar for navigation
- **Tech stack**: Material for MkDocs (Python-based static site generator), Google Analytics, LocalStorage for preferences.
- **Strengths**:
  - Rich per-dataset documentation with GEE code examples
  - Community-driven contribution model
  - AI search is a differentiator
  - Professional look despite being a single-person project
- **Weaknesses**:
  - Search is AI-based rather than structured faceted search
  - No map-based spatial browsing
  - No standardized metadata cards (each page is free-form)

### 1.3 Radiant Earth MLHub / Source Cooperative
- **URL**: https://mlhub.earth/ (legacy) / https://source.coop (current)
- **Creator**: Radiant Earth Foundation (nonprofit organization)
- **Presentation**: Card-based grid layout with featured products section. Each card shows title, description, organization, publication date, tags.
- **Organization**: Tag-based filtering (e.g., "sst", "nasa", "land cover", "pmtiles"). Products listed with organization/account attribution.
- **Key UI/UX features**:
  - Tag-based clickable filters
  - Cloud data access credentials per repository
  - File preview capability (Cloud-optimized GeoTIFFs, GeoJSON, Zarr)
  - Dark/light theme toggle
  - STAC-compliant API backend
  - Self-service organizational profiles
- **Tech stack**: Next.js with React Server Components, Radiant Design System, TypeScript.
- **Metadata shown**: Title, description, provider organization, publication date, visibility status (public/private), tags, data modality.
- **Strengths**:
  - Modern tech stack and clean design
  - STAC compliance ensures interoperability
  - File-level previews for geospatial formats
  - Scales to petabyte-class (1PB+ as of 2025)
- **Weaknesses**:
  - Requires authentication for data access credentials
  - Less intuitive for non-technical users

---

## 2. Institutional Data Discovery Tools

### 2.1 NASA Earthdata Search
- **URL**: https://search.earthdata.nasa.gov/
- **Creator**: NASA EOSDIS
- **Presentation**: Three-panel layout:
  - Left panel: search/filter controls
  - Center panel: results list (switchable between list and table view)
  - Right panel: interactive map
- **Organization**: 54,000+ collections, 1 billion+ data granules. Organized by topics, platforms, instruments, processing levels.
- **Key UI/UX features**:
  - Full-text keyword search
  - Date range selection (calendar widget)
  - Geographic search: draw polygons, rectangles, points, circles on map, or upload shapefiles
  - Faceted filtering by topic, platform, instrument, data center
  - Save and share projects
  - Data subscriptions (notifications for new data)
  - Customizable preferences (sorting, map views)
  - Consistent design via EUI (Earthdata User Interface) library
- **Tech stack**: Custom React application, EUI component library, Leaflet for maps.
- **Metadata shown**: Collection title, temporal range, spatial coverage (on map), data center, processing level, granule count.
- **Strengths**:
  - Gold standard for geospatial data discovery at scale
  - Spatial search is deeply integrated
  - Accessible and well-documented
  - Consistent design language across all NASA Earth science sites
- **Weaknesses**:
  - Complexity can overwhelm casual users
  - Focused on NASA data only

### 2.2 Google Earth Engine Data Catalog
- **URL**: https://developers.google.com/earth-engine/datasets/catalog
- **Creator**: Google
- **Presentation**: Responsive card grid layout. Each card has:
  - Thumbnail preview image
  - Dataset title
  - Brief description (truncated)
  - Multiple tags
  - Click-through to detailed page
- **Organization**: Multiple discovery paths:
  - By category (thematic)
  - By tag (searchable tag chips: "arctic", "elevation", "nasa", etc.)
  - By collection (Landsat, MODIS, Sentinel)
  - By publisher
  - All datasets view
- **Key UI/UX features**:
  - Tag chip buttons with hover effects
  - "Open in Earth Engine" one-click action
  - Dataset suggestion mechanism for missing data
  - Changelog and dataset status tracking
  - Clean card grid with CSS Grid (minmax 256px columns)
- **Tech stack**: Standard web (HTML/CSS/JS), Google's developer site framework. STAC metadata backend.
- **Metadata shown per card**: Title, thumbnail, description snippet, tags. Detail pages show: resolution, temporal range, bands, provider, citation, code examples.
- **Strengths**:
  - Excellent visual design with preview thumbnails
  - Tags provide flexible cross-cutting discovery
  - Direct integration with analysis platform (GEE)
  - Comprehensive per-dataset documentation
- **Weaknesses**:
  - Only datasets available in GEE
  - No spatial/map-based browsing in the catalog itself

### 2.3 Microsoft Planetary Computer
- **URL**: https://planetarycomputer.microsoft.com/catalog
- **Creator**: Microsoft
- **Presentation**: Two main interfaces:
  1. *Data Catalog*: browseable list of datasets with descriptions
  2. *Explorer*: two-pane interface (dataset selector + interactive map)
- **Organization**: Datasets organized by environmental domain. STAC-compliant backend.
- **Key UI/UX features**:
  - Explorer with date picker and visualization layer selector
  - Map-based spatial exploration (Azure Maps)
  - GeoParquet vector rendering support
  - Dataset preview and item-level preview via Data API
  - Feature flag system for gradual rollouts
  - Jupyter notebook integration for analysis
- **Tech stack**: React (Create React App), TypeScript (75.8% of codebase), Azure Functions backend, Azure Maps, Cypress for testing, Docker, GitHub Actions CI/CD to Azure Static Web Apps. **Fully open-source** on GitHub.
- **Metadata shown**: Dataset title, description, spatial coverage, temporal range, provider, license, bands/variables, example notebooks.
- **Strengths**:
  - Open-source codebase (reusable!)
  - Tight integration between catalog and visual explorer
  - STAC-native architecture
  - Supports both raster and vector data preview
- **Weaknesses**:
  - Heavy client-side application (requires JS)
  - Azure-specific infrastructure dependencies

### 2.4 Copernicus Data Space Ecosystem Browser
- **URL**: https://browser.dataspace.copernicus.eu/
- **Creator**: ESA / European Commission
- **Presentation**: Full-screen map-based interface with sidebar panels for data selection and configuration.
- **Organization**: By satellite mission/collection (Sentinel-1, 2, 3, 5P, etc.)
- **Key UI/UX features**:
  - Multi-language support
  - Spectral Explorer (view spectral signatures of selected regions)
  - Statistical Info tool (time-series analysis of pixel values)
  - Measurement tools (distance and area)
  - Elevation profile tool
  - Pin/bookmark system (save visualizations, export/import as JSON)
  - Cloud coverage filter
  - Direct download + workspace integration
  - Band combination customization
- **Tech stack**: Custom web application (Sentinel Hub technology).
- **Strengths**:
  - Extremely powerful analysis tools built into the browser
  - No download needed for basic analysis
  - Professional-grade visualization
- **Weaknesses**:
  - Steep learning curve
  - Not a "catalog" in the traditional browseable sense -- more of an analysis tool
  - Requires registration for full functionality

### 2.5 USGS EarthExplorer
- **URL**: https://earthexplorer.usgs.gov/
- **Creator**: USGS EROS
- **Presentation**: Step-by-step wizard interface (Search Criteria -> Data Sets -> Additional Criteria -> Results).
- **Key UI/UX features**:
  - Map-based area of interest selection (point, polygon, address, coordinates)
  - Date range filtering
  - 120+ datasets searchable simultaneously
  - Browse/preview images
  - Metadata export
  - Bulk download application (web-based, no install)
  - Scene list upload for batch operations
- **Strengths**:
  - Proven workflow for large-scale data ordering
  - Available 24/7
  - Supports bulk operations
- **Weaknesses**:
  - Dated UI design
  - Wizard workflow is rigid

### 2.6 ESA Open Science Catalog
- **URL**: https://opensciencedata.esa.int/catalog
- **Creator**: ESA (European Space Agency)
- **Presentation**: STAC Browser-based interface with faceted search. Material Design aesthetic.
- **Tech stack**: Vue.js (Nuxt.js), Vuetify Material Design framework, EOxElements library, PyCSW backend + static STAC catalog on GitHub Pages.
- **Key features**:
  - Faceted filtering via eox-itemfilter components
  - STAC-native data model with custom extension for science products
  - Dual backend: dynamic PyCSW search + static GitHub-hosted catalog
  - Community contribution via GitHub
- **Strengths**:
  - Standards-based (STAC)
  - Open contribution model
  - Clean Material Design interface
- **Weaknesses**:
  - Smaller catalog (focused on ESA-funded research outputs)

---

## 3. Curated Dataset Lists / Meta-Catalogs

### 3.1 GitHub Awesome Lists (multiple)

| Repository | Focus | Stars/Activity |
|---|---|---|
| `acgeospatial/awesome-earthobservation-code` | EO tools, tutorials, code, projects | Active |
| `elasticlabs/awesome-earthobservation` | EO coding libraries + open data | Active |
| `sacridini/Awesome-Geospatial` | Broad geospatial tools + resources | Active |
| `sshuair/awesome-gis` | Full GIS ecosystem | Active |
| `kartoza/awesome-geodata` | Geospatial data sources + services | Active |
| `iamtekson/awesome-geospatial-data-sources` | Open source data download sites | Active |
| `opengeos/Awesome-GEE` | Google Earth Engine resources | Active |
| `bchapuis/awesome-spatial-data` | Open + commercial spatial datasets | Active |

**Common presentation pattern**: Markdown README with hierarchical categories, bullet-pointed entries with name + link + 1-2 sentence description. Rendered by GitHub's Markdown renderer.

**Strengths**:
- Community-maintained via pull requests
- Version-controlled (change history visible)
- Zero hosting cost (GitHub)
- Familiar format for developers

**Weaknesses**:
- No search, filter, or sort beyond browser Ctrl+F
- No metadata standardization
- No spatial preview
- Quality varies by maintainer activity

### 3.2 Awesome Geospatial List (with website)
- **URL**: https://jerr0328.github.io/awesome-geospatial-list/
- **Creator**: Individual developer
- **Presentation**: Static page with table of contents and bulleted lists. Four main sections: Tools, Libraries, Data, Resources.
- **Tech stack**: GitHub Pages, Markdown, schema.org JSON-LD structured data.
- **Strengths**: Has a dedicated website (not just a GitHub README), includes structured data for SEO.
- **Weaknesses**: No dynamic filtering, same limitations as raw awesome lists.

### 3.3 CKAN-Based Open Data Portals (data.gov pattern)
- **URL**: https://catalog.data.gov/ (exemplar)
- **Creator**: CKAN open-source project, used by governments worldwide
- **Presentation**: Card-based organization pages + list-based dataset results. Each card shows logo/image, description, dataset count.
- **Key UI/UX features**:
  - Solr-powered full-text search
  - Faceted search (by organization, tag, format, license)
  - Data preview without download (maps, graphs, tables)
  - Tag clouds and format statistics in sidebar
  - Themeable per organization
  - API access
- **Tech stack**: Python (Pylons/Flask), PostgreSQL, Solr, Jinja2 templates.
- **Strengths**:
  - Battle-tested at massive scale (powers data.gov, data.humdata.org, open.canada.ca)
  - Rich faceted search
  - Inline data preview
  - Open-source and extensible
- **Weaknesses**:
  - Heavy infrastructure requirements
  - Overkill for personal/small catalogs
  - Default UI is functional but not visually distinctive

---

## 4. Non-GIS Platforms with Excellent Dataset Discovery (transferable patterns)

### 4.1 Hugging Face Datasets
- **URL**: https://huggingface.co/datasets
- **Creator**: Hugging Face (company)
- **Presentation**: Card-based list with rich filtering sidebar.
- **Key UI/UX features**:
  - Filter by modality (3D, Audio, Geospatial, Image, Tabular, Text, Time-series, Video)
  - Filter by size (row count ranges)
  - Filter by format (json, csv, parquet, etc.)
  - Filter by task, language, license
  - Full-text search
  - Auto-detected modality from file contents
  - Dataset cards (README.md with structured YAML front matter)
  - Inline dataset viewer (preview rows without download)
  - Trending/most downloaded sorting
- **Strengths**:
  - Best-in-class filtering UX
  - Structured metadata via YAML front matter is simple yet powerful
  - Dataset viewer is a killer feature
  - Community contribution model works at scale
- **Weaknesses**:
  - ML-focused, not geospatial-native
  - No spatial search/map view

### 4.2 CARTO Spatial Data Catalog
- **URL**: https://carto.com/spatial-data-catalog/
- **Creator**: CARTO (company)
- **Metadata shown per dataset**:
  - Provider, geographic coverage (countries), category
  - Sample data table (10 rows)
  - Full schema with variable names and descriptions
  - Map preview of spatial coverage
- **Strengths**:
  - Unified metadata system across heterogeneous data sources
  - Sample data preview is extremely useful
  - Map preview of coverage

---

## 5. Open-Source Discovery Platforms

### 5.1 STAC Browser
- **URL**: https://github.com/radiantearth/stac-browser
- **Demo**: https://radiantearth.github.io/stac-browser/
- **Creator**: Radiant Earth / community
- **Tech stack**: Vue.js, vue-cli, npm package
- **What it does**: Takes any STAC catalog URL or API endpoint and renders it as a browseable web interface. Supports STAC versions 0.6.0 through 1.1.0.
- **Strengths**:
  - Works with any STAC-compliant catalog
  - Zero configuration for basic use
  - Open-source and actively maintained
  - Used by ESA Open Science Catalog and others
- **Weaknesses**:
  - Generic UI (not customized for specific use cases)
  - Requires STAC-formatted data

### 5.2 GeoBlacklight
- **URL**: https://geoblacklight.org/
- **Creator**: Multi-institutional collaboration (Stanford, NYU, Cornell, Princeton, etc.)
- **Tech stack**: Ruby on Rails, Blacklight (Solr-powered discovery), OpenGeoMetadata schema.
- **Key features**:
  - Spatial search: map-based discovery that updates results as user pans/zooms ("dynamic spatial search")
  - Faceted search + full-text search + spatial search combined
  - Layer preview (WMS/WFS)
  - Attribute table exploration
  - Export to multiple formats (Shapefile, KML, GeoJSON)
  - Export to CARTO
  - Index map discovery and preview
- **Strengths**:
  - Dynamic spatial search is the standout feature
  - Federated discovery across institutions
  - Rich preview capabilities
- **Weaknesses**:
  - Heavy infrastructure (Rails + Solr)
  - Designed for institutional deployment, not personal sites

---

## 6. Synthesis: Key Patterns and Best Practices

### 6.1 Presentation Formats (ranked by prevalence)

| Format | Used By | Best For |
|---|---|---|
| **Card grid** | GEE, Planetary Computer, Source Coop, Hugging Face, CKAN | Visual browsing, moderate dataset counts |
| **Filterable list/table** | NASA Earthdata, Hugging Face, CKAN | Large catalogs, power users |
| **Categorized link list** | Robin Wilson, awesome lists, awesome-gee-community | Simple curated collections |
| **Map-first interface** | Copernicus Browser, EarthExplorer, GeoBlacklight | Spatially-oriented discovery |
| **Documentation pages** | GEE Community Catalog | Rich per-dataset documentation |

### 6.2 Essential Features (by priority for a personal research site)

**Must-Have:**
1. **Categorized organization** -- every successful catalog uses thematic categories
2. **Search** -- at minimum browser Ctrl+F; ideally client-side filtering
3. **Concise descriptions** -- 1-2 sentences per dataset (Robin Wilson's key insight)
4. **Direct links** -- to data source, documentation, and API endpoints
5. **Metadata per entry**: resolution, temporal coverage, spatial coverage, cost (free/paid), format

**Should-Have:**
6. **Tag/filter system** -- cross-cutting tags beyond hierarchical categories (GEE, Hugging Face pattern)
7. **Coverage indicator** -- at minimum text (global, Europe, Hungary); ideally a small map thumbnail
8. **Update status** -- when the catalog entry was last verified
9. **Data format indicators** -- GeoTIFF, Shapefile, API, cloud-native, etc.

**Nice-to-Have:**
10. **Interactive map** -- click to see what datasets cover a region
11. **Data size / storage estimation** -- how big is a download for a given area
12. **Sample preview** -- thumbnail or data snippet
13. **Cost/access indicator** -- free, registration required, commercial
14. **AI-powered search** -- as demonstrated by GEE Community Catalog

### 6.3 Technology Stack Recommendations (for a personal research site)

| Approach | Pros | Cons | Examples |
|---|---|---|---|
| **Static site (MkDocs/Hugo)** | Zero hosting cost, fast, easy maintenance, Markdown-based | No dynamic filtering without JS | GEE Community Catalog |
| **Static HTML + client-side JS** | Fast, filterable, hostable on GitHub Pages | More coding effort | Robin Wilson (minus the JS part) |
| **React/Vue SPA** | Rich interactivity, great UX | Heavier, needs build pipeline | Planetary Computer, Source Coop |
| **STAC + STAC Browser** | Standards-compliant, reusable | Requires structuring data as STAC | ESA Open Science Catalog |

**Recommendation for a personal research site**: A static site generator (Hugo or MkDocs) with client-side JavaScript for filtering/search provides the best balance of simplicity, performance, and functionality. Dataset entries can be stored as structured data (YAML/JSON) that feeds both the rendered pages and a client-side filter/search system.

### 6.4 Metadata Fields Worth Capturing

Based on what the best catalogs track:

| Field | Example Values | Used By |
|---|---|---|
| Name/Title | "Copernicus DEM GLO-30" | All |
| Description | 1-2 sentences | All |
| Provider/Source | ESA, NASA, USGS | GEE, Planetary Computer, Source Coop |
| Category | Elevation, Land Cover, Climate | All |
| Tags | ["dem", "global", "30m", "free"] | GEE, Hugging Face, Source Coop |
| Spatial Coverage | Global / Europe / Hungary | NASA, Copernicus, GeoBlacklight |
| Spatial Resolution | 30m, 10m, 1km | GEE, Planetary Computer |
| Temporal Coverage | 2015-present | GEE, NASA, Planetary Computer |
| Temporal Resolution | Daily, Monthly, Annual | GEE, NASA |
| Format/Access | GeoTIFF, API, Cloud-native COG | Planetary Computer, Source Coop |
| Cost/License | Free, CC-BY-4.0, Commercial | Hugging Face, CARTO |
| File Size Estimate | ~500 MB per tile | Few catalogs do this -- opportunity |
| API Endpoint | URL | Planetary Computer, Source Coop |
| Documentation URL | Link | All |
| Last Verified | 2026-01-15 | Robin Wilson (implicitly) |
| Thumbnail/Preview | Image URL | GEE, Planetary Computer |

### 6.5 Underserved Opportunities (features few catalogs offer)

1. **Download size estimator / calculator** -- Almost no catalog tells you "downloading this dataset for Hungary will be approximately X GB". This would be genuinely useful.
2. **Comparison tables** -- Side-by-side comparison of similar datasets (e.g., SRTM vs. Copernicus DEM vs. ALOS DEM).
3. **Decision flowcharts** -- "Which elevation dataset should I use?" guided selection.
4. **Personal annotations** -- "I used this for project X, quality was good for Y purpose" -- researcher's own experience notes.
5. **Processing recipes** -- Brief notes on how to access/process each dataset (beyond just a link).
6. **Cost estimation for commercial data** -- Calculators for satellite imagery pricing based on area + resolution.
7. **Data freshness indicators** -- Clear visual indicators of how current each dataset is.
8. **Cross-referencing** -- "If you're using dataset X, you might also need dataset Y" recommendations.

---

## 7. Design Recommendations for a Personal Research Website

Based on all findings, here is a suggested approach:

### Architecture
- **Static site** (Hugo or MkDocs Material) with dataset entries as structured YAML/JSON files
- **Client-side search/filter** using a lightweight JS library (Lunr.js, Fuse.js, or simple custom filtering)
- **No database** -- keep it simple, fast, and maintainable
- Host on GitHub Pages or Netlify (free)

### Layout
- **Landing view**: Card grid showing all datasets, with filter sidebar (categories, tags, resolution, coverage)
- **Detail view**: Per-dataset page with full metadata, description, access instructions, personal notes
- **Category views**: Thematic groupings (elevation, land cover, climate, etc.)
- **Comparison tables**: For dataset families (e.g., all DEMs side by side)

### Unique Differentiators (vs. existing catalogs)
1. **Researcher's perspective** -- personal experience notes, quality assessments, "gotchas"
2. **Hungarian/Central European focus** -- coverage-specific guidance
3. **Size estimation tools** -- "How much data will I need for my study area?"
4. **Processing notes** -- brief recipes for common workflows
5. **Maintained by a domain expert** -- curated quality over algorithmic breadth

---

## Sources

- [Robin Wilson's Free GIS Data](https://freegisdata.rtwilson.com/)
- [Robin Wilson's Blog - Categorised List](https://blog.rtwilson.com/categorised-list-of-free-gis-datasets/)
- [Google Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets/catalog)
- [Awesome GEE Community Catalog](https://gee-community-catalog.org/)
- [Microsoft Planetary Computer Catalog](https://planetarycomputer.microsoft.com/catalog)
- [Planetary Computer GitHub Repository](https://github.com/microsoft/PlanetaryComputerDataCatalog)
- [Planetary Computer Explorer Documentation](https://planetarycomputer.microsoft.com/docs/overview/explorer/)
- [NASA Earthdata Search](https://search.earthdata.nasa.gov/)
- [NASA Earthdata Tools](https://www.earthdata.nasa.gov/data/tools/earthdata-search)
- [Copernicus Data Space Browser](https://dataspace.copernicus.eu/ecosystem/services/copernicus-browser)
- [Copernicus Browser Documentation](https://documentation.dataspace.copernicus.eu/Applications/Browser.html)
- [USGS EarthExplorer](https://earthexplorer.usgs.gov/)
- [ESA Open Science Catalog](https://opensciencedata.esa.int/catalog)
- [ESA Open Science Catalog STAC Browser](https://opensciencedata.esa.int/stac-browser/)
- [Source Cooperative (Radiant Earth)](https://source.coop)
- [Radiant Earth - What is Source Cooperative](https://radiant.earth/blog/2023/10/what-is-source-cooperative/)
- [STAC Browser GitHub](https://github.com/radiantearth/stac-browser)
- [STAC Specification](https://stacspec.org/)
- [GeoBlacklight](https://geoblacklight.org/)
- [GeoBlacklight GitHub](https://github.com/geoblacklight/geoblacklight)
- [Hugging Face Datasets](https://huggingface.co/datasets)
- [Hugging Face Dataset Search Features](https://huggingface.co/blog/datasets-filters)
- [CKAN Data Management System](https://github.com/ckan/ckan)
- [data.gov Catalog](https://catalog.data.gov/)
- [awesome-earthobservation-code](https://github.com/acgeospatial/awesome-earthobservation-code)
- [awesome-earthobservation](https://github.com/elasticlabs/awesome-earthobservation)
- [Awesome-Geospatial](https://github.com/sacridini/Awesome-Geospatial)
- [awesome-gis](https://github.com/sshuair/awesome-gis)
- [awesome-geodata (Kartoza)](https://github.com/kartoza/awesome-geodata)
- [awesome-geospatial-list (with website)](https://jerr0328.github.io/awesome-geospatial-list/)
- [CARTO Spatial Data Catalog](https://docs.carto.com/data-and-analysis/data-observatory/guides/accessing-and-browsing-the-spatial-data-catalog)
- [Searchable Map Template (Leaflet)](https://github.com/datamade/searchable-map-template-csv)
