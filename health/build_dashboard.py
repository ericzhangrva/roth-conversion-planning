import os
import json
import sqlite3
import shutil
from glossary import TEST_GLOSSARY

HEALTH_DIR = "/Users/eric/Dropbox/ai/health"
JSON_PATH = os.path.join(HEALTH_DIR, "health_data.json")
HTML_PATH = os.path.join(HEALTH_DIR, "index.html")

def generate_dashboard():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    meta = data["metadata"]
    dates = meta["dates"]
    date_labels = [f"{d.split('-')[1]}/{d.split('-')[2]}/{d.split('-')[0]}" for d in dates]

    embedded_json = json.dumps(data)
    date_labels_json = json.dumps(date_labels)
    glossary_json = json.dumps(TEST_GLOSSARY)

    template = """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Health & Lab Results Tracker — Zhe Zhang</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns@3.0.0/dist/chartjs-adapter-date-fns.bundle.min.js"></script>
  <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            brand: {
              50: '#f0fdfa',
              100: '#ccfbf1',
              400: '#2dd4bf',
              500: '#14b8a6',
              600: '#0d9488',
              900: '#134e4a',
            },
            dark: {
              900: '#0b1120',
              850: '#0f172a',
              800: '#1e293b',
              750: '#283548',
              700: '#334155',
            }
          }
        }
      }
    };
  </script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');
    body {
      font-family: 'Inter', sans-serif;
      background-color: #0b1120;
      color: #f1f5f9;
    }
    .font-mono {
      font-family: 'JetBrains+Mono', monospace;
    }
    ::-webkit-scrollbar {
      width: 8px;
      height: 8px;
    }
    ::-webkit-scrollbar-track {
      background: #0f172a;
    }
    ::-webkit-scrollbar-thumb {
      background: #334155;
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #475569;
    }
    .glass-panel {
      background: rgba(30, 41, 59, 0.7);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.08);
    }
    .tab-active {
      background: rgba(20, 184, 166, 0.15) !important;
      color: #2dd4bf !important;
      border-bottom: 2px solid #2dd4bf !important;
    }
  </style>
</head>
<body class="min-h-screen antialiased flex flex-col">

  <!-- TOP HEADER -->
  <header class="border-b border-slate-800 bg-slate-900/80 sticky top-0 z-40 backdrop-blur-md">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
      <div class="flex items-center space-x-3">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-teal-500 to-emerald-400 flex items-center justify-center shadow-lg shadow-teal-500/20">
          <i data-lucide="activity" class="w-6 h-6 text-slate-950 font-bold"></i>
        </div>
        <div>
          <div class="flex items-center gap-2">
            <h1 class="text-xl font-bold tracking-tight text-white">Health & Lab Results Tracker</h1>
            <span class="px-2 py-0.5 text-xs font-semibold rounded-full bg-teal-500/10 text-teal-400 border border-teal-500/20">5-Year History</span>
          </div>
          <p class="text-xs text-slate-400">Patient: <strong class="text-slate-200">Zhe Zhang</strong> &nbsp;·&nbsp; DOB: 01/25/1976 (Age 50) &nbsp;·&nbsp; 6 Checkups (01/26/2022 – 08/12/2026)</p>
        </div>
      </div>

      <!-- Quick Actions / Search & Language -->
      <div class="flex items-center gap-3">
        <div class="relative w-full sm:w-60">
          <i data-lucide="search" class="w-4 h-4 text-slate-400 absolute left-3 top-2.5"></i>
          <input type="text" id="global-search" placeholder="Search any metric (e.g. Glucose)..." 
            class="w-full pl-9 pr-4 py-1.5 text-xs bg-slate-800/90 border border-slate-700 rounded-lg focus:outline-none focus:border-teal-500 text-slate-200 placeholder-slate-400 transition-colors">
        </div>

        <!-- Language Toggle Button -->
        <button id="btn-lang-toggle" onclick="toggleLanguage()" class="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-semibold bg-teal-500/15 hover:bg-teal-500/25 text-teal-300 border border-teal-500/30 rounded-lg transition-colors cursor-pointer shadow-sm" title="Toggle Explanation Language / 切换中文与英文说明">
          <i data-lucide="languages" class="w-3.5 h-3.5 text-teal-400"></i>
          <span id="lang-btn-text">中文 (ZH)</span>
        </button>

        <button onclick="downloadCSV()" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 text-xs font-medium bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 rounded-lg transition-colors cursor-pointer" title="Export CSV spreadsheet">
          <i data-lucide="file-spreadsheet" class="w-3.5 h-3.5 text-emerald-400"></i>
          CSV
        </button>
        <button onclick="downloadJSON()" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 text-xs font-medium bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 rounded-lg transition-colors cursor-pointer" title="Export JSON raw data">
          <i data-lucide="file-json" class="w-3.5 h-3.5 text-cyan-400"></i>
          JSON
        </button>
      </div>
    </div>

    <!-- CATEGORY TABS -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex space-x-1 overflow-x-auto border-t border-slate-800/60 no-scrollbar py-1 text-xs font-medium">
      <button onclick="switchTab('overview')" id="tab-overview" class="tab-btn px-3 py-2 rounded-md hover:text-white transition-colors flex items-center gap-1.5 tab-active">
        <i data-lucide="layout-dashboard" class="w-4 h-4"></i> Overview & Highlights
      </button>
      <button onclick="switchTab('cbc')" id="tab-cbc" class="tab-btn px-3 py-2 rounded-md text-slate-400 hover:text-white transition-colors flex items-center gap-1.5">
        <i data-lucide="droplet" class="w-4 h-4 text-rose-400"></i> Complete Blood Count (CBC)
      </button>
      <button onclick="switchTab('cmp')" id="tab-cmp" class="tab-btn px-3 py-2 rounded-md text-slate-400 hover:text-white transition-colors flex items-center gap-1.5">
        <i data-lucide="flask-conical" class="w-4 h-4 text-cyan-400"></i> Metabolic Panel (CMP)
      </button>
      <button onclick="switchTab('lipid')" id="tab-lipid" class="tab-btn px-3 py-2 rounded-md text-slate-400 hover:text-white transition-colors flex items-center gap-1.5">
        <i data-lucide="heart-pulse" class="w-4 h-4 text-amber-400"></i> Lipid Panel (Heart)
      </button>
      <button onclick="switchTab('hormones')" id="tab-hormones" class="tab-btn px-3 py-2 rounded-md text-slate-400 hover:text-white transition-colors flex items-center gap-1.5">
        <i data-lucide="dna" class="w-4 h-4 text-purple-400"></i> Hormones & Thyroid
      </button>
      <button onclick="switchTab('specialty')" id="tab-specialty" class="tab-btn px-3 py-2 rounded-md text-slate-400 hover:text-white transition-colors flex items-center gap-1.5">
        <i data-lucide="sun" class="w-4 h-4 text-yellow-400"></i> Vitamins & Specialty
      </button>
      <button onclick="switchTab('abnormal')" id="tab-abnormal" class="tab-btn px-3 py-2 rounded-md text-slate-400 hover:text-white transition-colors flex items-center gap-1.5">
        <i data-lucide="alert-triangle" class="w-4 h-4 text-red-400"></i> Out-of-Range Flags
      </button>
    </div>
  </header>

  <!-- MAIN CONTAINER -->
  <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 space-y-6">

    <!-- KPI SUMMARY CARDS -->
    <section class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-6 gap-3">
      <div class="glass-panel rounded-xl p-3.5 flex flex-col justify-between">
        <span class="text-xs text-slate-400 font-medium">Timeline Span</span>
        <div class="mt-1 flex items-baseline gap-1">
          <span class="text-lg font-bold text-white">4.6 yrs</span>
        </div>
        <span class="text-[11px] text-teal-400">01/26/2022 → 08/12/2026</span>
      </div>

      <div class="glass-panel rounded-xl p-3.5 flex flex-col justify-between">
        <span class="text-xs text-slate-400 font-medium">Lab Checkups</span>
        <div class="mt-1 flex items-baseline gap-1">
          <span class="text-lg font-bold text-white">6</span>
          <span class="text-xs text-slate-400">sessions</span>
        </div>
        <span class="text-[11px] text-slate-400">Family Practice Assoc.</span>
      </div>

      <div class="glass-panel rounded-xl p-3.5 flex flex-col justify-between">
        <span class="text-xs text-slate-400 font-medium">Tracked Tests</span>
        <div class="mt-1 flex items-baseline gap-1">
          <span class="text-lg font-bold text-white">53</span>
          <span class="text-xs text-slate-400">metrics</span>
        </div>
        <span class="text-[11px] text-slate-400">264 measurements</span>
      </div>

      <div class="glass-panel rounded-xl p-3.5 flex flex-col justify-between">
        <span class="text-xs text-slate-400 font-medium">Total Cholesterol</span>
        <div class="mt-1 flex items-baseline gap-1">
          <span class="text-lg font-bold text-emerald-400">132</span>
          <span class="text-xs text-slate-400">mg/dL</span>
        </div>
        <span class="text-[11px] text-emerald-400">↓ From 230 on 01/26/2022</span>
      </div>

      <div class="glass-panel rounded-xl p-3.5 flex flex-col justify-between">
        <span class="text-xs text-slate-400 font-medium">Fasting Glucose</span>
        <div class="mt-1 flex items-baseline gap-1">
          <span class="text-lg font-bold text-emerald-400">98</span>
          <span class="text-xs text-slate-400">mg/dL</span>
        </div>
        <span class="text-[11px] text-slate-400">Optimal (Ref 64-110)</span>
      </div>

      <div class="glass-panel rounded-xl p-3.5 flex flex-col justify-between">
        <span class="text-xs text-slate-400 font-medium">Kidney eGFR</span>
        <div class="mt-1 flex items-baseline gap-1">
          <span class="text-lg font-bold text-emerald-400">70.1</span>
          <span class="text-xs text-slate-400">>60</span>
        </div>
        <span class="text-[11px] text-emerald-400">Normal renal filtration</span>
      </div>
    </section>

    <!-- OVERVIEW TAB -->
    <div id="section-overview" class="space-y-6">
      <div class="glass-panel rounded-2xl p-5">
        <div class="flex items-center justify-between mb-4">
          <div>
            <h2 class="text-base font-semibold text-white flex items-center gap-2">
              <i data-lucide="sparkles" class="w-4 h-4 text-amber-400"></i>
              Key Health Trends & Vital Signposts
            </h2>
            <p class="text-xs text-slate-400">Core cardiovascular, metabolic, hormone, and renal markers tracked across all 6 clinical visits. <span class="text-teal-300">Hover over any metric name to view its medical explanation!</span></p>
          </div>
          <span class="text-xs px-2.5 py-1 rounded-md bg-slate-800 text-slate-300 border border-slate-700">6 Highlight Charts</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5" id="highlight-charts-grid">
          <!-- Populated by JS -->
        </div>
      </div>
    </div>

    <!-- CBC TAB -->
    <div id="section-cbc" class="space-y-6 hidden">
      <div class="glass-panel rounded-2xl p-5">
        <h2 class="text-base font-semibold text-white flex items-center gap-2 mb-1">
          <i data-lucide="droplet" class="w-4 h-4 text-rose-400"></i>
          Complete Blood Count (CBC)
        </h2>
        <p class="text-xs text-slate-400 mb-4">Cellular blood health: Red blood cells, oxygen delivery (hemoglobin/hematocrit), immune cells (WBC & differentials), and clotting platelets. (Hover any test for details)</p>
        <div class="overflow-x-auto rounded-xl border border-slate-800 mb-6" id="table-cbc"></div>
        <h3 class="text-sm font-semibold text-slate-200 mb-3 flex items-center gap-2">
          <i data-lucide="line-chart" class="w-4 h-4 text-teal-400"></i> Individual Metric Trends & Reference Thresholds
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5" id="charts-cbc"></div>
      </div>
    </div>

    <!-- CMP TAB -->
    <div id="section-cmp" class="space-y-6 hidden">
      <div class="glass-panel rounded-2xl p-5">
        <h2 class="text-base font-semibold text-white flex items-center gap-2 mb-1">
          <i data-lucide="flask-conical" class="w-4 h-4 text-cyan-400"></i>
          Comprehensive Metabolic Panel (CMP)
        </h2>
        <p class="text-xs text-slate-400 mb-4">Electrolytes, hydration, kidney filtration (BUN, Creatinine, eGFR), liver enzymes (ALT, AST, AlkPhos, Bilirubin), proteins, and blood sugar. (Hover any test for details)</p>
        <div class="overflow-x-auto rounded-xl border border-slate-800 mb-6" id="table-cmp"></div>
        <h3 class="text-sm font-semibold text-slate-200 mb-3 flex items-center gap-2">
          <i data-lucide="line-chart" class="w-4 h-4 text-teal-400"></i> Individual Metric Trends & Reference Thresholds
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5" id="charts-cmp"></div>
      </div>
    </div>

    <!-- LIPID TAB -->
    <div id="section-lipid" class="space-y-6 hidden">
      <div class="glass-panel rounded-2xl p-5">
        <h2 class="text-base font-semibold text-white flex items-center gap-2 mb-1">
          <i data-lucide="heart-pulse" class="w-4 h-4 text-amber-400"></i>
          Lipid Panel (Cardiovascular Profile)
        </h2>
        <p class="text-xs text-slate-400 mb-4">Total Cholesterol, Triglycerides, HDL (good), LDL (bad), and cardiovascular risk ratios. (Hover any test for details)</p>
        <div class="overflow-x-auto rounded-xl border border-slate-800 mb-6" id="table-lipid"></div>
        <h3 class="text-sm font-semibold text-slate-200 mb-3 flex items-center gap-2">
          <i data-lucide="line-chart" class="w-4 h-4 text-teal-400"></i> Individual Metric Trends & Reference Thresholds
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5" id="charts-lipid"></div>
      </div>
    </div>

    <!-- HORMONES TAB -->
    <div id="section-hormones" class="space-y-6 hidden">
      <div class="glass-panel rounded-2xl p-5">
        <h2 class="text-base font-semibold text-white flex items-center gap-2 mb-1">
          <i data-lucide="dna" class="w-4 h-4 text-purple-400"></i>
          Hormones, Endocrine & Men's Health
        </h2>
        <p class="text-xs text-slate-400 mb-4">Thyroid gland performance (uTSH, Free T4), Male endocrine markers (Total & Free Testosterone, Prolactin), and Prostate-Specific Antigen (PSA). (Hover any test for details)</p>
        <div class="overflow-x-auto rounded-xl border border-slate-800 mb-6" id="table-hormones"></div>
        <h3 class="text-sm font-semibold text-slate-200 mb-3 flex items-center gap-2">
          <i data-lucide="line-chart" class="w-4 h-4 text-teal-400"></i> Individual Metric Trends & Reference Thresholds
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5" id="charts-hormones"></div>
      </div>
    </div>

    <!-- SPECIALTY TAB -->
    <div id="section-specialty" class="space-y-6 hidden">
      <div class="glass-panel rounded-2xl p-5">
        <h2 class="text-base font-semibold text-white flex items-center gap-2 mb-1">
          <i data-lucide="sun" class="w-4 h-4 text-yellow-400"></i>
          Vitamins, Inflammation & Specialty Tests
        </h2>
        <p class="text-xs text-slate-400 mb-4">Vitamin D levels, 3-month average blood glucose (HgbA1c), systemic inflammation (Sed Rate / ESR), and COVID-19 antibody levels. (Hover any test for details)</p>
        <div class="overflow-x-auto rounded-xl border border-slate-800 mb-6" id="table-specialty"></div>
        <h3 class="text-sm font-semibold text-slate-200 mb-3 flex items-center gap-2">
          <i data-lucide="line-chart" class="w-4 h-4 text-teal-400"></i> Individual Metric Trends & Reference Thresholds
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5" id="charts-specialty"></div>
      </div>
    </div>

    <!-- ABNORMAL FLAGS TAB -->
    <div id="section-abnormal" class="space-y-6 hidden">
      <div class="glass-panel rounded-2xl p-5">
        <div class="flex items-center justify-between mb-3">
          <div>
            <h2 class="text-base font-semibold text-white flex items-center gap-2">
              <i data-lucide="alert-triangle" class="w-4 h-4 text-red-400"></i>
              Out-of-Range Clinical Flags History
            </h2>
            <p class="text-xs text-slate-400">All 17 measurements that fell above (High) or below (Low) the established clinical reference intervals.</p>
          </div>
          <span class="text-xs px-2.5 py-1 rounded-md bg-red-500/10 text-red-400 border border-red-500/20 font-medium">17 Flagged Results</span>
        </div>
        <div class="overflow-x-auto rounded-xl border border-slate-800" id="table-abnormal"></div>
      </div>
    </div>

    <!-- SEARCH RESULTS SECTION -->
    <div id="section-search" class="space-y-6 hidden">
      <div class="glass-panel rounded-2xl p-5">
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-base font-semibold text-white flex items-center gap-2">
            <i data-lucide="search" class="w-4 h-4 text-teal-400"></i>
            Search Results for "<span id="search-query-text" class="text-teal-300"></span>"
          </h2>
          <button onclick="clearSearch()" class="text-xs text-slate-400 hover:text-white underline">Clear search</button>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5" id="search-charts-grid"></div>
      </div>
    </div>

  </main>

  <!-- FLOATING MEDICAL POPUP WINDOW / TOOLTIP -->
  <div id="metric-tooltip" class="fixed hidden z-50 max-w-sm w-84 p-4 rounded-xl glass-panel shadow-2xl border border-teal-500/40 bg-slate-900/95 backdrop-blur-xl text-xs transition-opacity duration-150 pointer-events-none">
    <div class="flex items-start justify-between gap-2 border-b border-slate-800 pb-2 mb-2">
      <div>
        <h5 id="tooltip-title" class="font-bold text-white text-sm tracking-tight"></h5>
        <span id="tooltip-category" class="text-[10.5px] text-teal-400 font-medium"></span>
      </div>
      <span id="tooltip-ref" class="px-1.5 py-0.5 rounded text-[10px] font-mono bg-slate-800 text-slate-300 border border-slate-700 whitespace-nowrap"></span>
    </div>
    <div class="space-y-2">
      <div>
        <span id="tooltip-desc-label" class="text-[10px] uppercase font-bold text-slate-400 tracking-wider">What it is</span>
        <p id="tooltip-desc" class="text-slate-200 mt-0.5 leading-relaxed text-[11.5px]"></p>
      </div>
      <div id="tooltip-significance-box" class="pt-1.5 border-t border-slate-800/80">
        <span id="tooltip-sig-label" class="text-[10px] uppercase font-bold text-amber-400/90 tracking-wider">Clinical Significance</span>
        <p id="tooltip-significance" class="text-slate-300 mt-0.5 leading-relaxed text-[11px]"></p>
      </div>
    </div>
  </div>

  <!-- CLINICAL MILESTONE TOOLTIP POPOVER -->
  <div id="milestone-tooltip" class="fixed hidden z-50 max-w-sm w-80 p-3.5 rounded-xl glass-panel shadow-2xl bg-slate-900/95 backdrop-blur-xl text-xs transition-opacity duration-150 pointer-events-none border border-slate-700">
    <div class="flex items-center gap-2 mb-2 pb-2 border-b border-slate-800">
      <span id="milestone-tooltip-icon" class="text-lg"></span>
      <div>
        <h4 id="milestone-tooltip-title" class="font-bold text-slate-100 text-xs"></h4>
        <span id="milestone-tooltip-date" class="text-[10.5px] font-mono text-slate-400"></span>
      </div>
    </div>
    <p id="milestone-tooltip-desc" class="text-[11px] text-slate-200 leading-relaxed mb-2"></p>
    <div class="pt-2 border-t border-slate-800/80 text-[10.5px]">
      <span id="milestone-tooltip-impact-label" class="uppercase font-bold text-slate-400 tracking-wider text-[9.5px] block mb-0.5"></span>
      <p id="milestone-tooltip-impact-val" class="text-teal-300 font-normal leading-snug"></p>
    </div>
  </div>

  <!-- FOOTER -->
  <footer class="border-t border-slate-800 bg-slate-950 py-4 text-center text-xs text-slate-500">
    <p>Health & Lab Results Tracker &nbsp;·&nbsp; Data stored in SQLite (<code class="text-slate-400">health.db</code>), CSV, and JSON &nbsp;·&nbsp; Generated for Zhe Zhang</p>
  </footer>

  <!-- JAVASCRIPT LOGIC -->
  <script>
    const LAB_DATA = __EMBEDDED_DATA__;
    const DATES = LAB_DATA.metadata.dates;
    const DATE_LABELS = __DATE_LABELS__;
    const TESTS = LAB_DATA.tests;
    const TEST_GLOSSARY = __GLOSSARY_DATA__;

    // Timeline global chronological boundaries for true time-scaled x-axis
    let globalMinDate = '2021-10-01';
    let globalMaxDate = '2027-01-01';
    if (DATES && DATES.length > 0) {
      const firstDateObj = new Date(DATES[0] + 'T12:00:00');
      const lastDateObj = new Date(DATES[DATES.length - 1] + 'T12:00:00');
      const spanMs = Math.max(lastDateObj.getTime() - firstDateObj.getTime(), 365 * 24 * 3600 * 1000);
      const padMs = Math.max(spanMs * 0.04, 30 * 24 * 3600 * 1000);
      globalMinDate = new Date(firstDateObj.getTime() - padMs).toISOString().split('T')[0];
      globalMaxDate = new Date(lastDateObj.getTime() + padMs).toISOString().split('T')[0];
    }

    const chartInstances = {};
    const renderedTabs = {};

    // Language state: 'en' or 'zh' (default: 'en')
    let currentLang = localStorage.getItem('health_lang') || 'en';
    let activeTooltipTest = null;

    const CAT_MAP = {
      'cbc': [
        "WBC", "RBC", "HGB", "HCT", "MCV", "MCH", "MCHC", "RDW", 
        "PLT", "MPV", "LYM", "LYM%", "MID", "MID%", "GRAN", "GRAN%"
      ],
      'cmp': [
        "Glucose", "BUN", "Creatinine", "eGFR Non-African Amer.", "eGFR African Amer.",
        "Sodium", "Potassium", "Chloride", "CO2", "Calcium",
        "Total Protein", "Albumin", "Total Bili", "Alk Phosphatase", "AST (SGOT)", "ALT (SGPT)"
      ],
      'lipid': [
        "Cholesterol", "Triglycerides", "Direct HDL", "LDL-Calculated", 
        "LDL-Direct", "_VLDL", "Chol/HDL Ratio"
      ],
      'hormones': [
        "uTSH", "Free Thyroxine", "Testosterone", "Free Testosterone(Direct)", 
        "Prolactin", "PSA"
      ],
      'specialty': [
        "Vitamin D, 25-Hydroxy", "HgbA1c", "Magnesium", "Sed Rate",
        "SARS-CoV-2 Spike Ab Dilution", "SARS-CoV-2 Spike Ab Interp",
        "SARS-CoV-2 Semi-Quant Spike Ab", "SARS-CoV-2 Semi-Quant Total Ab"
      ]
    };

    // Metrics impacted by Atorvastatin (statin) and Lisinopril (ACE inhibitor) started on 9/26/2023
    const MEDS_TESTS = [
      "Cholesterol", "Triglycerides", "Direct HDL", "LDL-Calculated", "LDL-Direct", "_VLDL", "Chol/HDL Ratio",
      "ALT (SGPT)", "AST (SGOT)", "Alk Phosphatase", "Glucose", "HgbA1c",
      "Potassium", "BUN", "Creatinine", "eGFR Non-African Amer.", "eGFR African Amer.", "Sodium"
    ];

    // Metrics impacted by Gallbladder Removal (cholecystectomy) on 02/16/2025
    const GALLBLADDER_TESTS = [
      "Total Bili", "Alk Phosphatase", "ALT (SGPT)", "AST (SGOT)",
      "Cholesterol", "Triglycerides", "Direct HDL", "LDL-Calculated", "LDL-Direct", "_VLDL", "Chol/HDL Ratio",
      "Vitamin D, 25-Hydroxy"
    ];

    // Clinical Milestones Data Dictionary
    const CLINICAL_MILESTONES = {
      meds: {
        id: 'meds',
        dateStr: '2023-09-26',
        dateDisplay: '09/26/2023',
        icon: '💊',
        titleEn: 'Medication Regimen Started',
        titleZh: '开始服药方案',
        descEn: 'Started <strong>Atorvastatin 10mg</strong> (lipid-lowering statin) & <strong>Lisinopril 5mg</strong> (ACE inhibitor for blood pressure & renal protection).',
        descZh: '开始每日服用 <strong>阿托伐他汀 10mg</strong>（降脂他汀类药物）与 <strong>赖诺普利 5mg</strong>（降压及保护肾小球之ACE抑制剂）。',
        impactEn: 'Targeted reduction in circulating LDL/Cholesterol; monitoring renal hemodynamics & liver enzymes.',
        impactZh: '靶向大幅降低低密度脂蛋白与总胆固醇；定期监测肾脏滤过功能与肝脏转氨酶。',
        borderColor: 'border-amber-500/50'
      },
      gallbladder: {
        id: 'gallbladder',
        dateStr: '2025-02-16',
        dateDisplay: '02/16/2025',
        icon: '🏥',
        titleEn: 'Gallbladder Removal (Cholecystectomy)',
        titleZh: '胆囊切除手术 (Cholecystectomy)',
        descEn: 'Underwent laparoscopic cholecystectomy Sunday morning. Bile now drains continuously from the liver into the small intestine without reservoir concentration.',
        descZh: '于周日晨完成腹腔镜胆囊切除术。胆汁由肝脏直接持续缓慢排入十二指肠，无胆囊浓缩与阵发排空过程。',
        impactEn: 'Alters biliary dynamics (Bilirubin, AlkPhos), micellar lipid emulsion, and fat-soluble vitamin absorption (Vit D).',
        impactZh: '改变胆道流体动力学（胆红素、碱性磷酸酶）、脂质乳化代谢及脂溶性维生素吸收（维生素D）。',
        borderColor: 'border-rose-500/50'
      }
    };

    // Chart.js Custom Plugin for Vertical Clinical Milestone Lines
    const milestoneLinesPlugin = {
      id: 'milestoneLines',
      afterDraw(chart, args, options) {
        const { ctx, chartArea, scales: { x } } = chart;
        if (!chartArea || !x) return;
        const { top, bottom, left, right } = chartArea;
        const milestones = (options && options.milestones) || (chart.options.plugins && chart.options.plugins.milestoneLines && chart.options.plugins.milestoneLines.milestones) || [];
        if (!milestones.length) return;

        ctx.save();
        milestones.forEach(m => {
          let xPos = x.getPixelForValue(m.dateStr);
          if (xPos === undefined || isNaN(xPos)) {
            xPos = x.getPixelForValue(new Date(m.dateStr + 'T12:00:00').getTime());
          }
          if (xPos === undefined || isNaN(xPos) || xPos < left - 2 || xPos > right + 2) return;

          // Draw vertical dashed line
          ctx.beginPath();
          ctx.setLineDash([5, 4]);
          ctx.strokeStyle = m.color;
          ctx.lineWidth = 1.8;
          ctx.moveTo(xPos, top);
          ctx.lineTo(xPos, bottom);
          ctx.stroke();
        });
        ctx.restore();
      }
    };

    function getMilestonePosition(history, targetDateStr) {
      if (!history || !history.length) return null;
      const targetTime = new Date(targetDateStr).getTime();
      const dates = history.map(h => ({ dateStr: h.date, time: new Date(h.date).getTime() }));

      // Exact match
      for (let i = 0; i < dates.length; i++) {
        if (dates[i].dateStr === targetDateStr) {
          return { type: 'index', index: i };
        }
      }

      // Falls between two history dates
      for (let i = 0; i < dates.length - 1; i++) {
        if (dates[i].time <= targetTime && targetTime <= dates[i+1].time) {
          const frac = (targetTime - dates[i].time) / (dates[i+1].time - dates[i].time);
          return { type: 'fraction', index1: i, index2: i + 1, fraction: frac };
        }
      }

      return null;
    }

    let activeMilestoneKey = null;

    function showMilestoneTooltip(e, key) {
      activeMilestoneKey = key;
      const data = CLINICAL_MILESTONES[key];
      if (!data) return;

      const tip = document.getElementById('milestone-tooltip');
      const iconEl = document.getElementById('milestone-tooltip-icon');
      const titleEl = document.getElementById('milestone-tooltip-title');
      const dateEl = document.getElementById('milestone-tooltip-date');
      const descEl = document.getElementById('milestone-tooltip-desc');
      const impactLabelEl = document.getElementById('milestone-tooltip-impact-label');
      const impactValEl = document.getElementById('milestone-tooltip-impact-val');

      iconEl.textContent = data.icon;
      dateEl.textContent = data.dateDisplay;
      if (currentLang === 'zh') {
        titleEl.textContent = data.titleZh;
        descEl.innerHTML = data.descZh;
        impactLabelEl.textContent = '临床影响机制';
        impactValEl.textContent = data.impactZh;
      } else {
        titleEl.textContent = data.titleEn;
        descEl.innerHTML = data.descEn;
        impactLabelEl.textContent = 'Clinical Impact Mechanism';
        impactValEl.textContent = data.impactEn;
      }

      tip.className = `fixed z-50 max-w-sm w-80 p-3.5 rounded-xl glass-panel shadow-2xl bg-slate-900/95 backdrop-blur-xl text-xs transition-opacity duration-150 pointer-events-none border ${data.borderColor}`;

      tip.classList.remove('hidden');
      positionMilestoneTooltip(e);
    }

    function positionMilestoneTooltip(e) {
      const tip = document.getElementById('milestone-tooltip');
      if (!tip || tip.classList.contains('hidden')) return;

      const tipWidth = 320;
      const tipHeight = tip.offsetHeight || 160;
      const padding = 16;

      let x = e.clientX + 16;
      let y = e.clientY + 16;

      if (x + tipWidth > window.innerWidth - padding) {
        x = e.clientX - tipWidth - 16;
      }
      if (y + tipHeight > window.innerHeight - padding) {
        y = e.clientY - tipHeight - 16;
      }

      if (x < padding) x = padding;
      if (y < padding) y = padding;

      tip.style.left = x + 'px';
      tip.style.top = y + 'px';
    }

    function hideMilestoneTooltip() {
      activeMilestoneKey = null;
      const tip = document.getElementById('milestone-tooltip');
      if (tip) tip.classList.add('hidden');
    }

    function toggleLanguage() {
      currentLang = currentLang === 'en' ? 'zh' : 'en';
      localStorage.setItem('health_lang', currentLang);
      updateLangButton();
      updateMilestonesLanguage();
      if (activeTooltipTest) {
        updateTooltipContent(activeTooltipTest);
      }
    }

    function updateMilestonesLanguage() {
      if (activeMilestoneKey) {
        const dummyE = { clientX: window.innerWidth / 2, clientY: window.innerHeight / 2 };
        showMilestoneTooltip(dummyE, activeMilestoneKey);
      }
    }

    function updateLangButton() {
      const btnText = document.getElementById('lang-btn-text');
      if (btnText) {
        btnText.textContent = currentLang === 'en' ? '中文 (ZH)' : 'English (EN)';
      }
    }

    function updateTooltipContent(tName) {
      const info = TEST_GLOSSARY[tName] || {};
      const testItem = TESTS[tName] || {};

      const titleEl = document.getElementById('tooltip-title');
      const catEl = document.getElementById('tooltip-category');
      const refEl = document.getElementById('tooltip-ref');
      const descLabelEl = document.getElementById('tooltip-desc-label');
      const descEl = document.getElementById('tooltip-desc');
      const sigLabelEl = document.getElementById('tooltip-sig-label');
      const sigEl = document.getElementById('tooltip-significance');

      if (currentLang === 'zh') {
        titleEl.innerHTML = `${info.name_zh || tName} <span class="text-xs text-slate-400 font-normal">(${tName})</span>`;
        catEl.textContent = testItem.category || '';
        refEl.textContent = '标准: ' + (testItem.ref_range || '未注明') + (testItem.units ? ' ' + testItem.units : '');
        descLabelEl.textContent = '指标医学意义';
        descEl.textContent = info.desc_zh || '暂无详细解释。';
        sigLabelEl.textContent = '临床解读 (偏高 / 偏低)';
        sigEl.textContent = info.significance_zh || '请遵医嘱综合评估。';
      } else {
        titleEl.innerHTML = `${tName} <span class="text-xs text-slate-400 font-normal">(${info.name_en || ''})</span>`;
        catEl.textContent = testItem.category || '';
        refEl.textContent = 'Normal: ' + (testItem.ref_range || 'Not specified') + (testItem.units ? ' ' + testItem.units : '');
        descLabelEl.textContent = 'What it is';
        descEl.textContent = info.desc_en || 'No detailed description available.';
        sigLabelEl.textContent = 'Clinical Significance';
        sigEl.textContent = info.significance_en || 'Please consult your healthcare provider.';
      }
    }

    function showTooltip(e, tName) {
      activeTooltipTest = tName;
      updateTooltipContent(tName);
      const tip = document.getElementById('metric-tooltip');
      tip.classList.remove('hidden');
      positionTooltip(e);
    }

    function positionTooltip(e) {
      const tip = document.getElementById('metric-tooltip');
      if (!tip || tip.classList.contains('hidden')) return;

      const tipWidth = 330;
      const tipHeight = tip.offsetHeight || 220;
      const padding = 16;

      let x = e.clientX + 16;
      let y = e.clientY + 16;

      if (x + tipWidth > window.innerWidth - padding) {
        x = e.clientX - tipWidth - 16;
      }
      if (y + tipHeight > window.innerHeight - padding) {
        y = e.clientY - tipHeight - 16;
      }

      if (x < padding) x = padding;
      if (y < padding) y = padding;

      tip.style.left = x + 'px';
      tip.style.top = y + 'px';
    }

    function hideTooltip() {
      activeTooltipTest = null;
      const tip = document.getElementById('metric-tooltip');
      if (tip) tip.classList.add('hidden');
    }

    // Global event delegation for hover triggers
    document.addEventListener('mouseover', (e) => {
      const trigger = e.target.closest('.test-metric-trigger');
      if (trigger) {
        const testName = trigger.getAttribute('data-test');
        if (testName) {
          showTooltip(e, testName);
        }
      }
    });

    document.addEventListener('mousemove', (e) => {
      if (activeTooltipTest) {
        positionTooltip(e);
      }
      if (activeMilestoneKey) {
        positionMilestoneTooltip(e);
      }
    });

    document.addEventListener('mouseout', (e) => {
      const trigger = e.target.closest('.test-metric-trigger');
      if (trigger) {
        hideTooltip();
      }
    });

    function renderBadge(val, flag) {
      if (val === null || val === undefined || val === '') return '<span class="text-slate-600">—</span>';
      if (flag === 'H' || flag === 'HH') {
        return `<span class="inline-flex items-center gap-1 font-semibold text-rose-400 bg-rose-500/10 px-2 py-0.5 rounded border border-rose-500/25">${val} <span class="text-[10px]">▲H</span></span>`;
      }
      if (flag === 'L' || flag === 'LL') {
        return `<span class="inline-flex items-center gap-1 font-semibold text-cyan-400 bg-cyan-500/10 px-2 py-0.5 rounded border border-cyan-500/25">${val} <span class="text-[10px]">▼L</span></span>`;
      }
      return `<span class="text-slate-200">${val}</span>`;
    }

    function buildCategoryTable(testNames) {
      let html = `<table class="w-full text-left text-xs border-collapse">
        <thead>
          <tr class="border-b border-slate-800 bg-slate-900/90 text-slate-400 uppercase text-[10px] tracking-wider">
            <th class="py-3 px-4 font-semibold sticky left-0 bg-slate-900 z-10">Test Metric</th>
            <th class="py-3 px-3 font-semibold">Ref Range</th>
            <th class="py-3 px-2 font-semibold">Units</th>`;
      
      DATE_LABELS.forEach(d => {
        html += `<th class="py-3 px-3 font-semibold text-center">${d}</th>`;
      });
      html += `</tr></thead><tbody class="divide-y divide-slate-800/60">`;

      testNames.forEach(tName => {
        const item = TESTS[tName];
        if (!item) return;

        const byDate = {};
        item.history.forEach(h => {
          byDate[h.date] = h;
        });

        html += `<tr class="hover:bg-slate-800/40 transition-colors group">
          <td class="py-2.5 px-4 font-medium text-white group-hover:text-teal-300 transition-colors sticky left-0 bg-slate-900/90 group-hover:bg-slate-800/90 z-10">
            <span class="test-metric-trigger inline-flex items-center gap-1.5 cursor-help border-b border-dashed border-slate-600 hover:border-teal-400 pb-0.5 transition-colors" data-test="${tName}">
              ${tName}
              <i data-lucide="info" class="w-3.5 h-3.5 text-slate-500 hover:text-teal-300 inline opacity-60"></i>
            </span>
          </td>
          <td class="py-2.5 px-3 font-mono text-slate-400 text-[11px] whitespace-nowrap">${item.ref_range || '—'}</td>
          <td class="py-2.5 px-2 text-slate-400 text-[11px]">${item.units || '—'}</td>`;

        DATES.forEach(d => {
          const rec = byDate[d];
          if (rec) {
            html += `<td class="py-2.5 px-3 text-center font-mono whitespace-nowrap">${renderBadge(rec.value, rec.flag)}</td>`;
          } else {
            html += `<td class="py-2.5 px-3 text-center text-slate-600 font-mono">—</td>`;
          }
        });
        html += `</tr>`;
      });

      html += `</tbody></table>`;
      return html;
    }

    function renderChartCard(tName, containerId) {
      const item = TESTS[tName];
      if (!item) return;

      const safeId = tName.replace(/[^a-zA-Z0-9]/g, '_');
      const cardId = 'card-' + containerId + '-' + safeId;
      const canvasId = 'canvas-' + containerId + '-' + safeId;

      if (document.getElementById(cardId)) return;

      const isMeds = MEDS_TESTS.includes(tName);
      const isGallbladder = GALLBLADDER_TESTS.includes(tName);

      const cardHtml = `
        <div id="${cardId}" class="glass-panel rounded-xl p-4 flex flex-col justify-between hover:border-slate-700 transition-all">
          <div>
            <div class="flex items-start justify-between gap-2 mb-2">
              <div>
                <h4 class="text-sm font-semibold text-white tracking-tight test-metric-trigger cursor-help inline-flex items-center gap-1.5 border-b border-dashed border-transparent hover:border-teal-400 pb-0.5 transition-colors" data-test="${tName}">
                  ${tName}
                  <i data-lucide="info" class="w-3.5 h-3.5 text-slate-500 hover:text-teal-300 opacity-60"></i>
                </h4>
                <p class="text-[11px] text-slate-400 mt-0.5">Normal: <span class="text-teal-300 font-mono">${item.ref_range || 'Not specified'}</span> ${item.units ? '(' + item.units + ')' : ''}</p>
              </div>
              <div class="text-right whitespace-nowrap">
                <span class="text-xs font-mono font-bold text-slate-200" id="latest-${canvasId}"></span>
              </div>
            </div>
          </div>
          <div class="relative h-44 w-full mt-2">
            <canvas id="${canvasId}"></canvas>
          </div>
        </div>
      `;

      const container = document.getElementById(containerId);
      if (!container) return;
      container.insertAdjacentHTML('beforeend', cardHtml);

      const points = [];
      let latestVal = null;
      let latestFlag = null;

      item.history.forEach(h => {
        const parts = h.date.split("-");
        const dateLabel = `${parts[1]}/${parts[2]}/${parts[0]}`;
        points.push({
          x: h.date,
          y: h.numeric_value,
          rawVal: h.value,
          flag: h.flag,
          displayDate: dateLabel
        });
        latestVal = h.value;
        latestFlag = h.flag;
      });

      const latestEl = document.getElementById('latest-' + canvasId);
      if (latestEl) {
        latestEl.innerHTML = `Latest: ${renderBadge(latestVal, latestFlag)}`;
      }

      const cardMilestones = [];
      if (isMeds) {
        cardMilestones.push({
          key: 'meds',
          dateStr: '2023-09-26',
          color: 'rgba(245, 158, 11, 0.85)'
        });
      }

      if (isGallbladder) {
        cardMilestones.push({
          key: 'gallbladder',
          dateStr: '2025-02-16',
          color: 'rgba(244, 63, 94, 0.85)'
        });
      }

      const datasets = [
        {
          label: tName,
          data: points,
          borderColor: '#2dd4bf',
          backgroundColor: 'rgba(45, 212, 191, 0.1)',
          borderWidth: 2.5,
          tension: 0.25,
          pointBackgroundColor: points.map(p => {
            if (p.flag === 'H' || p.flag === 'HH') return '#f43f5e';
            if (p.flag === 'L' || p.flag === 'LL') return '#06b6d4';
            return '#14b8a6';
          }),
          pointBorderColor: '#0b1120',
          pointBorderWidth: 2,
          pointRadius: points.map(p => (p.flag ? 6 : 4)),
          pointHoverRadius: 0,
          fill: false,
          zIndex: 10
        }
      ];

      const minRef = item.ref_min;
      const maxRef = item.ref_max;

      if (maxRef !== null && maxRef !== undefined) {
        datasets.push({
          label: 'Upper Limit (' + maxRef + ')',
          data: [
            { x: globalMinDate, y: maxRef },
            { x: globalMaxDate, y: maxRef }
          ],
          borderColor: 'rgba(244, 63, 94, 0.6)',
          borderWidth: 1.5,
          borderDash: [4, 4],
          pointRadius: 0,
          pointHoverRadius: 0,
          fill: false,
          zIndex: 1
        });
      }

      if (minRef !== null && minRef !== undefined) {
        datasets.push({
          label: 'Lower Limit (' + minRef + ')',
          data: [
            { x: globalMinDate, y: minRef },
            { x: globalMaxDate, y: minRef }
          ],
          borderColor: 'rgba(6, 182, 212, 0.6)',
          borderWidth: 1.5,
          borderDash: [4, 4],
          pointRadius: 0,
          pointHoverRadius: 0,
          fill: false,
          zIndex: 1
        });
      }

      try {
        const canvasEl = document.getElementById(canvasId);
        if (!canvasEl) return;
        const ctx = canvasEl.getContext('2d');
        const chartObj = new Chart(ctx, {
          type: 'line',
          data: {
            datasets: datasets
          },
          plugins: [milestoneLinesPlugin],
          options: {
            responsive: true,
            maintainAspectRatio: false,
            layout: {
              padding: {
                top: 8,
                right: 12,
                bottom: 0,
                left: 4
              }
            },
            interaction: {
              mode: 'none'
            },
            plugins: {
              legend: {
                display: false
              },
              milestoneLines: {
                milestones: cardMilestones
              },
              tooltip: {
                enabled: false
              }
            },
            scales: {
              x: {
                type: 'time',
                min: globalMinDate,
                max: globalMaxDate,
                time: {
                  unit: 'year',
                  displayFormats: {
                    year: 'yyyy'
                  }
                },
                grid: {
                  color: 'rgba(255, 255, 255, 0.05)'
                },
                ticks: {
                  color: '#64748b',
                  font: { size: 10 }
                }
              },
              y: {
                grid: {
                  color: 'rgba(255, 255, 255, 0.05)'
                },
                ticks: {
                  color: '#64748b',
                  font: { size: 10 }
                }
              }
            }
          }
        });
        chartObj.milestones = cardMilestones;
        chartInstances[canvasId] = chartObj;

        // Interactive hover for vertical milestone lines on canvas
        if (cardMilestones.length > 0) {
          canvasEl.addEventListener('mousemove', (e) => {
            const rect = canvasEl.getBoundingClientRect();
            const mouseX = e.clientX - rect.left;
            const mouseY = e.clientY - rect.top;
            const { chartArea, scales: { x } } = chartObj;
            if (!chartArea || !x) return;

            if (mouseY < chartArea.top - 4 || mouseY > chartArea.bottom + 4) {
              hideMilestoneTooltip();
              return;
            }

            let foundKey = null;
            const hitRadius = 10;
            cardMilestones.forEach(m => {
              let xPos = x.getPixelForValue(m.dateStr);
              if (xPos === undefined || isNaN(xPos)) {
                xPos = x.getPixelForValue(new Date(m.dateStr + 'T12:00:00').getTime());
              }
              if (xPos !== undefined && Math.abs(mouseX - xPos) <= hitRadius) {
                foundKey = m.key;
              }
            });

            if (foundKey) {
              canvasEl.style.cursor = 'help';
              showMilestoneTooltip(e, foundKey);
            } else {
              canvasEl.style.cursor = 'default';
              hideMilestoneTooltip();
            }
          });

          canvasEl.addEventListener('mouseleave', () => {
            canvasEl.style.cursor = 'default';
            hideMilestoneTooltip();
          });
        }
      } catch (err) {
        console.error('Error rendering chart for ' + tName, err);
      }
    }

    function renderTabCharts(tabId) {
      if (renderedTabs[tabId]) {
        Object.keys(chartInstances).forEach(cId => {
          if (cId.includes(tabId)) {
            chartInstances[cId].resize();
          }
        });
        return;
      }

      if (tabId === 'overview') {
        const highlights = ["Cholesterol", "Triglycerides", "Glucose", "Vitamin D, 25-Hydroxy", "Testosterone", "eGFR Non-African Amer."];
        highlights.forEach(t => renderChartCard(t, 'highlight-charts-grid'));
        renderedTabs['overview'] = true;
      } else if (CAT_MAP[tabId]) {
        const testsInCat = CAT_MAP[tabId].filter(t => TESTS[t]);
        testsInCat.forEach(t => renderChartCard(t, 'charts-' + tabId));
        renderedTabs[tabId] = true;
      }
      lucide.createIcons();
    }

    function switchTab(tabId) {
      document.getElementById('section-search').classList.add('hidden');
      
      const sections = ['overview', 'cbc', 'cmp', 'lipid', 'hormones', 'specialty', 'abnormal'];
      sections.forEach(s => {
        const el = document.getElementById('section-' + s);
        const btn = document.getElementById('tab-' + s);
        if (s === tabId) {
          el.classList.remove('hidden');
          btn.classList.add('tab-active');
          btn.classList.remove('text-slate-400');
        } else {
          el.classList.add('hidden');
          btn.classList.remove('tab-active');
          btn.classList.add('text-slate-400');
        }
      });

      renderTabCharts(tabId);
    }

    function renderAbnormalTable() {
      const abnormalRows = [];
      Object.keys(TESTS).forEach(tName => {
        const t = TESTS[tName];
        t.history.forEach(h => {
          if (h.flag && ['H', 'L', 'A', 'HH', 'LL', '*'].includes(h.flag)) {
            abnormalRows.push({
              date: h.date,
              date_display: h.date_display,
              test: tName,
              category: t.category,
              value: h.value,
              flag: h.flag,
              ref_range: h.ref_range || t.ref_range,
              units: h.units || t.units
            });
          }
        });
      });

      abnormalRows.sort((a, b) => b.date.localeCompare(a.date));

      let html = `<table class="w-full text-left text-xs border-collapse">
        <thead>
          <tr class="border-b border-slate-800 bg-slate-900/90 text-slate-400 uppercase text-[10px] tracking-wider">
            <th class="py-3 px-4 font-semibold">Date</th>
            <th class="py-3 px-4 font-semibold">Category</th>
            <th class="py-3 px-4 font-semibold">Test Name</th>
            <th class="py-3 px-4 font-semibold text-center">Result</th>
            <th class="py-3 px-4 font-semibold">Reference Range</th>
            <th class="py-3 px-4 font-semibold">Units</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-slate-800/60">`;

      abnormalRows.forEach(r => {
        html += `<tr class="hover:bg-slate-800/40 transition-colors">
          <td class="py-2.5 px-4 font-mono text-slate-300">${r.date_display}</td>
          <td class="py-2.5 px-4 text-slate-400">${r.category}</td>
          <td class="py-2.5 px-4 font-medium text-white">
            <span class="test-metric-trigger inline-flex items-center gap-1.5 cursor-help border-b border-dashed border-slate-600 hover:border-teal-400 pb-0.5 transition-colors" data-test="${r.test}">
              ${r.test}
              <i data-lucide="info" class="w-3.5 h-3.5 text-slate-500 hover:text-teal-300 inline opacity-60"></i>
            </span>
          </td>
          <td class="py-2.5 px-4 text-center font-mono">${renderBadge(r.value, r.flag)}</td>
          <td class="py-2.5 px-4 font-mono text-slate-400">${r.ref_range || '—'}</td>
          <td class="py-2.5 px-4 text-slate-400">${r.units || '—'}</td>
        </tr>`;
      });

      html += `</tbody></table>`;
      document.getElementById('table-abnormal').innerHTML = html;
    }

    const searchInput = document.getElementById('global-search');
    searchInput.addEventListener('input', (e) => {
      const query = e.target.value.trim().toLowerCase();
      if (!query) {
        document.getElementById('section-search').classList.add('hidden');
        document.getElementById('section-overview').classList.remove('hidden');
        return;
      }

      document.querySelectorAll('main > div').forEach(el => el.classList.add('hidden'));
      const searchSec = document.getElementById('section-search');
      searchSec.classList.remove('hidden');
      document.getElementById('search-query-text').textContent = query;

      const grid = document.getElementById('search-charts-grid');
      grid.innerHTML = '';

      const matches = Object.keys(TESTS).filter(t => 
        t.toLowerCase().includes(query) || 
        TESTS[t].category.toLowerCase().includes(query) ||
        (TESTS[t].units && TESTS[t].units.toLowerCase().includes(query)) ||
        (TEST_GLOSSARY[t] && (TEST_GLOSSARY[t].name_zh.includes(query) || TEST_GLOSSARY[t].name_en.toLowerCase().includes(query)))
      );

      if (matches.length === 0) {
        grid.innerHTML = `<p class="col-span-3 text-center py-12 text-slate-500 text-sm">No test metrics found matching "${query}".</p>`;
        return;
      }

      matches.forEach(tName => {
        renderChartCard(tName, 'search-charts-grid');
      });
      lucide.createIcons();
    });

    function clearSearch() {
      searchInput.value = '';
      switchTab('overview');
    }

    function downloadJSON() {
      const blob = new Blob([JSON.stringify(LAB_DATA, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'health_data.json';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }

    function downloadCSV() {
      let csv = 'Collection_Date,Date_Display,Category,Test_Name,Value,Numeric_Value,Ref_Range,Ref_Min,Ref_Max,Units,Flag\\n';
      Object.keys(TESTS).forEach(tName => {
        const t = TESTS[tName];
        t.history.forEach(h => {
          const row = [
            h.date,
            h.date_display,
            `"${t.category}"`,
            `"${tName}"`,
            `"${h.value}"`,
            h.numeric_value !== null && h.numeric_value !== undefined ? h.numeric_value : '',
            `"${h.ref_range || t.ref_range || ''}"`,
            h.ref_min !== null && h.ref_min !== undefined ? h.ref_min : '',
            h.ref_max !== null && h.ref_max !== undefined ? h.ref_max : '',
            `"${h.units || t.units || ''}"`,
            h.flag || ''
          ];
          csv += row.join(',') + '\\n';
        });
      });
      const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'health_data.csv';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }

    window.addEventListener('DOMContentLoaded', () => {
      lucide.createIcons();
      updateLangButton();

      Object.keys(CAT_MAP).forEach(cat => {
        const testsInCat = CAT_MAP[cat].filter(t => TESTS[t]);
        const tblContainer = document.getElementById('table-' + cat);
        if (tblContainer) tblContainer.innerHTML = buildCategoryTable(testsInCat);
      });

      renderAbnormalTable();
      renderTabCharts('overview');
      lucide.createIcons();
    });
  </script>
</body>
</html>"""

    html_content = template.replace("__EMBEDDED_DATA__", embedded_json).replace("__DATE_LABELS__", date_labels_json).replace("__GLOSSARY_DATA__", glossary_json)

    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)
    shutil.copy(HTML_PATH, os.path.join(HEALTH_DIR, "dashboard.html"))
    print(f"Generated interactive dashboard HTML at: {HTML_PATH}")

if __name__ == "__main__":
    generate_dashboard()
