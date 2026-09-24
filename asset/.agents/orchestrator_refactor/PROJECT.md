# Project: Multi-Phase Roth Optimization & Timeline Validation Refactor

## Target
Target File: `/Users/eric/Dropbox/ai/asset/planning.html`

## Architecture
- **Single-file standalone application**: Vanilla HTML/CSS/JS with Chart.js loaded from CDN.
- **Engine Namespace**: `window.FinancialEngine` exposing defaults, math functions, `runSimulation()`, and `findOptimalConversion()`.
- **UI Controller**: DOM event listeners, dynamic input validation, 3-phase Roth conversion controls, KPI metric rendering, Chart.js rendering, and simulation data table rendering.

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Multi-Phase Roth Conversion | 3 dynamic phases ($k_1$: Yr 1-5, $k_2$: Yr 6 to 59.5, $k_3$: 59.5 to 75) | M1 | ORIGINAL_REQUEST R1 |
| 2 | Fast Multi-Phase Optimizer | Multi-start coordinate descent solver (<100ms, non-blocking) | M1 | ORIGINAL_REQUEST R1 |
| 3 | Input Validation Bounds | retireYear >= currentYear + 1, eolYear >= retireYear & currentYear + 1 | M2 | ORIGINAL_REQUEST R2 |
| 4 | Dynamic Input Auto-Correction | Auto-correct invalid timeline inputs on blur/change/4-digit entry | M2 | ORIGINAL_REQUEST R2 |
| 5 | Retirement Year Alignment | retireYear is first full year retired (`isRetired = true`, $0 earned income) | M3 | ORIGINAL_REQUEST R3 |
| 6 | UI & Chart Alignment | 3-Phase Conversion Cards, table retirement styling, chart marker at retireYear | M3 | ORIGINAL_REQUEST R1/R3 |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Implementation (R1, R2, R3) | Implement all algorithm, validation, alignment, and UI updates in `planning.html` | none | DONE |
| 2 | Gate Verification | 2 Reviewers, 2 Challengers, 1 Forensic Auditor | M1 | DONE |
| 3 | Synthesis & Handoff | Reconcile gate verdicts and produce final report | M2 | DONE |

## Code Layout
- Target File: `/Users/eric/Dropbox/ai/asset/planning.html`
- Styles: `<style>` block in `<head>`
- Markup: `<body>` contains Inputs Form, Optimizer Controls, KPIs, Chart Canvas, Data Table
- Scripts: `<script>` block containing `window.FinancialEngine` and UI controller / event bindings.
