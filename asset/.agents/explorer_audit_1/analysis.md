# Exhaustive Technical & Financial Audit: `planning.html`

**Target File**: `/Users/eric/Dropbox/ai/asset/planning.html` (1,841 lines, 69,447 bytes)  
**Authoritative Reference**: `/Users/eric/Dropbox/ai/asset/.agents/ORIGINAL_REQUEST.md`  
**Auditor**: Explorer Agent (`explorer_audit_1`)  
**Date**: 2026-09-24  
**Integrity Mode**: Read-Only Code Investigation  

---

## 1. Executive Technical Summary

An exhaustive line-by-line static analysis and financial engineering audit of `/Users/eric/Dropbox/ai/asset/planning.html` reveals significant structural blind spots, mathematical anomalies, unrealistic economic assumptions, and critical missing tax mechanics.

While the application features an attractive UI and functional single-file architecture with zero external build dependencies, its simulation engine contains severe financial flaws that invalidate long-term tax optimization results for high-net-worth retirees:

1. **Brokerage Returns Untaxed (Tax Haven Brokerage)**: Taxable brokerage investments ($300k starting, 9% annual return) generate zero annual tax on dividends/growth, and zero capital gains tax when liquidated to fund deficits.
2. **College Expense 400% Multiplication Anomaly**: College expenses use `[0.5, 1.0, 1.0, 1.0, 0.5]` instead of `[0.125, 0.25, 0.25, 0.25, 0.125]`, extracting **$400,000** instead of the specified **$100,000** total expense.
3. **Complete Absence of RMDs (SECURE 2.0 Act)**: Pre-tax retirement accounts cease conversions at age 75 and then compound at 9% tax-free until age 84 without forcing IRS Required Minimum Distributions.
4. **Medicare & IRMAA Omission**: At age 65, healthcare costs do not drop to zero or reflect Medicare Part B/D + IRMAA cliff surcharges; instead, the code charges an inflated $5,000/yr subsidized ACA premium into extreme old age.
5. **Net Investment Income Tax (NIIT, IRC § 1411) Missing**: High earners and high-conversion years never trigger the 3.8% NIIT on investment income.
6. **Flawed Roth 5-Year Lockup Past Age 59½**: The 5-year conversion lockup is enforced through age 84, violating IRC § 408A(d) rules where qualified distributions post-59½ are penalty-free and tax-free. Furthermore, Roth earnings are permanently inaccessible during liquidity deficits.
7. **Earned Income Dead-Zone in Year 1**: The UI's $275,000 earned income input is completely ignored in default runs because retirement is set to 2027 and the simulation starts in 2027.
8. **UI/Code Default Inconsistencies & Phantom Slider**: Defaults in JavaScript (`DEFAULT_INPUTS`) contradict DOM input defaults for Cash, Yield, and Roth balances. A slider (`#slider-conversion`) is referenced in JavaScript and styled in CSS but completely omitted from the HTML DOM.

---

## 2. Architecture & Code Structure Mapping

The single-file document spans 1,841 lines divided into three primary functional layers:

### 2.1 File Topology
- **Lines 1–8**: HTML Document setup and Chart.js 4.4.2 UMD CDN inclusion (`https://cdn.jsdelivr.net/npm/chart.js@4.4.2/dist/chart.umd.min.js`).
- **Lines 9–513**: Embedded CSS styling (dark-mode palette, responsive KPI grid, sidebar panels, data table sticky headers, custom tooltips).
- **Lines 514–789**: Semantic HTML DOM Layout:
  - Header with Export to PDF and Export to JPG actions (Lines 518–527).
  - 8 Summary KPI Cards (Lines 530–571): EOL Cash, EOL Brokerage, EOL Pre-tax, EOL Roth, Lifetime Raw Tax, Lifetime PV Tax, Lifetime FV Tax, Inherited Death Tax.
  - Sidebar Controls (Lines 576–719): Optimization Radio buttons (`raw` vs `tvm`), Action Buttons (`#btn-optimize`, `#btn-reset`), Input Forms (Timeline, Assets, Incomes, Expenses).
  - Main Visuals (Lines 722–789): Chart canvas (`#chart-canvas`) and 18-column Year-by-Year Simulation Table (`#table-simulation-body`).
- **Lines 791–1838**: Embedded Vanilla JavaScript Engine (UMD exportable).

### 2.2 Global State & Function Inventory

| Function / Object | Line Range | Parameters / Signatures | Core Responsibility |
| :--- | :--- | :--- | :--- |
| `SafeStorage` | Lines 800–828 | `getItem(key)`, `setItem(key, val)`, `removeItem(key)` | Wrap `localStorage` with in-memory fallback to avoid `file:///` `SecurityError` |
| `DEFAULT_INPUTS` | Lines 831–856 | Object dictionary | Baseline configuration fallback values |
| Tax Constants | Lines 858–884 | Constants (`BASE_STD_DEDUCTION_*`, `BASE_FED_BRACKETS_*`, `COLLEGE_DISTRIBUTION`) | Statutory tax thresholds and college disbursement factors |
| `computeFederalTax` | Lines 887–904 | `(taxableIncome, inflationFactor = 1.0, filingStatus = 'MFJ')` | Iterates 7-tier federal tax bracket ladder indexed by inflation |
| `computeStateTax` | Lines 907–912 | `(income, inflationFactor = 1.0, stateTaxRate = 0.0575, filingStatus = 'MFJ')` | Computes flat state income tax on income exceeding inflated standard deduction |
| `computeTaxableSS` | Lines 915–926 | `(ssAmount, otherIncome)` | Calculates taxable Social Security benefits under IRC § 86 provisional income tiers |
| `computeCollegeExpense` | Lines 929–935 | `(year, collegeStartYear, collegeTotal)` | Schedules 5-year college distributions based on `COLLEGE_DISTRIBUTION` |
| `computeHealthcareExpense` | Lines 938–944 | `(age, magi, yearIndex, inflationRate, healthSubsidized, healthUnsubsidized, isRetired, magiCliff = 90000)` | Calculates pre-Medicare ACA subsidy cliff costs and post-65 expenses |
| `computeDeathTax` | Lines 947–976 | `(pretaxBalanceEOL, eolYear, birthYear, inflationRate, stateTaxRate)` | Calculates SECURE Act 10-year inherited IRA liquidation marginal tax for 2 heirs |
| `runSimulation` | Lines 979–1210 | `(inputs, rothConvPhase1 = 0, rothConvPhase2 = 0)` | Core decumulation simulation engine (year-by-year cash flow, tax, and asset waterfall) |
| `findOptimalConversion` | Lines 1213–1317 | `(inputs, objective = 'raw')` | 2D coarse-to-fine parameter sweep over Phase 1 and Phase 2 Roth conversion amounts |
| `DOM_ID_ALIASES` | Lines 1320–1363 | Object dictionary | Compatibility mapping for camelCase vs kebab-case element identifiers |
| `fmtCurrency` | Lines 1376–1380 | `(n)` | Formats raw numeric dollars into thousands ($K) with hyphen for zero |
| `fmtCompact` | Lines 1382–1388 | `(n)` | Formats large dollar balances into compact notation ($M, $K) |
| `readInputsFromDOM` | Lines 1393–1428 | None | Extracts and parses all numeric form inputs from the DOM into a standardized parameter object |
| `renderSimulationToDOM`| Lines 1430–1505 | `(result, currentConversion)` | Updates KPI cards, renders all HTML table rows, and calls `renderChart` |
| `renderChart` | Lines 1507–1680 | `(result)` | Renders or updates Chart.js stacked bar (assets) and line (cumulative tax) chart |
| `exportToJPG` | Lines 1683–1704 | None | Dynamically loads `html2canvas` CDN and downloads raster dashboard screenshot |
| `triggerSimulation` | Lines 1706–1709 | None | Invokes `triggerOptimization()` |
| `triggerOptimization` | Lines 1711–1737 | None | Reads DOM, runs `findOptimalConversion`, updates status text, renders to DOM |
| Event Listeners Setup | Lines 1740–1796 | `DOMContentLoaded` handler | Attaches `input`, `click`, and `change` handlers across inputs and triggers initial optimization |
| `FinancialEngine` UMD | Lines 1800–1837 | Export object | Exposes public API to `module.exports` (Node.js/JSC) and `window.FinancialEngine` |

---

## 3. Deep Code-Level Financial Audit by Module

### Module A: Progressive Federal & State Tax Brackets & Inflation Indexation

#### Code Citations
- Lines 864–882:
  ```javascript
  const BASE_FED_BRACKETS_MFJ = [
    { max: 23850, rate: 0.10 },
    { max: 96950, rate: 0.12 },
    { max: 206700, rate: 0.22 },
    { max: 394600, rate: 0.24 },
    { max: 501050, rate: 0.32 },
    { max: 751600, rate: 0.35 },
    { max: Infinity, rate: 0.37 }
  ];
  ```
- Lines 887–904:
  ```javascript
  function computeFederalTax(taxableIncome, inflationFactor = 1.0, filingStatus = 'MFJ') {
    if (taxableIncome <= 0) return 0;
    const brackets = filingStatus === 'Single' ? BASE_FED_BRACKETS_SINGLE : BASE_FED_BRACKETS_MFJ;
    let tax = 0;
    let prevThreshold = 0;
    for (let i = 0; i < brackets.length; i++) {
      const b = brackets[i];
      const threshold = b.max === Infinity ? Infinity : b.max * inflationFactor;
      if (taxableIncome > threshold) {
        tax += (threshold - prevThreshold) * b.rate;
        prevThreshold = threshold;
      } else {
        tax += (taxableIncome - prevThreshold) * b.rate;
        break;
      }
    }
    return tax;
  }
  ```
- Lines 907–912:
  ```javascript
  function computeStateTax(income, inflationFactor = 1.0, stateTaxRate = 0.0575, filingStatus = 'MFJ') {
    if (income <= 0 || stateTaxRate <= 0) return 0;
    const stateStd = (filingStatus === 'Single' ? BASE_STATE_STD_DEDUCTION_SINGLE : BASE_STATE_STD_DEDUCTION_MFJ) * inflationFactor;
    const taxable = Math.max(0, income - stateStd);
    return taxable * stateTaxRate;
  }
  ```
- Lines 1005, 1027–1036:
  ```javascript
  const inflationFactor = Math.pow(1 + p.inflationRate, i);
  ...
  const otherIncome = earned + cashInterest + rothConversion;
  const taxableSS = computeTaxableSS(ssBenefit, otherIncome);
  const agi = otherIncome + taxableSS;

  const fedStd = BASE_STD_DEDUCTION_MFJ * inflationFactor;
  const taxableFed = Math.max(0, agi - fedStd);
  const fedTax = computeFederalTax(taxableFed, inflationFactor, 'MFJ');
  const stateTax = computeStateTax(agi, inflationFactor, Number(p.stateTaxRate), 'MFJ');
  const totalTaxYear = fedTax + stateTax;
  ```

#### Detailed Code Findings & Flaws
1. **Mathematical Indexation**:
   - `inflationFactor = Math.pow(1 + p.inflationRate, i)` where `i = year - startYear`.
   - The bracket thresholds `threshold = b.max * inflationFactor` and standard deduction `fedStd = BASE_STD_DEDUCTION_MFJ * inflationFactor` correctly compound geometrically at 3.5% per annum.
2. **Missing TCJA Sunset Mechanics**:
   - The code uses 2024/2025 Tax Cuts and Jobs Act (TCJA) brackets (10%, 12%, 22%, 24%, 32%, 35%, 37%) and standard deductions ($30,000 MFJ) for all years from 2027 to 2060.
   - Under current federal statute, the TCJA individual provisions expire on December 31, 2025. Without congressional extension, tax rates revert in 2026+ to 10%, 15%, 25%, 28%, 33%, 35%, and 39.6%, and standard deductions decrease by roughly 50%. The simulation does not provide a toggle or model for the scheduled statutory reversion.
3. **Missing Senior Additional Standard Deduction (IRC § 63(f))**:
   - For individuals aged 65 and older, IRS tax law provides an additional standard deduction ($1,550 per spouse for MFJ, $1,950 for Single in 2024, indexed for inflation).
   - `planning.html` maintains a flat base standard deduction of $30,000 inflated, ignoring the extra deduction available to retirees from age 65 to 84.
4. **State Tax Inaccuracy (Virginia 5.75%)**:
   - In Line 1034, `computeStateTax` receives `agi`, which contains `taxableSS` (taxable Social Security). Under Virginia law (Va. Code Ann. § 58.1-322.02(1)), Social Security benefits are 100% exempt from Virginia state income tax. Passing federal AGI directly into state tax calculation improperly taxes Social Security at 5.75%.
   - In Virginia, standard deductions are set by statute ($8,000 for MFJ) and are *not* automatically indexed for inflation every year, whereas the simulation inflates a baseline $6,000 deduction at 3.5% annually.
   - Virginia tax brackets are progressive (2%, 3%, 5%, and 5.75% on income over $17,000), but `planning.html` treats state tax as a flat 5.75% above standard deduction.

---

### Module B: Taxable Income & Brokerage Modeling (Capital Gains & Cost Basis)

#### Code Citations
- Lines 1009–1010:
  ```javascript
  const earned = isRetired ? 0 : Number(p.earnedIncome);
  const cashInterest = cash > 0 ? cash * Number(p.cashInterestRate) : 0;
  ```
- Lines 1027–1029:
  ```javascript
  const otherIncome = earned + cashInterest + rothConversion;
  const taxableSS = computeTaxableSS(ssBenefit, otherIncome);
  const agi = otherIncome + taxableSS;
  ```
- Lines 1063, 1075–1078:
  ```javascript
  if (netCashDeficit <= 0) {
    cash = cash + (-netCashDeficit);
    inv = inv * (1 + Number(p.invReturnRate));
    pretax = (pretax - rothConversion) * (1 + Number(p.invReturnRate));
    roth = (roth + rothConversion) * (1 + Number(p.invReturnRate));
  } else {
    ...
    // 2. Drawdown Taxable Investment
    const invWithGrowth = inv * (1 + Number(p.invReturnRate));
    const drawInv = Math.min(invWithGrowth, remDeficit);
    inv = invWithGrowth - drawInv;
    remDeficit -= drawInv;
  ```
- Line 1156 & Lines 1477, 1485:
  ```javascript
  // Line 1156 in runSimulation records:
  invReturn: inv * Number(p.invReturnRate),

  // Line 1477 in renderSimulationToDOM:
  const totalIncome = r.earnedIncome + r.ssBenefit + r.cashInterest + r.invReturn + r.rothConversion;
  ```

#### Critical Structural Blind Spot
1. **Total Omission of Brokerage Return from Taxable Income**:
   - Look at line 1027: `otherIncome = earned + cashInterest + rothConversion;`.
   - `invReturn` ($300,000 growing at 9% = $27,000+ per year) is **100% excluded from `agi` and `taxableFed`**!
   - In the UI table (line 1477), `invReturn` is displayed under "Investment Return ($K)" and added to "Total Income ($K)", giving the user the false visual illusion that investment income is accounted for. But in the actual tax engine (line 1027), it is never taxed!
2. **Zero Cost Basis Tracking & Zero Capital Gains Tax on Liquidation**:
   - In line 1076, when cash deficits force a liquidation of taxable brokerage assets (`drawInv`), the entire liquidation occurs with **$0 in taxes**.
   - The engine tracks no `costBasis`.
   - In real-world finance:
     - Realized capital gains = $\text{drawInv} \times \left(1 - \frac{\text{costBasis}}{\text{invWithGrowth}}\right)$.
     - These capital gains are taxed under preferential long-term capital gains brackets (0%, 15%, 20%), plus state tax (5.75%), plus NIIT (3.8%).
     - In `planning.html`, taxable brokerage assets function as an offshore tax haven: gains grow completely untaxed, dividends are untaxed, and liquidations are untaxed!

---

### Module C: Healthcare Subsidy Cliff & Medicare (ACA & IRMAA)

#### Code Citations
- Lines 938–944:
  ```javascript
  // Healthcare Expense & ACA Subsidy Cliff Step Function Calculator
  function computeHealthcareExpense(age, magi, yearIndex, inflationRate, healthSubsidized, healthUnsubsidized, isRetired, magiCliff = 90000) {
    const inflationFactor = Math.pow(1 + inflationRate, yearIndex);
    if (!isRetired || age >= 65) return healthSubsidized * inflationFactor;
    const inflatedCliff = magiCliff * inflationFactor;
    const baseCost = (magi <= inflatedCliff) ? healthSubsidized : healthUnsubsidized;
    return baseCost * inflationFactor;
  }
  ```
- Line 1039:
  ```javascript
  const healthExp = computeHealthcareExpense(age, agi, i, Number(p.inflationRate), Number(p.healthSubsidized), Number(p.healthUnsubsidized), isRetired, Number(p.magiCliff || 90000));
  ```

#### Detailed Code Findings & Flaws
1. **Violation of Acceptance Criteria at Age 65**:
   - Acceptance Criteria (ORIGINAL_REQUEST.md line 54) states: *"Healthcare expenses must drop off at Age 65."*
   - And line 30 states: *"At age 65 (Medicare), health insurance cost drops to $0 (or a negligible estimated default)."*
   - What does `planning.html` do at line 940?
     ```javascript
     if (!isRetired || age >= 65) return healthSubsidized * inflationFactor;
     ```
     At age 65+, the function returns `healthSubsidized * inflationFactor`!
     With `healthSubsidized = 5000` and 3.5% inflation over 30 years, retirees age 65 to 84 are charged **$10,000 to $16,000+ per year** in ACA health insurance instead of $0!
2. **Arbitrary $90,000 Hard Cliff vs Statutory ACA Mechanics**:
   - The simulation hardcodes `magiCliff = 90000` (inflated annually).
   - Under real ACA rules (IRC § 36B), prior to the American Rescue Plan Act (ARPA) and Inflation Reduction Act (IRA), the subsidy cliff was tied to 400% of the Federal Poverty Level (FPL) based on household size (for 2 people in 2024: ~$81,760; for 4 people: ~$124,800).
   - Under post-ARPA / IRA rules, the hard cliff was replaced with an 8.5% of household income cap for the benchmark Silver plan.
3. **Flawed ACA MAGI Definition**:
   - The simulation passes `agi` (`otherIncome + taxableSS`) as `magi`.
   - ACA MAGI under IRC § 36B(d)(2)(B) specifically requires adding back *non-taxable* Social Security benefits and tax-exempt interest:
     $$\text{MAGI}_{\text{ACA}} = \text{AGI} + \text{TaxExemptInterest} + \text{NonTaxableSS}$$
   - By omitting non-taxable Social Security, the engine understates MAGI when testing against the subsidy cliff.
4. **Complete Absence of Medicare IRMAA Surcharges**:
   - Medicare Part B and Part D premiums are subject to Income-Related Monthly Adjustment Amounts (IRMAA) based on MAGI from 2 years prior ($t-2$).
   - For high-net-worth retirees executing large Roth conversions ($100k–$300k+), IRMAA tiers (starting at $206,000 MFJ in 2024, scaling to $750,000+) impose sharp cliff penalties (adding up to $10,000–$14,000/yr in extra Medicare premiums for a couple).
   - `planning.html` completely omits IRMAA, failing to penalize conversion strategies that trigger severe Medicare surcharges.

---

### Module D: Roth IRA 5-Year Lockup Logic & Cash Flow Priority

#### Code Citations
- Lines 991–994:
  ```javascript
  // Vintage queue for Roth conversions: [{ year, principal, remaining }]
  const rothVintages = [];
  let accessibleOriginalPrincipal = Math.min(Number(p.rothPrincipalStart), roth);
  ```
- Lines 1021–1025:
  ```javascript
  // Add conversion to vintage queue (locked for 5 years)
  if (rothConversion > 0) {
    rothVintages.push({ year: year, principal: rothConversion, remaining: rothConversion });
  }
  ```
- Lines 1049–1056:
  ```javascript
  // Calculate accessible Roth principal prior to liquidation
  let accessibleVintages = 0;
  for (let v = 0; v < rothVintages.length; v++) {
    if ((year - rothVintages[v].year) >= 5) {
      accessibleVintages += rothVintages[v].remaining;
    }
  }
  const currentAccessibleRoth = accessibleOriginalPrincipal + accessibleVintages;
  ```
- Lines 1081–1100:
  ```javascript
  // 3. Drawdown Accessible Roth Principal
  let drawRoth = 0;
  if (remDeficit > 0) {
    drawRoth = Math.min(currentAccessibleRoth, remDeficit);
    remDeficit -= drawRoth;

    // Deplete accessible vintages (FIFO)
    let toDeduct = drawRoth;
    if (accessibleOriginalPrincipal > 0) {
      const deductOrig = Math.min(accessibleOriginalPrincipal, toDeduct);
      accessibleOriginalPrincipal -= deductOrig;
      toDeduct -= deductOrig;
    }
    for (let v = 0; v < rothVintages.length && toDeduct > 0; v++) {
      if ((year - rothVintages[v].year) >= 5 && rothVintages[v].remaining > 0) {
        const deductV = Math.min(rothVintages[v].remaining, toDeduct);
        rothVintages[v].remaining -= deductV;
        toDeduct -= deductV;
      }
    }
  }
  ```
- Lines 1106–1112:
  ```javascript
  const rothWithGrowth = (roth + rothConversion) * (1 + Number(p.invReturnRate));
  roth = Math.max(0, rothWithGrowth - drawRoth);

  if (remDeficit > 0.01) {
    isLiquidDeficit = true;
    isFeasible = false;
  }
  ```

#### Detailed Code Findings & Flaws
1. **IRS Roth Ordering Rules Misapplication Post-Age 59½**:
   - Under IRC § 408A(d) and Treas. Reg. § 1.408A-6, distributions from a Roth IRA follow strict ordering rules:
     1. Regular annual contributions (always tax-free and penalty-free).
     2. Conversion and rollover amounts on a FIFO basis.
     3. Earnings.
   - The 5-year holding rule for conversions (IRC § 72(t)(10)) imposes a 10% early withdrawal penalty **only on distributions prior to age 59½**!
   - Once a taxpayer reaches age 59½ and has held any Roth IRA for at least 5 taxable years, **all distributions from the Roth IRA (principal, conversions of any age, and earnings) are 100% qualified distributions — completely free of both income tax and the 10% penalty**!
   - In `planning.html`, the individual turns 59½ in 2035 (birth year 1976). Yet the simulation continues locking conversion principal behind a strict 5-year lockup through age 75 and beyond (lines 1051, 1118). A 74-year-old who converted funds at age 71 is treated by the engine as legally barred from spending their own principal to survive.
2. **Permanent Inaccessibility of Roth Earnings**:
   - Notice line 1083: `drawRoth = Math.min(currentAccessibleRoth, remDeficit);`.
   - `currentAccessibleRoth` tracks only `accessibleOriginalPrincipal` and `accessibleVintages` (principal).
   - Roth investment earnings (`rothWithGrowth - principal`) are **never added to accessible liquidity**.
   - As a result, even if the Roth account has grown to $5,000,000 of compounded earnings, if principal is exhausted and cash/brokerage is $0, line 1110 declares `isFeasible = false` and marks a fatal liquidity deficit! In reality, any post-59½ retiree can freely withdraw Roth earnings with zero taxes and zero penalties.

---

### Module E: Required Minimum Distributions (RMDs) & Post-75 Portfolio Growth

#### Code Citations
- Lines 1016–1020:
  ```javascript
  // Roth Conversion eligibility: startYear <= year <= birthYear + 75
  const isConvEligible = age <= 75;
  const targetConv = isConvEligible ? (i < 5 ? Number(rothConvPhase1) : Number(rothConvPhase2)) : 0;
  const rothConversion = Math.max(0, Math.min(targetConv, pretax));
  ```
- Lines 1064 & 1103:
  ```javascript
  pretax = (pretax - rothConversion) * (1 + Number(p.invReturnRate));
  ```

#### Critical Structural Blind Spot
1. **Complete Absence of Mandatory RMD Calculations**:
   - There is no function, variable, or calculation for RMDs in `planning.html`.
   - Under the SECURE 2.0 Act of 2022 (P.L. 117-328), the required beginning date for individuals born in 1960 or later (such as the 1976 birth year here) is **age 75**.
   - Starting at age 75, the retiree must take annual minimum distributions based on the IRS Uniform Lifetime Table (Table III):
     $$\text{RMD}_t = \frac{\text{PreTax Balance}_{t-1}}{\text{Distribution Period}(\text{Age}_t)}$$
     - Age 75 divisor: 24.6 (4.07%)
     - Age 80 divisor: 20.2 (4.95%)
     - Age 84 divisor: 16.8 (5.95%)
2. **Unrealistic Tax Sheltering from Age 76 to 84**:
   - In lines 1017–1019, once `age > 75`, `isConvEligible` becomes `false`, so `targetConv = 0` and `rothConversion = 0`.
   - What happens to `pretax` from age 76 to 84?
     It compounds completely untouched at 9% annual growth:
     $$\text{pretax}_{t} = \text{pretax}_{t-1} \times 1.09$$
   - Over those 9 years (2052 to 2060), pre-tax accounts double in size ($\approx 1.09^9 \approx 2.17\times$), generating **$0 in annual taxable income** and **$0 in annual taxes**!
   - Then at End of Life (age 84), the entire bloated balance is subjected to the terminal Inherited Death Tax.
   - In reality, the IRS does not allow an individual to leave an IRA untouched post-75. Forcing RMDs of hundreds of thousands of dollars each year would push the retiree into high tax brackets (32%–37%), dramatically altering the lifetime tax trajectory and shifting the optimal conversion curve.

---

### Module F: Net Investment Income Tax (NIIT, IRC § 1411)

#### Code Citations
- Lines 1027–1036:
  ```javascript
  const otherIncome = earned + cashInterest + rothConversion;
  const taxableSS = computeTaxableSS(ssBenefit, otherIncome);
  const agi = otherIncome + taxableSS;

  const fedStd = BASE_STD_DEDUCTION_MFJ * inflationFactor;
  const taxableFed = Math.max(0, agi - fedStd);
  const fedTax = computeFederalTax(taxableFed, inflationFactor, 'MFJ');
  const stateTax = computeStateTax(agi, inflationFactor, Number(p.stateTaxRate), 'MFJ');
  const totalTaxYear = fedTax + stateTax;
  ```

#### Detailed Code Findings & Flaws
1. **Omission of the 3.8% NIIT Surtax**:
   - Under IRC § 1411, a 3.8% Net Investment Income Tax applies to the lesser of:
     1. Net Investment Income (interest, dividends, capital gains, non-qualified annuities).
     2. Excess of Modified AGI over statutory thresholds:
        - **$250,000** for Married Filing Jointly (MFJ)
        - **$200,000** for Single
   - Formula:
     $$\text{NIIT} = 0.038 \times \min\Big(\text{Net Investment Income},\, \max(0, \text{MAGI} - \text{Threshold})\Big)$$
2. **Impact on Roth Conversion Strategy**:
   - NIIT statutory thresholds ($250k / $200k) are **not indexed for inflation**. Over a 34-year horizon with 3.5% inflation, ordinary income alone routinely breaches $250k.
   - Crucially, while Roth conversion amounts are not themselves Net Investment Income, **they do count towards MAGI**.
   - Therefore, converting $200,000+ of pre-tax IRA pushes MAGI far above $250,000, immediately subjecting 100% of cash interest ($20k–$25k/yr) and any investment dividends/gains to the 3.8% surtax.
   - By omitting NIIT, `planning.html` underestimates tax during high-conversion years.

---

### Module G: College Expense Modeling & Inherited IRA Death Tax

#### Code Citations: College Expense Schedule
- Line 884:
  ```javascript
  const COLLEGE_DISTRIBUTION = [0.5, 1.0, 1.0, 1.0, 0.5];
  ```
- Lines 929–935:
  ```javascript
  function computeCollegeExpense(year, collegeStartYear, collegeTotal) {
    const index = year - collegeStartYear;
    if (index >= 0 && index < COLLEGE_DISTRIBUTION.length) {
      return collegeTotal * COLLEGE_DISTRIBUTION[index];
    }
    return 0;
  }
  ```

#### Mathematical Flaw: 400% Multiplication Error
1. **Specification vs Implementation**:
   - `ORIGINAL_REQUEST.md` line 19: `College Total Expenses ($100K)`
   - `ORIGINAL_REQUEST.md` line 29: *"Spread the total expense over 5 years (Year 1: 12.5%, Year 2: 25%, Year 3: 25%, Year 4: 25%, Year 5: 12.5%)."*
   - `ORIGINAL_REQUEST.md` line 53 (Acceptance Criteria): *"College expenses must accurately span 5 years with the 12.5% / 25% / 25% / 25% / 12.5% distribution."*
2. **Code Execution Trace**:
   - `COLLEGE_DISTRIBUTION` is set to `[0.5, 1.0, 1.0, 1.0, 0.5]`.
   - The sum of these factors is:
     $$\sum = 0.5 + 1.0 + 1.0 + 1.0 + 0.5 = 4.0$$
   - In `computeCollegeExpense`:
     - Year 1 (2029): $\$100,000 \times 0.5 = \$50,000$
     - Year 2 (2030): $\$100,000 \times 1.0 = \$100,000$
     - Year 3 (2031): $\$100,000 \times 1.0 = \$100,000$
     - Year 4 (2032): $\$100,000 \times 1.0 = \$100,000$
     - Year 5 (2033): $\$100,000 \times 0.5 = \$50,000$
   - Total college expense drained from portfolio: **$400,000**!
   - This drains **$300,000 of phantom excess cash** out of the portfolio during years 2029–2033, severely depressing liquidity and prematurely forcing false liquidity deficits.
   - The correct array representing 12.5% / 25% / 25% / 25% / 12.5% must be:
     `const COLLEGE_DISTRIBUTION = [0.125, 0.25, 0.25, 0.25, 0.125];`

#### Code Citations: SECURE Act Inherited IRA Death Tax
- Lines 947–976:
  ```javascript
  // SECURE Act 10-Year Inherited IRA Liquidation Death Tax Calculator
  function computeDeathTax(pretaxBalanceEOL, eolYear, birthYear, inflationRate, stateTaxRate) {
    if (pretaxBalanceEOL <= 0) return 0;
    const yearIndex = eolYear - 2027;
    const inflationFactor = Math.pow(1 + inflationRate, yearIndex);

    // Liquidated by 2 heirs over 10 years => 20 equal annual portions
    const heirAnnualShare = pretaxBalanceEOL / 20;
    const heirBaseIncome = 150000 * inflationFactor;

    const stdSingle = BASE_STD_DEDUCTION_SINGLE * inflationFactor;
    const stateStdSingle = BASE_STATE_STD_DEDUCTION_SINGLE * inflationFactor;

    // Base tax on heir's $150K income
    const baseFedTaxable = Math.max(0, heirBaseIncome - stdSingle);
    const baseFedTax = computeFederalTax(baseFedTaxable, inflationFactor, 'Single');
    const baseStateTaxable = Math.max(0, heirBaseIncome - stateStdSingle);
    const baseStateTax = baseStateTaxable * stateTaxRate;
    const baseTotalTax = baseFedTax + baseStateTax;

    // Combined tax on ($150K + heirAnnualShare)
    const combinedIncome = heirBaseIncome + heirAnnualShare;
    const combFedTaxable = Math.max(0, combinedIncome - stdSingle);
    const combFedTax = computeFederalTax(combFedTaxable, inflationFactor, 'Single');
    const combStateTaxable = Math.max(0, combinedIncome - stateStdSingle);
    const combStateTax = combStateTaxable * stateTaxRate;
    const combTotalTax = combFedTax + combStateTax;

    const marginalTaxPerHeirAnnual = Math.max(0, combTotalTax - baseTotalTax);
    return 20 * marginalTaxPerHeirAnnual;
  }
  ```
- Lines 1182–1188:
  ```javascript
  const deathTax = computeDeathTax(pretax, eolYear, p.birthYear, p.inflationRate, Number(p.stateTaxRate));
  const deathTaxPV = deathTax / Math.pow(1 + p.inflationRate, numYears - 1);
  const deathTaxFV = deathTax;
  ```

#### Detailed Findings on Inherited IRA Death Tax
1. **Mathematical Structure**:
   - Accurately splits the pre-tax balance into 20 equal annual portions (2 heirs $\times$ 10 years).
   - Accurately inflates the heirs' $150k baseline income to `eolYear`.
   - Correctly isolates the *marginal* tax paid by each heir above their baseline income.
2. **Missing Post-Death Growth During 10-Year SECURE Period**:
   - The liquidation math assumes a static liquidation where the unliquidated portion inside the inherited IRA earns 0% return.
   - Under real SECURE Act administration, unliquidated balances remain invested tax-deferred over the 10-year window, compounding returns and expanding the taxable distributions in later years.
3. **Discounting Timing Discrepancy**:
   - In Line 1183, `deathTaxPV = deathTax / Math.pow(1 + p.inflationRate, numYears - 1)`.
   - This discounts the entire 10-year tax liability back to `startYear` as if it were paid as a single lump sum in year `eolYear`. In reality, the taxes are paid incrementally from `eolYear + 1` through `eolYear + 10`.

---

### Module H: UI Default Discrepancies, Parameter Consistency, & The Year 1 Dead-Zone

#### Code Citations: Defaults & DOM Elements
- Lines 831–856 (`DEFAULT_INPUTS`):
  ```javascript
  const DEFAULT_INPUTS = {
    cashStart: 500000,
    cashInterestRate: 0.05,
    rothStart: 120000,
    ...
  };
  ```
- Lines 624, 641, 653 (HTML inputs):
  ```html
  <!-- Line 624 -->
  <input type="number" class="form-input" id="input-cashInterestRate" step="0.1" value="4.0">

  <!-- Line 641 -->
  <input type="number" class="form-input" id="input-cashStart" step="10" value="400">

  <!-- Line 653 -->
  <input type="number" class="form-input" id="input-rothStart" step="5" value="250">
  ```
- Lines 1408–1413 (`readInputsFromDOM`):
  ```javascript
  cashStart: getVal('input-cashStart', 400) * 1000,
  cashInterestRate: getVal('input-cashInterestRate', 4.0) / 100,
  rothStart: getVal('input-rothStart', 250) * 1000,
  ```

#### Detailed Discrepancies
1. **Three-Way Discrepancy Between Spec, JS Defaults, and HTML Inputs**:
   - `cashStart`:
     - `ORIGINAL_REQUEST.md` line 16: **$500K**
     - `DEFAULT_INPUTS.cashStart`: **500,000**
     - HTML Input `#input-cashStart`: **400 ($400K)**
     - `readInputsFromDOM`: fallback **400 ($400K)**
   - `cashInterestRate`:
     - `ORIGINAL_REQUEST.md` line 16: **5%**
     - `DEFAULT_INPUTS.cashInterestRate`: **0.05 (5.0%)**
     - HTML Input `#input-cashInterestRate`: **4.0 (4.0%)**
     - `readInputsFromDOM`: fallback **4.0 (4.0%)**
   - `rothStart`:
     - `ORIGINAL_REQUEST.md` line 18: **$120K**
     - `DEFAULT_INPUTS.rothStart`: **120,000**
     - HTML Input `#input-rothStart`: **250 ($250K)**
     - `readInputsFromDOM`: fallback **250 ($250K)**
   - Any headless test running `runSimulation(DEFAULT_INPUTS)` tests an entirely different starting portfolio ($500k cash, 5% yield, $120k Roth) than a user loading `planning.html` in their browser ($400k cash, 4% yield, $250k Roth).

2. **The $275,000 Earned Income "Dead-Zone"**:
   - Look at line 1006–1009 in `runSimulation`:
     ```javascript
     const isRetired = year >= p.retireYear;
     const earned = isRetired ? 0 : Number(p.earnedIncome);
     ```
   - In default configuration:
     - `currentYear = 2026`
     - `startYear = 2026 + 1 = 2027`
     - `retireYear = 2027`
   - In year 1 of the simulation (`year = 2027`):
     `isRetired = (2027 >= 2027)` which evaluates to `true`!
     Therefore, `earned = 0`!
   - In all subsequent years, `year > 2027`, so `earned` remains 0!
   - **Result**: The UI prominent input field "Taxable Earned Income ($275K)" (line 666) is **never used at all** in the default simulation run! Users adjust this field and see absolutely no effect on cash flows or taxes unless they push `retireYear` into the future.

3. **TVM Discount Rate Assumption**:
   - In line 1141: `pvTaxSum += totalTaxYear / Math.pow(1 + p.inflationRate, i);`.
   - The time-value-of-money discount rate is hardcoded to `p.inflationRate` (3.5%).
   - In capital budgeting and wealth planning, discounting future tax liabilities at the inflation rate measures purchasing power, not financial opportunity cost. The economic opportunity cost of paying a tax dollar today versus in 20 years is the portfolio investment return (9.0%). Using 3.5% instead of 9.0% heavily biases the solver against deferring taxes.

---

### Module I: Optimization Engine & Solver Behavior

#### Code Citations
- Lines 1018, 1213–1281:
  ```javascript
  // Target conversion in runSimulation:
  const targetConv = isConvEligible ? (i < 5 ? Number(rothConvPhase1) : Number(rothConvPhase2)) : 0;
  ```
- Lines 1213–1235:
  ```javascript
  function findOptimalConversion(inputs, objective = 'raw') {
    const K_max = 1000000;
    const K_coarse_step = 25000;
    const K_fine_step = 1000;
    ...
    // Coarse Pass: 41 x 41 = 1,681 iterations
    for (let k1 = 0; k1 <= K_max; k1 += K_coarse_step) {
      for (let k2 = 0; k2 <= K_max; k2 += K_coarse_step) {
        totalEvaluated++;
        const res = runSimulation(inputs, k1, k2);
        ...
  ```
- Lines 1248–1257:
  ```javascript
    // Fine Pass: 51 x 51 = 2,601 iterations
    for (let k1 = k1_fine_start; k1 <= k1_fine_end; k1 += K_fine_step) {
      for (let k2 = k2_fine_start; k2 <= k2_fine_end; k2 += K_fine_step) {
        totalEvaluated++;
        const res = runSimulation(inputs, k1, k2);
        ...
  ```

#### Detailed Code Findings & Flaws
1. **Deviation from Authoritative Specification (2D vs Single Flat Amount)**:
   - `ORIGINAL_REQUEST.md` line 41 explicitly mandates:
     *"The engine must find the optimal **single flat dollar amount** for annual Roth conversions (applied from Retirement Year to Age 75)."*
     *"The solver must sweep through flat dollar amounts (e.g., $0 to $500K in $5K increments)..."*
   - The implementation instead split conversions into two distinct parameters:
     - `rothConvPhase1` (Years 1–5: 2027–2031)
     - `rothConvPhase2` (Years 6+: 2032–2051)
   - While a 2-phase conversion strategy offers greater financial fidelity (allowing higher conversions in the gap before Social Security begins), it diverges from the single-variable flat dollar contract specified in R4.
2. **Computational Load on Keystrokes**:
   - The coarse pass evaluates $41 \times 41 = 1,681$ simulations.
   - The fine pass evaluates $51 \times 51 = 2,601$ simulations.
   - Total evaluations per optimization: **4,282 full multi-decade simulation runs**!
   - In lines 1753–1757, `triggerOptimization` is bound to the `input` event of all 21 form input fields. Every keystroke triggers 4,282 simulation loops on the main JavaScript thread, risking UI unresponsiveness without debouncing.
3. **The Phantom Slider Bug**:
   - In lines 1786–1787:
     ```javascript
     const slider = document.getElementById('slider-conversion');
     if (slider && typeof slider.addEventListener === 'function') slider.addEventListener('input', triggerSimulation);
     ```
   - In `DOM_ID_ALIASES` (line 1356): `'slider-roth-conv': 'slider-conversion'`.
   - In CSS (lines 283–308): `.slider-box`, `.slider-header`, `.slider-title`, `.slider-value`, `.slider-input`.
   - **Yet in the HTML markup (lines 578–601), no slider element exists!**
   - The slider was stripped from the HTML DOM when the 2D solver was built, leaving dead JavaScript listeners, dead alias lookups, and dead CSS rules, while denying the user the ability to manually adjust conversion amounts.

---

## 4. Comprehensive Bug & Discrepancy Matrix

| Ref ID | Category | Severity | Location (Lines) | Description of Existing Code | Financial Impact | Remediation Formula / Code |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **BUG-01** | College Math | **Critical** | Lines 884, 930–934 | `COLLEGE_DISTRIBUTION = [0.5, 1.0, 1.0, 1.0, 0.5];` Sum = 4.0. Multiplies $100K to $400K. | Erroneously drains $400,000 instead of $100,000, causing artificial cash starvation. | Replace weights with `[0.125, 0.25, 0.25, 0.25, 0.125]`. |
| **BUG-02** | Tax Modeling | **Critical** | Line 1027, 1076 | Brokerage return `invReturn` excluded from `agi`. $0 capital gains tax on liquidation. | Brokerage grows and liquidates 100% tax-free. Understates lifetime tax by hundreds of thousands. | Add capital gains tax: $CG = \text{drawInv} \times (1 - \frac{\text{basis}}{\text{inv}})$. Apply LTCG brackets (0/15/20%). |
| **BUG-03** | RMDs | **Critical** | Lines 1017, 1064 | No RMD calculation post-age 75. Pre-tax compounds tax-free at 9% until age 84. | Omits mandatory IRS withdrawals, artificially suppressing lifetime tax during age 75–84. | Implement SECURE 2.0 RMDs starting at age 75 using IRS Uniform Lifetime Table III. |
| **BUG-04** | Healthcare | **Critical** | Line 940 | Returns `healthSubsidized * inflationFactor` for `age >= 65` ($10k–$16k/yr). | Violates acceptance criteria that healthcare drops to $0 / negligible at age 65. | Return 0 or base Medicare Part B/D premium, plus IRMAA. |
| **BUG-05** | Roth Ordering | **Major** | Lines 1051, 1083 | Enforces 5-year lockup past age 59½. Completely disallows withdrawal of Roth earnings. | Forces false portfolio insolvency even when millions in qualified Roth funds exist. | At age $\ge 59.5$, make all Roth conversions and earnings 100% accessible liquidity. |
| **BUG-06** | NIIT | **Major** | Lines 1027–1036 | No 3.8% Net Investment Income Tax (IRC § 1411) calculation. | Understates tax liability for high earners and during high Roth conversion years. | Calculate 3.8% on $\min(\text{NII}, \max(0, \text{MAGI} - 250000))$. |
| **BUG-07** | State Tax | **Major** | Line 1034 | Passes federal `agi` (including Social Security) to Virginia state tax. | Virginia exempts 100% of Social Security benefits from state income tax. | Deduct `taxableSS` from state taxable income: $\text{StateTaxable} = \max(0, \text{AGI} - \text{SS} - \text{StateStd})$. |
| **BUG-08** | Earned Income | **Moderate** | Line 1006 | `isRetired = year >= p.retireYear`. When start=2027 and retire=2027, earned income is $0 in yr 1. | $275,000 UI input is completely dead and ignored in default runs. | Redefine `isRetired = year > p.retireYear` or start simulation in pre-retirement. |
| **BUG-09** | UI Defaults | **Moderate** | Lines 641, 653, 837 | HTML default Cash is $400K (vs $500K spec) and Roth is $250K (vs $120K spec). | Discrepancy between UI presentation and headless test fixtures. | Align HTML input values with `DEFAULT_INPUTS` ($500K cash, 5% yield, $120K Roth). |
| **BUG-10** | Phantom Slider| **Minor** | Lines 578–601, 1786 | `#slider-conversion` exists in JS listeners, aliases, and CSS, but missing from HTML DOM. | User cannot manually interact with conversion amount via slider. | Add slider input to HTML or clean up orphaned JS/CSS. |

---

*(Report compiled by Teamwork Explorer Subagent `explorer_audit_1`. Detailed handoff summary located in `handoff.md`)*
