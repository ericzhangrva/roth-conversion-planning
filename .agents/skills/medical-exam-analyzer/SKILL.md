---
name: medical-exam-analyzer
description: >-
  End-to-end pipeline to process, extract, audit, and visualize comprehensive physical examination
  reports (体检报告) from PDF or scanned images (e.g. Chinese hospital reports like 浙二国际保健中心 or US EHRs).
  Converts SI units to US conventional units, verifies 100% data fidelity via clinical quality subagents,
  and builds a standalone bilingual interactive dashboard (index.html) with embedded charts.
---

# Medical Physical Exam Analyzer & Dashboard Generator (体检报告智能解析与仪表盘生成器)

This skill automates the complete end-to-end processing of comprehensive hospital physical examination reports (体检报告) from scanned or digital PDFs into an interactive, bilingual (Chinese/English), unit-converted (SI/US), and clinically audited single-file web dashboard.

---

## Capabilities & Key Features

1. **High-Fidelity PDF & Scanned Image Extraction**:
   - Converts multi-page clinical reports into 300+ DPI images and generates OCR text transcripts using Tesseract with bilingual Chinese/English support (`chi_sim+eng`).
   - Detects and corrects rotated or upside-down scans (e.g. 12-lead ECG rhythm strips).
   - Isolates and crops high-value diagnostic imagery (ECG rhythm strips, Arteriosclerosis PWV/ABI waveform reports, Ultrasound Bone Mineral Density T/Z charts).

2. **Full Clinical Entity Modeling**:
   - **Cover & Demographics**: Patient MRN, Card ID, DOB, clinical department, hospital name, confidentiality seals.
   - **Executive Diagnoses & Findings**: All primary abnormal findings (e.g. 14 numbered diagnoses) with verbatim hospital 【医学解释】 (Medical Rationale) and 【建议】 (Physician Recommendations).
   - **Laboratory Panels (70–90+ Tests)**: Complete metabolic panel (CMP), liver functions, kidney functions, lipid fractions, glycated hemoglobins (HbA1c/HbF), thyroid hormones & autoantibodies, tumor markers, vitamins, CBC with 5-part differential, stool routine & occult blood, urinalysis with microscopic sediment, and 13C urea breath tests.
   - **Specialized Diagnostic Devices**: Transcranial Doppler (TCD) 11-vessel hemodynamics, brachial-ankle pulse wave velocity (baPWV), ankle-brachial index (ABI), and calcaneus ultrasound BMD.

3. **Standardized Dual-Unit Medical Conversion**:
   - Converts all Chinese SI lab units (`mmol/L`, `μmol/L`, `g/L`) to US Conventional units (`mg/dL`, `g/dL`, `μIU/mL`, `lbs`, `in`).
   - Automatically maps standard US clinical reference intervals alongside Chinese hospital reference ranges.
   - Reference guide: `references/unit_conversions_reference.md`
   - Python library: `scripts/unit_converter.py`

4. **Multi-Agent Quality & Completeness Auditing**:
   - Leverages specialized subagents (`medical_auditor` and `completeness_auditor`) to perform line-by-line double-blind audits against the source document.
   - Guarantees 100.0% numerical precision, zero hallucinations, exact doctor attributions, and 100% complete coverage across all pages.

5. **Standalone All-in-One Dashboard (`index.html`)**:
   - Single-file zero-dependency architecture with inlined Base64 medical charts.
   - Instant single-toggle bilingual switcher (`🇺🇸 English` ⇄ `🇨🇳 中文`).
   - Instant single-toggle unit switcher (`🧪 美标 (US)` ⇄ `🧪 国际 (SI)`).
   - High-contrast segmented pill navigation tabs.
   - Real-time search and abnormal filter on all lab tests.
   - Ready for sharing via email, AirDrop, or messaging with no external asset folder required.

---

## Step-by-Step Execution Workflow

### Step 1: Ingest & Render PDF
Run the PDF extraction utility to produce high-resolution page images and OCR text files:
```bash
python3 /Users/eric/Dropbox/ai/.agents/skills/medical-exam-analyzer/scripts/pdf_to_images.py "<PATH_TO_PDF>" "<OUTPUT_DIR>"
```

### Step 2: Diagnostic Graphics Extraction & Orientation Correction
1. Identify graphical diagnostic pages:
   - 12-Lead ECG rhythm strip
   - Arteriosclerosis PWV/ABI waveform graph
   - Ultrasound Bone Mineral Density curve
2. Verify image orientation (rotate 90° or 180° if scanned in landscape or upside down):
```python
from PIL import Image
im = Image.open("<IMAGE_PATH>")
im.rotate(90, expand=True).save("<OUT_PATH>", quality=95)
```

### Step 3: Parse Structured Clinical JSON
Use `scripts/unit_converter.py` to compile `<OUTPUT_DIR>/china_exam_data.json` containing:
- `metadata`: Patient, hospital, dates, examiners, confidentiality notices.
- `vitals`: Height, weight, BMI, waist circumference, blood pressure, pulse, visual acuity.
- `abnormalities_summary`: Department-level summary of all identified abnormal items.
- `findings_14`: Detailed cards with verbatim hospital text, English translations, severity badges, and linked lab/imaging metrics.
- `lab_sections`: Array of panels with original SI values, converted US values, flags, and both hospital & US reference intervals.
- `specialized_diagnostics`: TCD matrix, PWV/ABI metrics, BMD scores, ECG parameters, organ-by-organ ultrasound findings, and radiology CT/CR reports.

### Step 4: Run Multi-Agent Quality & Completeness Audits
Deploy two specialized subagents:
1. `medical_auditor`: Audits all numbers, decimals, flags, and unit conversions against the original scan crops.
2. `completeness_auditor`: Audits page 1 to page N sequentially to verify that zero footnotes, doctors, or tests were dropped.

### Step 5: Build Standalone Interactive Dashboard
1. Generate the interactive dashboard `index.html`.
2. Encode cropped diagnostic images as Base64 Data URIs directly into `index.html` to make it 100% self-contained for easy sharing.
3. Open and verify in the default browser:
```bash
open "<OUTPUT_DIR>/index.html"
```
