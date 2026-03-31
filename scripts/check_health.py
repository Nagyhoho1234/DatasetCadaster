#!/usr/bin/env python3
"""
API Health Checker for Dataset Cadaster.

Pings dataset URLs (apiSupport=true) and a curated list of key API endpoints,
records status codes and response times, writes results to health.json.

Usage:
    python check_health.py --apply          # write health.json
    python check_health.py --apply --verbose # write + detailed output
    python check_health.py --verbose         # dry-run with detailed output
"""

import argparse
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

try:
    import urllib.request
    import urllib.error
    import ssl
except ImportError:
    pass

# ---------------------------------------------------------------------------
# Curated API endpoints (beyond what datasets.json provides)
# ---------------------------------------------------------------------------
CURATED_ENDPOINTS = [
    {"id": "copernicus-data-space",        "name": "Copernicus Data Space",         "apiUrl": "https://dataspace.copernicus.eu/api"},
    {"id": "google-earth-engine",          "name": "Google Earth Engine",           "apiUrl": "https://earthengine.googleapis.com"},
    {"id": "ms-planetary-computer",        "name": "MS Planetary Computer",         "apiUrl": "https://planetarycomputer.microsoft.com/api/stac/v1"},
    {"id": "worldpop",                     "name": "WorldPop",                      "apiUrl": "https://api.worldpop.org/v1"},
    {"id": "nasa-earthdata-search",        "name": "NASA Earthdata Search",         "apiUrl": "https://search.earthdata.nasa.gov/api"},
    {"id": "openaq",                       "name": "OpenAQ",                        "apiUrl": "https://openaq.org/v3"},
    {"id": "gbif",                         "name": "GBIF",                          "apiUrl": "https://api.gbif.org/v1"},
    {"id": "cmems",                        "name": "CMEMS",                         "apiUrl": "https://marine.copernicus.eu/api"},
    {"id": "cds-climate",                  "name": "CDS Climate",                   "apiUrl": "https://cds.climate.copernicus.eu/api"},
    {"id": "ads-atmosphere",               "name": "ADS Atmosphere",                "apiUrl": "https://ads.atmosphere.copernicus.eu/api"},
    {"id": "osm-overpass",                 "name": "OSM Overpass",                  "apiUrl": "https://overpass-api.de/api/status"},
    {"id": "wdpa-protected-planet",        "name": "WDPA Protected Planet",         "apiUrl": "https://api.protectedplanet.net/v3"},
    {"id": "obis-ocean-biodiversity",      "name": "OBIS",                          "apiUrl": "https://obis.org/api/v3"},
    {"id": "soilgrids",                    "name": "SoilGrids",                     "apiUrl": "https://rest.isric.org/soilgrids/v2.0"},
    {"id": "global-forest-watch",          "name": "Global Forest Watch",           "apiUrl": "https://data-api.globalforestwatch.org"},
    {"id": "opentopodata",                 "name": "OpenTopoData",                  "apiUrl": "https://api.opentopodata.org/v1"},
    {"id": "us-census-geocoding",          "name": "US Census Geocoding",           "apiUrl": "https://geocoding.geo.census.gov"},
    {"id": "arcgis-services",              "name": "ArcGIS Services",               "apiUrl": "https://services.arcgis.com"},
    {"id": "weatherapi",                   "name": "WeatherAPI",                    "apiUrl": "https://api.weatherapi.com"},
    {"id": "geonames",                     "name": "GeoNames",                      "apiUrl": "https://geonames.org/export"},
    # Additional key endpoints
    {"id": "usgs-earthexplorer",           "name": "USGS EarthExplorer",            "apiUrl": "https://m2m.cr.usgs.gov"},
    {"id": "sentinel-hub",                 "name": "Sentinel Hub",                  "apiUrl": "https://services.sentinel-hub.com/api/v1"},
    {"id": "opentopography",              "name": "OpenTopography",                "apiUrl": "https://portal.opentopography.org/API"},
    {"id": "nasa-power",                   "name": "NASA POWER",                    "apiUrl": "https://power.larc.nasa.gov/api"},
    {"id": "wmo-oscar",                    "name": "WMO OSCAR",                     "apiUrl": "https://oscar.wmo.int/surface/rest/api"},
    {"id": "ecmwf",                        "name": "ECMWF",                         "apiUrl": "https://apps.ecmwf.int/v1"},
    {"id": "emodnet",                      "name": "EMODnet",                       "apiUrl": "https://rest.emodnet.eu"},
    {"id": "noaa-ncei",                    "name": "NOAA NCEI",                     "apiUrl": "https://www.ncei.noaa.gov/access"},
    {"id": "esa-scihub",                   "name": "ESA SciHub",                    "apiUrl": "https://scihub.copernicus.eu"},
    {"id": "stac-browser",                "name": "STAC Index",                    "apiUrl": "https://stacindex.org/api"},
]


def ping_url(url, timeout=10):
    """Send a HEAD request (falling back to GET) and return (status, time_ms, error)."""
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    start = time.monotonic()
    try:
        req = urllib.request.Request(url, method="HEAD",
                                     headers={"User-Agent": "DatasetCadaster-HealthCheck/1.0"})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            status = resp.getcode()
            elapsed = int((time.monotonic() - start) * 1000)
            return status, elapsed, None
    except urllib.error.HTTPError as e:
        elapsed = int((time.monotonic() - start) * 1000)
        return e.code, elapsed, None
    except Exception:
        # HEAD might be blocked; try GET
        pass

    start = time.monotonic()
    try:
        req = urllib.request.Request(url, method="GET",
                                     headers={"User-Agent": "DatasetCadaster-HealthCheck/1.0"})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            status = resp.getcode()
            elapsed = int((time.monotonic() - start) * 1000)
            return status, elapsed, None
    except urllib.error.HTTPError as e:
        elapsed = int((time.monotonic() - start) * 1000)
        return e.code, elapsed, None
    except urllib.error.URLError as e:
        elapsed = int((time.monotonic() - start) * 1000)
        reason = str(getattr(e, "reason", e))
        return 0, elapsed, reason
    except Exception as e:
        elapsed = int((time.monotonic() - start) * 1000)
        return 0, elapsed, str(e)


def load_existing_health(path):
    """Load previous health.json to carry forward lastHealthy / consecutiveFailures."""
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return {ep["datasetId"]: ep for ep in data.get("endpoints", []) if "datasetId" in ep}
    except Exception:
        return {}


def build_check_list(datasets_path):
    """Build the combined list of URLs to check."""
    with open(datasets_path, "r", encoding="utf-8") as f:
        datasets = json.load(f)

    checks = []
    seen_ids = set()

    # 1. Datasets with apiSupport=true
    for d in datasets:
        if not d.get("apiSupport"):
            continue
        did = d.get("id", d.get("name", "").lower().replace(" ", "-"))
        checks.append({
            "datasetId": did,
            "name": d.get("name", ""),
            "url": d.get("url", ""),
            "apiUrl": None,  # may be overridden by curated list
            "source": "datasets.json",
        })
        seen_ids.add(did)

    # 2. Curated API endpoints
    for ep in CURATED_ENDPOINTS:
        if ep["id"] in seen_ids:
            # Merge: add apiUrl to existing entry
            for c in checks:
                if c["datasetId"] == ep["id"]:
                    c["apiUrl"] = ep["apiUrl"]
                    break
        else:
            checks.append({
                "datasetId": ep["id"],
                "name": ep["name"],
                "url": ep.get("apiUrl", ""),
                "apiUrl": ep["apiUrl"],
                "source": "curated",
            })
            seen_ids.add(ep["id"])

    return checks


def check_endpoint(item, timeout=10):
    """Check a single endpoint (main URL + optional apiUrl)."""
    result = {
        "datasetId": item["datasetId"],
        "name": item.get("name", ""),
        "url": item.get("url", ""),
        "apiUrl": item.get("apiUrl"),
    }

    # Ping main URL
    main_url = item.get("url", "")
    if main_url:
        status, rt, err = ping_url(main_url, timeout)
        result["status"] = status
        result["responseTime"] = rt
        result["error"] = err
        result["healthy"] = 200 <= status < 400
    else:
        result["status"] = 0
        result["responseTime"] = 0
        result["error"] = "no URL"
        result["healthy"] = False

    # Ping API URL if different
    api_url = item.get("apiUrl")
    if api_url and api_url != main_url:
        a_status, a_rt, a_err = ping_url(api_url, timeout)
        result["apiStatus"] = a_status
        result["apiResponseTime"] = a_rt
        result["apiError"] = a_err
        result["apiHealthy"] = 200 <= a_status < 400
        # overall health: both must be OK (if api url exists)
        result["healthy"] = result["healthy"] and result["apiHealthy"]
    else:
        result["apiStatus"] = None
        result["apiResponseTime"] = None

    return result


def classify(result):
    """Classify as 'healthy', 'degraded', or 'down'."""
    status = result.get("status", 0)
    rt = result.get("responseTime", 0)
    api_status = result.get("apiStatus")
    api_rt = result.get("apiResponseTime")

    if status == 0 or status >= 400:
        return "down"
    if api_status is not None and (api_status == 0 or api_status >= 400):
        return "down"

    # Degraded: redirect (3xx) or slow (>2s)
    is_redirect = (300 <= status < 400) or (api_status is not None and 300 <= api_status < 400)
    is_slow = rt > 2000 or (api_rt is not None and api_rt > 2000)
    if is_redirect or is_slow:
        return "degraded"

    return "healthy"


def main():
    parser = argparse.ArgumentParser(description="Dataset Cadaster API Health Checker")
    parser.add_argument("--apply", action="store_true", help="Write results to health.json")
    parser.add_argument("--verbose", action="store_true", help="Print detailed output")
    parser.add_argument("--workers", type=int, default=20, help="Number of concurrent workers")
    parser.add_argument("--timeout", type=int, default=10, help="Request timeout in seconds")
    args = parser.parse_args()

    base_dir = Path(__file__).resolve().parent.parent
    datasets_path = base_dir / "datasets.json"
    health_path = base_dir / "health.json"

    if not datasets_path.exists():
        print("ERROR: datasets.json not found at %s" % datasets_path)
        sys.exit(1)

    # Load previous results for continuity
    prev = load_existing_health(health_path)

    # Build check list
    checks = build_check_list(str(datasets_path))
    total = len(checks)
    print("Health check: %d endpoints to check (%d workers, %ds timeout)" % (total, args.workers, args.timeout))

    # Run checks concurrently
    results = []
    start_all = time.monotonic()

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(check_endpoint, item, args.timeout): item for item in checks}
        done_count = 0
        for future in as_completed(futures):
            done_count += 1
            try:
                result = future.result()
            except Exception as e:
                item = futures[future]
                result = {
                    "datasetId": item["datasetId"],
                    "name": item.get("name", ""),
                    "url": item.get("url", ""),
                    "apiUrl": item.get("apiUrl"),
                    "status": 0,
                    "responseTime": 0,
                    "error": str(e),
                    "healthy": False,
                }
            results.append(result)

            if args.verbose:
                tag = classify(result)
                sym = {"healthy": "+", "degraded": "~", "down": "!"}[tag]
                api_info = ""
                if result.get("apiStatus") is not None:
                    api_info = " | API:%d/%dms" % (result["apiStatus"], result.get("apiResponseTime", 0))
                print("  [%s] %s - %d/%dms%s (%d/%d)" % (
                    sym,
                    result.get("name", result["datasetId"])[:50],
                    result.get("status", 0),
                    result.get("responseTime", 0),
                    api_info,
                    done_count,
                    total
                ))

    elapsed_total = time.monotonic() - start_all

    # Merge with previous data for lastHealthy / consecutiveFailures
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    endpoints = []
    counts = {"healthy": 0, "degraded": 0, "down": 0}

    for r in sorted(results, key=lambda x: x.get("datasetId", "")):
        tag = classify(r)
        counts[tag] += 1

        prev_ep = prev.get(r["datasetId"], {})

        if tag == "healthy":
            last_healthy = today
            consec = 0
        else:
            last_healthy = prev_ep.get("lastHealthy", None)
            consec = prev_ep.get("consecutiveFailures", 0) + 1

        ep = {
            "datasetId": r["datasetId"],
            "url": r.get("url", ""),
            "apiUrl": r.get("apiUrl"),
            "status": r.get("status", 0),
            "responseTime": r.get("responseTime", 0),
            "healthy": r.get("healthy", False),
            "classification": tag,
            "lastHealthy": last_healthy,
            "consecutiveFailures": consec,
        }
        if r.get("apiStatus") is not None:
            ep["apiStatus"] = r["apiStatus"]
            ep["apiResponseTime"] = r.get("apiResponseTime", 0)
        if r.get("error"):
            ep["error"] = r["error"]
        if r.get("apiError"):
            ep["apiError"] = r["apiError"]

        endpoints.append(ep)

    health = {
        "lastCheck": now_iso,
        "totalChecked": total,
        "healthy": counts["healthy"],
        "degraded": counts["degraded"],
        "down": counts["down"],
        "checkDurationSeconds": round(elapsed_total, 1),
        "endpoints": endpoints,
    }

    # Summary
    print("")
    print("Results: %d healthy, %d degraded, %d down (%.1fs)" % (
        counts["healthy"], counts["degraded"], counts["down"], elapsed_total))

    if args.apply:
        with open(health_path, "w", encoding="utf-8") as f:
            json.dump(health, f, indent=2, ensure_ascii=True)
        print("Wrote %s" % health_path)
    else:
        print("Dry run - use --apply to write health.json")

    # Print down endpoints
    down_eps = [ep for ep in endpoints if ep["classification"] == "down"]
    if down_eps:
        print("")
        print("DOWN endpoints (%d):" % len(down_eps))
        for ep in down_eps:
            err = ep.get("error", "HTTP %d" % ep.get("status", 0))
            print("  - %s: %s" % (ep["datasetId"], err))

    return len(down_eps)


if __name__ == "__main__":
    sys.exit(0 if main() <= 5 else 1)
