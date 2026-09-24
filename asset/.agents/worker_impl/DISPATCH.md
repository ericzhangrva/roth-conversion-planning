# DISPATCH — worker_impl

## Mission
Build the complete, standalone, single-file financial dashboard `/Users/eric/Dropbox/ai/asset/planning.html` implementing all requirements (R1 UI Inputs & Defaults, R2 Simulation Engine Rules, R3 Output Visuals, R4 Optimization Loop) and all acceptance criteria.

## Working Directory
`/Users/eric/Dropbox/ai/asset/.agents/worker_impl`

## File Ownership
- Exclusively owns `/Users/eric/Dropbox/ai/asset/planning.html`.
- You MUST NOT modify any test runner files or other agent files.

## Mandatory Reading
1. `/Users/eric/Dropbox/ai/asset/.agents/ORIGINAL_REQUEST.md` (authoritative user requirements)
2. `/Users/eric/Dropbox/ai/asset/PROJECT.md` (project architecture, interface contracts, element IDs)
3. `/Users/eric/Dropbox/ai/asset/.agents/spec_miner_survey/report.md` (authoritative mathematical formulas and tax rules)
4. `/Users/eric/Dropbox/ai/asset/.agents/explorer_existing/report.md` (design tokens, existing portfolio values, and tax routines)
5. `/Users/eric/Dropbox/ai/asset/.agents/explorer_arch/report.md` (architecture, performance benchmarks, and headless export pattern)

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Detailed Requirements for `planning.html`
1. **Standalone Architecture**: Single file containing HTML5, clean modern dark-mode CSS (responsive, executive palette), and vanilla JS. Load Chart.js v4.4.x via CDN (`https://cdn.jsdelivr.net/npm/chart.js@4.4.2/dist/chart.umd.min.js`). Include fallback in case CDN is unavailable.
2. **SafeStorage**: Implement `SafeStorage` wrapper around `localStorage` with in-memory fallback to avoid `SecurityError` or CORS exceptions when running locally via `file:///`.
3. **R1 Inputs & Defaults**: Implement form controls matching element IDs in `PROJECT.md` with exact defaults: Birth 1976, Ret 2027, EOL 2060, Inflation 3.5%, Cash $500K (5%), Inv $300K (9%), Pre-tax $5M, Roth $120K, Roth Principal $25K, College $100K (2029), Health $5K (sub) / $25K (unsub), SS Age 62 ($60K), Earned Income $275K, Living Expenses $60K, State Tax 5.75%.
4. **R2 Simulation Engine**:
   - Loop year-by-year from (Current Year + 1) to End of Life.
   - Compounding 3.5% inflation on Living Expenses, Healthcare, and **Federal Tax Brackets** (both thresholds and standard deduction).
   - College expense: exactly 5 years (12.5%, 25%, 25%, 25%, 12.5%), zero inflation.
   - Healthcare: pre-65 $5K subsidized if MAGI <= $90K, $25K unsubsidized if MAGI > $90K; drops to $0 at age 65 (Medicare).
   - Social Security: starts at SS Start Age ($60K/yr baseline).
   - Pre-retirement earned income: $275K active strictly before Retirement Year.
   - Cash flow waterfall & deficit liquidation order: Cash -> Taxable Investments -> Accessible Roth.
   - Roth 5-Year Rule: Conversions enter a locked vintage queue; accessible 5 years post-conversion; compound tax-free; liquidity constraint: `Cash + Inv + Accessible Roth >= 0`.
   - SECURE Act EOL Death Tax: 2 heirs liquidating pre-tax balance over 10 years at $150K base income each.
   - TVM metrics: Raw Tax, PV (discounted to Year 1), FV (compounded to EOL).
5. **R3 Visuals**:
   - Data table with all required columns (Year, Age, YE Cash, YE Inv, YE Pre-tax, YE Roth, YE Accessible Roth, Living, Health, College, Taxes, Roth Conversion).
   - Chart.js mixed dual-axis chart: stacked bars (Cash, Inv, Pre-tax, Roth) on left axis (`y`), line overlay for Cumulative Tax Paid on right axis (`y1`).
   - Summary cards displaying EOL Cash, Inv, Pre-tax, Roth, Raw Tax, PV Tax, FV Tax, and Death Tax.
6. **R4 Optimization Loop**:
   - Flat annual conversion search ($0 to $500K in $5K increments from Retirement Year to Age 75, 101 points).
   - Objective toggle: "Minimize Raw Total Tax" vs "Minimize TVM-Adjusted Tax".
   - Instantaneous execution (<20ms), auto-selects optimal conversion, updates slider, and re-renders chart/table.
7. **Headless Test Export**:
   - Dual-environment UMD export exposing `FinancialEngine` via `if (typeof module !== 'undefined') module.exports = { FinancialEngine }; if (typeof window !== 'undefined') window.FinancialEngine = FinancialEngine;`.

## Deliverable
Build and verify `/Users/eric/Dropbox/ai/asset/planning.html`, run local verification checks, write your findings in `report.md`, and deliver `handoff.md`.

## 2026-09-23T17:09:03Z
Mission received: Implement `/Users/eric/Dropbox/ai/asset/planning.html` as a standalone single-file financial planning dashboard meeting all R1, R2, R3, R4 requirements and acceptance criteria.
Strict integrity rules apply. No dummy implementations, no hardcoded test results. Headless verification support via dual-environment UMD export.

