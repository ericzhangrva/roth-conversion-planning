"""
Email Notification Dispatcher
Sends automated HTML summary digests of new high-fit job opportunities
to Eric's mailbox (zhe.eric.zhang@gmail.com).
"""

import smtplib
import os
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from typing import List, Dict, Any

BASE_DIR = Path(__file__).resolve().parent.parent


def build_email_html(matches: List[Dict[str, Any]], candidate_name: str) -> str:
    """Constructs a clean, executive-ready HTML email digest."""
    top_matches = matches[:8]
    items_html = ""
    for j in top_matches:
        salary = f" &bull; <span style='color:#10b981;font-weight:600;'>{j['comp_verdict']}</span>" if j['comp_verdict'] != "Salary Unlisted" else ""
        items_html += f"""
        <tr style="border-bottom: 1px solid #e2e8f0;">
          <td style="padding: 12px 8px; vertical-align: top; width: 60px;">
            <div style="background: #0f172a; color: #38bdf8; font-weight: 800; font-size: 16px; border-radius: 8px; text-align: center; padding: 8px 4px;">
              {j['fit_score']}
            </div>
          </td>
          <td style="padding: 12px 10px;">
            <div style="font-size: 16px; font-weight: 700; color: #1e293b;">
              <a href="{j['url']}" style="color: #2563eb; text-decoration: none;">{j['title']}</a>
            </div>
            <div style="font-size: 13px; color: #64748b; margin-top: 3px;">
              <strong>{j['company']}</strong> &bull; {j['location']} {salary}
            </div>
            <div style="margin-top: 6px; font-size: 12px; color: #d97706; font-weight: 600;">
              Level: {j['matched_level']} | {j['location_tier']}
            </div>
          </td>
          <td style="padding: 12px 8px; text-align: right; vertical-align: middle; width: 110px;">
            <a href="{j['url']}" style="background: #2563eb; color: #ffffff; padding: 8px 14px; border-radius: 6px; text-decoration: none; font-size: 13px; font-weight: 600; display: inline-block;">
              Apply &rarr;
            </a>
          </td>
        </tr>
        """

    return f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"></head>
<body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background-color: #f8fafc; margin: 0; padding: 20px;">
  <div style="max-width: 650px; margin: 0 auto; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <div style="background: linear-gradient(135deg, #0f172a, #1e293b); padding: 24px; color: #ffffff;">
      <h1 style="margin: 0; font-size: 20px; font-weight: 700; color: #38bdf8;">Executive Opportunity Radar</h1>
      <p style="margin: 6px 0 0 0; font-size: 13px; color: #94a3b8;">
        New High-Fit Director / Leadership Matches for <strong>{candidate_name}</strong>
      </p>
    </div>
    
    <div style="padding: 20px;">
      <div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 12px 16px; margin-bottom: 20px; border-radius: 4px; font-size: 13px; color: #1e40af;">
        Found <strong>{len(matches)} qualified leadership matches</strong> (Card Fraud, Decision Systems, Risk &amp; Product Leadership, $200K+ Target).
      </div>

      <table style="width: 100%; border-collapse: collapse;">
        {items_html}
      </table>
    </div>

    <div style="background: #f1f5f9; padding: 16px; text-align: center; font-size: 12px; color: #64748b;">
      Run automatically by your local Job Search Co-Pilot &bull; Open your local dashboard for full interactive review.
    </div>
  </div>
</body>
</html>
"""


def send_email_digest(recipient_email: str, matches: List[Dict[str, Any]], smtp_config: Dict[str, Any] = None) -> bool:
    """Sends the HTML email digest via SMTP or prints preview."""
    if not matches:
        print("ℹ️ No new matches to email.")
        return False

    html_content = build_email_html(matches, "Eric Zhang")
    
    # Check if SMTP credentials exist in environment or config
    smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_user = os.getenv("SMTP_USER", "")
    smtp_pass = os.getenv("SMTP_PASS", "")

    if not smtp_user or not smtp_pass:
        # Save digest locally for viewing
        digest_path = BASE_DIR / "data" / "latest_email_digest.html"
        with open(digest_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"📧 Email digest preview saved to: {digest_path}")
        print("ℹ️ (To enable real email dispatch, set SMTP_USER and SMTP_PASS environment variables or in config)")
        return True

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"🎯 Executive Job Alert: {len(matches)} High-Fit Fraud & Risk Leadership Matches"
    msg["From"] = smtp_user
    msg["To"] = recipient_email
    msg.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.sendmail(smtp_user, recipient_email, msg.as_string())
        print(f"✅ Successfully dispatched email digest to {recipient_email}!")
        return True
    except Exception as e:
        print(f"[-] Failed to send email: {e}")
        return False
