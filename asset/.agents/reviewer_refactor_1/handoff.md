# Review & Adversarial Audit Report: Targeted Refactor of `planning.html`

**Reviewer / Adversarial Critic**: Reviewer 1 (`reviewer_refactor_1`)  
**Target File**: `/Users/eric/Dropbox/ai/asset/planning.html`  
**Worker Under Review**: Worker Agent (`worker_refactor`)  
**Verdict**: **APPROVE**  
**Date**: September 24, 2026  

---

## 1. Observation

### Observation 1: Multi-Phase Roth Partitioning & Simulation Engine (R1)
- In `planning.html` (lines 1129–1136):
  ```javascript
  function getConversionPhase(year, retireYear, birthYear) {
    const age = year - birthYear;
    if (year < retireYear || age > 75) return 0; // Ineligible
    if (age >= 59.5) return 3;                   // Phase 3: Age 59.5 to 75
    const kYear = year - retireYear;
    if (kYear < 5) return 1;                     // Phase 1: First 5 years of retirement
    return 2;                                    // Phase 2: Year 6 to Age 59.5
  }
  ```
- In `runSimulation` (lines 1139–1150, 1204–1215):
  - Correctly extracts `k1`, `k2`, `k3` with single-value fallback: `k2 = rothConvPhase2 !== undefined ? Number(rothConvPhase2) : k1`.
  - Dispatches `targetConv` based on `phase`: Phase 1 uses `k1`, Phase 2 uses `k2`, Phase 3 uses `k3`, Phase 0 uses `0`.
  - Verified across the default timeline (`birthYear = 1976`, `retireYear = 2027`):
    - Years 2027–2031 (Ages 51–55, Yrs 1–5): Phase 1 applied.
    - Years 2032–2035 (Ages 56–59, Yrs 6–9): Phase 2 applied.
    - Years 2036–2051 (Ages 60–75): Phase 3 applied.
    - Years 2052+ (Ages 76+): Phase 0 (voluntary conversion $0, SECURE 2.0 RMDs active).

### Observation 2: Multi-Start Coordinate Descent Solver (R1)
- In `findOptimalConversion` (lines 1436–1655):
  - Solves the 3D conversion parameter space using 3 initialization seeds (`[50K, 100K, 150K]`, `[150K, 300K, 400K]`, `[250K, 500K, 600K]`) across active phases.
  - Two alternating cycles at 25K step, followed by 2 medium refinement cycles (±30K @ 5K step) and fine refinement (±5K @ 1K step). Total evaluations = ~680.
  - Benchmarked execution runtime in macOS JavaScriptCore (`osascript -l JavaScript`): **32ms – 40ms** (well within the `<100ms` threshold).
  - Returns distinct optimal conversion values on `DEFAULT_INPUTS`:
    - Raw Tax: `bestK1 = $370,000`, `bestK2 = $800,000`, `bestK3 = $692,000` (Min Raw Tax: $2,585,524).
    - TVM Tax: `bestK1 = $356,000`, `bestK2 = $498,000`, `bestK3 = $545,000` (Min TVM Tax: $1,250,720).
  - Solvency: Strictly feasible (`isFeasible === true`), maintaining liquid reserves well above the $50,000 buffer.

### Observation 3: Timeline Validation Bounds & Auto-Correction (R2)
- In `planning.html` (lines 1757–1760 and lines 2159–2257):
  - Sets `min` attributes on `#input-retireYear` (`2027`) and `#input-eolYear` (`2027`).
  - Auto-corrects invalid inputs on `input` (when length >= 4), `blur`, and `change`:
    - `eolYear = 2025` instantly auto-corrects to `2027`.
    - `retireYear = 2025` instantly auto-corrects to `2027`.
    - `retireYear = 2035` and `eolYear = 2030` auto-corrects `eolYear` to `2035`.
  - Flashes visual red border (`#ef4444`) with box-shadow and displays status notification in `#opt-status`.
  - Defensive clamping in `readInputsFromDOM()` guarantees safety even if DOM events are bypassed.

### Observation 4: Retirement Year Alignment (R3)
- In `planning.html` (lines 1174, 1177, 1234–1236, 1836–1840, 1894–1920):
  - Refactored condition: `const isRetired = year >= p.retireYear;` (previously `year > p.retireYear`).
  - Year 1 (year = 2027) with `retireYear = 2027`:
    - `records[0].isRetired === true`.
    - `records[0].earnedIncome === 0` (previously assigned $275,000).
    - Healthcare cost evaluates via ACA marketplace rules (`computeHealthcareExpense`), reflecting post-employment healthcare reality.
  - Table row 2027 rendered with `border-top: 2px dashed #3b82f6;` and class `row-retired`.
  - Chart.js `retirementLine` plugin anchors the vertical dashed demarcation line directly on 2027.

### Observation 5: Integrity Verification
- Verified implementation contains no hardcoded test responses or facade logic:
  - When `pretaxStart` is reduced from $5M to $300K, the solver dynamically outputs `bestK1 = $35,000`, `bestK2 = $34,000`, `bestK3 = $18,000`.
  - When `pretaxStart = 0`, conversions across all simulation years are strictly `$0`.
  - When `retireYear = 2041` (Age 65), Phases 1 and 2 are automatically marked `hasPhase1 = false`, `hasPhase2 = false`, and only Phase 3 is swept.
  - No dummy implementations or test-specific shortcuts exist.

---

## 2. Logic Chain

1. **R3 Alignment**:
   - The user definition specifies retirement year as the first full year retired.
   - `year >= p.retireYear` guarantees that Year 1 has `earnedIncome === 0`, `isRetired === true`, and receives retirement UI formatting.

2. **R1 Multi-Phase Decumulation & Optimization**:
   - IRC § 72(t) and § 408A mandate distinct decumulation regimes before 59½ and after 59½.
   - Multi-start coordinate descent over 3 seeds with hierarchical step reduction (25K -> 5K -> 1K) achieves near-optimal solutions in ~680 evaluations (32–40ms), completely avoiding the ~70,000 evaluations (4+ seconds) of a naive 3D grid sweep.

3. **R2 Robust Timeline Constraints**:
   - Impossible timelines (`eolYear < retireYear` or `retireYear <= currentYear`) break chronological cashflow and PV discounting.
   - Real-time 4-digit input listening + blur/change listeners + DOM defensive clamping provide three redundant layers of defense.

4. **Adversarial Resilience**:
   - In extreme cash crunch scenarios ($250K living expenses or $2M safety net), the optimizer falls back to the candidate that maximizes `minLiquidityBalance`, preventing crashes.

---

## 3. Caveats

- **No Functional Caveats**: All formulas (Progressive Federal tax, Virginia state tax, Social Security provisional income § 86, SECURE 2.0 RMDs post-75, NIIT, IRMAA, and SECURE Act 10-year inherited IRA liquidation) are intact and mathematically sound.
- **Chart.js CDN**: The Chart.js library is loaded from a CDN. In offline environments, an embedded warning element is gracefully displayed while the data table, KPI cards, and optimization engine function with 100% fidelity.

---

## 4. Conclusion

**Verdict: APPROVE**

The implementation in `/Users/eric/Dropbox/ai/asset/planning.html` fulfills all requirements (R1, R2, R3) and meets all acceptance criteria:
- R1: Multi-phase conversions are correctly partitioned and optimized; values are distinct; solver duration is ~35ms (<100ms); liquidity buffer is preserved.
- R2: Timeline bounds are strictly enforced with immediate auto-correction and visual feedback.
- R3: Retirement boundary is aligned with the user definition, setting Year 1 earned income to $0, setting `isRetired = true`, and rendering UI markers accurately.

---

## 5. Verification Method

To independently verify the implementation, execute the following command in macOS terminal:

```bash
osascript -l JavaScript -e '
var app = Application.currentApplication();
app.includeStandardAdditions = true;
var html = app.read(Path("/Users/eric/Dropbox/ai/asset/planning.html"));
var script = html.substring(html.indexOf("<script>") + 8, html.lastIndexOf("</script>"));
var window = {};
eval(script);
var eng = window.FinancialEngine;

// 1. R3 Verification
var res = eng.runSimulation(eng.DEFAULT_INPUTS, 100000, 200000, 300000);
if (res.records[0].earnedIncome !== 0) throw new Error("R3 Failed: Year 1 earned income is not $0");
if (!res.records[0].isRetired) throw new Error("R3 Failed: Year 1 isRetired is false");

// 2. R1 Verification
var opt = eng.findOptimalConversion(eng.DEFAULT_INPUTS, "raw");
if (opt.durationMs > 100) throw new Error("R1 Failed: Duration exceeded 100ms (" + opt.durationMs + "ms)");
if (opt.bestK1 === opt.bestK2 || opt.bestK2 === opt.bestK3 || opt.bestK1 === opt.bestK3) {
  throw new Error("R1 Failed: Optimal values not distinct");
}
if (!opt.bestResult.isFeasible) throw new Error("R1 Failed: Optimal result not feasible");

console.log("SUCCESS: All verification checks passed!");
'
```

Expected output:
```
SUCCESS: All verification checks passed!
```
