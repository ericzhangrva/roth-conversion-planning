"""
Google Sheet & Multi-Tab Excel Company Importer
Loads target companies from a Google Sheet URL (CSV export) or local .xlsx / .csv file.
"""

import json
import re
import ssl
import urllib.request
from pathlib import Path
from typing import List, Dict, Any

ssl_context = ssl._create_unverified_context()
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}


def import_from_google_sheet_url(sheet_url: str, sheet_name: str = "Sheet1") -> List[Dict[str, Any]]:
    """
    Imports company list from a Google Sheets URL.
    Works for any sheet shared with 'Anyone with the link can view'.
    """
    match = re.search(r"/spreadsheets/d/([a-zA-Z0-9-_]+)", sheet_url)
    if not match:
        print(f"[-] Invalid Google Sheet URL: {sheet_url}")
        return []

    sheet_id = match.group(1)
    # Use Google Visualization API CSV export
    export_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={urllib.parse.quote(sheet_name)}"
    
    companies = []
    try:
        req = urllib.request.Request(export_url, headers=HEADERS)
        with urllib.request.urlopen(req, context=ssl_context, timeout=12) as resp:
            lines = resp.read().decode("utf-8").splitlines()
            if not lines:
                return []
            
            # Simple CSV parse
            import csv
            reader = csv.DictReader(lines)
            for row in reader:
                # Look for common column names: Company, Name, URL, Category, etc.
                comp_name = row.get("Company") or row.get("Company Name") or row.get("name") or list(row.values())[0]
                career_url = row.get("Career URL") or row.get("URL") or row.get("Website") or ""
                category = row.get("Category") or row.get("Industry") or "Imported Company"
                
                if comp_name and comp_name.strip():
                    companies.append({
                        "name": comp_name.strip(),
                        "category": category.strip(),
                        "career_url": career_url.strip(),
                        "ats_type": "custom",
                        "priority": "High"
                    })
            print(f"✅ Successfully imported {len(companies)} companies from Google Sheet tab '{sheet_name}'")
    except Exception as e:
        print(f"[-] Error importing Google Sheet: {e}")
    return companies
