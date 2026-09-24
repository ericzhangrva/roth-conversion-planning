# Original User Request

## Initial Request — 2026-09-23T17:00:27Z

Build a standalone, single-file financial dashboard (`planning.html`) using vanilla HTML/JS and Chart.js to simulate and optimize lifetime tax liability from retirement to End of Life.

Working directory: `/Users/eric/Dropbox/ai/asset/`
Integrity mode: development

## Requirements

### R1. UI Inputs & Defaults
Build a modern HTML interface with the following inputs:
- Birth Year (1976), Retirement Year (2027), End of Life Year (2060)
- Inflation Rate (3.5%)
- Cash ($500K), Interest Rate (5%)
- Investment ($300K), Investment Return (9%)
- Retirement Pre-tax ($5M), Retirement Roth ($120K), Roth Principal ($25K)
- College Total Expenses ($100K), College Start Year (2029)
- Health Insurance w/ Subsidy ($5K), Health Insurance w/o Subsidy ($25K)
- Social Security Start Age (62), SS Amount ($60K/yr)
- Taxable Earned Income ($275K, valid only pre-retirement)
- Living Expenses ($60K/yr in Year 1)
- State Tax Rate (5.75%)

### R2. Simulation Engine Rules
The simulation must loop year-by-year from (Current Year + 1) to End of Life. 
- **Inflation:** Apply the 3.5% inflation rate cumulatively to Living Expenses, Healthcare, and **Federal Tax Brackets** every year. Do *not* inflate College expenses.
- **College:** Spread the total expense over 5 years (Year 1: 12.5%, Year 2: 25%, Year 3: 25%, Year 4: 25%, Year 5: 12.5%).
- **Healthcare:** Apply the input costs up to age 64. At age 65 (Medicare), health insurance cost drops to $0 (or a negligible estimated default). Subsidy cliff: switch to unsubsidized if MAGI exceeds an estimated cliff (e.g., $90K).
- **Social Security:** Kicks in at the specified start age.
- **Roth 5-Year Rule:** Roth conversions become accessible 5 years after conversion. They stay inside the Roth to grow tax-free, but if the liquidity constraint requires it (Cash + Inv drops below $0), the accessible Roth principal is drawn down.
- **Inheritance Tax:** At End of Life, the remaining Pre-Tax balance is liquidated by 2 heirs over 10 years (assume they have $150K base income each). This "Death Tax" is added to the total lifetime tax.

### R3. Output Visuals
- **Data Table:** List YE Cash, Investment, Pre-tax, Roth, Roth Principal, Living Expenses, Health Insurance, College Expenses, Taxes (based on income, interest, returns, conversions), and Roth Conversion Amount for every year.
- **Chart:** Use Chart.js to render a stacked bar chart (Cash, Investment, Pre-tax, Roth) overlayed with a line chart showing Cumulative Tax Paid.
- **Summary:** Below the chart, show EOL Cash, Inv, Pre-tax, Roth. Show Total Tax Paid (Raw), Total Tax Paid (PV to start year), and Total Tax Paid (FV to EOL).

### R4. Optimization Loop
The engine must find the optimal **single flat dollar amount** for annual Roth conversions (applied from Retirement Year to Age 75). 
- Include a radio button to let the user optimize for either **"Minimize Raw Total Tax"** or **"Minimize TVM-Adjusted Tax"**.
- The solver must sweep through flat dollar amounts (e.g., $0 to $500K in $5K increments) and find the absolute minimum tax without ever violating the liquidity constraint (Cash + Inv + Accessible Roth >= 0).

## Acceptance Criteria

### Execution & Environment
- [ ] Must be a single `planning.html` file with no external build steps (can load Chart.js via CDN).
- [ ] Must run locally via `file:///` without throwing CORS or localStorage `SecurityError` exceptions (wrap storage in try/catch).

### Mathematical Accuracy
- [ ] Federal tax bracket thresholds must correctly inflate by the inflation rate every year in the simulation loop.
- [ ] College expenses must accurately span 5 years with the 12.5% / 25% / 25% / 25% / 12.5% distribution.
- [ ] Healthcare expenses must drop off at Age 65.
- [ ] Optimization loop must successfully brute-force a flat annual conversion amount and render the optimal path instantly.

## Follow-up — 2026-09-24T05:19:38Z

# Teamwork Project Prompt — Draft

> Status: Launched
> Goal: Craft prompt → get user approval → delegate to teamwork_preview
> Requested team: Small focused team

This is a single self-contained review; keep it small and focused. Provide a comprehensive financial and logical audit of the `planning.html` simulation engine to identify missing variables, unreasonable assumptions, and structural blind spots in the lifetime tax and cash flow projection.

Working directory: /Users/eric/Dropbox/ai/asset/
Integrity mode: development

## Requirements

### R1. Deep Financial Audit
Review the mathematical and logical assumptions embedded in the simulation, including a strict evaluation of the UI's default variables and stated assumptions. Evaluate the accuracy of the progressive tax brackets, inflation adjustments, healthcare subsidy cliffs, college distribution modeling, and the Roth 5-year lockup logic. Do NOT modify the code; output findings as a report.

### R2. Advanced Tax Mechanics & Blind Spots
Identify critical financial mechanics that are currently missing from the simulation but are essential for a realistic high-net-worth retirement projection. Specifically evaluate the absence of Capital Gains tax brackets (and cost basis tracking), Net Investment Income Tax (NIIT), Medicare IRMAA surcharges, and RMDs vs. voluntary conversions post-75.

### R3. Assessment Report
Produce a detailed Markdown report (`simulation_audit.md`) that categorizes findings into "Critical Flaws", "Unreasonable Assumptions", and "Missing Features". For each finding, provide concrete mathematical formulas or logic flows that would be required to implement it.

## Acceptance Criteria

### Verification
- [ ] The report successfully identifies at least 3 distinct structural or mathematical limitations in the current simulation engine.
- [ ] The report provides concrete, programmatic solutions or formulas for how to address each identified flaw.
- [ ] The assessment does not just list generic financial advice, but specifically cites the JavaScript functions and math currently present in `planning.html`.

## Follow-up — 2026-09-24T06:04:54Z

# Teamwork Project Prompt — Draft

> Status: Launched
> Goal: Craft prompt → get user approval → delegate to teamwork_preview
> Requested team: Small focused team

A targeted refactor of the `planning.html` financial simulation engine to upgrade the optimization algorithm to support multi-phase Roth conversions and enforce strict timeline validation on user inputs.

Working directory: /Users/eric/Dropbox/ai/asset/
Integrity mode: development

## Requirements

### R1. Multi-Phase Roth Optimization
The current optimizer uses a flat, single-value sweep across the entire simulation. Refactor `findOptimalConversion` to independently optimize across three distinct liquidity phases:
1. **Phase 1 (First 5 Years):** High liquidity constraint due to the 5-year Roth conversion lockup.
2. **Phase 2 (Year 6 to Age 59.5):** Conversions begin unlocking, but the age 59.5 penalty rules still apply.
3. **Phase 3 (Age 59.5 to Age 75):** All Roth funds are penalty-free and fully liquid.
*(Note: Because optimizing 3 phases creates a 3D search space, the JavaScript algorithm must use a performant mathematical approach—like a coarse-to-fine sweep or a sequential greedy solver—so the standalone HTML file continues to calculate instantly without freezing the browser. The approximation must be close to optimal).*

### R2. Input Validation Bounds
Add JavaScript validation to the DOM inputs to prevent impossible timelines:
- `retireYear` must be ≥ `currentYear + 1`.
- `eolYear` must be ≥ `retireYear` and ≥ `currentYear + 1`.
Ensure the engine dynamically corrects or rejects invalid inputs before running the simulation.

### R3. Retirement Year Alignment
Correct the boundary logic regarding "Retirement Year". The user specifies that the "retirement year" is the first full year they are retired. Ensure the UI labels, table rows, and underlying simulation logic flawlessly align with this definition so it is exactly the year entered by the user.

## Acceptance Criteria

### Verification
- [ ] The optimizer (`findOptimalConversion`) successfully returns distinct optimal conversion values for Phase 1, Phase 2, and Phase 3, avoiding liquidity crashes while minimizing lifetime tax.
- [ ] If the user enters `eolYear = 2025` (when current year is 2026), the UI instantly rejects or auto-corrects the input to 2027.
- [ ] If the user enters `retireYear = 2027`, the simulation designates 2027 as the first year of retirement (`isRetired = true`) and adjusts earned income accordingly.


