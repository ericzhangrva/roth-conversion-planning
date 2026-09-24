import os
import glob
import re
import json
import sqlite3
import csv
from datetime import datetime
from html.parser import HTMLParser

HEALTH_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(HEALTH_DIR, "health.db")
JSON_PATH = os.path.join(HEALTH_DIR, "health_data.json")
CSV_PATH = os.path.join(HEALTH_DIR, "health_data.csv")
HTML_PATH = os.path.join(HEALTH_DIR, "index.html")

CATEGORIES = {
    "Complete Blood Count (CBC)": [
        "WBC", "RBC", "HGB", "HCT", "MCV", "MCH", "MCHC", "RDW", 
        "PLT", "MPV", "LYM", "LYM%", "MID", "MID%", "GRAN", "GRAN%"
    ],
    "Comprehensive Metabolic Panel (CMP)": [
        "Glucose", "BUN", "Creatinine", "eGFR Non-African Amer.", "eGFR African Amer.",
        "Sodium", "Potassium", "Chloride", "CO2", "Calcium",
        "Total Protein", "Albumin", "Total Bili", "Alk Phosphatase", "AST (SGOT)", "ALT (SGPT)"
    ],
    "Lipid Panel (Cardiovascular)": [
        "Cholesterol", "Triglycerides", "Direct HDL", "LDL-Calculated", 
        "LDL-Direct", "_VLDL", "Chol/HDL Ratio"
    ],
    "Hormones, Endocrine & Thyroid": [
        "uTSH", "Free Thyroxine", "Total T4", "Total T3", "Free T3",
        "Prolactin", "FSH", "LH", "Estradiol", "Progesterone", "Testosterone"
    ],
    "Vitamins, Inflammation & Specialty": [
        "Vitamin D, 25-Hydroxy", "Vitamin B12", "Folate", "Ferritin", "Iron",
        "HgbA1c", "Magnesium", "Sed Rate", "CRP", "hs-CRP",
        "SARS-CoV-2 Spike Ab Dilution", "SARS-CoV-2 Spike Ab Interp",
        "SARS-CoV-2 Semi-Quant Spike Ab", "SARS-CoV-2 Semi-Quant Total Ab"
    ]
}

def get_category(test_name):
    for cat, tests in CATEGORIES.items():
        if test_name in tests:
            return cat
    return "Other / Miscellaneous"

def parse_ref_range(ref_str):
    ref_str = (ref_str or "").strip()
    if not ref_str or ref_str == "--":
        return None, None
    m_range = re.match(r"^([0-9.]+)\s*-\s*([0-9.]+)$", ref_str)
    if m_range:
        return float(m_range.group(1)), float(m_range.group(2))
    if ref_str.startswith(">"):
        val = re.sub(r"[^0-9.]", "", ref_str)
        return float(val) if val else None, None
    if ref_str.startswith("<") or "Negative<" in ref_str:
        val = re.sub(r"[^0-9.]", "", ref_str.split("<")[-1])
        return None, float(val) if val else None
    return None, None

class LabHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_font = False
        self.current_font = []
        self.tokens = []
        
    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'font':
            self.in_font = True
            self.current_font = []
        elif tag.lower() in ('tr', 'br'):
            self.tokens.append('__NEWLINE__')

    def handle_endtag(self, tag):
        if tag.lower() == 'font':
            self.in_font = False
            text = ''.join(self.current_font).strip()
            if text:
                self.tokens.append(text)
            self.current_font = []

    def handle_data(self, data):
        if self.in_font:
            self.current_font.append(data)
        else:
            cleaned = data.strip()
            if cleaned:
                self.tokens.append(cleaned)

def parse_lab_file(file_path):
    with open(file_path, 'r', encoding='latin1') as f:
        html = f.read()

    # Metadata
    m_date = re.search(r'COLLECTION DATE / TIME.*?</TR>\s*<TR[^>]*>.*?<FONT[^>]*>(\d{2}/\d{2}/\d{4})', html, re.DOTALL | re.IGNORECASE)
    coll_date = m_date.group(1) if m_date else None
    if not coll_date:
        m_dates = re.findall(r'(\d{2}/\d{2}/\d{4})\s+\d{2}:\d{2}:\d{2}', html)
        if m_dates:
            coll_date = m_dates[-1]

    # Convert to ISO date YYYY-MM-DD
    iso_date = None
    if coll_date:
        dt = datetime.strptime(coll_date, "%m/%d/%Y")
        iso_date = dt.strftime("%Y-%m-%d")

    m_acc = re.search(r'ACCESSION #.*?</TR>\s*<TR[^>]*>.*?<FONT[^>]*>([^<]+)</FONT>', html, re.DOTALL | re.IGNORECASE)
    accession = m_acc.group(1).strip() if m_acc else ""

    m_prov = re.search(r'ORDERING PROVIDER.*?</TR>\s*<TR[^>]*>.*?<FONT[^>]*>([^<]+)</FONT>', html, re.DOTALL | re.IGNORECASE)
    provider = m_prov.group(1).strip() if m_prov else ""

    # Patient demographics
    m_patient = re.search(r'PATIENT DEMOGRAPHICS.*?</TABLE></TD>.*?<FONT[^>]*>([^<]+)<BR>', html, re.DOTALL | re.IGNORECASE)
    patient_name = m_patient.group(1).strip() if m_patient else ""
    if not patient_name:
        m_p2 = re.search(r'PATIENT DEMOGRAPHICS.*?</TABLE></TD>.*?<FONT[^>]*>([A-Za-z\s]+)', html, re.DOTALL | re.IGNORECASE)
        patient_name = m_p2.group(1).strip() if m_p2 else "Fei"

    m_dob = re.search(r'DOB.*?</TR>\s*<TR[^>]*>.*?<FONT[^>]*>(\d{2}/\d{2}/\d{4})', html, re.DOTALL | re.IGNORECASE)
    dob = m_dob.group(1).strip() if m_dob else ""

    parser = LabHTMLParser()
    parser.feed(html)
    tokens = parser.tokens

    records = []
    in_results = False
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if tok == "NAME" and i+5 < len(tokens) and "VALUE" in tokens[i:i+5]:
            in_results = True
            i += 1
            continue
        if in_results and tok.startswith("-") and not tok.startswith("--"):
            test_name = tok.lstrip("-").strip()
            sub = []
            j = i + 1
            while j < len(tokens) and len(sub) < 7:
                if tokens[j] != "__NEWLINE__":
                    if (tokens[j].startswith("-") and not tokens[j].startswith("--")) or "Amazing Charts" in tokens[j] or "Signed Off by" in tokens[j]:
                        break
                    sub.append(tokens[j])
                j += 1
            
            raw_val = sub[0] if len(sub) > 0 else ""
            ref = sub[1] if len(sub) > 1 else ""
            units = sub[2] if len(sub) > 2 else ""
            flag = ""
            if len(sub) > 3 and sub[3] in ("H", "L", "A", "HH", "LL", "*"):
                flag = sub[3]
            elif len(sub) > 4 and sub[4] in ("H", "L", "A", "HH", "LL", "*"):
                flag = sub[4]

            num_val = None
            try:
                num_val = float(raw_val)
            except ValueError:
                num_val = None

            ref_min, ref_max = parse_ref_range(ref)

            # Auto-calculate flag if lab omitted it or for clinical consistency
            if not flag and num_val is not None:
                if ref_min is not None and num_val < ref_min:
                    flag = "L"
                elif ref_max is not None and num_val > ref_max:
                    flag = "H"

            records.append({
                "file": os.path.basename(file_path),
                "date_display": coll_date,
                "date": iso_date,
                "accession": accession,
                "provider": provider,
                "test": test_name,
                "category": get_category(test_name),
                "value": raw_val,
                "numeric_value": num_val,
                "ref_range": ref,
                "ref_min": ref_min,
                "ref_max": ref_max,
                "units": units,
                "flag": flag,
                "patient": patient_name,
                "dob": dob
            })
        i += 1

    return records

def build_database(all_records):
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    pat_name = all_records[0].get("patient", "FEI") if all_records else "FEI"
    pat_dob = all_records[0].get("dob", "") if all_records else ""

    cur.execute("""
    CREATE TABLE IF NOT EXISTS patient (
        id INTEGER PRIMARY KEY,
        name TEXT,
        dob TEXT,
        gender TEXT
    )""")
    cur.execute("INSERT INTO patient (name, dob, gender) VALUES (?, ?, 'F')", (pat_name, pat_dob))

    cur.execute("""
    CREATE TABLE IF NOT EXISTS test_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file TEXT,
        collection_date TEXT,
        date_display TEXT,
        category TEXT,
        test_name TEXT,
        value TEXT,
        numeric_value REAL,
        ref_range TEXT,
        ref_min REAL,
        ref_max REAL,
        units TEXT,
        flag TEXT,
        provider TEXT,
        accession TEXT
    )""")

    for r in all_records:
        cur.execute("""
        INSERT INTO test_results (
            file, collection_date, date_display, category, test_name, value, 
            numeric_value, ref_range, ref_min, ref_max, units, flag, provider, accession
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            r['file'], r['date'], r['date_display'], r['category'], r['test'], 
            r['value'], r['numeric_value'], r['ref_range'], r['ref_min'], r['ref_max'], 
            r['units'], r['flag'], r['provider'], r['accession']
        ))

    cur.execute("""
    CREATE VIEW IF NOT EXISTS v_test_trends AS
    SELECT test_name, category, collection_date, date_display, value, numeric_value, ref_range, ref_min, ref_max, units, flag
    FROM test_results
    ORDER BY test_name, collection_date
    """)

    cur.execute("""
    CREATE VIEW IF NOT EXISTS v_abnormal_results AS
    SELECT collection_date, date_display, category, test_name, value, ref_range, units, flag
    FROM test_results
    WHERE flag IN ('H', 'L', 'A', 'HH', 'LL', '*')
    ORDER BY collection_date DESC, test_name
    """)

    conn.commit()
    conn.close()
    print(f"Built SQLite database at: {DB_PATH}")

def export_csv(all_records):
    fieldnames = [
        "collection_date", "date_display", "category", "test_name", "value", 
        "numeric_value", "ref_range", "ref_min", "ref_max", "units", "flag", 
        "file", "provider", "accession"
    ]
    with open(CSV_PATH, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in all_records:
            writer.writerow({
                "collection_date": r['date'],
                "date_display": r['date_display'],
                "category": r['category'],
                "test_name": r['test'],
                "value": r['value'],
                "numeric_value": r['numeric_value'],
                "ref_range": r['ref_range'],
                "ref_min": r['ref_min'],
                "ref_max": r['ref_max'],
                "units": r['units'],
                "flag": r['flag'],
                "file": r['file'],
                "provider": r['provider'],
                "accession": r['accession']
            })
    print(f"Exported CSV at: {CSV_PATH}")

def export_json(all_records):
    # Group by test
    tests_dict = {}
    dates_set = set()

    for r in all_records:
        t = r['test']
        dates_set.add(r['date'])
        if t not in tests_dict:
            tests_dict[t] = {
                "name": t,
                "category": r['category'],
                "units": r['units'],
                "ref_range": r['ref_range'],
                "ref_min": r['ref_min'],
                "ref_max": r['ref_max'],
                "history": []
            }
        tests_dict[t]["history"].append({
            "date": r['date'],
            "date_display": r['date_display'],
            "value": r['value'],
            "numeric_value": r['numeric_value'],
            "flag": r['flag'],
            "ref_range": r['ref_range'],
            "ref_min": r['ref_min'],
            "ref_max": r['ref_max'],
            "units": r['units']
        })

    # Sort each test history chronologically
    for t, data in tests_dict.items():
        data["history"].sort(key=lambda x: x["date"])
        # If ref_range was missing on some dates, inherit from non-empty
        if not data["ref_range"]:
            for h in data["history"]:
                if h["ref_range"]:
                    data["ref_range"] = h["ref_range"]
                    data["ref_min"] = h["ref_min"]
                    data["ref_max"] = h["ref_max"]
                    break

    sorted_dates = sorted(list(dates_set))
    pat_name = all_records[0].get("patient", "Fei") if all_records else "Fei"
    pat_dob = all_records[0].get("dob", "") if all_records else ""

    out = {
        "metadata": {
            "patient": pat_name,
            "dob": pat_dob,
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_records": len(all_records),
            "dates": sorted_dates,
            "categories": list(CATEGORIES.keys()) + ["Other / Miscellaneous"]
        },
        "tests": tests_dict
    }

    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=2)
    print(f"Exported JSON at: {JSON_PATH}")
    return out

if __name__ == "__main__":
    files = sorted(glob.glob(os.path.join(HEALTH_DIR, "*.html")))
    # Exclude index.html or dashboard.html if present
    files = [f for f in files if os.path.basename(f) not in ("index.html", "dashboard.html")]
    print(f"Processing {len(files)} raw HTML report files...")

    all_records = []
    for f in files:
        recs = parse_lab_file(f)
        all_records.extend(recs)

    # Sort all records chronologically
    all_records.sort(key=lambda x: (x['date'], x['test']))

    build_database(all_records)
    export_csv(all_records)
    export_json(all_records)
    print("Done generating DB, CSV, and JSON.")
