"""
Interactive Web Dashboard & Local Application Server
Serves the opportunity dashboard, handles feedback state (Applied/Interested/Dismissed),
and triggers on-demand LaTeX resume tailoring & compilation.
"""

import http.server
import json
import urllib.parse
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from src.feedback import load_feedback, set_job_status
from src.tailor import tailor_and_compile

PORT = 8088


class JobDashboardHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        
        if parsed.path == "/" or parsed.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            with open(BASE_DIR / "data" / "report.html", "rb") as f:
                self.wfile.write(f.read())
            return
            
        elif parsed.path == "/api/matches":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            matches_file = BASE_DIR / "data" / "matches.json"
            if matches_file.exists():
                with open(matches_file, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.wfile.write(b"[]")
            return
            
        elif parsed.path == "/api/feedback":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(load_feedback()).encode("utf-8"))
            return

        # Serve static tailored PDFs
        elif parsed.path.startswith("/tailored/"):
            filename = parsed.path.replace("/tailored/", "")
            pdf_path = BASE_DIR / "tailored_resumes" / filename
            if pdf_path.exists():
                self.send_response(200)
                self.send_header("Content-Type", "application/pdf")
                self.end_headers()
                with open(pdf_path, "rb") as f:
                    self.wfile.write(f.read())
                return

        return super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8")
        data = json.loads(body) if body else {}

        if parsed.path == "/api/status":
            job_id = data.get("job_id")
            status = data.get("status")
            notes = data.get("notes", "")
            res = set_job_status(job_id, status, notes)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "record": res}).encode("utf-8"))
            return

        elif parsed.path == "/api/tailor":
            job = data.get("job", {})
            res = tailor_and_compile(job)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(res).encode("utf-8"))
            return

        self.send_response(404)
        self.end_headers()


def start_server(port=PORT):
    server = http.server.HTTPServer(("127.0.0.1", port), JobDashboardHandler)
    print(f"\n🚀 Interactive Opportunity Dashboard running at: http://127.0.0.1:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping dashboard server...")


if __name__ == "__main__":
    start_server()
