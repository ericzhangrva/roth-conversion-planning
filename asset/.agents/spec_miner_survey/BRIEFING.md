# BRIEFING — 2026-09-23T17:04:55Z

## Mission
Rigorously analyze and document all requirements (R1, R2, R3, R4) and acceptance criteria for the lifetime tax simulation and optimization dashboard (planning.html), resolving ambiguities into precise mathematical equations and algorithms.

## 🔒 My Identity
- Archetype: specification_miner
- Roles: Teamwork specialist, external domain expert in financial planning algorithms and tax specification mining
- Working directory: /Users/eric/Dropbox/ai/asset/.agents/spec_miner_survey
- Original parent: c99153ea-1117-48ac-ab66-c9c7d4b0ab8f
- Milestone: Milestone 1 - Specification Mining & Formal Requirements Formulation

## 🔒 Key Constraints
- Do NOT implement anything — read-only spec miner role
- Single-file planning.html vanilla HTML/JS + Chart.js via CDN
- Must run locally via file:/// without CORS or localStorage SecurityError (try/catch storage)
- Rigorously define tax equations, cash waterfall, TVM discounting, Roth 5-year vintage tracking, inheritance death tax, and optimization brute-force bounds
- Output report to /Users/eric/Dropbox/ai/asset/.agents/spec_miner_survey/report.md
- Deliver 5-component handoff.md and notify parent via send_message

## Current Parent
- Conversation ID: c99153ea-1117-48ac-ab66-c9c7d4b0ab8f
- Updated: 2026-09-23T17:04:55Z

## Task Summary
- **What to build**: Specification report (`report.md`) detailing the exact equations, algorithms, data structures, UI specifications, and edge cases for `planning.html`.
- **Success criteria**: Complete coverage of R1, R2, R3, R4 and all acceptance criteria, fully resolving all ambiguities (brackets, deductions, inflation indexing, waterfall order, MAGI calculation, provisional income, SS taxation, capital gains vs ordinary income, TVM formula, Roth vintage FIFO/LIFO tracking, inheritance tax calculation, optimization search algorithm).
- **Interface contracts**: `/Users/eric/Dropbox/ai/asset/.agents/ORIGINAL_REQUEST.md` and `/Users/eric/Dropbox/ai/asset/.agents/spec_miner_survey/DISPATCH.md`
- **Code layout**: HTML/JS implementation will be `/Users/eric/Dropbox/ai/asset/planning.html`

## Key Decisions Made
- Formulated 7 progressive federal tax brackets + standard deduction with annual compounding inflation indexation for both MFJ and Single filers.
- Formulated college funding as piecewise function of 5 fixed steps (12.5%, 25%, 25%, 25%, 12.5%) with zero inflation.
- Formulated healthcare cost as piecewise function with inflation, pre-65 MAGI cliff at $90k ($5k vs $25k), dropping strictly to $0 at age 65 (Medicare).
- Decoupled MAGI from healthcare expense (since MAGI is driven by income/conversions), eliminating circular dependency.
- Specified IRC Section 86 provisional income formula for Social Security (start age 62, $60k with COLA, max 85% taxable tier).
- Defined cash interest (5%) as ordinary income and investment return (9%) with preferential capital gains taxation on realized yield.
- Specified Roth 5-year conversion vintage queue with FIFO drawdown of accessible conversion principal; initial $25k principal is accessible in Year 1.
- Formulated SECURE Act EOL Death Tax: 2 heirs, 10-year liquidation, $150k base income each, marginal tax on inheritance.
- Mathematically proved that minimizing PV of taxes is equivalent to minimizing FV of taxes.
- Documented brute-force grid search algorithm across 101 points ($0 to $500k in $5k steps) over 34 years (3,434 iterations, <2ms runtime).

## Artifact Index
- `/Users/eric/Dropbox/ai/asset/.agents/spec_miner_survey/report.md` — Formal specification & mathematical model report (Complete)
- `/Users/eric/Dropbox/ai/asset/.agents/spec_miner_survey/handoff.md` — 5-component handoff report (Pending)
