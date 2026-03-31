# Dataset Cadaster & GeoEstimator — Maintenance and Pricing Update Strategy

> Version 1.0 | 2026-03-31
> For a single-researcher maintainer of static web apps (HTML/CSS/JS, no backend)

---

## Table of Contents

1. [Context and Research Findings](#1-context-and-research-findings)
2. [Data Architecture for Maintainability](#2-data-architecture-for-maintainability)
3. [Update Schedule](#3-update-schedule)
4. [Automation Options](#4-automation-options)
5. [Community Contribution Model](#5-community-contribution-model)
6. [Semi-Automated Price Tracking](#6-semi-automated-price-tracking)
7. [One Hour Per Month Routine](#7-one-hour-per-month-routine)
8. [File Structure Recommendation](#8-file-structure-recommendation)

---

## 1. Context and Research Findings

### How Often Do Satellite Data Prices Change?

Research shows that satellite imagery pricing changes are **infrequent but significant** when they occur:

- **Maxar** overhauled its pricing in **December 2024**, simplifying the structure and eliminating the "newer than 90 days" premium tier. Major pricing restructures happen roughly every 1-2 years, with minor adjustments in between.
- **Planet Labs** uses flexible, quote-based pricing that shifts gradually. Their public pricing page changes only a few times per year, but individual contract terms evolve continuously.
- **Airbus, ICEYE, Capella Space** all use **custom quote-based pricing** — they do not publish fixed price lists. What changes is not a price number on a webpage, but the existence of new products, new tiers, or new access models.
- **Industry trend**: The market is moving from price-per-km2 toward subscription and insights-as-a-service models, meaning the *structure* of pricing changes more often than specific numbers.

**Practical implication**: Price data needs review **quarterly**, not monthly. Most changes are structural (new products, retired tiers) rather than numeric.

### How Fast Do URLs Break (Link Rot)?

Research from multiple studies provides clear decay rates:

| Time Period | Survival Rate | Links Lost |
|---|---|---|
| 1 month | 96.6% | ~3.4% |
| 3 months | 92.0% | ~8.0% |
| 1 year | 82.4% | ~17.6% |
| 3 years | 71.6% | ~28.4% |
| 7 years | 56.6% | ~43.4% |

A dataset catalog with ~500 URLs can expect **~88 broken links per year** if unchecked. Government and institutional URLs tend to be more stable than commercial ones, but reorganizations (e.g., NASA migrating all sites to Earthdata through 2026) cause bulk breakage.

**Practical implication**: URL checking must be **weekly or biweekly** via automation — manual checking is not feasible.

### How Do Successful Curated Lists Handle Maintenance?

- **awesome-gee-community-catalog** (Samapriya Roy): Uses GitHub Issues templates for dataset submissions, reviews/preprocesses each contribution personally, updates on a mix of fixed cadence and ad-hoc requests. Unfunded grassroots project — very similar to our situation.
- **awesome-public-datasets**: Accepts contributions via PRs with automated checks, has a Slack community for coordination.
- **sindresorhus/awesome**: Defines strict inclusion criteria, requires consistent formatting, and uses community PRs with maintainer review.
- **Common pattern**: All successful lists separate *discovery* (community-driven) from *validation* (maintainer-driven).

---

## 2. Data Architecture for Maintainability

### 2.1 Split JSON Architecture

The current monolithic `datasets.json` should be split into purpose-specific files to isolate changes and reduce merge conflicts:

```
data/
  datasets.json          # Core dataset metadata (stable, changes rarely)
  pricing.json           # Commercial pricing info (changes quarterly)
  health.json            # Auto-generated URL health status
  changelog.json         # Machine-readable change log
  meta.json              # Database version, last-updated dates, stats
```

**Why split pricing from datasets?** Pricing changes on a different cadence than metadata. Separating them means you can update prices without risking accidental edits to stable dataset descriptions. It also makes it obvious *when* pricing was last reviewed.

### 2.2 Core `datasets.json` Structure

The app currently reads either a flat array or `{ datasets: [...] }`. The recommended structure wraps the array with metadata:

```json
{
  "$schema": "./schemas/datasets.schema.json",
  "version": "2.4.0",
  "generated": "2026-03-31",
  "datasets": [
    {
      "id": "copernicus-dem-30",
      "name": "Copernicus DEM GLO-30",
      "category": "dem-lidar",
      "subcategory": "global-dem",
      "operator": "European Space Agency / Airbus",
      "description": "Global 30m DEM derived from TanDEM-X mission",
      "url": "https://spacedata.copernicus.eu/collections/copernicus-digital-elevation-model",
      "altUrls": [
        "https://registry.opendata.aws/copernicus-dem/"
      ],
      "cost": "free",
      "apiSupport": true,
      "apiType": "STAC",
      "spatialResolution": "30m",
      "temporalResolution": "static",
      "temporalCoverage": "2021-present",
      "scope": "global",
      "formats": "GeoTIFF, COG",
      "license": "Free and open",
      "tags": ["elevation", "DEM", "TanDEM-X", "Copernicus"],
      "region": ["global"],
      "dateAdded": "2025-01-15",
      "dateVerified": "2026-03-01",
      "status": "active",
      "notes": ""
    }
  ]
}
```

**Key additions over the current schema:**
- `id` — stable machine-readable identifier (kebab-case, never changes even if the name does)
- `altUrls` — fallback/mirror URLs; helps when the primary URL breaks
- `apiType` — distinguishes STAC, OGC, REST, etc.
- `subcategory` — finer grouping without over-complicating filters
- `dateAdded` — when entry was first added to the catalog
- `dateVerified` — when a human last confirmed the entry is correct
- `status` — one of `active`, `deprecated`, `unavailable`, `restructured`
- `notes` — free-text for temporary issues ("migrating to new platform Q2 2026")

### 2.3 Separate `pricing.json`

```json
{
  "version": "1.2.0",
  "lastReviewed": "2026-03-01",
  "nextReviewDue": "2026-06-01",
  "pricing": [
    {
      "datasetId": "maxar-worldview-archive",
      "pricingModel": "per-area",
      "currency": "USD",
      "tiers": [
        {
          "label": "Archive imagery (>90 days)",
          "unit": "km2",
          "minPrice": 14,
          "maxPrice": 24,
          "minOrder": "25 km2",
          "notes": "Simplified pricing effective Dec 2024"
        },
        {
          "label": "New tasking",
          "unit": "km2",
          "minPrice": 24,
          "maxPrice": 35,
          "minOrder": "100 km2",
          "notes": ""
        }
      ],
      "pricingUrl": "https://www.maxar.com/products/imagery",
      "lastVerified": "2026-03-01",
      "lastChanged": "2024-12-05",
      "priceConfidence": "published",
      "sourceNotes": "Simplified pricing unveiled Dec 5 2024 per Apollo Mapping"
    },
    {
      "datasetId": "planet-daily",
      "pricingModel": "subscription",
      "currency": "USD",
      "tiers": [
        {
          "label": "Explorer (basic access)",
          "unit": "month",
          "minPrice": null,
          "maxPrice": null,
          "minOrder": null,
          "notes": "Contact sales; quote-based"
        }
      ],
      "pricingUrl": "https://www.planet.com/pricing/",
      "lastVerified": "2026-03-01",
      "lastChanged": null,
      "priceConfidence": "estimate",
      "sourceNotes": "Planet uses custom quotes; ranges are researcher estimates"
    }
  ]
}
```

**`priceConfidence` values:**
- `published` — provider publishes a price list (e.g., Maxar via resellers)
- `estimate` — based on researcher experience, community reports, or reseller quotes
- `unavailable` — quote-only, no public reference
- `free` — no cost

### 2.4 Auto-Generated `health.json`

Generated by the weekly link checker (Section 4). Not hand-edited.

```json
{
  "lastCheck": "2026-03-29T18:00:00Z",
  "totalChecked": 523,
  "healthy": 509,
  "broken": 8,
  "timeout": 4,
  "redirected": 2,
  "issues": [
    {
      "datasetId": "usgs-earth-explorer",
      "url": "https://earthexplorer.usgs.gov/",
      "status": 503,
      "lastHealthy": "2026-03-22",
      "consecutiveFailures": 1
    }
  ]
}
```

### 2.5 Version Numbering

Use **calendar-aware semantic versioning**:

```
MAJOR.MINOR.PATCH

MAJOR  — structural schema changes (fields added/removed, breaking format changes)
MINOR  — content additions (new datasets, new pricing entries)
PATCH  — corrections (fixed URLs, updated prices, typo fixes)
```

Examples:
- `2.0.0` — added `pricing.json` as a separate file (schema change)
- `2.1.0` — added 15 new ocean/bathymetry datasets
- `2.1.1` — fixed 3 broken URLs, updated Maxar pricing

### 2.6 Changelog

Maintain a human-readable `CHANGELOG.md` and a machine-readable `changelog.json`:

```json
{
  "changes": [
    {
      "version": "2.1.1",
      "date": "2026-03-15",
      "type": "patch",
      "summary": "Quarterly price review + broken link fixes",
      "details": [
        "Updated Maxar archive pricing to reflect Dec 2024 simplification",
        "Fixed 3 broken URLs (USGS, ESA Heritage, NOAA NCEI)",
        "Marked 1 dataset as deprecated (Sentinel-5P L1 via old portal)"
      ]
    }
  ]
}
```

---

## 3. Update Schedule

### 3.1 What Changes and How Often

| What | Change Frequency | Check Cadence | Detection Method |
|---|---|---|---|
| URLs (link rot) | ~3.4%/month | **Weekly** (automated) | Lychee link checker via GitHub Actions |
| Prices (numeric) | 1-2x/year per provider | **Quarterly** (manual) | Manual review of ~20 pricing URLs |
| Pricing structure (new tiers/models) | 1-2x/year | **Quarterly** (manual) | Google Alerts + RSS feeds |
| New datasets | Continuous | **Monthly** (manual scan) | RSS feeds, newsletters, community tips |
| Deprecated/removed datasets | ~5-10/year | **Quarterly** | Link checker flags + manual review |
| API changes | 2-3x/year per provider | **Quarterly** | API endpoint health check + changelogs |
| Platform reorganizations | 1-2x/year (major) | **As they happen** | Google Alerts, community reports |

### 3.2 Priority Tiers

**Tier 1 — Automated (no human time required):**
- URL health checks (weekly)
- Basic API endpoint pings (weekly)

**Tier 2 — Monthly human review (15 min):**
- Triage automated link check results (fix or mark broken)
- Scan RSS feeds for new datasets
- Review any community-submitted Issues/PRs

**Tier 3 — Quarterly deep review (2-3 hours):**
- Visit all pricing URLs and update `pricing.json`
- Check for new products/constellations from major providers
- Review deprecated datasets (status = unavailable for >3 months? remove or archive)
- Update `dateVerified` on all entries touched
- Bump version, update changelog

**Tier 4 — Annual (half day):**
- Full catalog audit: every entry opened and verified
- Schema review: do we need new fields?
- Community outreach: post to relevant forums asking for corrections
- Statistics review: how many datasets added/removed/broken this year?

---

## 4. Automation Options (Free/Low-Cost)

### 4.1 Weekly Link Checking with Lychee (GitHub Actions)

Lychee is the recommended tool: written in Rust, fast (checks ~500 links in under 2 minutes), supports caching, has a mature GitHub Action, and is completely free.

Create `.github/workflows/link-check.yml`:

```yaml
name: Link Health Check

on:
  schedule:
    - cron: '0 6 * * 0'  # Every Sunday at 06:00 UTC
  workflow_dispatch:       # Manual trigger

jobs:
  check-links:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Restore lychee cache
        uses: actions/cache@v4
        with:
          path: .lycheecache
          key: cache-lychee-${{ github.sha }}
          restore-keys: cache-lychee-

      - name: Check URLs in datasets.json
        uses: lycheeverse/lychee-action@v2
        with:
          args: >-
            --cache
            --max-cache-age 3d
            --timeout 30
            --max-retries 3
            --accept 200..=299,403,429
            --exclude-mail
            --exclude 'localhost'
            --format json
            --output link-report.json
            data/datasets.json
            data/pricing.json
          fail: false

      - name: Generate health report
        if: always()
        run: |
          python scripts/parse-link-report.py link-report.json data/health.json

      - name: Create issue if broken links found
        if: always()
        uses: peter-evans/create-issue-from-file@v5
        with:
          title: "Weekly Link Check: broken links detected"
          content-filepath: link-report-summary.md
          labels: link-rot, automated
          assignees: your-github-username
```

**Cost**: Free for public repos on GitHub (2,000 Actions minutes/month). For private repos, the free tier provides 500 minutes/month — more than enough for a weekly 2-minute job.

### 4.2 Additional Automation Ideas

**Google Alerts (free, zero maintenance):**

Set up alerts for:
- `"Maxar" pricing OR "price change" OR "new pricing"`
- `"Planet Labs" pricing OR subscription`
- `"Copernicus" new dataset OR "data access"`
- `"Sentinel" new product OR decommission`
- `"ICEYE" pricing OR "new product"`
- `"Airbus" "Pleiades Neo" OR "SPOT" pricing`

These arrive via email and require no infrastructure.

**RSS Feeds to Monitor:**

| Feed | URL | What It Catches |
|---|---|---|
| NASA Earthdata | https://www.earthdata.nasa.gov/learn/rss-feeds | New NASA datasets, platform changes |
| Copernicus Data Space | https://dataspace.copernicus.eu/stay-informed/RSSfeeds | New Copernicus data, access changes |
| ESA Earth Online | https://earth.esa.int/ (RSS) | ESA mission updates, new data |
| USGS News | USGS RSS feeds | Landsat, NAIP updates |

Subscribe to these in any RSS reader (Feedly free tier is sufficient).

### 4.3 Why Not Scrape Pricing Pages Automatically?

Legal and practical analysis:

- **Legally**: Scraping publicly available pricing data for personal/research use is generally low-risk, especially if you respect `robots.txt`, use reasonable request rates, and do not republish raw scraped content.
- **Practically**: It is fragile and not worth the effort. Pricing pages use varied HTML structures, change layout frequently, and most commercial providers (Airbus, ICEYE, Capella) do not even publish prices — they require quotes. The ~10 providers with public pricing can be checked manually in 15 minutes quarterly.
- **Recommendation**: Do **not** automate price scraping. Instead, use manual checks with a structured checklist (Section 6).

---

## 5. Community Contribution Model

### 5.1 GitHub Issues Templates

Create `.github/ISSUE_TEMPLATE/suggest-dataset.yml`:

```yaml
name: Suggest a Dataset
description: Propose a new dataset for the catalog
title: "[Dataset] "
labels: ["new-dataset", "community"]
body:
  - type: markdown
    attributes:
      value: "Thanks for suggesting a dataset! Please fill in what you can."
  - type: input
    id: name
    attributes:
      label: Dataset Name
      placeholder: "e.g., Copernicus DEM GLO-30"
    validations:
      required: true
  - type: input
    id: url
    attributes:
      label: URL
      placeholder: "https://..."
    validations:
      required: true
  - type: dropdown
    id: cost
    attributes:
      label: Cost Model
      options:
        - Free
        - Freemium
        - Commercial
        - Unknown
  - type: dropdown
    id: category
    attributes:
      label: Category
      options:
        - dem-lidar
        - satellite-optical
        - satellite-sar
        - land-use-land-cover
        - climate-weather
        - air-quality-atmospheric
        - geology-geophysics
        - ocean-marine-bathymetry
        - population-urban-built
        - admin-boundaries-cadastral
        - geodetic
        - other
  - type: textarea
    id: details
    attributes:
      label: Additional Details
      description: "Resolution, coverage, API support, etc."
```

Create `.github/ISSUE_TEMPLATE/report-problem.yml`:

```yaml
name: Report a Problem
description: Report a broken link, wrong price, or outdated information
title: "[Fix] "
labels: ["correction", "community"]
body:
  - type: dropdown
    id: problem-type
    attributes:
      label: Problem Type
      options:
        - Broken link (404 or unreachable)
        - Wrong price or pricing model
        - Dataset deprecated or removed
        - Incorrect metadata (resolution, coverage, etc.)
        - URL changed (I know the new one)
        - Other
    validations:
      required: true
  - type: input
    id: dataset-name
    attributes:
      label: Dataset Name
      placeholder: "Which dataset has the problem?"
    validations:
      required: true
  - type: textarea
    id: details
    attributes:
      label: Details
      description: "What is wrong and what should it be?"
    validations:
      required: true
```

### 5.2 CONTRIBUTING.md

```markdown
# Contributing to Dataset Cadaster

Thank you for helping keep this catalog accurate!

## How to Contribute

### Report a problem
Use the "Report a Problem" issue template. No technical knowledge needed.

### Suggest a new dataset
Use the "Suggest a Dataset" issue template. Provide the URL and basic info;
the maintainer will fill in the rest.

### Submit a direct fix (for those comfortable with JSON)
1. Fork the repository
2. Edit the relevant file in `data/`
3. Run `node scripts/validate.js` to check your JSON
4. Submit a pull request

### What makes a good dataset entry?
- The dataset must be **currently available** (not just announced)
- It must be relevant to **geospatial or environmental research**
- Provide a **direct URL** to the data access page (not a news article about it)
- Commercial datasets are welcome — include pricing if publicly available

### What the maintainer does after your submission
- Verifies the URL and metadata
- Adds standardized fields (id, tags, dates)
- Merges into the catalog with credit

## Credit
Contributors are acknowledged in CHANGELOG.md with their GitHub username.
```

### 5.3 Crediting Contributors

In `CHANGELOG.md`, each entry includes contributors:

```markdown
## v2.2.0 — 2026-06-15
- Added 8 new datasets (thanks @contributor1, @contributor2)
- Fixed pricing for Planet SkySat (thanks @contributor3)
- Removed 2 deprecated ESA Heritage Mission entries
```

No separate contributors file is needed at this scale — changelog credit is sufficient and low-maintenance.

### 5.4 Review Process

All community contributions go through the maintainer:

1. **Issue submitted** (via template) -- auto-labeled
2. **Maintainer reviews** during monthly check (or sooner if notified)
3. **Maintainer creates the JSON entry** (community members should not need to understand the schema)
4. **Merge + changelog entry** with credit
5. **Close issue** with a thank-you

For direct PRs to data files:
1. PR submitted
2. Automated JSON validation runs (GitHub Action)
3. Maintainer reviews accuracy
4. Merge or request changes

---

## 6. Semi-Automated Price Tracking

### 6.1 Quarterly Price Check Checklist

Visit these ~20 URLs quarterly. Estimated time: 15-20 minutes.

**VHR Optical Providers (published pricing):**

| # | Provider | Check URL | What to Look For |
|---|---|---|---|
| 1 | Maxar (via Apollo Mapping) | apollomapping.com/imagery-price-list | Archive & tasking rates per km2 |
| 2 | Maxar (direct) | maxar.com/products | Product tier changes |
| 3 | Planet | planet.com/pricing | Subscription tiers, Explorer pricing |
| 4 | Airbus (via resellers) | apollomapping.com/imagery-price-list | Pleiades, SPOT per km2 |
| 5 | SkyWatch/EarthCache | skywatch.com/pricing | API access tiers |
| 6 | UP42 | up42.com/pricing | Credit-based pricing changes |
| 7 | LAND INFO | landinfo.com/satellite-imagery-pricing | Aggregated price overview |
| 8 | OnGeo Intelligence | ongeo-intelligence.com/blog/satellite-imagery-pricing-guide | Price guide updates |

**SAR Providers (quote-based — check for structural changes):**

| # | Provider | Check URL | What to Look For |
|---|---|---|---|
| 9 | ICEYE | iceye.com/products | New products, access model changes |
| 10 | Capella Space | capellaspace.com/data | New tiers, API changes |
| 11 | Umbra | umbra.space/pricing | On-demand tasking rates |

**Free/Open Data Platforms (check for access changes):**

| # | Platform | Check URL | What to Look For |
|---|---|---|---|
| 12 | Copernicus Data Space | dataspace.copernicus.eu | Access policy changes, quotas |
| 13 | NASA Earthdata | earthdata.nasa.gov | Migration status, new collections |
| 14 | USGS EarthExplorer | earthexplorer.usgs.gov | Landsat pricing, NAIP updates |
| 15 | Google Earth Engine | earthengine.google.com | Commercial licensing changes |
| 16 | Microsoft Planetary Computer | planetarycomputer.microsoft.com | Access policy, new datasets |
| 17 | AWS Open Data | registry.opendata.aws | New geospatial datasets |

**Regional (Central Europe):**

| # | Platform | Check URL | What to Look For |
|---|---|---|---|
| 18 | Hungarian Lechner (fentrol.hu) | fentrol.hu | New datasets, access changes |
| 19 | EU Open Data Portal | data.europa.eu | New geospatial collections |
| 20 | Eurostat GISCO | ec.europa.eu/eurostat/web/gisco | Boundary updates, new products |

### 6.2 Price History Log

Maintain a simple CSV at `data/price-history.csv`:

```csv
date,datasetId,tier,minPrice,maxPrice,unit,currency,source,notes
2024-12-05,maxar-worldview-archive,archive,14,24,km2,USD,apollomapping.com,"Simplified pricing - removed 90-day premium"
2025-06-01,maxar-worldview-archive,archive,14,24,km2,USD,apollomapping.com,"No change"
2025-09-01,maxar-worldview-archive,archive,14,24,km2,USD,apollomapping.com,"No change"
2026-03-01,maxar-worldview-archive,archive,14,24,km2,USD,apollomapping.com,"No change"
```

**Why CSV?** It is the simplest format for a time-series log. A researcher can open it in Excel, plot trends, and append rows without learning JSON. It also diffs cleanly in git.

Record "no change" entries — they prove you checked and confirm stability.

### 6.3 Displaying "Last Verified" in the UI

Add a subtle indicator to dataset cards and the estimator. In the card HTML:

```html
<span class="verified-date" title="Price last verified March 2026">
  Verified: Mar 2026
</span>
```

Style it as a small, muted badge. If `dateVerified` is older than 6 months, show it in yellow/orange as a warning. If older than 12 months, show in red.

This is trivially implemented in the existing `cardHTML()` function by reading `dateVerified` from each dataset entry.

---

## 7. One Hour Per Month Routine

### The Monthly Maintenance Session

Block 60 minutes on your calendar, ideally the first Monday of each month.

**Minutes 0-10: Triage automated results**
1. Open the latest GitHub Actions link-check results
2. For each broken URL:
   - If it is a temporary server error (503, timeout) and has <3 consecutive failures: ignore, it will be rechecked next week
   - If it has 3+ consecutive failures: search for the new URL, update `datasets.json`, or mark status as `unavailable`
3. Close or comment on the automated issue

**Minutes 10-20: Scan for new datasets**
1. Check your RSS reader (NASA Earthdata, Copernicus, ESA feeds)
2. Scan Google Alert emails for the past month
3. Check GitHub Issues for community suggestions
4. For each promising new dataset: add a quick entry to a "to-add" list (a simple text file or a GitHub Issue labeled `backlog`)

**Minutes 20-35: Process the to-add list**
1. For each new dataset, create a JSON entry with all required fields
2. Verify the URL works
3. Add to `datasets.json`
4. Commit with a descriptive message

**Minutes 35-45: Review community contributions**
1. Check open Issues and PRs
2. For dataset suggestions: validate and create entry, or ask for clarification
3. For problem reports: fix and close, or acknowledge and label for quarterly review
4. Credit contributors in commit messages

**Minutes 45-55: Quick spot-checks**
1. Open the live site and try 5 random dataset links
2. Check that filters and search still work
3. If this is a quarter-end month (March, June, September, December): do the quarterly pricing review instead (takes an extra hour)

**Minutes 55-60: Housekeeping**
1. Update `meta.json` with new date and counts
2. Bump patch version
3. Update `CHANGELOG.md`
4. Commit and deploy

### If Time Is Extremely Limited (15-minute version)

1. (5 min) Check automated link-check results, fix any with 3+ failures
2. (5 min) Skim GitHub Issues, triage the obvious ones
3. (5 min) Commit fixes, bump version, deploy

Skip new dataset discovery and pricing review — they can wait for next month.

---

## 8. File Structure Recommendation

### 8.1 Complete Directory Layout

```
DatasetCadaster/
|
|-- app/
|   |-- landing.html              # Landing page
|   |-- index.html                # Dataset Cadaster (catalog browser)
|   |-- estimator.html            # GeoEstimator (cost calculator)
|
|-- data/
|   |-- datasets.json             # Core dataset metadata (THE source of truth)
|   |-- pricing.json              # Commercial pricing details (separate cadence)
|   |-- health.json               # Auto-generated link health report
|   |-- price-history.csv         # Append-only price change log
|   |-- meta.json                 # Version, dates, statistics
|   |-- changelog.json            # Machine-readable changelog
|   |-- schemas/
|   |   |-- datasets.schema.json  # JSON Schema for validation
|   |   |-- pricing.schema.json   # JSON Schema for validation
|
|-- scripts/
|   |-- validate.js               # Validates JSON against schemas
|   |-- parse-link-report.py      # Converts lychee output to health.json
|   |-- stats.js                  # Generates meta.json statistics
|
|-- .github/
|   |-- workflows/
|   |   |-- link-check.yml        # Weekly automated URL check
|   |   |-- validate.yml          # PR validation (schema check)
|   |-- ISSUE_TEMPLATE/
|   |   |-- suggest-dataset.yml   # Community dataset suggestion form
|   |   |-- report-problem.yml    # Community problem report form
|
|-- CHANGELOG.md                  # Human-readable changelog
|-- CONTRIBUTING.md               # How to contribute
|-- README.md                     # Project overview (already exists or add)
|-- LICENSE                       # License file
```

### 8.2 Backward Compatibility

The current app reads `../datasets.json` (one level up from `app/`). With the new structure, `datasets.json` moves to `data/datasets.json`. Update the fetch paths in the HTML files:

```javascript
// Before:
fetch("../datasets.json")

// After:
fetch("../data/datasets.json")
```

Alternatively, during migration, place a small `datasets.json` at the root that re-exports:

```json
// Root datasets.json — compatibility shim (remove after transition)
// The app should fetch from data/datasets.json instead
```

Or simply update the three HTML files — it is a one-line change in each.

### 8.3 Example `meta.json`

```json
{
  "version": "2.1.1",
  "lastUpdated": "2026-03-31",
  "lastLinkCheck": "2026-03-29",
  "lastPriceReview": "2026-03-01",
  "nextPriceReview": "2026-06-01",
  "stats": {
    "totalDatasets": 523,
    "freeDatasets": 341,
    "freemiumDatasets": 67,
    "commercialDatasets": 115,
    "withApi": 198,
    "categories": 12,
    "brokenLinks": 3,
    "avgDaysSinceVerified": 42
  },
  "maintainer": "Your Name",
  "repository": "https://github.com/yourname/DatasetCadaster"
}
```

### 8.4 How the App Loads Data (Updated)

The app can load `datasets.json` and optionally merge in `pricing.json` to enrich commercial entries:

```javascript
// In index.html — load core data, then optionally enrich with pricing
Promise.all([
  fetch("../data/datasets.json").then(r => r.json()),
  fetch("../data/pricing.json").then(r => r.json()).catch(() => null)
]).then(([dsData, prData]) => {
  allData = dsData.datasets || dsData;

  // Merge pricing into dataset entries if pricing file loaded
  if (prData && prData.pricing) {
    const priceMap = {};
    prData.pricing.forEach(p => { priceMap[p.datasetId] = p; });
    allData.forEach(d => {
      if (priceMap[d.id]) {
        d._pricing = priceMap[d.id];
      }
    });
  }

  updateStats();
  applyFilters();
});
```

This keeps the catalog fully functional even if `pricing.json` fails to load.

---

## Summary of Key Decisions

| Decision | Recommendation | Rationale |
|---|---|---|
| Monolithic vs. split JSON | **Split** (datasets + pricing + health) | Different update cadences; isolates risk |
| Link checking tool | **Lychee** via GitHub Actions | Fastest, best GitHub integration, free |
| Link check frequency | **Weekly** (automated) | ~3.4% link rot/month demands frequent checks |
| Price check frequency | **Quarterly** (manual) | Prices change 1-2x/year; not worth automating |
| Price scraping | **Do not automate** | Fragile, legally gray, only ~10 public URLs |
| Community model | **GitHub Issues templates** | Low friction for contributors, maintainer controls quality |
| New dataset discovery | **RSS + Google Alerts + community** | Passive discovery costs zero ongoing time |
| Time budget | **1 hour/month + 1 extra hour quarterly** | Sustainable for a solo researcher |
| Version scheme | **Semver (MAJOR.MINOR.PATCH)** | Simple and widely understood |
| Price display in UI | **"Verified: MMM YYYY" badge** with age-based coloring | Honest about data freshness |

---

## Sources

Research informing this plan drew on the following:

- [Satellite Imagery Pricing Guide (Nimbo Earth)](https://nimbo.earth/stories/satellite-imagery-pricing/)
- [Simplified Maxar Pricing (Apollo Mapping)](https://apollomapping.com/blog/simplified-maxar-pricing-unveiled-on-december-5th)
- [Planet Labs Pricing](https://www.planet.com/pricing/)
- [SkyWatch Pricing Guide](https://skywatch.com/satellite-imagery-pricing-what-you-need-to-know/)
- [OnGeo Satellite Imagery Pricing Guide 2025](https://ongeo-intelligence.com/blog/satellite-imagery-pricing-guide)
- [Link Rot Analysis (John Defeo)](https://www.johnwdefeo.com/articles/link-rot-analysis)
- [Ahrefs Link Rot Study](https://ahrefs.com/blog/link-rot-study/)
- [Link Rot (Wikipedia)](https://en.wikipedia.org/wiki/Link_rot)
- [Lychee Link Checker](https://github.com/lycheeverse/lychee)
- [Lychee GitHub Action](https://github.com/lycheeverse/lychee-action)
- [awesome-gee-community-catalog Contributing](https://gee-community-catalog.org/contributing/)
- [awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets)
- [sindresorhus/awesome](https://github.com/sindresorhus/awesome)
- [NASA Earthdata RSS Feeds](https://www.earthdata.nasa.gov/learn/rss-feeds)
- [Copernicus Data Space RSS](https://dataspace.copernicus.eu/stay-informed/RSSfeeds)
- [Is Web Scraping Legal? (ScraperAPI)](https://www.scraperapi.com/web-scraping/is-web-scraping-legal/)
- [Is Price Scraping Legal? (ProWebScraper)](https://prowebscraper.com/blog/is-price-scraping-legal/)
- [LAND INFO Satellite Imagery Pricing](https://landinfo.com/satellite-imagery-pricing/)
