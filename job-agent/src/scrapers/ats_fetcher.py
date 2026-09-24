"""
Multi-Platform ATS Fetcher for Greenhouse, Ashby, SmartRecruiters, and Workday.
Zero external dependencies (pure Python standard library).
"""

import json
import ssl
import urllib.request
import urllib.error
from typing import List, Dict, Any

ssl_context = ssl._create_unverified_context()
DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json"
}


def fetch_greenhouse_jobs(board_token: str, company_name: str) -> List[Dict[str, Any]]:
    """Fetch from Greenhouse API."""
    url = f"https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs?content=true"
    req = urllib.request.Request(url, headers=DEFAULT_HEADERS)
    jobs = []
    try:
        with urllib.request.urlopen(req, context=ssl_context, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            for rj in data.get("jobs", []):
                jobs.append({
                    "id": f"gh_{board_token}_{rj.get('id')}",
                    "title": rj.get("title", "").strip(),
                    "company": company_name,
                    "location": rj.get("location", {}).get("name", "Unknown"),
                    "url": rj.get("absolute_url", ""),
                    "updated_at": rj.get("updated_at", ""),
                    "content": rj.get("content", ""),
                    "source": "Greenhouse",
                    "board_token": board_token
                })
    except Exception as e:
        print(f"[-] Error fetching Greenhouse for {company_name}: {e}")
    return jobs


def fetch_ashby_jobs(board_token: str, company_name: str) -> List[Dict[str, Any]]:
    """Fetch from Ashby API."""
    url = f"https://api.ashbyhq.com/posting-api/job-board/{board_token}"
    req = urllib.request.Request(url, headers=DEFAULT_HEADERS)
    jobs = []
    try:
        with urllib.request.urlopen(req, context=ssl_context, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            for rj in data.get("jobs", []):
                location = rj.get("location", "")
                if not location and rj.get("secondaryLocations"):
                    location = ", ".join(rj.get("secondaryLocations", []))
                jobs.append({
                    "id": f"ashby_{board_token}_{rj.get('id')}",
                    "title": rj.get("title", "").strip(),
                    "company": company_name,
                    "location": location or "Remote / Multiple",
                    "url": rj.get("jobUrl", ""),
                    "updated_at": rj.get("publishedAt", ""),
                    "content": rj.get("descriptionHtml", ""),
                    "source": "Ashby",
                    "board_token": board_token
                })
    except Exception as e:
        print(f"[-] Error fetching Ashby for {company_name}: {e}")
    return jobs


def fetch_smartrecruiters_jobs(board_token: str, company_name: str) -> List[Dict[str, Any]]:
    """Fetch from SmartRecruiters Public API (Visa, Experian, Block/Square)."""
    url = f"https://api.smartrecruiters.com/v1/companies/{board_token}/postings?limit=100"
    req = urllib.request.Request(url, headers=DEFAULT_HEADERS)
    jobs = []
    try:
        with urllib.request.urlopen(req, context=ssl_context, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            for rj in data.get("content", []):
                loc = rj.get("location", {})
                city = loc.get("city", "")
                region = loc.get("region", "")
                country = loc.get("country", "")
                loc_str = f"{city}, {region} ({country})".strip(", ()")
                if loc.get("remote"):
                    loc_str = f"Remote / {loc_str}"
                
                # Direct apply link
                direct_url = f"https://jobs.smartrecruiters.com/{board_token}/{rj.get('id')}"
                jobs.append({
                    "id": f"sr_{board_token}_{rj.get('id')}",
                    "title": rj.get("name", "").strip(),
                    "company": company_name,
                    "location": loc_str or "Remote / Multiple",
                    "url": direct_url,
                    "updated_at": rj.get("releasedDate", ""),
                    "content": rj.get("typeOfEmployment", {}).get("label", ""),
                    "source": "SmartRecruiters",
                    "board_token": board_token
                })
    except Exception as e:
        print(f"[-] Error fetching SmartRecruiters for {company_name}: {e}")
    return jobs


def fetch_workday_jobs(domain: str, client_id: str, company_name: str) -> List[Dict[str, Any]]:
    """Fetch from Workday Public CXS API (Mastercard, Citi, Synchrony, EWS, TransUnion, Equifax)."""
    url = f"https://{domain}/wday/cxs/{client_id}/jobs"
    payload = json.dumps({"appliedFacets": {}, "limit": 20, "offset": 0, "searchText": "fraud risk"}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={**DEFAULT_HEADERS, "Content-Type": "application/json"}
    )
    jobs = []
    try:
        with urllib.request.urlopen(req, context=ssl_context, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            for rj in data.get("jobPostings", []):
                ext_path = rj.get("externalPath", "")
                direct_url = f"https://{domain}/en-US/{client_id}{ext_path}" if ext_path else f"https://{domain}"
                jobs.append({
                    "id": f"wd_{client_id}_{rj.get('bulletFields', [''])[0] or ext_path[-10:]}",
                    "title": rj.get("title", "").strip(),
                    "company": company_name,
                    "location": rj.get("locationsText", "Multiple Locations"),
                    "url": direct_url,
                    "updated_at": rj.get("postedOn", ""),
                    "content": rj.get("title", ""),
                    "source": "Workday",
                    "board_token": client_id
                })
    except Exception as e:
        print(f"[-] Error fetching Workday for {company_name}: {e}")
    return jobs
