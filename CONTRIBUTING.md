# Contributing to Dataset Cadaster

Thank you for your interest in improving the catalog! This guide covers the main ways to contribute.

***

## Suggest a New Dataset

1. Open a new Issue using the **[Dataset Suggestion](../../issues/new?template=suggest-dataset.yml)** template
2. Fill in as many fields as you can: name, URL, category, country, cost, API support
3. A maintainer will review and add it to `datasets.json`

**Alternatively**, submit a Pull Request directly:

1. Fork the repository
2. Add your entry to `datasets.json` following the existing schema:
   ```json
   {
     "id": "cc-provider-short-name",
     "name": "Full Dataset Name",
     "category": "hydrology",
     "scope": "national",
     "country": "HU",
     "cost": "free",
     "apiSupport": true,
     "description": "One-sentence description of what this dataset provides.",
     "url": "https://example.com/data"
   }
   ```
3. Run `python scripts/build_summary.py` to regenerate the summary file
4. Submit a PR with a clear title (e.g., "Add Hungarian flood risk dataset")

***

## Report a Broken Link

1. Open a new Issue using the **[Broken Link](../../issues/new?template=broken-link.yml)** template
2. Provide the dataset name (or ID) and the URL that is broken
3. If you know the new URL, include it in the description

The automated link checker runs weekly, but manual reports are still valuable -- especially for links that return 200 but have moved or changed content.

***

## Update Pricing Information

1. Open a new Issue using the **[Price Update](../../issues/new?template=price-update.yml)** template
2. Include the dataset name, the old price (if known), and the new price
3. Link to the official pricing page if possible

The automated price monitor detects page changes but cannot always extract exact prices. Human-reported updates are the most reliable source.

***

## Add a New Country

To improve coverage for a country that is underrepresented:

1. Research the country's national mapping agency, geoportal, environmental agency, meteorological service, and statistical office
2. Add entries to `datasets.json` following the schema above
3. Use the ISO 3166-1 alpha-2 country code (e.g., `"HU"`, `"DE"`, `"BR"`)
4. Run `python scripts/build_summary.py`
5. Submit a PR

***

## Code Style Guidelines

This project uses **pure JavaScript** with no frameworks, transpilers, or build tools.

- **HTML**: Semantic HTML5. One page = one file. Shared styles and scripts in `shared.css` / `shared.js`.
- **CSS**: Use CSS custom properties (variables) defined in `shared.css`. Mobile-first responsive design.
- **JavaScript**: ES6+ (modules are not used -- scripts are loaded via `<script>` tags). No jQuery, no React, no Vue.
- **Python**: Standard library only. No pip dependencies. Python 3.10+ compatibility.
- **Data**: All dataset information lives in `datasets.json`. Do not duplicate data across files.
- **Naming**: Use kebab-case for file names, camelCase for JS variables and functions, BEM-like naming for CSS classes where practical.

***

## General Guidelines

- Keep PRs focused -- one feature or fix per PR
- Test your changes locally by opening the HTML files in a browser
- Do not introduce external dependencies (npm packages, CDN libraries beyond Leaflet, Python packages)
- Write clear commit messages describing **what** changed and **why**
