"""
Autonomous Price Monitor for Dataset Cadaster
Runs via GitHub Actions on a weekly schedule (or manually).

What it does:
1. Fetches each provider's pricing page(s)
2. Hashes the page content to detect changes
3. If content changed → flags provider for review, extracts prices where possible
4. Updates pricing.json with new hashes, timestamps, and extracted prices
5. Commits and pushes if anything changed

Usage:
  python scripts/check_prices.py              # dry-run (print changes)
  python scripts/check_prices.py --apply      # apply changes to files
  python scripts/check_prices.py --apply --commit  # apply + git commit
"""

import json
import hashlib
import re
import sys
import os
from datetime import datetime, timedelta
from pathlib import Path

# Optional imports - graceful fallback
try:
    import urllib.request
    import urllib.error
    HAS_URLLIB = True
except ImportError:
    HAS_URLLIB = False

ROOT = Path(__file__).parent.parent
PRICING_FILE = ROOT / "pricing.json"
DATASETS_FILE = ROOT / "datasets.json"
REPORT_FILE = ROOT / "scripts" / "price_check_report.json"

APPLY = "--apply" in sys.argv
COMMIT = "--commit" in sys.argv

USER_AGENT = "DatasetCadaster-PriceBot/1.0 (https://github.com/nagyhoho1234/DatasetCadaster)"
TIMEOUT = 15  # seconds


def fetch_page(url):
    """Fetch a URL and return (status_code, content_text, error_msg)."""
    if not HAS_URLLIB:
        return (0, "", "urllib not available")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            content = resp.read().decode("utf-8", errors="replace")
            return (resp.status, content, None)
    except urllib.error.HTTPError as e:
        return (e.code, "", str(e))
    except Exception as e:
        return (0, "", str(e))


def content_hash(text):
    """Hash page content, stripping volatile elements (timestamps, nonces, etc.)."""
    # Remove common volatile patterns
    cleaned = re.sub(r'\b\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', '', text)  # ISO dates
    cleaned = re.sub(r'nonce="[^"]*"', '', cleaned)  # CSP nonces
    cleaned = re.sub(r'csrf[_-]?token[^"]*"[^"]*"', '', cleaned, flags=re.I)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return hashlib.sha256(cleaned.encode()).hexdigest()[:16]


def extract_prices_from_text(text, currency="USD"):
    """Try to extract price-like patterns from page text."""
    patterns = [
        # $15/km², €25/month, $2,700/year etc.
        r'[\$€£][\d,]+(?:\.\d{2})?(?:\s*(?:per|/)\s*(?:km²|km2|sq\s*km|month|mo|year|yr|scene|image))',
        # "from $500" patterns
        r'(?:from|starting\s+at)\s+[\$€£][\d,]+',
        # "$X - $Y" ranges
        r'[\$€£][\d,]+\s*[-–—]\s*[\$€£]?[\d,]+',
    ]
    found = []
    for pat in patterns:
        matches = re.findall(pat, text, re.IGNORECASE)
        found.extend(matches)
    return list(set(found))[:10]  # deduplicate, limit to 10


def run_check():
    """Main check routine."""
    with open(PRICING_FILE, "r", encoding="utf-8") as f:
        pricing = json.load(f)

    report = {
        "checkDate": datetime.now().isoformat()[:19],
        "totalProviders": len(pricing["providers"]),
        "checked": 0,
        "changed": 0,
        "errors": 0,
        "unchanged": 0,
        "changes": [],
        "errors_detail": []
    }

    for provider in pricing["providers"]:
        pid = provider["datasetId"]
        urls_to_check = provider.get("monitorUrls", [])
        if not urls_to_check and provider.get("pricingUrl"):
            urls_to_check = [provider["pricingUrl"]]
        if not urls_to_check:
            print(f"  SKIP {pid}: no URLs to monitor")
            continue

        combined_content = ""
        any_error = False

        for url in urls_to_check:
            status, content, error = fetch_page(url)
            if error or status >= 400:
                print(f"  ERROR {pid}: {url} -> {status} {error}")
                report["errors"] += 1
                report["errors_detail"].append({
                    "datasetId": pid,
                    "url": url,
                    "status": status,
                    "error": error
                })
                any_error = True
                continue
            combined_content += content

        if not combined_content:
            continue

        report["checked"] += 1
        new_hash = content_hash(combined_content)
        old_hash = provider.get("pageHash")

        if old_hash and new_hash != old_hash:
            # PAGE CHANGED
            report["changed"] += 1
            extracted = extract_prices_from_text(combined_content, provider.get("currency", "USD"))
            change_entry = {
                "datasetId": pid,
                "provider": provider["provider"],
                "oldHash": old_hash,
                "newHash": new_hash,
                "extractedPrices": extracted,
                "urls": urls_to_check
            }
            report["changes"].append(change_entry)
            print(f"  CHANGED {pid} ({provider['provider']})")
            if extracted:
                print(f"    Extracted prices: {extracted}")

            if APPLY:
                provider["pageHash"] = new_hash
                provider["lastVerified"] = datetime.now().strftime("%Y-%m-%d")
                if extracted:
                    provider["_extractedPrices"] = extracted
                    provider["_changeDetected"] = datetime.now().strftime("%Y-%m-%d")
        else:
            report["unchanged"] += 1
            if APPLY:
                provider["pageHash"] = new_hash
                provider["lastVerified"] = datetime.now().strftime("%Y-%m-%d")
            if not old_hash:
                print(f"  INIT {pid}: hash stored for first time")
            else:
                print(f"  OK {pid}: no change")

    # Update metadata
    if APPLY:
        pricing["lastAutoCheck"] = datetime.now().strftime("%Y-%m-%d")
        pricing["nextCheckDue"] = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")

        with open(PRICING_FILE, "w", encoding="utf-8") as f:
            json.dump(pricing, f, indent=2, ensure_ascii=False)
        print(f"\n[OK] Updated {PRICING_FILE}")

    # Save report
    os.makedirs(REPORT_FILE.parent, exist_ok=True)
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"[OK] Report saved to {REPORT_FILE}")

    # Summary
    print(f"\n{'='*50}")
    print(f"Price Check Summary ({report['checkDate'][:10]})")
    print(f"  Checked: {report['checked']}")
    print(f"  Changed: {report['changed']}")
    print(f"  Unchanged: {report['unchanged']}")
    print(f"  Errors: {report['errors']}")

    if report["changes"]:
        print(f"\n[!] PRICE CHANGES DETECTED:")
        for c in report["changes"]:
            print(f"  > {c['provider']} ({c['datasetId']})")
            if c["extractedPrices"]:
                print(f"    New prices found: {', '.join(c['extractedPrices'])}")

    if COMMIT and APPLY and report["changed"] > 0:
        os.system('git add pricing.json scripts/price_check_report.json')
        msg = f"auto: price check {report['checkDate'][:10]} — {report['changed']} changes detected"
        os.system(f'git commit -m "{msg}"')
        print("[OK] Changes committed")

    return report


if __name__ == "__main__":
    print(f"Dataset Cadaster — Autonomous Price Monitor")
    print(f"{'='*50}")
    print(f"Mode: {'APPLY + COMMIT' if APPLY and COMMIT else 'APPLY' if APPLY else 'DRY RUN'}")
    print(f"Checking {PRICING_FILE}...\n")
    run_check()
