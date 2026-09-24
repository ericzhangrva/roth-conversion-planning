# DISPATCH — spec_miner_survey

## Mission
Analyze `/Users/eric/Dropbox/ai/asset/.agents/ORIGINAL_REQUEST.md` to extract and document complete, unambiguous specifications, mathematical formulations, edge cases, and tax rules for `planning.html`.

## Working Directory
`/Users/eric/Dropbox/ai/asset/.agents/spec_miner_survey`

## Scope & Key Questions
1. Detailed analysis of R1 (UI Inputs & Defaults).
2. Detailed mathematical specification of R2 (Simulation Engine Rules):
   - Federal tax brackets: base brackets (e.g. 2026/2027 IRS single vs MFJ, or 10%, 12%, 22%, 24%, 32%, 35%, 37%), standard deduction, bracket inflation indexing every year.
   - Living expenses inflation compounding vs college expenses (not inflated, 12.5%/25%/25%/25%/12.5% distribution across 5 years).
   - Healthcare costs: under 65 subsidized ($5k) vs unsubsidized ($25k) based on MAGI cliff ($90k); at age 65 (Medicare) drop to $0.
   - Social Security taxation (provisional income rule / 85% taxable) or flat taxable, and start age.
   - Earned income ($275k) active only pre-retirement.
   - Year-by-year cash flow waterfall & liquidity order: Living expenses, Healthcare, College, Taxes. In what order are Cash, Investment, and Accessible Roth tapped when expenses exceed income/distributions?
   - Roth 5-Year Rule: Tracking conversion vintages; accessible 5 years after conversion; liquidity constraint definition (`Cash + Inv + Accessible Roth >= 0`).
   - Investment returns (9%) vs Cash interest (5%): are they taxed as ordinary income or capital gains / qualified dividends?
   - Inheritance Tax at EOL: 2 heirs, 10-year liquidation of remaining Pre-tax balance, $150k base income each. Detailed tax computation.
   - TVM discounting: PV to start year, FV to EOL. What discount rate (inflation rate or interest rate)?
3. Detailed specification of R3 (Output Visuals): Data table columns, Chart.js stacked bar + line chart, Summary cards.
4. Detailed specification of R4 (Optimization Loop): Objective functions ("Minimize Raw Total Tax" vs "Minimize TVM-Adjusted Tax"), parameter sweep ($0 to $500K in $5K increments, retirement year to age 75), feasibility constraint.

## Deliverable
Write a comprehensive report to `/Users/eric/Dropbox/ai/asset/.agents/spec_miner_survey/report.md` and deliver `handoff.md`.

## 2026-09-23T17:02:42Z
You are spec_miner_survey. Your working directory is `/Users/eric/Dropbox/ai/asset/.agents/spec_miner_survey`.
You MUST read the authoritative user request at `/Users/eric/Dropbox/ai/asset/.agents/ORIGINAL_REQUEST.md` before starting work.
Also read `/Users/eric/Dropbox/ai/asset/.agents/spec_miner_survey/DISPATCH.md`.
Your mission is to rigorously analyze and document all requirements (R1, R2, R3, R4) and acceptance criteria, resolving ambiguities into precise mathematical equations and algorithms.
Write your complete findings and analysis to `/Users/eric/Dropbox/ai/asset/.agents/spec_miner_survey/report.md` and deliver `handoff.md`. Notify the orchestrator via send_message when finished.

