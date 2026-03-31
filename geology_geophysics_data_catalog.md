# Geology, Geophysics, Seismology & Mineral Resources Data Catalog

Last updated: 2026-03-31

---

## 1. Geological Maps & General Geology

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| **OneGeology** | https://onegeology.org / http://portal.onegeology.org | Global | Geological maps, lithology, age, faults | 1:1M typical, varies by country | Free | Yes (WMS, WFS, WCS) | Geological maps from 180+ countries served directly by national surveys | Distributed architecture; each survey owns its data. OGC-compliant services. No central download -- data served from source organizations |
| **EGDI** (European Geological Data Infrastructure) | https://www.europe-geology.eu | Europe | Geological maps, 3D models, boreholes, minerals, groundwater, geohazards, geochemistry, geophysics | Multi-scale (1:5M to 1:50k) | Free | Yes (WMS, WFS, CSW, INSPIRE) | 900+ datasets; pan-European geological map; mineral resources (MIN4EU); groundwater; coastal hazards; borehole index | INSPIRE-compliant. FAIR data. Operated by EuroGeoSurveys. Portal + map viewer |
| **GSEU** (Geological Service for Europe) | https://www.geologicalservice.eu | Europe | Harmonized geological data, groundwater, geoenergy, raw materials | Pan-European | Free | Via EGDI services | Harmonized datasets delivered through EGDI; pan-European atlases | Horizon Europe project (2022-2027), 49 partners from 36 countries. Successor to GeoERA |
| **USGS NGMDB** (National Geologic Map Database) | https://ngmdb.usgs.gov | USA (primarily) | Geological maps, stratigraphic nomenclature | Varies (1:24k to 1:2.5M) | Free | Limited (MapView interface) | 110,000+ maps and reports from 630+ agencies; MapView interactive viewer | Congressionally mandated archive. Raster + vector downloads |
| **USGS Mineral Resources (mrdata)** | https://mrdata.usgs.gov | Global | Geological maps, mineral deposits, geochemistry, geophysics | Varies | Free | Yes (WMS, WFS, REST) | MRDS mineral deposit database; state geologic maps; geochemistry; geophysics; global mineral assessments | Shapefile, GeoJSON, KML downloads. Public domain |
| **BGS OpenGeoscience** | https://www.bgs.ac.uk/geological-data/opengeoscience/ | UK | Geological maps, boreholes, hazards, hydrogeology, geochemistry, geophysics | 1:625k to 1:50k | Free | Yes (WMS, WFS) | 1:625k geology download; GeoIndex with 156 dataset layers; iGeology app; borehole records | Open Government Licence. ESRI + MapInfo formats |
| **BGS GeoIndex** | https://www.bgs.ac.uk/map-viewers/geoindex-onshore/ | UK | Boreholes, hazards, geochemistry, geophysics, hydrogeology, minerals | Multi-scale | Free (viewer); some data commercial | Yes (WMS) | 156 dataset layers covering onshore UK geology | Map-based index to all BGS datasets |
| **BRGM InfoTerre** | https://infoterre.brgm.fr | France | Geological maps, boreholes (BSS), natural risks, groundwater | 1:1M to 1:50k | Free | Yes (OGC WMS/WFS, SPARQL, Hub'eau API) | Geological maps at multiple scales; BSS subsoil database; risk maps; groundwater data | INSPIRE-compliant. Open data policy since 2017 for digital geological maps |
| **BGR Geoportal** | https://geoportal.bgr.de | Germany | Geological maps, soil, geochemistry, geophysics, groundwater, raw materials | 1:200k to 1:1M | Free | Yes (WMS, WFS) | Geological overview maps; INSPIRE-compliant versions; soil maps; hydrogeological maps | Shapefile + GML downloads. German Federal Institute for Geosciences and Natural Resources |
| **MBFSZ** (Mining and Geological Survey of Hungary) | https://mbfsz.gov.hu | Hungary | Geological maps, geothermal (OGRe), hydrogeology, mineral inventory | National scale | Free (most) | Limited (WMS via OGRe) | OGRe geothermal portal (map.mbfsz.gov.hu/ogre_en); Hydrogeological Data Store; mineral inventory via EGDI/MIN4EU | EOV coordinate system (EPSG:23700). Hungarian + English interfaces |
| **Macrostrat** | https://macrostrat.org | Global | Stratigraphy, lithology, geological maps, columns | Variable; 35,000+ units | Free | Yes (REST API) | Global geological map (Burwell); 1,500+ stratigraphic columns; age-lithology compilations | CC-BY-4.0. R package (rmacrostrat). API at macrostrat.org/api |
| **GLiM** (Global Lithological Map) | https://www.geo.uni-hamburg.de/en/geologie/forschung/aquatische-geochemie/glim.html | Global | Lithology | 0.5deg gridded; polygons at higher res | Free | No | 1,235,400 polygons from 92 regional maps; 16 lithological classes | Gridded version on PANGAEA (DOI:10.1594/PANGAEA.788537). University of Hamburg |
| **INSPIRE Geoportal** | https://inspire-geoportal.ec.europa.eu | Europe | All INSPIRE spatial data themes including geology | Varies by member state | Free | Yes (WMS 1.3, WFS 2.0, ATOM) | 34 spatial data themes; geology from all EU member states | Mandated by EU INSPIRE Directive. Data quality varies by country. GML format |

---

## 2. Seismology & Earthquake Hazards

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| **USGS Earthquake Hazards** | https://earthquake.usgs.gov | Global | Earthquake catalog, real-time feeds, hazard maps, shakemaps | Continuous, real-time | Free | Yes (FDSN fdsnws/event/1; REST; GeoJSON feeds) | Real-time earthquake catalog; ShakeMaps; PAGER alerts; historical seismicity; USGS Seismic Hazard Maps | QuakeML + GeoJSON output. Public domain. Comprehensive documentation |
| **EMSC** (European-Mediterranean Seismological Centre) | https://www.emsc-csem.org | Euro-Mediterranean + Global | Earthquake parameters, felt reports, moment tensors | Real-time + historical | Free | Yes (autoDRM; FDSN-compatible; CSV/KML export) | European earthquake catalog; real-time earthquake parameters; crowd-sourced felt reports (LastQuake app) | Data query page at emsc-csem.org/Earthquake_data/Data_queries.php |
| **ISC** (International Seismological Centre) | https://www.isc.ac.uk | Global | Earthquake bulletin, reviewed hypocenters, focal mechanisms | Historical (1900-present) | Free | Yes (web services; FTP; ISF/QuakeML/CSV) | ISC Bulletin (definitive global catalog); ISC-GEM catalog (M5.5+, 1904-2021); ISC-EHB dataset | Gold standard for research-grade earthquake data. Monthly reviewed bulletins |
| **GEM Foundation** | https://www.globalquakemodel.org | Global | Seismic hazard, risk, exposure models | Global mosaic | Free (open versions) / Commercial (full) | Yes (via OpenQuake Engine) | Global Seismic Hazard Map (2023.1); Global Risk Map; Global Exposure Model; ISC-GEM Catalogue | CC BY-NC-SA 4.0 for open versions. OpenQuake Engine is open-source (GitHub) |
| **EFEHR / ESHM20** | http://www.efehr.org | Europe + Mediterranean | Seismic hazard maps, source models, GMMs | Pan-European | Free | Yes (GitLab repository; web services) | ESHM20 (2020 European Seismic Hazard Model); harmonized earthquake catalog; fault database; source zone model | CC BY 4.0. Data on hazard.efehr.org and EFEHR GitLab |
| **ORFEUS / EIDA** | https://www.orfeus-eu.org | Europe + Mediterranean | Seismic waveforms, station metadata | Broadband, continuous | Free (mostly open data) | Yes (FDSN fdsnws dataselect + station) | 23,000+ station waveforms across Pan-Europe; AdriaArray; EIDA federated archive | miniSEED format. Access via ObsPy, wget, FDSN clients. Foundation for European seismology |
| **IRIS / EarthScope** | https://ds.iris.edu | Global | Seismic waveforms, station metadata | Broadband, all bands | Free | Yes (FDSN fdsnws; SEED/miniSEED; web services) | Global seismic waveform archive; GSN, USArray data; temporary experiments | SEED format. ObsPy, Wilber3, SOD for access. Java/Matlab/Python clients |
| **EPOS** (European Plate Observing System) | https://www.epos-eu.org | Europe | Multi-disciplinary: seismology, GNSS, volcanology, geology | 250+ data sources | Free | Yes (unified portal API; FDSN; OGC) | Seismogenic faults; GNSS stations; earthquake catalogs; volcanic data; geological maps; magnetometer data; tsunami hazard | Integrates ORFEUS, EMSC, EFEHR and other European infrastructures |

---

## 3. Volcanic Hazards

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| **Smithsonian GVP** (Global Volcanism Program) | https://volcano.si.edu | Global | Volcano locations, eruption history, activity reports | Point data + descriptions | Free | No formal API (XML/Excel download; GeoJSON via E3 app) | Volcanoes of the World database (v5.3.4); Holocene volcano list; Weekly/monthly activity reports; eruption catalog | ~1,500 Holocene volcanoes. Also mirrored at NOAA NCEI. Definitive global volcano reference |
| **Copernicus EMS** (Emergency Management Service) | https://mapping.emergency.copernicus.eu | Global (EU focus) | Satellite-derived hazard maps (including volcanic eruptions, landslides) | High-res (aerial LIDAR, satellite) | Free | Limited (map downloads) | Post-disaster landslide maps; volcanic eruption mapping (e.g., La Palma 2021); DTM/DEM products | Activation-based. Not a continuous database but a rapid response mapping service |

---

## 4. Mineral Resources

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| **MINERALS4EU / Mintell4EU** | https://minerals4eu.brgm-rec.fr (legacy) / via EGDI | Europe | Mineral deposits, production statistics, trade data | National + deposit-level | Free | Via EGDI WMS/WFS | Electronic European Minerals Yearbook (2004-2019); Minerals Inventory with spatial data; critical raw materials | Now integrated into EGDI. Data from multiple EU projects (Minerals4EU, ORAMA, Mintell4EU) |
| **ProMine** | http://ptrarc.gtk.fi/ProMine/default.aspx | Europe | Mineral deposits, anthropogenic concentrations | Deposit-level | Free | WMS layers | 12,979 mineral deposit records across 34 European countries; 3,408 anthropogenic concentration records | EU FP7 project (2009-2013). Standardized vocabulary. May have limited maintenance |
| **USGS MRDS** | https://mrdata.usgs.gov/mrds/ | Global | Metallic and nonmetallic mineral deposits | Point data | Free | Yes (REST, WMS, WFS) | Mineral deposit locations, commodities, references, geological characteristics, production data worldwide | Public domain. Part of mrdata.usgs.gov suite |
| **USGS USMIN** | https://www.usgs.gov/centers/gggsc/science/usmin-mineral-deposit-database | USA | Mineral deposits | Deposit-level | Free | Yes (REST) | U.S. mineral deposit database with detailed geological and commodity information | Under active development |
| **BGS MineralsUK** | https://www.bgs.ac.uk/mineralsuk/ | Global + UK | Mineral statistics, European mineral statistics | National aggregates | Free | No | World Mineral Production; European Mineral Statistics; UK mineral planning data | Annual statistical publications. Excel/PDF downloads |

---

## 5. Marine Geology

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| **EMODnet Geology** | https://emodnet.ec.europa.eu/en/geology | European seas | Seabed substrates, seafloor geology, coastal behaviour, marine minerals, submarine landslides | 1:1M to 1:1,500 (multi-scale) | Free | Yes (WMS, WFS, REST) | Seabed substrate maps (Folk classification); seafloor lithology & stratigraphy; Quaternary geology; submerged landscapes; marine mineral resources | EU DG MARE funded. Harmonized with 5/7/16-class substrate schemes |
| **NOAA NCEI Marine Geophysics** | https://www.ncei.noaa.gov/products/marine-geology-geophysics | Global | Bathymetry, magnetics, gravity, seismic reflection/refraction | Trackline data (1939-present) | Free | Yes (web services; MGD77T format) | Marine trackline geophysical database; airborne magnetics; global gravity; seafloor sediment data | MGD77T exchange format. Interactive map viewer |

---

## 6. Geothermal Data

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| **Global Heat Flow Database** (IHFC) | https://www.heatflow.world | Global | Terrestrial heat flow, thermal conductivity | Point measurements | Free | Yes (data portal with filtering) | 100,000+ heat flow entries; quality-assessed measurements; multi-dimensional quality flags | Maintained by IHFC at GFZ Potsdam + TU Dresden. FAIR-compliant. Doubled in size recently |
| **GDR** (Geothermal Data Repository, DOE/OpenEI) | https://gdr.openei.org | USA (primarily) | Geothermal resource data, well logs, temperature, geochemistry | Site-level | Free | Yes (OpenEI API) | 4,900+ resources, 19,400+ files, 322 TB; well data, EGS experiments, resource assessments | DOE Geothermal Technologies Office funded. Data lake for large datasets |
| **EGEC** (European Geothermal Energy Council) | https://www.egec.org | Europe | Geothermal market reports, statistics | Country-level | Freemium (reports may be paid) | No | Geothermal Market Reports; European geothermal statistics | Industry association; more policy/market data than raw geological data |
| **MBFSZ OGRe** | https://map.mbfsz.gov.hu/ogre_en/ | Hungary | Geothermal, hydrogeological, geophysical data | National | Free | WMS | Interactive geothermal maps; well data; temperature gradients; aquifer information | Unique national geothermal platform |

---

## 7. Boreholes & Subsurface

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| **EGDI Borehole Index** | https://www.europe-geology.eu/scientific-themes/boreholes/ | Europe | Borehole locations, basic metadata | Point index | Free | WMS (WFS planned) | Pan-European borehole index compliant with INSPIRE/GeoSciML | Currently discovery-only; detailed logs link to national surveys |
| **BGS Borehole Records** (via GeoIndex) | https://www.bgs.ac.uk/map-viewers/geoindex-onshore/ | UK | Borehole logs, geological records | Point + depth logs | Free (scans) / Commercial (interpreted) | WMS | Millions of borehole records across UK; scanned logs; geological descriptions | Most scans free under OGL; detailed interpreted data may require licence |
| **BRGM BSS** (Banque du Sous-Sol) | https://infoterre.brgm.fr | France | Borehole logs, geological logs, water well data | Point + depth | Free | OGC services | French national subsurface database; geological and hydrogeological well logs | Accessed via InfoTerre viewer |

---

## 8. Multi-disciplinary Data Repositories

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|
| **PANGAEA** | https://www.pangaea.de | Global | Earth & environmental science data (geology, geophysics, geochemistry, paleoclimate, ocean) | Varies | Free | Yes (REST API; OAI-PMH; Elasticsearch) | 419,000+ datasets; 25 billion+ measurements; geological/geophysical data from marine and terrestrial studies | DOI-based citation. CC-BY. Operated by AWI + MARUM Bremen. Pioneer of FAIR data |
| **NOAA NCEI** (all geophysical) | https://www.ncei.noaa.gov | Global | Geomagnetic, gravity, bathymetry, seismicity, tsunamis, paleoclimatology | Varies | Free | Yes (various web services) | Global magnetic models (IGRF, WMM); tsunami database; paleoclimate proxies; marine geology | Successor to NGDC. Comprehensive US federal archive |

---

## 9. GeoERA Legacy Projects (data now in EGDI)

| Project | Focus | Key Outputs |
|---|---|---|
| **GeoConnect3d** | Cross-border 3D geological framework | Structural framework models |
| **HIKE** | Hazard and Impact Knowledge for Europe | Seismogenic fault database; induced seismicity |
| **MINDeSEA** | Seabed mineral deposits | Marine mineral deposit maps |
| **HOVER** | Groundwater resources | Groundwater vulnerability; natural background levels |
| **Mintell4EU** | Mineral intelligence | Updated Minerals Yearbook + inventory |
| **GeoERA Information Platform** | Data infrastructure | All outputs served via EGDI (https://www.europe-geology.eu) |

---

## Quick Reference: API Protocols Summary

| Protocol | Platforms Using It |
|---|---|
| **FDSN fdsnws** (event, dataselect, station) | USGS EQ, EMSC, ORFEUS/EIDA, IRIS, ISC |
| **OGC WMS** | EGDI, OneGeology, BGS, BRGM, BGR, EMODnet, INSPIRE, MBFSZ |
| **OGC WFS** | EGDI, BGS, BRGM, BGR, EMODnet, INSPIRE, USGS mrdata |
| **OGC WCS** | OneGeology (some services) |
| **REST/JSON** | USGS EQ (GeoJSON), Macrostrat, PANGAEA, GEM/OpenQuake |
| **SPARQL** | BRGM (geological registers) |
| **OAI-PMH** | PANGAEA |

---

## Quick Reference: Data Format Summary

| Format | Common Use |
|---|---|
| **GeoJSON** | USGS EQ feeds, Smithsonian GVP E3, Macrostrat |
| **QuakeML** | USGS EQ, ISC, EMSC |
| **miniSEED / SEED** | ORFEUS, IRIS, all FDSN waveform services |
| **Shapefile (ESRI)** | BGS, BGR, USGS mrdata, many national surveys |
| **GML / INSPIRE GML** | EGDI, BGR, INSPIRE services |
| **GeoTIFF** | GEM hazard maps, EMODnet |
| **CSV** | ISC, EMSC, USGS, most platforms |
| **MGD77T** | NOAA marine trackline data |
| **NetCDF** | PANGAEA, some hazard models |

---

## Sources

- [OneGeology Portal](http://portal.onegeology.org/OnegeologyGlobal/)
- [EGDI - European Geological Data Infrastructure](https://www.europe-geology.eu)
- [GSEU - Geological Service for Europe](https://www.geologicalservice.eu/)
- [EuroGeoSurveys](https://eurogeosurveys.org/data/)
- [USGS Mineral Resources Online Spatial Data](https://mrdata.usgs.gov/)
- [USGS NGMDB](https://ngmdb.usgs.gov/)
- [USGS Earthquake Hazards Program](https://earthquake.usgs.gov)
- [BGS OpenGeoscience](https://www.bgs.ac.uk/geological-data/opengeoscience/)
- [BGS GeoIndex](https://www.bgs.ac.uk/map-viewers/geoindex-onshore/)
- [BRGM InfoTerre](https://infoterre.brgm.fr)
- [BGR Geoportal](https://geoportal.bgr.de)
- [MBFSZ](https://mbfsz.gov.hu)
- [EMSC](https://www.emsc-csem.org/)
- [ISC](https://www.isc.ac.uk/)
- [GEM Foundation](https://www.globalquakemodel.org/)
- [EFEHR / ESHM20](http://www.efehr.org/)
- [ORFEUS / EIDA](https://www.orfeus-eu.org/)
- [IRIS / EarthScope](https://ds.iris.edu)
- [EPOS](https://www.epos-eu.org/)
- [Smithsonian GVP](https://volcano.si.edu/)
- [MINERALS4EU](https://minerals4eu.brgm-rec.fr/)
- [ProMine](http://ptrarc.gtk.fi/ProMine/default.aspx)
- [EMODnet Geology](https://emodnet.ec.europa.eu/en/geology)
- [NOAA NCEI Marine Geophysics](https://www.ncei.noaa.gov/products/marine-geology-geophysics)
- [Global Heat Flow Database](https://www.heatflow.world)
- [GDR / OpenEI](https://gdr.openei.org/)
- [EGEC](https://www.egec.org/)
- [PANGAEA](https://www.pangaea.de/)
- [Macrostrat](https://macrostrat.org/)
- [GLiM](https://www.geo.uni-hamburg.de/en/geologie/forschung/aquatische-geochemie/glim.html)
- [INSPIRE Geoportal](https://inspire-geoportal.ec.europa.eu/)
- [GeoERA](https://geoera.eu/projects/)
- [Copernicus EMS](https://mapping.emergency.copernicus.eu/)
