"""
LaTeX Resume Tailor and PDF Compiler
Customizes resume.tex based on target job description keywords and compiles
a tailored 1-page PDF using /Library/TeX/texbin/pdflatex.
"""

import os
import re
import subprocess
from pathlib import Path
from typing import Dict, Any, Optional

BASE_DIR = Path(__file__).resolve().parent.parent
RESUME_TEX_PATH = BASE_DIR / "resume.tex"
TAILORED_DIR = BASE_DIR / "tailored_resumes"
PDFLATEX_BIN = "/Library/TeX/texbin/pdflatex"


def tailor_and_compile(job: Dict[str, Any], custom_summary: Optional[str] = None) -> Dict[str, Any]:
    """
    Tailors the master LaTeX resume for a specific job and compiles it to PDF.
    """
    TAILORED_DIR.mkdir(parents=True, exist_ok=True)
    
    with open(RESUME_TEX_PATH, "r", encoding="utf-8") as f:
        tex_content = f.read()

    company = re.sub(r"[^a-zA-Z0-9_-]", "_", job.get("company", "Target"))
    title = re.sub(r"[^a-zA-Z0-9_-]", "_", job.get("title", "Role"))
    output_stem = f"Eric_Zhang_Resume_{company}_{title}"[:60]
    tailored_tex_path = TAILORED_DIR / f"{output_stem}.tex"
    tailored_pdf_path = TAILORED_DIR / f"{output_stem}.pdf"

    # Optional: Customize the summary section if targeted keywords are provided
    if custom_summary:
        tex_content = re.sub(
            r"(\\section\{Summary\}\n)(.*?)(\n\n\\section)",
            r"\1" + custom_summary + r"\3",
            tex_content,
            flags=re.DOTALL
        )

    # Write tailored tex
    with open(tailored_tex_path, "w", encoding="utf-8") as f:
        f.write(tex_content)

    # Compile with pdflatex
    cmd = [
        PDFLATEX_BIN,
        "-interaction=nonstopmode",
        f"-output-directory={str(TAILORED_DIR)}",
        str(tailored_tex_path)
    ]
    
    try:
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=15)
        if proc.returncode == 0 and tailored_pdf_path.exists():
            return {
                "success": True,
                "pdf_path": str(tailored_pdf_path),
                "tex_path": str(tailored_tex_path),
                "message": f"Successfully compiled tailored resume to {tailored_pdf_path.name}"
            }
        else:
            return {
                "success": False,
                "error": "Compilation failed. Check LaTeX log.",
                "log": proc.stdout[-500:]
            }
    except Exception as e:
        return {"success": False, "error": str(e)}
