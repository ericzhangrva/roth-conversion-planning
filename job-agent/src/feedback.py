"""
User Feedback and Application State Manager
Maintains status for each job posting:
- 'new'
- 'interested'
- 'applied' (with applied timestamp)
- 'not_a_fit'
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

FEEDBACK_FILE = Path(__file__).resolve().parent.parent / "data" / "user_feedback.json"


def load_feedback() -> Dict[str, Any]:
    if not FEEDBACK_FILE.exists():
        return {}
    try:
        with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_feedback(data: Dict[str, Any]):
    FEEDBACK_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def set_job_status(job_id: str, status: str, notes: str = "") -> Dict[str, Any]:
    """Updates job status: 'applied', 'interested', 'not_a_fit', or 'new'."""
    data = load_feedback()
    record = data.get(job_id, {})
    record["status"] = status
    record["updated_at"] = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    if status == "applied" and "applied_at" not in record:
        record["applied_at"] = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    if notes:
        record["notes"] = notes
    data[job_id] = record
    save_feedback(data)
    return record


def get_job_status(job_id: str) -> Dict[str, Any]:
    data = load_feedback()
    return data.get(job_id, {"status": "new"})
