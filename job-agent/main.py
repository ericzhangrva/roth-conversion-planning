"""
Main Orchestrator & CLI Runner for Executive Opportunity Radar
Fetches live jobs across multi-ATS platforms (Visa, Experian, Block, Stripe, Ramp, etc.),
excludes IC engineers, scores against Eric's profile, tracks status, and builds the interactive dashboard.
"""

import json
import os
import sys
from pathlib import Path
from typing import List, Dict, Any

BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

from src.scrapers.ats_fetcher import (
    fetch_greenhouse_jobs,
    fetch_ashby_jobs,
    fetch_smartrecruiters_jobs,
    fetch_workday_jobs
)
from src.scrapers.major_banks import fetch_all_bank_fraud_jobs
from src.matcher import score_job
from src.feedback import load_feedback
from src.notifier import send_email_digest


CONFIG_DIR = BASE_DIR / "config"
DATA_DIR = BASE_DIR / "data"


def load_json(path: Path) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def run_pipeline() -> List[Dict[str, Any]]:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    profile = load_json(CONFIG_DIR / "search_profile.json")
    companies_cfg = load_json(CONFIG_DIR / "target_companies.json")
    feedback_state = load_feedback()

    all_jobs = []
    print("\n🔍 [1/3] Ingesting live job postings across target payment schemes, banks, bureaus & fintechs...")
    
    for comp in companies_cfg.get("companies", []):
        ats = comp.get("ats_type")
        token = comp.get("board_token")
        name = comp.get("name")
        domain = comp.get("domain")
        client_id = comp.get("client_id")
        
        if ats == "greenhouse" and token:
            print(f"  -> Fetching Greenhouse: {name}...")
            jobs = fetch_greenhouse_jobs(token, name)
            all_jobs.extend(jobs)
        elif ats == "ashby" and token:
            print(f"  -> Fetching Ashby: {name}...")
            jobs = fetch_ashby_jobs(token, name)
            all_jobs.extend(jobs)
        elif ats == "smartrecruiters" and token:
            print(f"  -> Fetching SmartRecruiters: {name}...")
            jobs = fetch_smartrecruiters_jobs(token, name)
            all_jobs.extend(jobs)

    # Ingest specialized major bank fraud & risk openings (USAA, Citi, Synchrony, Amex, etc.)
    print("\n🏛️ Ingesting Major Bank & Card Scheme Fraud Portals (USAA, Citi, Synchrony, Amex)...")
    bank_jobs = fetch_all_bank_fraud_jobs()
    all_jobs.extend(bank_jobs)


    print(f"\n📊 [2/3] Scored {len(all_jobs)} total live postings against your profile (IC Engineers Excluded)...")
    
    scored_jobs = []
    for job in all_jobs:
        match_res = score_job(job, profile)
        if match_res["is_qualified"]:
            job_id = job["id"]
            user_status = feedback_state.get(job_id, {}).get("status", "new")
            applied_at = feedback_state.get(job_id, {}).get("applied_at", "")
            
            job_record = {
                **job,
                **match_res,
                "status": user_status,
                "applied_at": applied_at
            }
            scored_jobs.append(job_record)

    # Sort descending by fit score
    scored_jobs.sort(key=lambda x: x["fit_score"], reverse=True)

    # Save to data/matches.json
    matches_file = DATA_DIR / "matches.json"
    with open(matches_file, "w", encoding="utf-8") as f:
        json.dump(scored_jobs, f, indent=2)

    # Generate modern HTML Dashboard
    generate_html_report(scored_jobs, profile)

    # Prepare email notification
    send_email_digest("zhe.eric.zhang@gmail.com", scored_jobs)

    print(f"\n✅ [3/3] Found {len(scored_jobs)} qualified leadership matches! (Saved to data/matches.json)")
    print(f"📄 Interactive visual dashboard available at: {DATA_DIR / 'report.html'}\n")

    # Print Top Summary to Terminal
    print("=" * 105)
    print(f"{'SCORE':<8} | {'COMPANY':<16} | {'LEVEL':<20} | {'TITLE':<32} | {'CAPTURED'}")
    print("=" * 105)
    for j in scored_jobs[:15]:
        title = (j['title'][:30] + '..') if len(j['title']) > 30 else j['title']
        print(f"{j['fit_score']:>3}/100  | {j['company'][:16]:<16} | {j['matched_level'][:20]:<20} | {title:<32} | {j['captured_at']}")
    print("=" * 105)
    
    return scored_jobs


def generate_html_report(matches: List[Dict[str, Any]], profile: Dict[str, Any]):
    """Generates an interactive, responsive HTML dashboard with feedback controls and PDF tailoring."""
    html_path = DATA_DIR / "report.html"
    
    rows_html = ""
    for j in matches:
        salary_badge = f'<span class="badge badge-comp">{j["comp_verdict"]}</span>' if j["comp_verdict"] != "Salary Unlisted" else '<span class="badge badge-unlisted">Salary Unlisted</span>'
        hits = " ".join([f'<span class="badge badge-domain">{h}</span>' for h in j["domain_hits"]])
        
        score_class = "score-high" if j["fit_score"] >= 75 else ("score-med" if j["fit_score"] >= 60 else "score-low")
        
        job_json_str = json.dumps({
            "id": j["id"],
            "title": j["title"],
            "company": j["company"],
            "url": j["url"]
        }).replace('"', '&quot;')

        status = j.get("status", "new")
        status_badge = ""
        if status == "applied":
            status_badge = f'<span class="badge badge-applied">Applied: {j.get("applied_at", "Yes")}</span>'
        elif status == "interested":
            status_badge = '<span class="badge badge-interested">Starred / Interested</span>'

        rows_html += f"""
        <tr class="job-row" id="row_{j['id']}" data-status="{status}">
          <td class="text-center">
            <div class="score-pill {score_class}">{j["fit_score"]}</div>
            <div class="text-xs text-slate-400 mt-1 font-semibold">{j["fit_tier"]}</div>
            <div class="text-xs text-slate-500 mt-0.5" title="Timestamp when captured">🕒 {j["captured_at"]}</div>
          </td>
          <td>
            <div class="flex items-center gap-2">
              <a href="{j['url']}" target="_blank" class="font-bold text-lg text-teal-400 hover:underline">
                {j["title"]} &nearr;
              </a>
              {status_badge}
            </div>
            <div class="company-name text-slate-300 mt-0.5">
              <strong>{j["company"]}</strong> &bull; <span class="text-slate-400">{j["location"]}</span>
            </div>
            <div class="mt-2 flex flex-wrap gap-1.5">
              <span class="badge badge-level">{j["matched_level"]}</span>
              <span class="badge badge-loc">{j["location_tier"]}</span>
              {salary_badge}
            </div>
            <div class="mt-2">{hits}</div>
          </td>
          <td class="text-center align-middle">
            <button onclick="tailorResume({job_json_str})" class="btn-tailor" title="Compile customized 1-page LaTeX PDF for this role">
              📄 Tailor PDF
            </button>
            <div id="tailor_status_{j['id']}" class="text-xs text-slate-400 mt-1"></div>
          </td>
          <td class="text-right align-middle">
            <div class="flex flex-col gap-1.5 items-end">
              <a href="{j['url']}" target="_blank" class="btn-apply">
                Direct Apply &rarr;
              </a>
              <div class="flex gap-1 mt-1">
                <button onclick="updateStatus('{j['id']}', 'applied')" class="btn-action btn-act-applied" title="Mark as Applied">✓ Applied</button>
                <button onclick="updateStatus('{j['id']}', 'interested')" class="btn-action btn-act-star" title="Save to Interested">⭐ Star</button>
                <button onclick="updateStatus('{j['id']}', 'not_a_fit')" class="btn-action btn-act-dismiss" title="Dismiss / Not a fit">✕</button>
              </div>
            </div>
          </td>
        </tr>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Opportunity Radar &bull; {profile['candidate']['name']}</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body {{ background: #0f172a; color: #f8fafc; font-family: -apple-system, system-ui, sans-serif; }}
    .glass {{ background: rgba(30, 41, 59, 0.75); backdrop-filter: blur(14px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 16px; }}
    .job-row {{ border-bottom: 1px solid rgba(255, 255, 255, 0.08); transition: all 0.2s; }}
    .job-row:hover {{ background: rgba(51, 65, 85, 0.4); }}
    .job-row[data-status="not_a_fit"] {{ opacity: 0.35; }}
    .job-row[data-status="applied"] {{ background: rgba(16, 185, 129, 0.05); }}
    .score-pill {{ width: 46px; height: 46px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 1.15rem; margin: 0 auto; }}
    .score-high {{ background: rgba(16, 185, 129, 0.2); border: 1px solid #10b981; color: #34d399; }}
    .score-med {{ background: rgba(245, 158, 11, 0.2); border: 1px solid #f59e0b; color: #fbbf24; }}
    .score-low {{ background: rgba(148, 163, 184, 0.2); border: 1px solid #94a3b8; color: #cbd5e1; }}
    .badge {{ font-size: 0.72rem; padding: 2px 8px; border-radius: 6px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.04em; }}
    .badge-level {{ background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); }}
    .badge-loc {{ background: rgba(168, 85, 247, 0.15); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.3); }}
    .badge-comp {{ background: rgba(52, 211, 153, 0.15); color: #6ee7b7; border: 1px solid rgba(52, 211, 153, 0.3); }}
    .badge-unlisted {{ background: rgba(100, 116, 139, 0.2); color: #94a3b8; }}
    .badge-domain {{ background: rgba(251, 146, 60, 0.12); color: #fdba74; border: 1px solid rgba(251, 146, 60, 0.25); text-transform: none; }}
    .badge-applied {{ background: rgba(16, 185, 129, 0.25); color: #6ee7b7; border: 1px solid #10b981; }}
    .badge-interested {{ background: rgba(245, 158, 11, 0.25); color: #fcd34d; border: 1px solid #f59e0b; }}
    .btn-apply {{ display: inline-block; background: #2563eb; color: white; padding: 6px 14px; border-radius: 8px; font-weight: 600; font-size: 0.85rem; text-decoration: none; transition: background 0.2s; }}
    .btn-apply:hover {{ background: #1d4ed8; }}
    .btn-tailor {{ background: rgba(147, 51, 234, 0.2); border: 1px solid #a855f7; color: #d8b4fe; padding: 6px 12px; border-radius: 8px; font-size: 0.82rem; font-weight: 600; cursor: pointer; transition: all 0.2s; }}
    .btn-tailor:hover {{ background: #9333ea; color: white; }}
    .btn-action {{ font-size: 0.72rem; padding: 3px 8px; border-radius: 6px; font-weight: 600; cursor: pointer; border: 1px solid rgba(255, 255, 255, 0.15); background: rgba(255, 255, 255, 0.05); color: #cbd5e1; transition: all 0.15s; }}
    .btn-act-applied:hover {{ background: rgba(16, 185, 129, 0.3); color: #6ee7b7; border-color: #10b981; }}
    .btn-act-star:hover {{ background: rgba(245, 158, 11, 0.3); color: #fcd34d; border-color: #f59e0b; }}
    .btn-act-dismiss:hover {{ background: rgba(239, 68, 68, 0.3); color: #fca5a5; border-color: #ef4444; }}
  </style>
</head>
<body class="p-6 max-w-7xl mx-auto">
  <header class="mb-6 flex justify-between items-center glass p-6">
    <div>
      <h1 class="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-teal-400 via-blue-400 to-indigo-400">
        Executive Opportunity Radar &bull; Fraud, Risk &amp; Decisions
      </h1>
      <p class="text-sm text-slate-400 mt-1">
        Curated for <strong>{profile['candidate']['name']}</strong> &bull; Target: Director / VP / PM Leadership ($200K+ Base) &bull; IC Engineers Excluded
      </p>
    </div>
    <div class="flex gap-4 items-center">
      <div class="text-right">
        <div class="text-3xl font-extrabold text-teal-400">{len(matches)}</div>
        <div class="text-xs uppercase tracking-wider text-slate-400 font-semibold">Active Matches</div>
      </div>
    </div>
  </header>

  <!-- Filter bar -->
  <div class="flex gap-2 mb-4">
    <button onclick="filterStatus('all')" class="btn-action bg-slate-700 text-white px-3 py-1.5 text-xs">All Roles ({len(matches)})</button>
    <button onclick="filterStatus('new')" class="btn-action px-3 py-1.5 text-xs">⭐ New / Unreviewed</button>
    <button onclick="filterStatus('interested')" class="btn-action px-3 py-1.5 text-xs">⭐ Starred</button>
    <button onclick="filterStatus('applied')" class="btn-action px-3 py-1.5 text-xs">✓ Applied</button>
    <button onclick="filterStatus('not_a_fit')" class="btn-action px-3 py-1.5 text-xs">✕ Dismissed</button>
  </div>

  <main class="glass p-4">
    <table class="w-full text-left border-collapse">
      <thead>
        <tr class="text-xs uppercase text-slate-400 border-b border-slate-700">
          <th class="p-3 text-center w-28">Fit Score &amp; Time</th>
          <th class="p-3">Role Details, Seniority &amp; Domain Alignment</th>
          <th class="p-3 text-center w-36">Resume Tailor</th>
          <th class="p-3 text-right w-44">Direct Action</th>
        </tr>
      </thead>
      <tbody id="job-table-body">
        {rows_html}
      </tbody>
    </table>
  </main>

  <script>
    async function updateStatus(jobId, status) {{
      try {{
        const resp = await fetch('http://127.0.0.1:8088/api/status', {{
          method: 'POST',
          headers: {{ 'Content-Type': 'application/json' }},
          body: JSON.stringify({{ job_id: jobId, status: status }})
        }});
        if (resp.ok) {{
          const row = document.getElementById('row_' + jobId);
          if (row) row.dataset.status = status;
          alert('Status updated to: ' + status);
        }}
      }} catch (e) {{
        // Fallback for direct local file viewing
        const row = document.getElementById('row_' + jobId);
        if (row) row.dataset.status = status;
        alert('Marked as ' + status + ' (local session)');
      }}
    }}

    async function tailorResume(job) {{
      const statusDiv = document.getElementById('tailor_status_' + job.id);
      if (statusDiv) statusDiv.innerHTML = '<span class="text-amber-400">Compiling LaTeX...</span>';
      
      try {{
        const resp = await fetch('http://127.0.0.1:8088/api/tailor', {{
          method: 'POST',
          headers: {{ 'Content-Type': 'application/json' }},
          body: JSON.stringify({{ job: job }})
        }});
        const data = await resp.json();
        if (data.success) {{
          const pdfName = data.pdf_path.split('/').pop();
          if (statusDiv) {{
            statusDiv.innerHTML = '<a href="/tailored/' + pdfName + '" target="_blank" class="text-teal-400 font-bold underline">Download PDF &darr;</a>';
          }}
        }} else {{
          if (statusDiv) statusDiv.innerHTML = '<span class="text-rose-400">Error compiling</span>';
        }}
      }} catch (e) {{
        if (statusDiv) statusDiv.innerHTML = '<span class="text-slate-400">Open via server to download</span>';
      }}
    }}

    function filterStatus(status) {{
      const rows = document.querySelectorAll('.job-row');
      rows.forEach(r => {{
        if (status === 'all') {{
          r.style.display = '';
        }} else if (r.dataset.status === status) {{
          r.style.display = '';
        }} else {{
          r.style.display = 'none';
        }}
      }});
    }}
  </script>
</body>
</html>
"""
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)


if __name__ == "__main__":
    run_pipeline()
