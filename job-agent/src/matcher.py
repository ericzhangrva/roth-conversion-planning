"""
Intelligent Matching, Card Fraud Weighting & Active Feedback Learning Engine
- Heavily focuses on Credit Card Fraud, Transaction Monitoring, Decision Science & Risk Leadership.
- Strictly excludes IC engineering positions.
- Dynamically adapts based on user feedback ('not_a_fit' dismissals vs 'interested'/'applied' stars).
"""

import re
import html
from datetime import datetime
from typing import Dict, Any, List
from src.feedback import load_feedback


def strip_html(html_text: str) -> str:
    """Removes HTML tags and normalizes whitespace."""
    if not html_text:
        return ""
    clean = re.sub(r"<[^>]+>", " ", html_text)
    clean = html.unescape(clean)
    return re.sub(r"\s+", " ", clean).strip()


def extract_salary_range(text: str) -> Dict[str, Any]:
    """Extracts base salary ranges from text using regex heuristics."""
    patterns = [
        r"\$([0-9]{2,3}),?([0-9]{3})\s*(?:-|to|–)\s*\$([0-9]{2,3}),?([0-9]{3})",
        r"\$([0-9]{2,3})[kK]\s*(?:-|to|–)\s*\$([0-9]{2,3})[kK]",
        r"base\s*(?:salary|pay)?\s*(?:range|of)?\s*:?\s*\$([0-9]{2,3}),?([0-9]{3})"
    ]
    for p in patterns:
        m = re.search(p, text, re.IGNORECASE)
        if m:
            groups = m.groups()
            if len(groups) == 4:
                low = int(groups[0] + groups[1])
                high = int(groups[2] + groups[3])
                return {"min": low, "max": high, "text": f"${low:,} - ${high:,}"}
            elif len(groups) == 2:
                low = int(groups[0]) * 1000
                high = int(groups[1]) * 1000
                return {"min": low, "max": high, "text": f"${low:,} - ${high:,}"}
    return {"min": None, "max": None, "text": "Not Listed / Equity Based"}


def is_excluded_engineering_role(title: str) -> bool:
    """Returns True if the role is a pure individual contributor engineering position."""
    if re.search(r"\b(director|head of|vp|vice president|group product manager|principal product manager)\b", title, re.IGNORECASE):
        return False

    ic_eng_patterns = [
        r"\bsoftware engineer\b",
        r"\bsoftware engineering\b",
        r"\bbackend engineer\b",
        r"\bfrontend engineer\b",
        r"\bfull stack engineer\b",
        r"\binfrastructure engineer\b",
        r"\bdevops\b",
        r"\bsre\b",
        r"\bsite reliability\b",
        r"\bsecurity engineer\b",
        r"\bsecurity detection engineer\b",
        r"\bciam software engineer\b",
        r"\bplatform engineer\b",
        r"\bdata engineer\b",
        r"\bml engineer\b",
        r"\bmachine learning engineer\b",
        r"\bqa engineer\b",
        r"\btest engineer\b",
        r"\bintern\b",
        r"\binternship\b",
        r"\bco-op\b"
    ]
    for pat in ic_eng_patterns:
        if re.search(pat, title, re.IGNORECASE):
            return True
    return False


def get_feedback_adjustments(title: str, user_feedback: Dict[str, Any]) -> int:
    """
    Active Learning: Analyzes user feedback ('not_a_fit' dismissals vs 'interested'/'applied').
    Penalizes titles similar to dismissed roles, boosts titles similar to starred/applied roles.
    """
    penalty = 0
    boost = 0
    t_lower = title.lower()

    for job_id, record in user_feedback.items():
        status = record.get("status")
        notes = record.get("notes", "").lower()
        
        # If user explicitly dismissed non-fraud roles (e.g. creative, corporate finance)
        if status == "not_a_fit":
            # Extract negative terms from job ID or common non-fit keywords
            if any(term in t_lower for term in ["creative", "designer", "brand", "sales", "recruiter", "tax", "accounting"]):
                penalty += 25
        elif status in ["interested", "applied"]:
            if any(term in t_lower for term in ["fraud", "risk", "decision", "card", "authorization"]):
                boost += 10

    return boost - penalty


def is_outside_us(location: str, title: str) -> bool:
    """Returns True if the role is explicitly located outside the United States and not US Remote."""
    loc_lower = f"{location} {title}".lower()
    
    # If explicitly marked as US Remote or in USA / US states, it's valid
    if re.search(r"\b(remote\s*-\s*us|remote\s*us|us\s*remote|remote\s*\(us\)|united states|usa|u\.s\.|remote\s*in\s*us)\b", loc_lower):
        return False
        
    # Check for foreign countries / international cities
    intl_indicators = [
        r"\bcanada\b", r"\btoronto\b", r"\bvancouver\b", r"\bmontreal\b",
        r"\buk\b", r"\bunited kingdom\b", r"\blondon\b", r"\bdublin\b", r"\bireland\b",
        r"\bsingapore\b", r"\bindia\b", r"\bbangalore\b", r"\bhyderabad\b", r"\bgurgaon\b", r"\bmumbai\b",
        r"\bjapan\b", r"\btokyo\b", r"\bgermany\b", r"\bberlin\b", r"\bpoland\b", r"\bwarsaw\b", r"\bkrakow\b",
        r"\baustralia\b", r"\bsydney\b", r"\bmelbourne\b", r"\bphilippines\b", r"\bmanila\b",
        r"\bcosta rica\b", r"\bmexico\b", r"\bbrazil\b", r"\bfrance\b", r"\bparis\b",
        r"\bnetherlands\b", r"\bamsterdam\b", r"\bspain\b", r"\bmadrid\b", r"\bswitzerland\b", r"\bzurich\b",
        r"\bemea\b", r"\bapac\b", r"\blatam\b"
    ]
    for pat in intl_indicators:
        if re.search(pat, loc_lower):
            return True
            
    return False


def score_job(job: Dict[str, Any], search_profile: Dict[str, Any]) -> Dict[str, Any]:
    """
    Computes a focused Fit Score (0-100%) emphasizing Credit Card Fraud, Risk, and Decision Systems.
    """
    title = job.get("title", "")
    content = strip_html(job.get("content", ""))
    location = job.get("location", "")
    full_text = f"{title} {location} {content}".lower()
    now_iso = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    user_feedback = load_feedback()

    # 1. Hard Filter: Exclude pure IC Engineering roles
    if is_excluded_engineering_role(title):
        return {
            "fit_score": 0,
            "fit_tier": "Excluded: IC Engineer",
            "is_qualified": False,
            "captured_at": now_iso
        }

    # 2. Hard Filter: Exclude non-US locations unless Remote US
    if is_outside_us(location, title):
        return {
            "fit_score": 0,
            "fit_tier": "Excluded: Non-US Location",
            "is_qualified": False,
            "captured_at": now_iso
        }

    # 2. Seniority & Leadership Title Scoring (Weight: 30)
    seniority_score = 0
    matched_level = "Other"
    
    if re.search(r"\b(head of|vp|vice president)\b", title, re.IGNORECASE):
        seniority_score = 30
        matched_level = "Head of / VP"
    elif re.search(r"\b(senior director|sr\.? director)\b", title, re.IGNORECASE):
        seniority_score = 30
        matched_level = "Senior Director"
    elif re.search(r"\b(director)\b", title, re.IGNORECASE) and not re.search(r"\b(associate director|assistant director)\b", title, re.IGNORECASE):
        seniority_score = 28
        matched_level = "Director"
    elif re.search(r"\b(group product manager|principal product manager|director.*product)\b", title, re.IGNORECASE):
        seniority_score = 28
        matched_level = "Product Leadership / GPM"
    elif re.search(r"\b(senior manager|sr\.? manager|group manager)\b", title, re.IGNORECASE):
        seniority_score = 24
        matched_level = "Senior Manager"
    elif re.search(r"\b(manager|lead|principal|product manager)\b", title, re.IGNORECASE):
        seniority_score = 18
        matched_level = "Manager / Lead"

    # 3. Card Fraud & Decision Science Domain Focus (Weight: 45)
    domain_score = 0
    domain_hits = []
    
    # Heavily weight core Card Fraud & Authorization Decisioning competencies
    core_fraud_weights = {
        "credit card fraud": 20,
        "card fraud": 20,
        "fraud strategy": 18,
        "fraud detection": 18,
        "fraud risk": 18,
        "authorization": 14,
        "decision science": 14,
        "decisioning": 12,
        "transaction monitoring": 12,
        "payment fraud": 12,
        "disputes": 10,
        "chargeback": 10,
        "authentication": 10,
        "feature store": 10,
        "feature factory": 12,
        "link analysis": 10,
        "identity": 8,
        "risk operations": 8,
        "data strategy": 6,
        "analytics": 4
    }

    for term, weight in core_fraud_weights.items():
        if term in full_text:
            domain_score += weight
            domain_hits.append(term)
            
    domain_score = min(45, domain_score)

    # 4. Location Tier Scoring (Weight: 15)
    location_score = 10 # Default baseline since Eric is open to relocation
    loc_tier = "Open Relocation"
    
    if re.search(r"\b(remote|us remote|virtual|anywhere in us)\b", f"{location} {title}", re.IGNORECASE):
        location_score = 15
        loc_tier = "Tier 1: 100% Remote"
    elif re.search(r"\b(richmond|va|virginia)\b", location, re.IGNORECASE) and not re.search(r"\b(west virginia)\b", location, re.IGNORECASE):
        location_score = 15
        loc_tier = "Tier 1: Richmond Metro"
    elif re.search(r"\b(mclean|tysons|reston|arlington|fairfax|alexandria|washington dc|dc metro|nova)\b", location, re.IGNORECASE):
        location_score = 13
        loc_tier = "Tier 2: NOVA / DC Metro"

    # 5. Compensation Scoring (Weight: 10)
    salary_info = extract_salary_range(content)
    comp_score = 7
    comp_verdict = "Salary Unlisted"

    min_target = search_profile.get("targeting", {}).get("compensation", {}).get("min_base_salary_usd", 200000)

    if salary_info["min"]:
        if salary_info["max"] and salary_info["max"] >= min_target:
            comp_score = 10
            comp_verdict = f"Meets $200K+ ({salary_info['text']})"
        elif salary_info["min"] >= min_target:
            comp_score = 10
            comp_verdict = f"Meets $200K+ ({salary_info['text']})"
        else:
            comp_score = 3
            comp_verdict = f"Below $200K ({salary_info['text']})"

    # 6. Active Learning Feedback Adjustment
    feedback_adj = get_feedback_adjustments(title, user_feedback)

    total_score = seniority_score + domain_score + location_score + comp_score + feedback_adj
    total_score = max(0, min(100, total_score))

    # Determine match rating
    if total_score >= 80:
        fit_tier = "Top Fraud Match ⭐⭐⭐"
    elif total_score >= 65:
        fit_tier = "Strong Match ⭐⭐"
    elif total_score >= 50:
        fit_tier = "Moderate Match ⭐"
    else:
        fit_tier = "Low Fit"

    # Require minimum fraud domain presence or high-level risk seniority
    is_qualified = (domain_score >= 12 and seniority_score >= 15 and total_score >= 55)

    return {
        "fit_score": total_score,
        "fit_tier": fit_tier,
        "matched_level": matched_level,
        "location_tier": loc_tier,
        "salary_info": salary_info,
        "comp_verdict": comp_verdict,
        "domain_hits": list(set(domain_hits))[:6],
        "captured_at": now_iso,
        "is_qualified": is_qualified
    }
