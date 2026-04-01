#!/usr/bin/env python3
"""Build a lightweight summary JSON from the full datasets.json.

Output contains only the fields needed for listing/counting/filtering pages
(landing.html, widget.js). Reduces ~1.2 MB down to ~100-150 KB.

Usage:
    python scripts/build_summary.py
"""

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT = os.path.join(ROOT, "datasets.json")
OUTPUT = os.path.join(ROOT, "datasets-summary.json")

SUMMARY_FIELDS = ["id", "name", "category", "scope", "country", "cost", "apiSupport", "description", "url"]


def build_summary():
    with open(INPUT, "r", encoding="utf-8") as f:
        datasets = json.load(f)

    summary = []
    for ds in datasets:
        entry = {}
        for field in SUMMARY_FIELDS:
            entry[field] = ds.get(field)
        summary.append(entry)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, separators=(",", ":"))

    input_size = os.path.getsize(INPUT)
    output_size = os.path.getsize(OUTPUT)
    print(f"Full:    {input_size:>10,} bytes  ({len(datasets)} entries)")
    print(f"Summary: {output_size:>10,} bytes  ({len(summary)} entries)")
    print(f"Reduction: {100 * (1 - output_size / input_size):.1f}%")


if __name__ == "__main__":
    build_summary()
