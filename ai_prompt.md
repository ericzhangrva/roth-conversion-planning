# AI System Specification: Lifetime Financial & Tax Optimization Dashboard

**Goal:** Recreate a fully functional, single-file HTML/JS/CSS financial modeling and Roth conversion optimization dashboard.

## 1. Architecture & Environment Constraints
* **Format:** A single `index.html` file containing all HTML, CSS, and vanilla JavaScript (ES6+).
* **Dependencies:** Only Chart.js (via CDN) for data visualization. Use `html2canvas` (via CDN injection) for JPG exporting.
* **Execution:** Must run 100% client-side via the `file:///` protocol. No CORS violations, no server-side backend, no build steps (no Webpack/React).
* **Storage:** Implement a `SafeStorage` memory wrapper to prevent `SecurityError` exceptions when `localStorage` is blocked in local/incognito modes.

## 2. User Interface (UI) Layout
* **Theme:** Dark mode (`#0f172a` background, `#3b82f6` accents).
* **Layout Grid:** 
  * **Top Header:** Title and export buttons (PDF/JPG).
  * **Top KPIs:** 8 metric cards (End Cash, End Inv, End Pre-tax, End Roth, Lifetime Tax Raw, Lifetime Tax PV, Lifetime Tax FV, Inherited Death Tax).
  * **Main Content (Left):** Chart.js stacked bar chart (Asset balances) + line chart (Cumulative Tax) followed by a granular, sticky-header year-by-year data table.
  * **Sidebar (Right):** Optimization controls (Objective toggles, 4-Phase Sliders/Inputs) followed by data input panels (Life Timeline, Rate Assumptions, Asset Balances, Incomes, Living & Major Expenses).

## 3. Core Simulation Engine Rules
The simulation iterates year-by-year from `(Current Year + 1)` to `EOL Year`.

### A. Income & Tax
* **Standard Deductions & Brackets:** Inflate standard IRS MFJ/Single brackets annually by the user's `Inflation Rate`.
* **Social Security:** Scales dynamically based on the IRS actuarial curve depending on the chosen `SS Start Age`. Taxable amount is calculated via the IRC § 86 provisional income formula.
* **State Taxes:** Calculate state-specific tax (handling standard deduction variants, e.g., VA's progressive brackets vs flat states).
* **NIIT:** Calculate 3.8% Net Investment Income Tax on excess MAGI.

### B. Expense Modeling
* **Inflation:** Apply inflation cumulatively to Living Expenses and Healthcare.
* **Healthcare:** 
  * Pre-65: Use subsidized cost if MAGI ≤ Cliff ($90K), otherwise unsubsidized cost.
  * Post-65: Health cost = $0 base + Medicare IRMAA surcharges based on MAGI from 2 years prior.
* **College:** Total expense disbursed over 5 years (12.5%, 25%, 25%, 25%, 12.5%). No inflation applied.

### C. Liquidity & Drawdown Waterfall
* Calculate net cash deficit: `(Taxes + Expenses) - (Earned Income + SS + Cash Interest + RMDs)`.
* **Surplus:** Any cash surplus beyond the target `Cash Reserve` is swept into the `Taxable Brokerage` account for growth.
* **Deficit Priority Drawdown:**
  1. Cash Reserves
  2. Taxable Brokerage (Investments)
  3. Accessible Roth Principal (Strictly enforce the 5-year lockup rule for pre-59½ conversions using a FIFO vintage queue. Post-59½, all Roth funds are liquid).

### D. SECURE 2.0 & Terminal Wealth
* **RMDs:** Begin at age 75 using the IRS Uniform Lifetime Table III divisors. RMDs are forced distributions swept into Taxable Brokerage if unspent.
* **Death Tax:** At EOL, the remaining Pre-Tax balance is liquidated over 10 years by `N` heirs (assumed $150K base income each). Compute the marginal federal + state tax burden and add to the Lifetime Tax.

## 4. Roth Optimization Algorithm
* **Objective:** Find the mathematically optimal flat conversion amounts across 4 distinct life phases to minimize either Raw Lifetime Tax or TVM-Adjusted Lifetime Tax, while maintaining a strict minimum liquidity constraint.
* **The 4 Phases:**
  * Phase 1: Pre-Retirement to Year 5
  * Phase 2: Year 6 to Age 59½
  * Phase 3: Age 59½ to Age 74
  * Phase 4: Age 75+ (RMD Active)
* **Solver Method:** Implement a Multi-Start Coordinate Descent grid search.
  * **Seeds:** Start with multiple 4D vectors (e.g., `[50k, 100k, 150k, 0]`, `[150k, 300k, 400k, 0]`).
  * **Sweep 1 (Coarse):** Iterate each phase by $25K steps independently. Keep the best resulting metric. Run 2 complete cycles.
  * **Sweep 2 (Medium):** Iterate ±$30K around the coarse winner in $5K steps.
  * **Sweep 3 (Fine):** Iterate ±$5K around the medium winner in $1K steps.
* **Performance:** Execution must be blocking but fast enough (<300ms) to run inside the main browser thread on `input` events (with a 200ms debounce). Update the UI sliders automatically to reflect the optimal values.
