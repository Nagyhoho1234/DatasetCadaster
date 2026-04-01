import json
import glob
import os

DB = "C:/DatasetCadaster/datasets.json"

with open(DB, "r", encoding="utf-8") as f:
    data = json.load(f)

existing_ids = {d["id"] for d in data}
existing_urls = {(d.get("url","") or "").lower().strip().rstrip("/") for d in data}

total_added = 0
total_skipped = 0

for fpath in sorted(glob.glob("C:/DatasetCadaster/supplement_*.json")):
    fname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8") as f:
        entries = json.load(f)

    added = 0
    skipped = 0
    for e in entries:
        eid = e.get("id", "")
        url = (e.get("url", "") or "").lower().strip().rstrip("/")
        if eid in existing_ids or (url and url in existing_urls):
            skipped += 1
            continue
        existing_ids.add(eid)
        if url:
            existing_urls.add(url)
        data.append(e)
        added += 1

    print(f"  {fname}: +{added} added, {skipped} skipped")
    total_added += added
    total_skipped += skipped

data.sort(key=lambda x: x.get("name", "").lower())
with open(DB, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

scopes = {}
countries = {}
for e in data:
    scopes[e.get("scope", "?")] = scopes.get(e.get("scope", "?"), 0) + 1
    if e.get("country"):
        countries[e["country"]] = countries.get(e["country"], 0) + 1

print(f"\nTotal added: {total_added}, skipped: {total_skipped}")
print(f"Database now: {len(data)} datasets across {len(countries)} countries")
print(f"\nBy scope:")
for k, v in sorted(scopes.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")
print(f"\nNational by country:")
for k, v in sorted(countries.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")
