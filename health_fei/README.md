# 🩺 Health & Lab Results Tracking System — Fei Han

A self-contained health tracking and analytics system built for **Fei Han** to monitor historical laboratory bloodwork, clinical metrics, and biomarker trends over time.

---

## 🚀 Quick Start: Viewing Results

Open the interactive dashboard directly in any web browser:

```bash
open /Users/eric/Dropbox/ai/health_fei/index.html
```

---

## 📊 Summary of Tracked Data

- **Patient:** Fei Han (DOB: 07/23/1975)
- **Time Span:** October 2, 2019 → September 8, 2026 (6.9 years, ~7-Year History)
- **Checkup Dates (6 visits / 12 reports):**
  1. `10/02/2019`
  2. `01/19/2023`
  3. `01/27/2025` – `01/28/2025`
  4. `04/06/2026`
  5. `09/08/2026`
- **Total Metrics Tracked:** 184 individual test results across Complete Blood Count (CBC), Comprehensive Metabolic Panel (CMP), Lipid Panel (Cholesterol/Triglycerides/HDL/LDL), Hormones & Thyroid, and Specialty tests.

---

## 📁 System Files & Database Architecture

| File | Type | Purpose |
| :--- | :--- | :--- |
| **`index.html`** / **`dashboard.html`** | Interactive Web Dashboard | Tabular views + trend charts with normal threshold reference lines and Chinese/English bilingual explanations |
| **`health.db`** | SQLite Database | Relational database for querying, analysis, and backups |
| **`health_data.csv`** | CSV Spreadsheet | Flat export ready to open in Microsoft Excel or Apple Numbers |
| **`health_data.json`** | JSON Data | Structured format for programmatic access or web scripts |
| **`import_labs.py`** | Automation Script | One-command CLI tool to parse new HTML reports and update everything |
| **`process_labs.py`** | Core Extraction Engine | HTML parsing, date extraction, threshold parsing, and DB building logic |
| **`build_dashboard.py`** | HTML Generator | Compiles data into the standalone responsive Chart.js dashboard |
| **`glossary.py`** | Medical Glossary | Clinical definitions and Chinese explanations for all lab biomarkers |

---

## 🗄️ SQLite Database (`health.db`)

You can query `health.db` using the terminal (`sqlite3 health.db`):

```sql
-- View all abnormal results flagged as High (H) or Low (L)
SELECT date_display, test_name, value, ref_range, flag 
FROM v_abnormal_results;

-- View chronological trend for any test
SELECT date_display, test_name, value, ref_range, units, flag 
FROM v_test_trends 
WHERE test_name = 'Cholesterol';
```

---

## 🔄 Adding Future Test Results

Whenever you receive a new HTML lab report from Family Practice Associates / Updox:
1. Save the `.html` file into `/Users/eric/Dropbox/ai/health_fei/`.
2. Run the update command in your terminal:
   ```bash
   cd /Users/eric/Dropbox/ai/health_fei
   python3 import_labs.py
   ```
3. The script automatically parses the new file, updates `health.db`, re-exports the CSV/JSON, and regenerates `index.html`!
