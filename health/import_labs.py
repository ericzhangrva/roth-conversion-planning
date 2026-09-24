#!/usr/bin/env python3
"""
Automated Lab Results Importer & Dashboard Generator
Usage:
    python3 import_labs.py              # Process all HTML files in current directory
    python3 import_labs.py <file1.html> # Process specific file(s)
"""

import sys
import os
import glob
from process_labs import parse_lab_file, build_database, export_csv, export_json, HEALTH_DIR
from build_dashboard import generate_dashboard

def main():
    if len(sys.argv) > 1:
        target_files = sys.argv[1:]
    else:
        all_files = sorted(glob.glob(os.path.join(HEALTH_DIR, "*.html")))
        target_files = [f for f in all_files if os.path.basename(f) not in ("index.html", "dashboard.html")]

    print(f"=== Health & Lab Results Ingestion ===")
    print(f"Scanning {len(target_files)} lab report files...")

    all_records = []
    for f in target_files:
        if not os.path.isfile(f):
            print(f"Warning: file not found: {f}")
            continue
        recs = parse_lab_file(f)
        all_records.extend(recs)
        if recs:
            print(f"  ✓ {os.path.basename(f):20} | Date: {recs[0]['date_display']} | Extracted {len(recs)} tests")
        else:
            print(f"  ⚠ {os.path.basename(f):20} | No tests found (or non-lab HTML)")

    all_records.sort(key=lambda x: (x['date'], x['test']))

    print(f"\nTotal extracted records across all dates: {len(all_records)}")
    print("1. Updating SQLite Database (health.db)...")
    build_database(all_records)

    print("2. Exporting CSV spreadsheet (health_data.csv)...")
    export_csv(all_records)

    print("3. Exporting structured JSON (health_data.json)...")
    export_json(all_records)

    print("4. Regenerating interactive dashboard (index.html)...")
    generate_dashboard()

    print("\n✓ All health trackers and dashboards updated successfully!")

if __name__ == "__main__":
    main()
