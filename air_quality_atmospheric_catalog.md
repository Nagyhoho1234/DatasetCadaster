# Air Quality and Atmospheric Data Sources

## Global Satellite Products

| Platform | URL | Scope | Data Type | Resolution | Temporal | Cost | API | Notes |
|---|---|---|---|---|---|---|---|---|
| Sentinel-5P TROPOMI | s5phub.copernicus.eu | Global | NO2, O3, SO2, CO, CH4, HCHO, aerosol | 3.5x5.5 km (nadir) | 2018-present | Free | OData API | Near-real-time and offline products |
| S5P-PAL | data-portal.s5p-pal.com | Global | Gridded TROPOMI L3 | 0.01-0.05° | 2018-present | Free | No | Pre-processed TROPOMI grids |
| EUMETSAT AC SAF | acsaf.org | Global | Satellite trace gas, UV, aerosol | Varies | 2007-present | Free | No | GOME-2, IASI derived products |
| TEMIS | temis.nl | Global | Satellite L3 trace gases, UV | 0.125-0.5° | 2004-present | Free | No | TROPOMI/OMI/GOME-2 gridded products |
| ESA CCI Aerosol | climate.esa.int | Global | Aerosol CDR | 1° / 10km | 1995-present | Free | No | Climate Data Record from multiple sensors |

## Global Reanalysis and Models

| Platform | URL | Scope | Data Type | Resolution | Temporal | Cost | API | Notes |
|---|---|---|---|---|---|---|---|---|
| CAMS Global | atmosphere.copernicus.eu | Global | Reanalysis + forecast AQ | 0.4° (rean) / 0.1° (fc) | 2003-present | Free | CDS API (Python) | EAC4 reanalysis; 5-day forecast; 50+ species |
| CAMS European | atmosphere.copernicus.eu | Europe | Regional AQ ensemble | 0.1° (~10km) | 2015-present | Free | CDS API (Python) | 9-model ensemble; 4-day forecast |
| NASA MERRA-2 | gmao.gsfc.nasa.gov | Global | Aerosol reanalysis | 0.5°x0.625° (~50km) | 1980-present | Free | OPeNDAP / GES DISC | Aerosol optical depth, PM2.5 diagnostics |
| CIESIN/SEDAC PM2.5 Grids | sedac.ciesin.columbia.edu | Global | Annual mean PM2.5 | 0.01° (~1km) | 1998-2021 | Free | No | van Donkelaar et al. satellite-model fusion |

## Global Ground-Based Networks

| Platform | URL | Scope | Data Type | Resolution | Temporal | Cost | API | Notes |
|---|---|---|---|---|---|---|---|---|
| OpenAQ | openaq.org | Global | 30k+ monitoring locations | Station-level | 2015-present | Free, CC-BY 4.0 | REST API v2/v3 | Aggregates government AQ data worldwide |
| AQICN | aqicn.org | Global | 12k+ stations AQI | Station-level | Real-time | Freemium | REST API (token) | Real-time AQI; free tier rate-limited |
| WHO Air Quality Database | who.int | Global | 6000+ cities annual means | City-level | 2010-present | Free | Bulk download | PM2.5, PM10 annual means |
| AERONET | aeronet.gsfc.nasa.gov | Global | 500+ stations aerosol optics | Station-level | 1993-present | Free | Web API (URL-based) | Sun/sky photometer network; AOD, SSA, size |
| GAW / WDCGG (WMO) | gaw.kishou.go.jp | Global | Background GHG, ozone, aerosol | Station-level | 1950s-present | Free | No | ~400 stations; background atmosphere |
| TOAR Database | toar-data.org | Global | Harmonized surface ozone | Station-level | 1970-present | Free | REST API | Tropospheric Ozone Assessment Report data |

## European Networks and Portals

| Platform | URL | Scope | Data Type | Resolution | Temporal | Cost | API | Notes |
|---|---|---|---|---|---|---|---|---|
| EEA Air Quality Portal | discomap.eea.europa.eu/map/fme/AirQualityExport.htm | Europe | 4000+ stations, all pollutants | Station-level | 2013-present | Free | REST / SPARQL | E1a/E2a validated + up-to-date data |
| EEA AirBase | eea.europa.eu | Europe | Historical AQ data | Station-level | 1969-2012 | Free | No | Legacy database; superseded by e-Reporting |
| EMEP | emep.int | Europe | Model + monitoring | 0.1° (model) / station | 1970s-present | Free | No | Transboundary pollution assessment |
| EBAS | ebas.nilu.no | Europe+ | Atmospheric composition obs | Station-level | 1970s-present | Free | REST API | EMEP/GAW/ACTRIS data repository |
| E-PRTR | industry.eea.europa.eu | Europe | Facility-level emissions | Facility point | 2007-present | Free | SPARQL / REST | 30k+ facilities; 91 pollutants |
| EDGAR | edgar.jrc.ec.europa.eu | Global | Emission inventories | 0.1° | 1970-present | Free | Bulk download | CO2, CH4, N2O, F-gases, air pollutants |
| TNO-MACC | tno.nl | Europe | Emission gridmaps | ~7km (0.0625°) | 2000-present | Free for research | No | High-res European emissions; request access |
| ICOS | icos-cp.eu | Europe | High-precision GHG obs | Station-level | 2016-present | Free | SPARQL / REST | CO2/CH4/N2O; atmosphere/ecosystem/ocean |
| ACTRIS | actris.nilu.no | Europe | Aerosol, cloud, trace gas | Station-level | 2000s-present | Free | REST API | Research infrastructure; quality-assured |
| EURDEP | remon.jrc.ec.europa.eu | Europe | Radiation dose rates | Station-level | Real-time | Free | No | ~5500 stations; automatic gamma dose |
| Urban Atlas AQ (Copernicus) | land.copernicus.eu | Europe | Urban AQ indicators | FUA level | 2006/2012/2018 | Free | No | Linked to Urban Atlas land use |

## European National Networks

| Platform | URL | Scope | Pollutants | Stations | Cost | API | Notes |
|---|---|---|---|---|---|---|---|
| Hungarian OLM | legszennyezettseg.met.hu | Hungary | PM10, PM2.5, O3, NO2, SO2, CO | ~30 | Free | No | Operated by HungaroMet |
| Czech CHMI | chmi.cz | Czech Republic | PM, O3, NO2, SO2 | ~150 | Free | No | Czech Hydrometeorological Institute |
| Slovak SHMU | shmu.sk | Slovakia | PM, O3, NO2, SO2 | ~40 | Free | No | Slovak Hydrometeorological Institute |
| Austrian UBA | umweltbundesamt.at | Austria | PM, O3, NO2, SO2 | ~175 | Free | No | Federal Environment Agency |
| German UBA | umweltbundesamt.de | Germany | PM, O3, NO2, SO2, CO | ~500 | Free | REST API | Federal + state networks |
| Polish GIOS | powietrze.gios.gov.pl | Poland | PM, O3, NO2, SO2, CO, C6H6 | ~250 | Free | REST API | Chief Inspectorate of Environmental Protection |
| Romanian CALITATEAER | calitateaer.ro | Romania | PM, O3, NO2, SO2 | ~140 | Free | No | National Air Quality Monitoring Network |
| Croatian DHMZ | kvaliteta-zraka.hr | Croatia | PM, O3, NO2, SO2 | ~30 | Free | No | Meteorological and Hydrological Service |
| Slovenian ARSO | arso.gov.si | Slovenia | PM, O3, NO2, SO2 | ~20 | Free | No | Slovenian Environment Agency |
| UK DEFRA | uk-air.defra.gov.uk | UK | PM, O3, NO2, SO2, CO | 300+ | Free | REST API | AURN + other networks |

## US Networks

| Platform | URL | Scope | Data Type | Resolution | Temporal | Cost | API | Notes |
|---|---|---|---|---|---|---|---|---|
| US EPA AirNow | airnow.gov | USA | Real-time AQI | Station-level | Real-time | Free | REST API | Real-time + forecast AQI |
| US EPA AQS | aqs.epa.gov | USA | Historical AQ data | Station-level | 1980-present | Free | REST API | Quality-assured annual summaries |

## Citizen Science / Low-Cost Sensors

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Notes |
|---|---|---|---|---|---|---|---|
| Sensor.Community (Luftdaten) | sensor.community | Global | Low-cost PM, temp, humidity | Station-level | 2015-present | Free | REST API | ~15k+ sensors worldwide |
| PurpleAir | purpleair.com | Global | Low-cost PM2.5 sensors | Station-level | 2017-present | Free data | REST API | Real-time + historical; API key needed |
| IQAir / AirVisual | iqair.com | Global | AQI from mixed sources | City/station | Real-time | Freemium | REST API | Free tier limited calls |

## Emissions and Greenhouse Gases

| Platform | URL | Scope | Data Type | Resolution | Temporal | Cost | API | Notes |
|---|---|---|---|---|---|---|---|---|
| Climate TRACE | climatetrace.org | Global | Facility-level GHG | Facility point | 2015-present | Free, CC-BY 4.0 | REST API | AI+satellite derived emissions |
| GHGSat | ghgsat.com | Global | Methane point sources | 25m | 2016-present | Commercial | No | PULSE portal free for exploration |
| UNFCCC GHG Data | di.unfccc.int | Global | Country-level GHG | Country | 1990-present | Free | No | National inventory submissions |
| IEA Global Methane Tracker | iea.org | Global | Methane emissions by sector | Country/region | Annual | Free | No | Oil, gas, coal, bioenergy methane |

## Fire Emissions

| Platform | URL | Scope | Data Type | Resolution | Temporal | Cost | API | Notes |
|---|---|---|---|---|---|---|---|---|
| GFED | globalfiredata.org | Global | Fire emissions | 0.25° | 1997-present | Free | No | Global Fire Emissions Database v4 |
| CAMS GFAS | atmosphere.copernicus.eu | Global | Fire radiative power + emissions | 0.1° | 2003-present | Free | CDS API | Daily fire emissions; near-real-time |

## Pollen

| Platform | URL | Scope | Data Type | Resolution | Cost | API | Notes |
|---|---|---|---|---|---|---|---|
| European Pollen Network | polleninfo.org | Europe | Pollen counts + forecast | Station-level | Seasonal | Free | No | EAN network; multiple taxa |
| Hungarian NNK Pollen | antsz.hu (NNK) | Hungary | Pollen monitoring | Station-level | Seasonal | Free | No | Hungarian pollen network |
