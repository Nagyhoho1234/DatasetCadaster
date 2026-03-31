# Geodetic, InSAR & Ground Deformation Data Sources Catalog

*Compiled: 2026-03-31*

---

## 1. SAR / InSAR Raw Data Portals

| Platform | URL | Scope | Data Type | Spatial Res | Temporal Res | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **Copernicus Data Space Ecosystem** | https://dataspace.copernicus.eu/ | Global | Sentinel-1 C-band SAR (SLC, GRD, OCN) | 5x20 m (IW SLC) | 6 days (constellation) | Free | Yes (OData, Sentinel Hub, OpenSearch) | Sentinel-1A/B/C full archive, Sentinel-2/3/5P | Replaced Open Access Hub (Oct 2023). Free registration required. NetCDF/GeoTIFF/SAFE. |
| **ASF DAAC (Alaska Satellite Facility)** | https://search.asf.alaska.edu/ | Global | Sentinel-1, ALOS PALSAR, NISAR, ARIA GUNW, ERS, JERS, Radarsat-1 | 5x20 m (S1 IW) | 6-12 days | Free | Yes (SearchAPI, asf_search Python, CMR) | Sentinel-1 SLC/GRD, ALOS PALSAR L1.1, NISAR L0-L3, ARIA-S1-GUNW interferograms | NASA Earthdata login. HyP3 on-demand processing (RTC, InSAR). Migrating to Earthdata Cloud by end 2026. |
| **COSMO-SkyMed (ASI/e-GEOS)** | https://www.e-geos.it/en/satellite-data/cosmo-skymed-constellation/ | Global | X-band SAR (Spotlight, StripMap, ScanSAR) | 1 m (Spotlight) to 100 m (ScanSAR) | 12 hours (constellation revisit) | Commercial (free for approved research via ESA TPM) | Yes (ESA EO Gateway catalogue) | CSK 1st & 2nd Gen archive, new tasking | Proposal-based free access for science. Commercial via e-GEOS. HH/VV/HV/VH polarizations. |
| **TerraSAR-X / TanDEM-X (DLR)** | https://sss.terrasar-x.dlr.de/ | Global | X-band SAR (Spotlight, StripMap, ScanSAR) | 0.25 m (Staring Spotlight) to 40 m | 11-day repeat | Commercial (free for approved science proposals) | Yes (EOWEB GeoPortal) | TSX/TDX archive, DEM products | Proposal via Science Service System. EOWEB GeoPortal for discovery/download. |
| **ALOS PALSAR / PALSAR-2 (JAXA)** | https://www.eorc.jaxa.jp/ALOS/en/dataset/alos_open_and_free_e.htm | Global | L-band SAR | 10 m (Fine) to 100 m (ScanSAR) | 14-day repeat | Free (open & free policy since 2015) | Yes (G-Portal, AWS Registry) | ALOS-1 PALSAR archive, ALOS-2 PALSAR-2 (2014-present), 25 m global mosaics, forest/non-forest maps | Also via ASF DAAC and Google Earth Engine. CARD4L compliant products on AWS. |
| **NISAR (NASA/ISRO)** | https://www.earthdata.nasa.gov/data/platforms/space-based-platforms/nisar | Global | L-band + S-band SAR | 3-10 m | 12-day repeat | Free | Yes (ASF DAAC APIs, Earthdata CMR) | L0B raw, L1 SLC/GCOV, L2 surface displacement, L3 soil moisture | Launched Jul 2025, operational Jan 2026. 100,000+ products already released. Data via ASF DAAC. |

---

## 2. Processed InSAR / Ground Motion Products

| Platform | URL | Scope | Data Type | Spatial Res | Temporal Res | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **European Ground Motion Service (EGMS)** | https://egms.land.copernicus.eu/ | Europe (EEA39) | PS-InSAR & SBAS ground motion maps | 5x20 m (Basic/Calibrated), 100x100 m (Ortho) | 6-12 days (annual update) | Free | Yes (EGMS Explorer download) | Basic (LOS velocity), Calibrated (GNSS-referenced), Ortho (E-W + vertical) from 2016-present | Copernicus Land Monitoring Service. mm/yr precision. CSV/GeoPackage. Updated annually. |
| **COMET LiCSAR** | https://comet.nerc.ac.uk/comet-lics-portal/ | Global (tectonic/volcanic) | Sentinel-1 interferograms, coherence, unwrapped phase | 100 m | 6-12 days | Free | Yes (Python scripts, LiCSBAS download tools) | Wrapped/unwrapped interferograms, coherence maps, velocity maps for 250x250 km frames | GeoTIFF. Auto-processed within 2 weeks of acquisition. LiCSBAS for time series. CEDA archive. |
| **ARIA-S1-GUNW (JPL/ASF)** | https://aria.jpl.nasa.gov/products/ | Global (hazard areas) | Geocoded unwrapped interferograms | 90 m | 6-12 days | Free | Yes (ASF SearchAPI, Earthdata CMR) | 1M+ GUNW products: unwrapped phase, coherence, connected components, ionospheric corrections | CF-compliant NetCDF4. On-demand generation via ASF Vertex. Ready for MintPy time series analysis. |
| **COMET Volcano Deformation Database** | https://comet.nerc.ac.uk/comet-volcano-portal/ | Global | Volcanic deformation catalogue (InSAR, GPS, tilt) | Variable | Event-based | Free | No (web portal) | 339 deformation episodes at 160+ volcanoes; displacement rates, spatial extents, causes | Hosted at U. Bristol. Includes null results. Links to LiCSAR interferograms for online analysis. |
| **COMET Subsidence Portal** | https://comet-subsidencedb.org/ | Global | Subsidence measurements database | Variable | Event-based | Free | No (web portal) | Subsidence records with rates, causes, methods | Complementary to volcano portal. Literature-based compilation. |
| **Bodemdalingskaart (Netherlands)** | https://bodemdalingskaart.nl/ | Netherlands | InSAR vertical ground motion | 4x4 km cells (aggregated from billions of PS) | Multi-year | Free | No (web viewer) | Nationwide deformation map, object-level stability | SkyGeo processing. Covers buildings, bridges, railways. NCG initiative. |

---

## 3. GNSS Data & Products

| Platform | URL | Scope | Data Type | Spatial Res | Temporal Res | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **IGS (International GNSS Service)** | https://igs.org/ | Global | GNSS orbits, clocks, troposphere, ionosphere, RINEX obs | 500+ stations | 30s/1s obs; daily/hourly products | Free | Yes (FTP/HTTPS at BKG, CDDIS) | Ultra-rapid/Rapid/Final orbits & clocks, RINEX from 500+ stations, ANTEX, SINEX | Foundation of global geodetic reference. Multi-GNSS (GPS, GLONASS, Galileo, BeiDou). |
| **NASA CDDIS** | https://cddis.nasa.gov/ | Global | GNSS, SLR, VLBI, DORIS data & products | Global network | Daily/hourly/sub-hourly | Free | Yes (HTTPS, Earthdata login) | IGS GNSS archive, SLR normal points, VLBI databases, ITRF solutions | NASA Earthdata login required. Primary IGS data center. Supports space geodesy community since 1982. |
| **UNAVCO / EarthScope GAGE** | https://www.unavco.org/data/ | N. America + Global | GNSS RINEX, position time series, velocity fields | 3000+ stations | Daily positions | Free | Yes (REST web services, Python CLI) | GAGE 2025 velocity fields, PBO/NOTA/TLALOCNet time series, campaign GPS | Earthdata login. Transitioned from FTP to HTTPS. Includes meteorological colocated data. |
| **EUREF Permanent Network (EPN)** | https://www.epncb.oma.be/ | Europe | GNSS RINEX, coordinates, velocities | 300+ stations | Daily/hourly/real-time | Free | Yes (FTP at BKG/BEV RDCs, NTRIP for real-time) | ETRS89 coordinates, RINEX obs, combined solutions, velocity fields | Open data policy. RDCs at BKG (DE) and BEV (AT). Real-time streams via NTRIP. Historical archive at ROB. |
| **Nevada Geodetic Laboratory (NGL)** | https://geodesy.unr.edu/ | Global | GNSS position time series, velocities | 17,000+ stations | Daily | Free | Yes (HTTP text files, bulk download) | Daily PPP time series (ITRF2014/2020), MIDAS velocities, steps database | Updated daily. Covers 1996-present. Used by SONEL for vertical land motion at tide gauges. |
| **NOAA CORS Network (NCN)** | https://geodesy.noaa.gov/CORS/ | USA + territories | GNSS RINEX observations | ~2000 stations | 1s/30s obs | Free | Yes (HTTPS, AWS Open Data) | Multi-GNSS RINEX, OPUS solutions, station metadata | 230+ contributing organizations. Supports OPUS online positioning. Data also on AWS. |
| **GNSSnet.hu (Hungary)** | https://www.sgo-penc.hu/services.php | Hungary + neighbors | RTK corrections, GNSS RINEX | 35 HU + 19 cross-border stations (60-80 km spacing) | Real-time + archived | Freemium (RTK service may require subscription) | Yes (NTRIP for real-time) | Real-time RTK corrections, RINEX archive, PENC/PEN2 (IGS stations) | Part of EUREF via PENC, PEN2, BUTE, OROS, SOPR stations. Built on OGPSH foundation (1153 points). |
| **SONEL** | https://www.sonel.org/ | Global (coastal) | GNSS vertical land motion at tide gauges | 1523 co-located stations | Daily | Free | Yes (web services) | Vertical velocities at tide gauges, NGL20 solution (ITRF2020), position time series | Essential for absolute sea level studies. Links GPS to tide gauge records. |

---

## 4. Integrated / Multi-Disciplinary Platforms

| Platform | URL | Scope | Data Type | Spatial Res | Temporal Res | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **EPOS Data Portal** | https://www.epos-eu.org/dataportal | Europe | GNSS, seismology, InSAR, geology, volcanology | Multi-source | Variable | Free | Yes (REST APIs) | Integrated solid Earth data: GNSS time series/velocities, seismic waveforms, InSAR products, geological maps | EU research infrastructure. Single portal for distributed data. Operational since Jan 2023. |
| **Geohazards Exploitation Platform (GEP)** | https://geohazards-tep.eu/ | Global | SAR processing platform (InSAR, PSI, SBAS) | Variable (depends on input) | On-demand | Free (ESA-sponsored, resource limits) | Yes (REST, WPS) | Sentinel-1 InSAR, ERS/Envisat archive (70+ TB), P-SBAS, SNAPPING, DInSAR | ESA cloud processing. Includes GAMMA, SNAP, QGIS. On-demand and systematic processing. |
| **Copernicus EMS (Emergency)** | https://emergency.copernicus.eu/ | Global (activation-based) | Rapid mapping, risk analysis, ground motion | Variable | Event-driven | Free | Yes (web portal) | Rapid damage maps, risk assessments, deformation maps for disasters | Activation by authorized users only (EU/national civil protection). Products openly available post-activation. |

---

## 5. Commercial InSAR Services

| Platform | URL | Scope | Data Type | Spatial Res | Temporal Res | Cost | API | Key Datasets | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **TRE Altamira (CLS Group)** | https://site.tre-altamira.com/ | Global | PSInSAR, SqueeSAR ground deformation | mm precision, point density varies | 6-12 days (S1) | Commercial | Yes (TREmaps web platform) | SqueeSAR time series, historical ERS/Envisat/CSK archives, nationwide monitoring | World leader in multi-temporal InSAR. 20+ years experience. SqueeSAR replaces PSInSAR. Contributed to EGMS production. |
| **SkyGeo** | https://www.skygeo.com/ | Global | InSAR optimization & assessment, ground motion maps | mm precision | 6-12 days | Commercial | Yes (web portal) | Decision-grade InSAR products, Dutch Bodemdalingskaart, infrastructure monitoring | Specializes in InSAR quality assurance. Geotechnical risk planning. Portal-based delivery. |

---

## 6. Open-Source Processing Tools (not data portals, but essential for the workflow)

| Tool | URL | Purpose | Input Sources | Cost | Notes |
|---|---|---|---|---|---|
| **SNAP (ESA)** | https://step.esa.int/main/toolboxes/snap/ | SAR/InSAR processing GUI + CLI | Sentinel-1, ERS, Envisat, Radarsat, ALOS | Free (GPL) | 500K+ downloads. Calibration, interferometry, polarimetry. Python (snappy) scripting. |
| **MintPy** | https://github.com/insarlab/MintPy | InSAR time series analysis (SBAS/PS) | ISCE, ARIA, LiCSAR, HyP3, GAMMA, SNAP, GMTSAR | Free (BSD) | Standard tool for InSAR time series. Reads multiple processor outputs. Produces 3D displacement fields. |
| **LiCSBAS** | https://github.com/yumorishita/LiCSBAS | InSAR time series from LiCSAR | LiCSAR GeoTIFF products | Free | Integrated with LiCSAR portal. Automated download + processing. |
| **ISCE (JPL)** | https://github.com/isce-framework | InSAR Scientific Computing Environment | Sentinel-1, ALOS, NISAR, CSK, TSX | Free | Core processor behind ARIA products. Supports topsStack, stripmapStack. |

---

## 7. Additional / Specialized Sources

| Platform | URL | Scope | Data Type | Cost | Notes |
|---|---|---|---|---|---|
| **WInSAR Consortium** | https://winsar.unavco.org/ | W. North America | SAR data archive (ERS, Envisat, Radarsat, TSX, CSK) | Free (member institutions) | Membership required. Via UNAVCO GAGE facility. SSARA search interface. |
| **BGS InSAR (UK)** | https://www.bgs.ac.uk/geology-projects/geodesy/insar-research/ | UK | Ground motion from PS-InSAR | Free (selected datasets) | Coal mining subsidence, landslide monitoring, shale gas baseline. ERS/Envisat/S1. UKGEOS data catalogue. |
| **OGPSH (Hungary)** | https://inspire-geoportal.ec.europa.eu/ (INSPIRE metadata) | Hungary | National GPS reference network | Free (metadata) | 1153 points, ~10 km spacing. Foundation for GNSSnet.hu. INSPIRE compliant. |
| **Sentinel Hub** | https://www.sentinel-hub.com/ | Global | SAR/optical processing API | Freemium | Part of Copernicus Data Space. OGC services (WMS/WCS/WFS). Statistical API. Commercial tiers for heavy use. |
| **Google Earth Engine** | https://earthengine.google.com/ | Global | Sentinel-1 GRD/SLC, ALOS mosaics | Free (research), Commercial | Cloud processing. JavaScript/Python API. Large-scale SAR analysis. |
| **AWS Open Data (Sentinel-1)** | https://registry.opendata.aws/sentinel-1/ | Global | Sentinel-1 SLC (IW) | Free | Cloud-optimized. Also hosts ALOS PALSAR-2 CARD4L products. |

---

## Summary Statistics

- **Total platforms cataloged**: 33
- **Free data sources**: 25
- **Commercial/Freemium**: 5
- **Open-source tools**: 4 (processing, not data)
- **With API access**: 26
- **Global scope**: 18
- **European scope**: 4
- **National/Regional**: 6

---

## Key Recommendations for Hungary / Central Europe

1. **EGMS** -- Free pan-European ground motion at mm/yr precision, covers Hungary fully
2. **GNSSnet.hu** -- National GNSS reference, 35 stations, RTK service
3. **EUREF EPN** -- 5 Hungarian stations in the European reference frame
4. **Copernicus Data Space** -- Free Sentinel-1 SAR for custom InSAR processing
5. **LiCSAR** -- Free pre-computed Sentinel-1 interferograms including Hungarian frames
6. **EPOS** -- Integrated European solid Earth data portal
7. **NISAR** -- New L-band SAR mission, free global data, excellent for deformation monitoring in vegetated areas
