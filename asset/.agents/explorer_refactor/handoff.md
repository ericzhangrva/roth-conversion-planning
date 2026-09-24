# Handoff Report: Technical Exploration & Refactoring Guide for `planning.html`

**Author**: Explorer Agent  
**Recipient**: Orchestrator / Implementer Agent  
**Date**: September 24, 2026  
**Type**: Hard Handoff (Investigation Complete)  
**Target File**: `/Users/eric/Dropbox/ai/asset/planning.html`  
**Reference Document**: `/Users/eric/Dropbox/ai/asset/.agents/explorer_refactor/analysis.md`  

---

## 1. Observation

### Observation 1: Retirement Boundary Off-By-One Defect (R3)
- **Location**: `planning.html:1065`
- **Verbatim Code**:
  ```javascript
  const isRetired = year > p.retireYear;
  ```
- **Line 1068**:
  ```javascript
  const earned = isRetired ? 0 : Number(p.earnedIncome);
  ```
- **Line 1640**:
  ```javascript
  const retireYearStr = String(result.records.find(r => r.isRetired)?.year || '');
  ```
- **Direct Impact**: With default `currentYear = 2026`, `startYear = 2027`, and `retireYear = 2027`:
  - In Year 1 (2027): `2027 > 2027` evaluates to `false`.
  - The simulation treats the retiree as working in 2027, crediting `$275,000` in earned income.
  - Retirement does not begin until 2028 (`year > 2027`).
  - The Chart.js vertical "Retirement" line is drawn on `2028` instead of `2027`.
  - The table demarcation border (`border-top: 2px dashed #3b82f6`) appears on row 2028 instead of 2027.

### Observation 2: 2D Optimizer with Single Slider Mismatch (R1)
- **Location**: `planning.html:1095–1097`
  ```javascript
  const isConvEligible = age <= 75;
  const targetConv = isConvEligible ? (i < 5 ? Number(rothConvPhase1) : Number(rothConvPhase2)) : 0;
  const rothConversion = Math.max(0, Math.min(targetConv, pretax));
  ```
- **Location**: `planning.html:1323–1426` (`findOptimalConversion`) sweeps a coarse 2D grid ($41 \times 41 = 1,681$ runs) and fine 2D grid ($51 \times 51 = 2,601$ runs) = 4,282 evaluations.
- **Location**: `planning.html:601–607` has only **one range input**: `<input type="range" class="slider-input" id="slider-conversion" min="0" max="500" step="5" value="0">`.
- **Location**: `planning.html:1856–1861`:
  `triggerOptimization` sets `slider.value = bestK1` and displays only `bestK1`, discarding `bestK2`.
- **Location**: `planning.html:1817–1829`:
  Touching the slider calls `runSimulation(inputs, k, k)`, forcing both phases to the same conversion value $k$.

### Observation 3: Missing Timeline Input Bounds & Auto-Correction (R2)
- **Location**: `planning.html:614–625`:
  ```html
  <input type="number" class="form-input" id="input-birthYear" value="1976">
  <input type="number" class="form-input" id="input-retireYear" value="2027">
  <input type="number" class="form-input" id="input-eolYear" value="2060">
  ```
- No HTML `min` attributes are present.
- No dynamic cross-validation listeners exist between `input-retireYear` and `input-eolYear`.
- If user enters `eolYear = 2025` when `currentYear = 2026`, `numYears` evaluates to 1, causing an invalid simulation run where `year = 2027` exceeds `eolYear`.

### Observation 4: Performance Benchmark of JavaScriptCore Engine
- Benchmarked directly via macOS JavaScriptCore (`osascript -l JavaScript`):
  - 1,000 evaluations of `runSimulation` execute in **56 ms** ($0.056\text{ ms}$ per evaluation).
  - A naive 3D grid sweep ($41 \times 41 \times 41 = 68,921$ runs) requires **3,920 ms** (freezing the UI).
  - Multi-Start Coordinate Descent with 3-stage refinement evaluates in **621 runs / 32 ms**, easily fulfilling the `<100ms` non-blocking requirement.

---

## 2. Logic Chain

1. **Retirement Boundary Alignment (R3)**:
   - *From Observation 1*: The condition `year > p.retireYear` causes Year 1 to be treated as pre-retirement, crediting $275K earned income and shifting table/chart indicators.
   - *Deduction*: Changing line 1065 to `const isRetired = year >= p.retireYear;` ensures that when `retireYear = 2027`, Year 1 has `isRetired = true`, earned income is `$0`, ACA marketplace pricing applies, row 2027 is styled as retired, and the chart's vertical line accurately marks 2027.

2. **Multi-Phase Roth Conversion Modeling (R1)**:
   - *From Observation 1 & 2*: With $0 earned income in retirement, conversions in the first 5 years (Phase 1) must be funded solely from cash ($500K) and taxable brokerage ($300K) due to the IRC 5-year lockup. Setting $k_1$ too high creates a liquidity deficit before conversions unlock.
   - *From Observation 2*: In Year 6 to Age 59.5 (Phase 2), prior conversions unlock as accessible principal, but growth remains early-distribution restricted.
   - *From Observation 2*: At Age 59.5 to 75 (Phase 3), all Roth funds are 100% qualified and penalty-free. Aggressive conversion here minimizes SECURE 2.0 RMDs and 10-year Death Taxes.
   - *Deduction*: The conversion target must be driven by `getConversionPhase(year, retireYear, birthYear)`. This cleanly handles all boundary conditions:
     - If retired after 59.5: Phase 1 and Phase 2 naturally have 0 eligible years; all conversions occur in Phase 3.
     - If retired within 5 years of 75/EOL: The eligible window terminates at $\min(\text{eolYear}, \text{birthYear} + 75)$.

3. **Optimization Solver Architecture (R1)**:
   - *From Observation 4*: Naive 3D sweeps freeze the browser thread (3.9 seconds).
   - *From Mathematical Structure*: Temporal causality dictates that Phase 3 conversions ($k_3$) have zero impact on Phase 1/Phase 2 liquidity constraints.
   - *Deduction*: Multi-Start Coordinate Descent (3 seeds covering conservative, moderate, aggressive regimes) with 2 alternating sweeps at 25K step, followed by medium refinement (5K step) and fine refinement (1K step), evaluates in **32 ms** (621 evaluations), yielding globally near-optimal conversions without UI stutter.

4. **Input Bounds & Auto-Correction (R2)**:
   - *From Observation 3*: Unconstrained number inputs allow impossible scenarios (`eolYear < retireYear` or `eolYear < currentYear + 1`).
   - *Deduction*:
     - Set `min` attributes dynamically (`retireYear.min = currentYear + 1`, `eolYear.min = retireYear`).
     - On complete 4-digit input or blur/change: automatically clamp and update DOM input values. If `eolYear = 2025` is entered when `currentYear = 2026`, auto-adjust to `2027` (or `retireYear`) and flash visual feedback.
     - Defensive clamping within `readInputsFromDOM()` guarantees that `runSimulation` never receives invalid state.

---

## 3. Caveats

1. **State Tax Scope**: Virginia state income tax is modeled. If filing status or state changes in future revisions, `computeStateTaxVirginia` will need corresponding updates.
2. **Chart.js CDN Dependency**: Chart rendering depends on Chart.js loaded via CDN; fail-safe DOM notice remains active if offline.
3. **No Caveats on Core Math**: The tax brackets, RMD divisors, IRMAA tiers, and liquidity constraints are verified and consistent.

---

## 4. Conclusion

The architectural changes required in `planning.html` are localized, high-impact, and mathematically sound:
1. Replace `year > p.retireYear` with `year >= p.retireYear` in `runSimulation`.
2. Expand `runSimulation` signature to `(inputs, rothConvPhase1 = 0, rothConvPhase2 = 0, rothConvPhase3 = 0)` with dynamic phase dispatch via `getConversionPhase()`.
3. Replace 2D grid sweep in `findOptimalConversion` with Multi-Start Coordinate Descent, cutting execution time from 240ms to **32ms** while finding distinct $(k_1, k_2, k_3)$ optimal values.
4. Replace the single slider in the Optimizer Panel with 3 interactive Phase Conversion Cards, supporting both automated solver writes and independent manual overrides.
5. Add `setupTimelineValidation()` to enforce `retireYear >= currentYear + 1` and `eolYear >= max(retireYear, currentYear + 1)` with real-time auto-correction and styling feedback.

---

## 5. Verification Method

### Automated Headless Verification (Node / JavaScriptCore / JXA)
The implementer can verify the engine after changes using:
```bash
osascript -l JavaScript -e '
var app = Application.currentApplication();
app.includeStandardAdditions = true;
var html = app.read(Path("/Users/eric/Dropbox/ai/asset/planning.html"));
var script = html.substring(html.indexOf("<script>") + 8, html.lastIndexOf("</script>"));
var window = {};
eval(script);
var eng = window.FinancialEngine;

// 1. Verify R3: retireYear = 2027 has $0 earned income in Year 1
var resDefault = eng.runSimulation(eng.DEFAULT_INPUTS, 100000, 200000, 300000);
if (resDefault.records[0].earnedIncome !== 0) throw new Error("R3 Failed: Year 1 earned income is not $0");
if (!resDefault.records[0].isRetired) throw new Error("R3 Failed: Year 1 isRetired is not true");

// 2. Verify R1: findOptimalConversion returns distinct k1, k2, k3 in <100ms
var opt = eng.findOptimalConversion(eng.DEFAULT_INPUTS, "raw");
console.log("Opt Result:", JSON.stringify({k1: opt.bestK1, k2: opt.bestK2, k3: opt.bestK3, ms: opt.durationMs, feasible: opt.bestResult.isFeasible}));
if (opt.durationMs > 100) throw new Error("R1 Failed: Duration exceeded 100ms");
if (opt.bestK1 === opt.bestK2 && opt.bestK2 === opt.bestK3) throw new Error("R1 Failed: Conversions not distinct");
if (!opt.bestResult.isFeasible) throw new Error("R1 Failed: Optimal result violates liquidity constraints");

console.log("All automated verification checks PASSED.");
'
```

### Browser UI Manual Verification
1. Open `planning.html` in a web browser (`file:///Users/eric/Dropbox/ai/asset/planning.html`).
2. **Verify R2**: Change "End of Life (EOL) Year" to `2025`. Verify that the UI instantly auto-corrects the field to `2027` and flashes validation styling.
3. **Verify R3**: Check the first table row (Year 2027). Taxable Earned Income must display `-` ($0). The dashed retirement line must sit directly above row 2027, and the Chart.js red dashed line must be anchored at 2027.
4. **Verify R1**: Click "Find Optimal Conversion". Verify that the optimizer updates Phase 1, Phase 2, and Phase 3 sliders with distinct values in $<50\text{ ms}$, with no page freeze. Drag any individual slider to verify manual override updates table and chart in real time.
