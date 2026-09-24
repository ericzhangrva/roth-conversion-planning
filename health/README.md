# 🩺 Health & Lab Results Tracking System

A self-contained health tracking and analytics system built for **Zhe Zhang** to monitor historical laboratory bloodwork and clinical metrics over time.

---

## 🚀 Quick Start: Viewing Your Results

You can open the interactive dashboard directly in any web browser:

👉 Open **`index.html`** (or **`dashboard.html`**) in Chrome, Safari, or Edge:
```bash
open /Users/eric/Dropbox/ai/health/index.html
```

---

## 📊 Summary of Tracked Data

- **Patient:** Zhe Zhang (DOB: 01/25/1976)
- **Time Span:** January 26, 2022 → August 12, 2026 (4.6 years)
- **Checkup Dates (6 visits):**
  1. `01/26/2022`
  2. `09/26/2023`
  3. `12/21/2023`
  4. `10/28/2024`
  5. `12/02/2025`
  6. `08/12/2026`
- **Total Metrics Tracked:** 53 distinct tests (264 total data points)

---

## 📁 System Files & Database Architecture

| File | Type | Purpose |
| :--- | :--- | :--- |
| **`index.html`** | Interactive Web Dashboard | Full tabular view + 53 historical trend charts with normal threshold lines |
| **`health.db`** | SQLite Database | Relational database for querying, analysis, and backups |
| **`health_data.csv`** | CSV Spreadsheet | Flat export ready to open in Microsoft Excel or Apple Numbers |
| **`health_data.json`** | JSON Data | Structured format for programmatic access or web scripts |
| **`import_labs.py`** | Automation Script | One-command CLI tool to parse new HTML reports and update everything |
| **`process_labs.py`** | Core Extraction Engine | HTML parsing, date extraction, threshold parsing, and DB building logic |
| **`build_dashboard.py`**| HTML Generator | Compiles data into the standalone responsive Chart.js dashboard |

---

## 🗄️ SQLite Database (`health.db`)

You can query `health.db` using the terminal (`sqlite3 health.db`) or any GUI tool (e.g., DB Browser for SQLite):

### Key Views:
1. **`v_test_trends`**: Chronological progression of all test values:
   ```sql
   SELECT test_name, date_display, value, ref_range, units, flag 
   FROM v_test_trends 
   WHERE test_name = 'Cholesterol';
   ```

2. **`v_abnormal_results`**: All historical results flagged as High (`H`) or Low (`L`):
   ```sql
   SELECT date_display, test_name, value, ref_range, flag 
   FROM v_abnormal_results;
   ```

---

## 🔄 Adding Future Test Results

Whenever you receive a new HTML lab report:
1. Save the new `.html` file into `/Users/eric/Dropbox/ai/health/`.
2. Run the update command in your terminal:
   ```bash
   cd /Users/eric/Dropbox/ai/health
   python3 import_labs.py
   ```
3. The script will automatically parse the new file, update `health.db`, re-export the CSV/JSON, and refresh `index.html`!
