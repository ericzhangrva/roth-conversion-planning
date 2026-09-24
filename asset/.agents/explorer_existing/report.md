# Comprehensive Investigation Report: Existing Workspace Assets

**Agent**: `explorer_existing`  
**Date**: September 23, 2026  
**Target Project**: `planning.html` (Standalone Financial Tax Optimization Dashboard)  
**Examined Artifacts**:  
- `/Users/eric/Dropbox/ai/asset/asset.html`
- `/Users/eric/Dropbox/ai/asset/build_dashboard.py`
- `/Users/eric/Dropbox/ai/asset/health_cost.py`
- `/Users/eric/Dropbox/ai/asset/assets_data.json`
- `/Users/eric/Dropbox/ai/asset/update_assets.py`
- `/Users/eric/Dropbox/ai/asset/README.md`
- `/Users/eric/Dropbox/ai/asset/.agents/ORIGINAL_REQUEST.md`

---

## 1. Executive Summary

The existing repository contains a sophisticated, production-grade executive portfolio dashboard (`asset.html`) generated via Python (`build_dashboard.py`) and backed by a granular portfolio ledger (`assets_data.json`). The system was built for high-net-worth retirement and tax consulting, featuring dark-mode executive styling, an early retirement cash flow simulator (ages 50–60), and an ACA subsidy vs. SECURE Act RMD tax optimization model (ages 60–75 and End-of-Life).

While `asset.html` utilized pure SVG vector donuts to maximize offline tablet compatibility, the mathematical core contains proven vanilla JavaScript implementations for:
1. Federal MFJ progressive tax calculation (7 brackets + $29.2K standard deduction).
2. Virginia state tax modeling (5.75% flat).
3. SECURE Act 10-year inherited IRA liquidation by 2 heirs ($150K base income each).
4. TVM tax adjustment discounting and compounding.
5. ACA subsidy cliff logic based on modified adjusted gross income ($90K MAGI threshold).
6. Brute-force optimization sweeping over annual Roth conversion amounts.

These algorithms and UI tokens can be directly ported and adapted to satisfy the requirements for `planning.html`.

---

## 2. Inventory & File Structure Analysis

| File | Purpose | Key Findings & Relevance to `planning.html` |
|---|---|---|
| `assets_data.json` | Master financial ledger | 100% debt-free portfolio ($6.71M Net Worth). Pre-Tax retirement accounts comprise $4.84M (72% of NW), Roth is $116.9K (with $25K principal), Taxable Brokerage is $277.8K, Cash is $419.8K. Directly matches R1 default inputs. |
| `build_dashboard.py` | Dashboard builder & generator | Contains full HTML/CSS/JS template strings, SVG donut generator, quote fetchers, and complete simulation + RMD calculation logic. |
| `asset.html` | Compiled client-facing HTML | Standalone interactive dashboard with live JavaScript simulation tables, local storage auto-save, print/PDF export, and dark-theme UI. |
| `health_cost.py` | ACA healthcare cost projection | Age-bracketed ACA premium formulas, 3.7% age-inflation multiplier curve (50 to 64), Medicare transition at age 65 ($5,500/yr/person), child dependent aging. |
| `update_assets.py` | Account balance updater | Helper script showing mapping of holdings across accounts (Fidelity TOD, Self-Employed 401k, Cash Balance Plan, BSMH 403b). |
| `README.md` | Executive overview | Explains executive presentation philosophy: figures strictly rounded to $K, vector charts, high-level KPI cards, and strategic consultation agenda. |

---

## 3. Asset Modeling & Portfolio Baseline

The data in `assets_data.json` forms the exact foundation for the defaults specified in `ORIGINAL_REQUEST.md` (R1):

### A. Core Balances & Account Categorization
1. **Cash Reserves**:
   - `bank_cash.high_yield_savings`: **$419,846.00**
   - Brokerage cash: **$19,426.83** (TOD) + **$11,936.06** (Solo 401k) + **$158,940.60** (DB Plan) = $190,303.49 total liquid/semi-liquid cash.
   - Default for `planning.html`: **$500K Cash** at **5% Interest**.
2. **Taxable Brokerage (Investments)**:
   - `taxable_brokerage.etrade` (COF stock): **$93,031.17**
   - `taxable_brokerage.fidelity_individual_tod`: **$184,782.73**
   - Total Taxable Brokerage: **$277,813.90** (~$300K).
   - Default for `planning.html`: **$300K Investment** at **9% Return**.
3. **Qualified Pre-Tax Retirement**:
   - Capital One 401(k) Pre-Tax: **$1,956,127.90**
   - Self-Employed 401(k): **$913,068.61**
   - Cash Balance Defined Benefit Plan: **$1,302,138.66**
   - BSMH 403(b) Plan: **$664,346.08**
   - Total Pre-Tax: **$4,835,681.25** (~$5.0M).
   - Default for `planning.html`: **$5M Pre-Tax**.
4. **Roth Accounts**:
   - Capital One 401(k) Roth: **$116,919.90** (~$120K).
   - Roth Principal: **$25,000.00** (immediately penalty-free/liquid).
   - Default for `planning.html`: **$120K Roth**, **$25K Roth Principal**.
5. **Real Estate & Property** (Non-liquid context):
   - Primary Home: $660K (unencumbered)
   - Vacation Home: $300K (unencumbered)
   - Personal Property: $100K
   - Total Net Worth: $6,710,261.05. Zero debt.

---

## 4. UI/UX Design System & Reusable CSS

The styling in `asset.html` offers a cohesive dark executive palette that can be adopted for `planning.html`:

### CSS Custom Properties & Color Palette
```css
:root {
    --bg: #090d16;             /* Ultra-dark slate background */
    --panel-bg: #131b2e;       /* Card/panel background */
    --panel-border: #1f2d47;   /* Structural dividers & card borders */
    --text-white: #f8fafc;     /* Primary text */
    --text-sub: #94a3b8;       /* Secondary labels & metadata */
    --blue: #3b82f6;           /* Primary accents / Real Estate */
    --purple: #8b5cf6;         /* Pre-Tax Qualified accounts */
    --green: #10b981;          /* Cash & positive balances */
    --amber: #f59e0b;          /* Taxable Brokerage */
    --pink: #ec4899;           /* Roth accounts */
    --red: #ef4444;            /* Deficits, taxes, penalties */
    --cyan: #38bdf8;           /* Subsidies & highlights */
    --gray: #64748b;           /* Neutral property / muted */
}
```

### UI Component Patterns
- **Header**: Curved container (`border-radius: 16px`) with gradient background (`linear-gradient(135deg, #1e293b 0%, #0f172a 100%)`), left title block, right giant KPI headline.
- **KPI Summary Cards**: Top accent bar (`height: 3px; background: var(--category-color);`), uppercase tracker title, 28px numeric readout, subtitle percentage.
- **Form Controls**:
  - Dark inputs: `background: #0f172a; border: 1px solid #334155; color: #fff; padding: 6px 10px; border-radius: 6px; font-size: 13px;`
  - Disabled/Readonly inputs: `background: #1e293b; color: #94a3b8; cursor: not-allowed;`
- **Data Table (`summary-table`)**:
  - Subtle borders: `border-bottom: 1px solid rgba(255,255,255,0.04)`
  - Uppercase headers: `font-size: 11px; letter-spacing: 0.5px; color: var(--text-sub); text-transform: uppercase;`
  - Alternating or highlighted rows: Red text (`#ef4444`) when cash/brokerage drops below zero; green (`#6ee7b7`) when liquid.
- **Badges**:
  - Pill badges with 15% opacity background: e.g., `background: rgba(139, 92, 246, 0.15); color: #a78bfa;`
- **Printing & LocalStorage Safety**:
  - Encapsulate all `localStorage` access in `try { ... } catch (e) { console.warn(...) }` to avoid `SecurityError` under `file:///` in Safari/Chrome.
  - `@media print` rules hiding interactive controls and formatting white-page printouts.

---

## 5. Tax Calculation Algorithms & Bracket Logic

### A. Federal Progressive Tax (MFJ)
In `asset.html` lines 924–947:
```javascript
function calcFedTax(income_k) {
    let taxable = Math.max(0, (income_k * 1000) - 29200); // 2024/2026 MFJ Standard Deduction
    let tax = 0;
    if (taxable > 731200) { tax += (taxable - 731200) * 0.37; taxable = 731200; }
    if (taxable > 487450) { tax += (taxable - 487450) * 0.35; taxable = 487450; }
    if (taxable > 383900) { tax += (taxable - 383900) * 0.32; taxable = 383900; }
    if (taxable > 201050) { tax += (taxable - 201050) * 0.24; taxable = 201050; }
    if (taxable > 94300)  { tax += (taxable - 94300)  * 0.22; taxable = 94300; }
    if (taxable > 23200)  { tax += (taxable - 23200)  * 0.12; taxable = 23200; }
    if (taxable > 0)      { tax += taxable * 0.10; }
    return tax / 1000;
}
```

### B. Dynamic Tax Bracket Inflation (Crucial Requirement for `planning.html`)
In `ORIGINAL_REQUEST.md` R2 & Acceptance Criteria:
> "Apply the 3.5% inflation rate cumulatively to Living Expenses, Healthcare, and **Federal Tax Brackets** every year."
> "Federal tax bracket thresholds must correctly inflate by the inflation rate every year in the simulation loop."

Existing code in `asset.html` used static 2026 bracket thresholds. For `planning.html`, the brackets must be parameterized by year:
```javascript
// Base 2026 MFJ Thresholds:
const BASE_STD_DEDUCTION = 29200;
const BASE_FED_BRACKETS = [
    { limit: 23200,  rate: 0.10 },
    { limit: 94300,  rate: 0.12 },
    { limit: 201050, rate: 0.24 },
    { limit: 383900, rate: 0.32 },
    { limit: 487450, rate: 0.35 },
    { limit: 731200, rate: 0.37 },
    { limit: Infinity, rate: 0.37 }
];

function calcFedTaxInflated(incomeDollars, yearIndex, inflationRate) {
    const inflationFactor = Math.pow(1 + inflationRate, yearIndex);
    const stdDeduction = BASE_STD_DEDUCTION * inflationFactor;
    let taxable = Math.max(0, incomeDollars - stdDeduction);
    let tax = 0;
    let prevLimit = 0;
    
    for (let i = 0; i < BASE_FED_BRACKETS.length; i++) {
        const b = BASE_FED_BRACKETS[i];
        const currentLimit = b.limit === Infinity ? Infinity : b.limit * inflationFactor;
        const bracketSpan = currentLimit - prevLimit;
        
        if (taxable > bracketSpan) {
            tax += bracketSpan * b.rate;
            taxable -= bracketSpan;
            prevLimit = currentLimit;
        } else {
            tax += taxable * b.rate;
            taxable = 0;
            break;
        }
    }
    return tax;
}
```

### C. State Tax Rate
- Modeled in `asset.html` as Virginia state tax: `0.0575` (5.75%).
- Applied to taxable income / conversions.

### D. SECURE Act 10-Year Inheritance "Death Tax"
In `asset.html` lines 1006–1032:
```javascript
let kidBase = 150000; // $150K base income each for 2 heirs
let inheritedPretax = finalPretaxBal;

for (let y = 1; y <= 10; y++) {
    let dist = inheritedPretax / (11 - y); // Straight-line depletion over 10 years
    let perKid = dist / 2;
    // Marginal tax increase on top of heir's $150K base income:
    let taxPerKid = (calcFedTaxDollars(kidBase + perKid) - calcFedTaxDollars(kidBase)) + (perKid * stateTaxRate);
    let totalTaxThisYear = taxPerKid * 2;
    
    inheritedPretax -= dist;
    inheritedPretax *= (1 + investmentReturn);
    totalInheritanceTax += totalTaxThisYear;
}
```
This aligns with R2 requirement:
> "At End of Life, the remaining Pre-Tax balance is liquidated by 2 heirs over 10 years (assume they have $150K base income each). This 'Death Tax' is added to the total lifetime tax."

---

## 6. Healthcare, Medicare, and Subsidy Cliff Modeling

From `health_cost.py` and `asset.html`:
1. **ACA Subsidized vs. Unsubsidized**:
   - Subsidized Default: **$5,000/yr** (employer rate or subsidized exchange).
   - Unsubsidized Default: **$25,000/yr** (full retail unsubsidized exchange for couple).
2. **Subsidy Cliff**:
   - In `asset.html`: When retired and MAGI (Interest + Returns + Roth Conversions) > **$90K**, healthcare switches from subsidized ($5K) to unsubsidized ($25K).
3. **Medicare Transition at Age 65**:
   - In `health_cost.py`: Medicare Part B + Part D + Medigap is modeled at $5,500/person.
   - In `ORIGINAL_REQUEST.md` (R2):
     > "At age 65 (Medicare), health insurance cost drops to $0 (or a negligible estimated default)."
   - This drop-off at age 65 (current year - birth year >= 65) must be strictly implemented.
4. **Inflation**:
   - Healthcare costs inflate at the cumulative inflation rate (3.5% default) up to age 64.

---

## 7. College, Social Security, and Roth 5-Year Rule

### A. College Expenses
- Total Expense: **$100,000** total.
- Start Year: **2029** (user input).
- Distribution: **5-Year distribution**:
  - Year 1: **12.5%** ($12,500)
  - Year 2: **25.0%** ($25,000)
  - Year 3: **25.0%** ($25,000)
  - Year 4: **25.0%** ($25,000)
  - Year 5: **12.5%** ($12,500)
- Note: Do **not** apply inflation to college expenses (per R2).

### B. Social Security
- Start Age: **62** (user input, e.g., 62–70).
- Annual Amount: **$60,000/yr** (user input).
- Kicks in when `currentAge >= ssStartAge`.
- Counts toward taxable income / MAGI.

### C. Roth 5-Year Rule & Liquidity Constraint Mechanics
In `asset.html`:
- The previous implementation released matured Roth conversion principal directly into cash/brokerage after 5 years unconditionally.
In `ORIGINAL_REQUEST.md` (R2 & R4):
- **Crucial Distinction**: Roth conversions stay inside the Roth account to compound tax-free.
- Only the **accessible Roth principal** (initial $25K principal + any conversions completed >= 5 years ago that haven't been drawn down) serves as a liquidity reserve.
- Liquidity constraint: `Cash + Investment + Accessible Roth Principal >= 0`.
- If `Cash + Investment < 0` (deficit), the required deficit is drawn down from accessible Roth principal without penalty. If accessible Roth principal is exhausted and total liquidity < 0, the liquidity constraint is violated.

---

## 8. Chart.js & Data Visualization Strategy for `planning.html`

In `asset.html`, vector SVG donuts were used instead of Chart.js. However, `ORIGINAL_REQUEST.md` explicitly calls for:
> "Chart: Use Chart.js to render a stacked bar chart (Cash, Investment, Pre-tax, Roth) overlayed with a line chart showing Cumulative Tax Paid."
> "Must be a single `planning.html` file with no external build steps (can load Chart.js via CDN)."

### Reusable Chart.js Configuration Pattern
CDN URL:
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
```

Mixed Chart Pattern (Stacked Bar + Line Overlay):
```javascript
const ctx = document.getElementById('lifetimeChart').getContext('2d');
const chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: yearsArray,
        datasets: [
            {
                type: 'line',
                label: 'Cumulative Tax Paid',
                data: cumulativeTaxArray,
                borderColor: '#ef4444',
                backgroundColor: 'rgba(239, 68, 68, 0.1)',
                borderWidth: 3,
                yAxisID: 'yTax',
                tension: 0.3,
                pointRadius: 2,
                order: 1
            },
            {
                type: 'bar',
                label: 'Cash',
                data: cashBalArray,
                backgroundColor: '#10b981',
                stack: 'assets',
                order: 2
            },
            {
                type: 'bar',
                label: 'Taxable Investment',
                data: invBalArray,
                backgroundColor: '#f59e0b',
                stack: 'assets',
                order: 2
            },
            {
                type: 'bar',
                label: 'Pre-Tax Qualified',
                data: pretaxBalArray,
                backgroundColor: '#8b5cf6',
                stack: 'assets',
                order: 2
            },
            {
                type: 'bar',
                label: 'Roth Balance',
                data: rothBalArray,
                backgroundColor: '#ec4899',
                stack: 'assets',
                order: 2
            }
        ]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        interaction: { mode: 'index', intersect: false },
        scales: {
            x: {
                stacked: true,
                grid: { color: 'rgba(255,255,255,0.05)' },
                ticks: { color: '#94a3b8' }
            },
            y: {
                stacked: true,
                position: 'left',
                title: { display: true, text: 'Asset Portfolio Balance ($)', color: '#94a3b8' },
                grid: { color: 'rgba(255,255,255,0.05)' },
                ticks: {
                    color: '#94a3b8',
                    callback: (v) => '$' + (v / 1000).toLocaleString() + 'K'
                }
            },
            yTax: {
                position: 'right',
                title: { display: true, text: 'Cumulative Tax Paid ($)', color: '#ef4444' },
                grid: { drawOnChartArea: false },
                ticks: {
                    color: '#ef4444',
                    callback: (v) => '$' + (v / 1000).toLocaleString() + 'K'
                }
            }
        },
        plugins: {
            legend: { labels: { color: '#f8fafc', font: { size: 12 } } },
            tooltip: {
                callbacks: {
                    label: function(context) {
                        return `${context.dataset.label}: $${Math.round(context.raw).toLocaleString()}`;
                    }
                }
            }
        }
    }
});
```

---

## 9. Optimization Engine: Existing vs. Required Architecture

| Parameter | Existing Implementation (`asset.html`) | Required Implementation (`planning.html`) |
|---|---|---|
| **Conversion Horizon** | 2027 to 2036 (10 years) | Retirement Year (e.g. 2027) to **Age 75** |
| **Conversion Strategy** | Checkbox per year + 2-phase RMD simulation | Single flat annual dollar amount applied each year from retirement to age 75 |
| **Optimization Target** | TVM Tax at 2036 | Radio button: **"Minimize Raw Total Tax"** OR **"Minimize TVM-Adjusted Tax"** |
| **Search Space** | $0 to $1,000K in $5K or $10K increments | $0 to $500K in $5K increments (101 simulation runs) |
| **Liquidity Check** | `min(tempSave, tempInv) >= 0` | `Cash + Inv + Accessible Roth Principal >= 0` for all simulated years |
| **Execution Performance** | Fast (<30ms for 100 iterations) | Sweeping 101 candidates across ~35 years takes ~3,500 year-iterations, executing in <15ms in modern V8/WebKit JS engines. Instant real-time UI response. |

---

## 10. Architectural Recommendations for Implementation

1. **Self-Contained Single File**:
   - Zero external build dependencies.
   - Load Chart.js via CDN (`https://cdn.jsdelivr.net/npm/chart.js`).
   - Pure CSS embedded in `<style>`, full simulation engine and Chart.js instantiation embedded in `<script>`.
2. **Defensive Storage**:
   - Wrap all `localStorage` reads/writes in `try / catch` blocks to eliminate `SecurityError` crashes when loaded via `file:///Users/...`.
3. **Form Layout & Reactive Architecture**:
   - 2-column or 3-column structured grid for user inputs with clear visual groupings (Demographics, Rates & Balances, Expenses & Healthcare, Optimization Mode).
   - `input` event listeners on all inputs triggering debounced re-simulation (`requestAnimationFrame` or `setTimeout(100ms)`).
4. **Data Table & Summary Metrics**:
   - Render year-by-year rows with formatting: `Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 })`.
   - Clear summary cards displaying: EOL Cash, EOL Inv, EOL Pre-tax, EOL Roth, Raw Total Lifetime Tax, PV Total Tax (discounted at Investment Return to start year), and FV Total Tax (compounded to EOL).
