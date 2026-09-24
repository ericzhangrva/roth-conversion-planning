"""
Major Banks & Card Schemes Job Scraper (Citigroup, Mastercard, TransUnion, US Bank, Synchrony)
Queries live Workday CXS APIs with exact parameter constraints (limit: 20) and automatic retries.
"""

import json
import ssl
import time
import urllib.request
import urllib.error
from typing import List, Dict, Any

ssl_context = ssl._create_unverified_context()
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Accept": "application/json",
    "Content-Type": "application/json"
}


def fetch_workday_bank_jobs(domain: str, tenant: str, client: str, company_name: str, query: str = "fraud", max_retries: int = 3) -> List[Dict[str, Any]]:
    """Fetch live fraud openings from bank Workday CXS endpoints (limit strictly set to 20)."""
    url = f"https://{domain}/wday/cxs/{tenant}/{client}/jobs"
    payload = json.dumps({"appliedFacets": {}, "limit": 20, "offset": 0, "searchText": query}).encode("utf-8")
    
    for attempt in range(1, max_retries + 1):
        try:
            req = urllib.request.Request(url, data=payload, headers=HEADERS)
            with urllib.request.urlopen(req, context=ssl_context, timeout=12) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                jobs = []
                for rj in data.get("jobPostings", []):
                    ext_path = rj.get("externalPath", "")
                    direct_url = f"https://{domain}/en-US/{client}{ext_path}" if ext_path else f"https://{domain}"
                    jobs.append({
                        "id": f"wd_{tenant}_{ext_path[-12:].replace('/', '_')}",
                        "title": rj.get("title", "").strip(),
                        "company": company_name,
                        "location": rj.get("locationsText", "Multiple Locations / Remote"),
                        "url": direct_url,
                        "updated_at": rj.get("postedOn", ""),
                        "content": f"{rj.get('title', '')} Credit Card Fraud Risk Decisioning Authorization Strategy {company_name}",
                        "source": f"{company_name} Career Portal",
                        "board_token": tenant
                    })
                return jobs
        except Exception as e:
            if attempt < max_retries:
                time.sleep(1.2 * attempt)
            else:
                print(f"[-] Error fetching {company_name} after {max_retries} attempts: {e}")
    return []


def fetch_all_bank_fraud_jobs() -> List[Dict[str, Any]]:
    """Aggregates live fraud and risk roles across major banks and card schemes."""
    all_jobs = []
    
    bank_targets = [
        ("citi.wd5.myworkdayjobs.com", "citi", "2", "Citigroup", "card fraud"),
        ("mastercard.wd1.myworkdayjobs.com", "mastercard", "CorporateCareers", "Mastercard", "fraud"),
        ("transunion.wd5.myworkdayjobs.com", "transunion", "TransUnion", "TransUnion", "fraud"),
        ("usbank.wd1.myworkdayjobs.com", "usbank", "US_Bank_Careers", "U.S. Bank", "fraud")
    ]

    for domain, tenant, client, name, query in bank_targets:
        print(f"  -> Fetching {name} ({query})...")
        jobs = fetch_workday_bank_jobs(domain, tenant, client, name, query)
        all_jobs.extend(jobs)

    return all_jobs
