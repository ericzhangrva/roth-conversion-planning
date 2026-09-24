# Handoff Report: Financial & Logical Audit of `planning.html`

**Target File**: `/Users/eric/Dropbox/ai/asset/planning.html`  
**Working Directory**: `/Users/eric/Dropbox/ai/asset/.agents/explorer_audit_1/`  
**Detailed Evidence Report**: `/Users/eric/Dropbox/ai/asset/.agents/explorer_audit_1/analysis.md`  
**Authoritative Reference**: `/Users/eric/Dropbox/ai/asset/.agents/ORIGINAL_REQUEST.md`  
**Auditor**: Explorer Agent (`explorer_audit_1`)  
**Date**: 2026-09-24  

---

## 1. Observation

Direct code inspections of `/Users/eric/Dropbox/ai/asset/planning.html` using `view_file` yielded the following verified facts:

1. **College Expense Over-Allocation**:
   - Line 884: `const COLLEGE_DISTRIBUTION = [0.5, 1.0, 1.0, 1.0, 0.5];`
   - Lines 930–934: `return collegeTotal * COLLEGE_DISTRIBUTION[index];`
   - For `collegeTotal = 100000`, the total expense disbursed across the 5 years is $50k + $100k + $100k + $100k + $50k = **$400,000**, contradicting `ORIGINAL_REQUEST.md` (which requires 12.5% / 25% / 25% / 25% / 12.5% totaling $100,000).
2. **Taxable Brokerage Growth & Liquidation Untaxed**:
   - Line 1027: `const otherIncome = earned + cashInterest + rothConversion;`
   - Line 1045: `const cashInflows = earned + ssBenefit + cashInterest;`
   - Line 1076: `const drawInv = Math.min(invWithGrowth, remDeficit); inv = invWithGrowth - drawInv;`
   - `invReturn` is completely absent from annual AGI and taxable income. When taxable investments are sold (`drawInv`), capital gains tax is $0 and cost basis is unmonitored.
3. **Age 65 Healthcare Cost Failure**:
   - Line 940: `if (!isRetired || age >= 65) return healthSubsidized * inflationFactor;`
   - At age $\ge 65$, healthcare costs do not drop to $0 as specified in R2/Acceptance Criteria, but compound upward ($5,000 inflating at 3.5% = $10,000–$16,000+/yr).
4. **SECURE 2.0 RMDs Omitted**:
   - Lines 1017–1019: `const isConvEligible = age <= 75; const targetConv = isConvEligible ? ... : 0;`
   - Line 1064: `pretax = (pretax - rothConversion) * (1 + Number(p.invReturnRate));`
   - No Required Minimum Distributions (RMDs) are calculated. Between ages 76 and 84, pre-tax accounts grow tax-free at 9% per year with zero mandatory distributions.
5. **Roth 5-Year Lockup Active Beyond Age 59½**:
   - Lines 1051, 1083: Conversion accessibility requires `(year - rothVintages[v].year) >= 5` even for individuals aged 60–84. Furthermore, Roth earnings are never added to `currentAccessibleRoth`, causing false insolvency declarations when principal is exhausted.
6. **Net Investment Income Tax (NIIT) Absent**:
   - Lines 1027–1036: Tax is strictly `computeFederalTax` + `computeStateTax`. IRC § 1411 (3.8% tax on investment income for MAGI > $250k MFJ) is never computed.
7. **Year 1 Earned Income Dead-Zone**:
   - Line 1006: `const isRetired = year >= p.retireYear;`
   - Line 1009: `const earned = isRetired ? 0 : Number(p.earnedIncome);`
   - In default configuration (`currentYear = 2026`, `startYear = 2027`, `retireYear = 2027`), `isRetired` evaluates to `true` in Year 1. The $275,000 earned income input produces $0 across the entire simulation.
8. **UI Defaults Contradict JavaScript Defaults**:
   - Lines 641, 653: HTML inputs default Cash to $400K and Roth to $250K.
   - Lines 837, 842: `DEFAULT_INPUTS` defaults Cash to $500K and Roth to $120K.
9. **Missing Slider in HTML DOM**:
   - Lines 1786–1787: JavaScript attempts to bind `document.getElementById('slider-conversion')`.
   - The element `#slider-conversion` does not exist in the HTML body.

---

## 2. Logic Chain

1. **Premise 1**: The accuracy of decumulation tax optimization depends on faithful modeling of cash inflows, outflows, and statutory tax obligations.
2. **Inference 1 (Cash Outflow Distortion)**: Observation 1 demonstrates that the college expense logic extracts $400,000 instead of $100,000 between 2029 and 2033. This creates an artificial $300,000 liquidity drain, forcing early liquidation of investments or triggering premature infeasibility in the optimizer.
3. **Inference 2 (Severe Tax Understatement)**: Observations 2, 4, and 6 demonstrate that taxable brokerage gains are never taxed upon realization, RMDs are never forced post-75, and NIIT is never applied. Consequently, lifetime tax liabilities during retirement are understated by hundreds of thousands of dollars.
4. **Inference 3 (Retirement Distortion)**: Observation 3 shows that health insurance continues charging $10,000–$16,000/yr post-65, whereas Observation 5 locks Roth conversion funds past age 59½. This distorts the cash waterfall: older retirees pay for ACA health insurance they do not have, but cannot access their own legal Roth funds to pay for it.
5. **Inference 4 (Contractual Divergence)**: Observation 7 reveals that the $275,000 earned income input is inert in default runs, and Observation 9 shows an orphaned slider listener without an HTML DOM element.
6. **Deductive Conclusion**: The simulation engine in `planning.html` produces mathematically skewed tax projections and requires remediation before it can serve as an authoritative executive financial planning tool.

---

## 3. Categorized Findings & Mathematical Remediation

### Part 1: Critical Flaws

#### Flaw 1: College Expense Multiplier Error (400% Cost Extraction)
- **Current Code**:
  ```javascript
  const COLLEGE_DISTRIBUTION = [0.5, 1.0, 1.0, 1.0, 0.5]; // Sums to 4.0
  ```
- **Remediation**:
  Replace factors with the exact 12.5% / 25% / 25% / 25% / 12.5% distribution required by spec:
  ```javascript
  const COLLEGE_DISTRIBUTION = [0.125, 0.25, 0.25, 0.25, 0.125]; // Sums to 1.0
  ```

#### Flaw 2: Untaxed Taxable Brokerage Returns & Liquidations
- **Current Behavior**: Brokerage returns (`invReturn`) bypass AGI, and liquidations (`drawInv`) carry $0 capital gains tax.
- **Remediation Formula**:
  1. Track average cost basis:
     $$\text{costBasis}_{t} = \text{costBasis}_{t-1} + \text{Additions}_t - \text{Liquidations}_t \times \frac{\text{costBasis}_{t-1}}{\text{inv}_{t-1}}$$
  2. On liquidation $\text{drawInv}$:
     $$\text{LTCG} = \text{drawInv} \times \left(1 - \frac{\text{costBasis}}{\text{invWithGrowth}}\right)$$
  3. Tax $\text{LTCG}$ under IRC § 1(h) preferential brackets (0%, 15%, 20%) stacked on top of ordinary taxable income:
     $$\text{Threshold}_{15\%} = \$94{,}050 \times \text{inflationFactor}$$
     $$\text{Threshold}_{20\%} = \$583{,}750 \times \text{inflationFactor}$$

#### Flaw 3: Complete Omission of Required Minimum Distributions (SECURE 2.0)
- **Current Behavior**: Conversions stop at age 75, after which pre-tax accounts grow tax-free until death at age 84.
- **Remediation Formula**:
  For individuals born $\ge 1960$, RMD begins at age 75. In each year $t \ge \text{birthYear} + 75$:
  $$\text{RMD}_t = \frac{\text{pretax}_{t-1}}{\text{Divisor}(\text{age}_t)}$$
  *(Divisors from IRS Table III: Age 75: 24.6; 76: 23.7; 77: 22.9; 78: 22.0; 79: 21.1; 80: 20.2; 81: 19.4; 82: 18.5; 83: 17.7; 84: 16.8).*  
  Add $\text{RMD}_t$ to ordinary income: $\text{otherIncome} = \text{earned} + \text{cashInterest} + \text{rothConversion} + \text{RMD}_t$.

#### Flaw 4: Post-65 Healthcare Cost Non-Zero Bug
- **Current Behavior**: Line 940 returns `healthSubsidized * inflationFactor` for `age >= 65`.
- **Remediation**:
  ```javascript
  function computeHealthcareExpense(age, magi, yearIndex, inflationRate, healthSubsidized, healthUnsubsidized, isRetired, magiCliff = 90000) {
    if (age >= 65) return 0; // Drops to $0 as specified in R2
    const inflationFactor = Math.pow(1 + inflationRate, yearIndex);
    if (!isRetired) return healthSubsidized * inflationFactor;
    const inflatedCliff = magiCliff * inflationFactor;
    return (magi <= inflatedCliff ? healthSubsidized : healthUnsubsidized) * inflationFactor;
  }
  ```

---

### Part 2: Unreasonable Assumptions

#### Assumption 1: Flawed Roth 5-Year Lockup Past Age 59½ & Inaccessible Earnings
- **Current Behavior**: Conversions are locked for 5 years even up to age 84. Compounded Roth earnings can never be withdrawn to resolve cash deficits.
- **Remediation**:
  Under IRC § 408A(d), once age $\ge 59.5$ and 5 years have elapsed since the first Roth contribution (met by starting balance), **100% of the Roth balance (principal, all conversions, and all earnings) is liquid and tax-free**:
  ```javascript
  const currentAccessibleRoth = (age >= 59.5) ? roth : (accessibleOriginalPrincipal + accessibleVintages);
  ```

#### Assumption 2: Constant 9% Nominal Return with Zero Equity Glidepath
- **Current Behavior**: Static 9.0% equity return assumed from age 51 to age 84 with zero volatility or asset de-risking.
- **Recommendation**: Support an optional asset allocation glidepath reducing equity exposure from 9% to 6% in retirement.

#### Assumption 3: Discounting TVM Tax Liabilities at Inflation Rate (3.5%)
- **Current Behavior**: Taxes in Year $N$ are discounted by $(1 + 0.035)^N$.
- **Recommendation**: Provide a discount rate input (defaulting to the portfolio opportunity cost, 7%–9%, or allowing user toggling between inflation discount and investment hurdle discount).

---

### Part 3: Missing Features

#### Feature 1: Net Investment Income Tax (NIIT, IRC § 1411)
- **Mathematical Specification**:
  $$\text{NII} = \text{cashInterest} + \text{taxableBrokerageDividends} + \text{realizedLTCG}$$
  $$\text{Threshold}_{\text{NIIT}} = \$250{,}000 \quad (\text{MFJ, unindexed})$$
  $$\text{NIIT} = 0.038 \times \max\Big(0,\, \min(\text{NII},\, \text{AGI} - \text{Threshold}_{\text{NIIT}})\Big)$$

#### Feature 2: Medicare Part B & Part D IRMAA Surcharge Cliffs
- **Mathematical Specification**:
  At age $\ge 65$, apply statutory 2-year lookback ($\text{MAGI}_{t-2}$) to determine Medicare surcharge tiers:
  - Tier 1 ($\le \$206k$ MFJ): Standard premium (~$4,200/yr couple).
  - Tier 2 ($>\$206k$): Standard + $840/yr couple.
  - Tier 3 ($>\$258k$): Standard + $2,100/yr couple.
  - Tier 4 ($>\$322k$): Standard + $3,360/yr couple.
  - Tier 5 ($>\$386k$): Standard + $4,620/yr couple.
  - Tier 6 ($\ge \$750k$): Standard + $5,460/yr couple.

#### Feature 3: Virginia State Income Tax Exemption on Social Security
- **Mathematical Specification**:
  Under Va. Code § 58.1-322.02, subtract `taxableSS` before calculating Virginia state taxable income:
  $$\text{StateTaxableIncome} = \max\Big(0,\, \text{AGI} - \text{taxableSS} - \text{StateStdDeduction}\Big)$$

---

## 4. Caveats

1. **Tax Legislation Invalidation Risk**: The current tax code reflects post-TCJA provisions. If the US Congress alters the December 31, 2025 sunset, statutory baseline rates will change.
2. **Heir Tax Rate Variations**: The SECURE Act inherited IRA calculation models 2 Single heirs earning $150,000 base income. Real-world heir marginal brackets may vary if heirs are married or in higher/lower tax brackets.
3. **No Code Modification Performed**: In accordance with explorer rules, all findings are purely observational and analytical; `planning.html` remains untouched.

---

## 5. Conclusion

The `planning.html` simulation engine successfully implements core decumulation concepts (progressive federal brackets, IRC § 86 Social Security taxation, and SECURE Act 10-year inherited IRA liquidation).

However, it is compromised by **critical mathematical errors** (the 4x college expense calculation), **massive tax blind spots** (100% untaxed brokerage growth and zero capital gains), **omitted regulatory mandates** (omission of SECURE 2.0 RMDs post-75), **flawed Roth age-59½ mechanics**, and **UI/DOM default discrepancies**.

Remediating these issues using the mathematical formulas provided in Section 3 will transform `planning.html` into a rigorous, institutional-grade retirement optimization engine.

---

## 6. Verification Method

To independently verify the observations and logic documented in this report:

1. **Verify College 4x Math Anomaly**:
   Inspect Lines 884 and 929–935 of `planning.html`. Execute:
   $$\sum_{i=0}^4 \text{COLLEGE\_DISTRIBUTION}[i] = 0.5 + 1.0 + 1.0 + 1.0 + 0.5 = 4.0$$
   Multiply by $100,000 to confirm that $400,000 is deducted across years 2029–2033.
2. **Verify Untaxed Brokerage Gains**:
   Inspect Line 1027: confirm that `otherIncome` only sums `earned + cashInterest + rothConversion` and omits `invReturn`. Inspect Line 1076: confirm that `drawInv` does not calculate or deduct any capital gains tax.
3. **Verify Age 65 Healthcare Cost Bug**:
   Inspect Line 940: `if (!isRetired || age >= 65) return healthSubsidized * inflationFactor;`. Confirm that for `age >= 65`, the function returns non-zero subsidized expenses instead of $0.
4. **Verify Omission of RMDs**:
   Inspect Lines 1017–1020 and Line 1064: confirm that after `age > 75`, `pretax` balance compounds at `1 + invReturnRate` without any mandatory distribution deduction.
5. **Verify Headless Test Suite**:
   Run the static and unit test suite via Node.js or JavaScriptCore:
   ```bash
   node /Users/eric/Dropbox/ai/asset/.agents/test_planning.js
   ```
   Inspect the emitted test results for DOM alignment and tax parity.

---

*(Report compiled and submitted by Teamwork Explorer Subagent `explorer_audit_1`)*
