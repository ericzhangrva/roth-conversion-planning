# Progress — spec_miner_survey

Last visited: 2026-09-23T17:04:45Z

## Status
- [x] Initialized DISPATCH.md and BRIEFING.md
- [x] Investigate existing project context and files (`asset.html`, `assets_data.json`, `health_cost.py`, etc.)
- [x] Analyze R1: UI Inputs, Form Structure, Default Values, Validation Constraints
- [x] Analyze R2: Simulation Engine Mathematical Formulations
  - [x] Federal tax brackets, standard deduction, inflation indexing
  - [x] State tax computation (5.75% Virginia rate)
  - [x] Living expenses inflation compounding vs college expenses schedule (12.5%, 25%, 25%, 25%, 12.5% zero inflation)
  - [x] Healthcare cost modeling: under 65 subsidized ($5k) vs unsubsidized ($25k), MAGI cliff ($90k), age 65 Medicare drop ($0)
  - [x] Social Security modeling: start age 62, $60k benefit, provisional income & IRC § 86 taxation rules
  - [x] Earned income rule ($275k valid pre-retirement)
  - [x] Year-by-year balance updates, returns (Cash 5%, Inv 9%), and tax classification of returns
  - [x] Cash flow waterfall and deficit liquidation priority order (Cash -> Inv -> Accessible Roth)
  - [x] Roth 5-year rule and vintage tracking, accessible principal vs earnings, liquidity constraint
  - [x] Inheritance "Death Tax" at EOL: 2 heirs, 10-year liquidation, $150k base income each
  - [x] TVM discounting: PV to start year, FV to EOL, discount rate definition and equivalence proof
- [x] Analyze R3: Output Visuals, Table Columns, Chart.js stacked bar + line spec, Summary KPIs
- [x] Analyze R4: Optimization Loop, Objective Functions ("Minimize Raw Total Tax" vs "Minimize TVM-Adjusted Tax"), Parameter Sweep (101 points), Constraints
- [x] Analyze Acceptance Criteria & Technical Constraints (file:/// compatibility, no CORS, single file, etc.)
- [x] Compile comprehensive `report.md` (delivered at `/Users/eric/Dropbox/ai/asset/.agents/spec_miner_survey/report.md`)
- [ ] Update `BRIEFING.md`
- [ ] Write 5-component `handoff.md`
- [ ] Notify parent via send_message
