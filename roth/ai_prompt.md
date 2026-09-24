# System Prompt: Financial Simulation Engine

You are an expert AI software engineer and financial modeler. 
Your task is to build a single-file, client-side HTML/JS application that simulates lifetime financial drawdowns, Roth conversions, and SECURE 2.0 inherited death taxes.

Use the following detailed mathematical specification and architectural constraints to generate the complete engine.

---
# Exhaustive Financial & Technical Audit: Retirement Simulation Engine (`planning.html`)

**Target File**: `/Users/eric/Dropbox/ai/asset/planning.html` (1,841 lines, 69,447 bytes)  
**Authoritative Reference**: `/Users/eric/Dropbox/ai/asset/.agents/ORIGINAL_REQUEST.md`  
**Audit Date**: September 24, 2026  
**Auditor**: Teamwork Financial Engineering & Quality Assurance Group  
**Status**: Completed — Ready for Executive Review & Implementation  

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Codebase Topography & Function Registry](#2-codebase-topography--function-registry)
3. [Category 1: Critical Flaws (Structural & Mathematical Failures)](#3-category-1-critical-flaws-structural--mathematical-failures)
   - [1.1 The 400% College Expense Over-Allocation Anomaly](#11-the-400-college-expense-over-allocation-anomaly)
   - [1.2 Untaxed Brokerage Portfolio (Tax Haven Brokerage & $0 Capital Gains)](#12-untaxed-brokerage-portfolio-tax-haven-brokerage--0-capital-gains)
   - [1.3 Complete Omission of SECURE 2.0 Required Minimum Distributions (RMDs)](#13-complete-omission-of-secure-20-required-minimum-distributions-rmds)
   - [1.4 Age 65 Healthcare Cost Logic Failure (Subsidized ACA Charges Post-65)](#14-age-65-healthcare-cost-logic-failure-subsidized-aca-charges-post-65)
4. [Category 2: Unreasonable Assumptions & Economic Blind Spots](#4-category-2-unreasonable-assumptions--economic-blind-spots)
   - [2.1 Flawed Roth 5-Year Lockup Logic Past Age 59½ & Inaccessible Earnings](#21-flawed-roth-5-year-lockup-logic-past-age-59½--inaccessible-earnings)
   - [2.2 The Year 1 Earned Income Dead-Zone & Retirement Boundary](#22-the-year-1-earned-income-dead-zone--retirement-boundary)
   - [2.3 Time Value of Money (TVM) Discounting at Inflation Instead of Opportunity Cost](#23-time-value-of-money-tvm-discounting-at-inflation-instead-of-opportunity-cost)
   - [2.4 Static 9% Equity Returns Without Volatility or Asset Allocation Glidepath](#24-static-9-equity-returns-without-volatility-or-asset-allocation-glidepath)
5. [Category 3: Missing Features & Statutory Tax Mechanics](#5-category-3-missing-features--statutory-tax-mechanics)
   - [3.1 Net Investment Income Tax (NIIT, IRC § 1411)](#31-net-investment-income-tax-niit-irc--1411)
   - [3.2 Medicare Part B & Part D IRMAA Surcharges with 2-Year Lookback](#32-medicare-part-b--part-d-irmaa-surcharges-with-2-year-lookback)
   - [3.3 Virginia State Income Tax Treatment of Social Security & Deductions](#33-virginia-state-income-tax-treatment-of-social-security--deductions)
   - [3.4 Federal TCJA Sunset Mechanics & Senior Additional Standard Deduction](#34-federal-tcja-sunset-mechanics--senior-additional-standard-deduction)
6. [Category 4: UI/DOM Integrity, Solver Architecture & Usability](#6-category-4-uidom-integrity-solver-architecture--usability)
   - [4.1 Tripartite Parameter Inconsistencies (Spec vs JS Defaults vs HTML DOM)](#41-tripartite-parameter-inconsistencies-spec-vs-js-defaults-vs-html-dom)
   - [4.2 The Phantom Conversion Slider Bug](#42-the-phantom-conversion-slider-bug)
   - [4.3 Optimization Solver Deviation & Main-Thread Keystroke Flooding](#43-optimization-solver-deviation--main-thread-keystroke-flooding)
7. [Comprehensive Modernization Blueprint & Integrated Engine Architecture](#7-comprehensive-modernization-blueprint--integrated-engine-architecture)
8. [Summary Audit Matrix & Implementation Action Plan](#8-summary-audit-matrix--implementation-action-plan)

---

## 1. Executive Summary

This report delivers a comprehensive mathematical, logical, and regulatory audit of the lifetime retirement simulation and tax optimization engine contained in `/Users/eric/Dropbox/ai/asset/planning.html`. 

The web application was designed to simulate year-by-year portfolio decumulation from retirement (2027) through End of Life (2060) for a high-net-worth household (initial liquid net worth: $5.92M across cash, taxable brokerage, pre-tax traditional IRA/401(k), and Roth accounts). Its stated objective is to compute federal and state taxes, track cash flow constraints, and find the optimal Roth conversion policy that minimizes lifetime tax liability.

### Summary of Audit Findings
While the application achieves an impressive aesthetic presentation—complete with an interactive dark-mode dashboard, responsive Key Performance Indicator (KPI) cards, sticky data tables, and Chart.js visualizations—the underlying financial simulation engine contains **severe structural blind spots, mathematical anomalies, and statutory omissions**. 

These errors invalidate the model's tax projections, distort optimal conversion recommendations, and create artificial portfolio insolvency:

1. **400% College Expense Extraction**: A multiplier error in `COLLEGE_DISTRIBUTION = [0.5, 1.0, 1.0, 1.0, 0.5]` extracts **$400,000** instead of the specified **$100,000** total college expense, draining $300,000 of phantom liquidity during years 2029–2033.
2. **Untaxed Taxable Brokerage Portfolio**: Taxable brokerage investments ($300k starting balance compounding at 9.0% annually) generate **$0 of taxable income** in annual Modified Adjusted Gross Income (MAGI) and **$0 of capital gains tax** upon liquidation, creating an accidental offshore tax haven.
3. **Complete Absence of SECURE 2.0 RMDs**: Mandatory IRS Required Minimum Distributions starting at age 75 under SECURE 2.0 are entirely missing. Pre-tax retirement accounts are allowed to compound tax-free at 9.0% from age 76 to 84 with zero taxable distributions, generating $0 of annual tax until an unrealistic terminal "Death Tax" is assessed at age 84.
4. **Post-65 Healthcare Cost Anomaly**: Healthcare costs fail to drop to $0 or transition to Medicare at age 65 as required by project specifications; instead, the code charges retirees an inflated subsidized Affordable Care Act (ACA) premium ($10,000 to $16,000+ per year) up to age 84.
5. **Flawed Roth 5-Year Lockup Past Age 59½**: The 5-year conversion lockup rule is enforced through age 84, directly violating Internal Revenue Code (IRC) § 408A(d) qualified distribution rules. Furthermore, compounded Roth earnings are permanently excluded from accessible liquidity, declaring portfolios "insolvent" even when millions of dollars in qualified Roth funds remain.
6. **Omission of Statutory High-Net-Worth Surtaxes**: The engine completely omits the **3.8% Net Investment Income Tax (NIIT, IRC § 1411)** and **Medicare Part B & Part D Income-Related Monthly Adjustment Amounts (IRMAA)**, both of which heavily penalize large Roth conversions.
7. **Virginia State Tax Social Security Violation**: Federal Adjusted Gross Income (including taxable Social Security) is taxed directly at 5.75%, violating Virginia Code Ann. § 58.1-322.02, which grants a 100% state tax exemption for Social Security benefits.
8. **UI/Code Default Inconsistencies & Phantom Slider**: Defaults in JavaScript (`DEFAULT_INPUTS`) contradict DOM input defaults for Cash, Yield, and Roth balances. A conversion slider (`#slider-conversion`) is referenced in JavaScript event listeners and CSS, but does not exist in the HTML DOM.

### Master Findings Heatmap

| Finding ID | Categorization | Severity | Primary Module / Location | Financial Distortion |
| :--- | :--- | :--- | :--- | :--- |
| **FLAW-01** | Critical Flaw | **Blocker** | Lines 884, 929–935 (`computeCollegeExpense`) | Siphons $400,000 vs $100,000 spec; causes false cash insolvency |
| **FLAW-02** | Critical Flaw | **Blocker** | Lines 1027, 1075–1078 (`runSimulation`) | Brokerage gains & liquidations 100% tax-free; understates lifetime tax by $150k–$400k+ |
| **FLAW-03** | Critical Flaw | **Blocker** | Lines 1016–1020, 1064 (`runSimulation`) | Omits SECURE 2.0 RMDs post-75; pre-tax grows tax-free from 76 to 84 |
| **FLAW-04** | Critical Flaw | **High** | Lines 938–944 (`computeHealthcareExpense`) | Charges $10k–$16k/yr ACA premium post-65; drains ~$200k phantom cash |
| **ASSUMP-01** | Unreasonable Assumption | **High** | Lines 1051, 1083 (`runSimulation`) | Locks conversions & earnings past 59½; premature insolvency failure |
| **ASSUMP-02** | Unreasonable Assumption | **Medium** | Lines 1006–1009 (`runSimulation`) | $275,000 UI earned income input produces $0 in default runs (Year 1 dead-zone) |
| **ASSUMP-03** | Unreasonable Assumption | **Medium** | Lines 855, 1141 (`runSimulation`) | TVM discounting uses CPI inflation (3.5%) rather than portfolio hurdle (9.0%) |
| **ASSUMP-04** | Unreasonable Assumption | **Low** | Line 840, 1063–1065 (`runSimulation`) | Constant 9.0% equity return across 34 years with zero sequence of returns |
| **FEAT-01** | Missing Feature | **High** | Lines 1027–1036 (`runSimulation`) | Omits 3.8% NIIT (IRC § 1411) triggered on high Roth conversion years |
| **FEAT-02** | Missing Feature | **High** | Lines 938–944, 1039 (`computeHealthcareExpense`)| Omits Medicare Part B & Part D IRMAA surcharge cliffs (2-year lookback) |
| **FEAT-03** | Missing Feature | **Medium** | Lines 907–912, 1034 (`computeStateTax`) | Virginia state tax improperly assesses 5.75% tax on Social Security |
| **FEAT-04** | Missing Feature | **Medium** | Lines 859–882 (`computeFederalTax`) | Omits TCJA 2026 statutory sunset reversion & Senior Standard Deduction |
| **UI-01** | UI / Architecture | **Medium** | Lines 624, 641, 653 vs 837–843 | Three-way default discrepancy (Spec vs JS Defaults vs HTML inputs) |
| **UI-02** | UI / Architecture | **Low** | Lines 1786–1787, 1356, 283–308 | Phantom slider in JS and CSS missing from HTML DOM |
| **UI-03** | UI / Architecture | **Medium** | Lines 1213–1281, 1753–1757 | 2D parameter sweep (4,282 runs) on un-debounced form input events |

---

## 2. Codebase Topography & Function Registry

The audit target is a standalone file (`planning.html`) containing 1,841 lines of code structured as follows:

```
planning.html
├── Lines 1–8:       HTML Head & CDN Scripts (Chart.js 4.4.2 UMD)
├── Lines 9–513:     Embedded CSS Stylesheet (Theme variables, grid layout, custom tooltips)
├── Lines 514–789:   Semantic HTML Layout
│   ├── Lines 518–527: Header actions (PDF / JPG Export)
│   ├── Lines 530–571: 8 KPI Metric Summary Cards
│   ├── Lines 576–719: Sidebar Controls (Optimization panel, Timeline, Assets, Incomes, Expenses)
│   └── Lines 722–789: Main Content (Chart canvas #chart-canvas & 18-column Table #table-simulation-body)
└── Lines 791–1838:  Embedded JavaScript Engine
    ├── Lines 800–828: SafeStorage abstraction (localStorage fallback)
    ├── Lines 831–884: Constants (DEFAULT_INPUTS, Brackets, Deductions, COLLEGE_DISTRIBUTION)
    ├── Lines 887–976: Pure Calculation Functions
    │   ├── computeFederalTax() [Lines 887–904]
    │   ├── computeStateTax() [Lines 907–912]
    │   ├── computeTaxableSS() [Lines 915–926]
    │   ├── computeCollegeExpense() [Lines 929–935]
    │   ├── computeHealthcareExpense() [Lines 938–944]
    │   └── computeDeathTax() [Lines 947–976]
    ├── Lines 979–1210: Core Simulation Engine (runSimulation)
    ├── Lines 1213–1317: Optimization Solver (findOptimalConversion)
    ├── Lines 1320–1363: DOM Alias Dictionary (DOM_ID_ALIASES)
    ├── Lines 1376–1505: DOM Input Reading & Table Rendering
    ├── Lines 1507–1680: Chart.js Rendering Engine (renderChart)
    ├── Lines 1683–1796: Export Utilities & DOMContentLoaded Event Wiring
    └── Lines 1800–1837: Dual-Environment Headless UMD Module Export
```

### Existing Function Signatures & Mathematical Responsibilities

```javascript
// Lines 887–904: Calculates progressive federal income tax across 7 brackets
computeFederalTax(taxableIncome, inflationFactor = 1.0, filingStatus = 'MFJ')

// Lines 907–912: Calculates flat state income tax over standard deduction
computeStateTax(income, inflationFactor = 1.0, stateTaxRate = 0.0575, filingStatus = 'MFJ')

// Lines 915–926: Calculates taxable Social Security under IRC § 86 provisional income tiers
computeTaxableSS(ssAmount, otherIncome)

// Lines 929–935: Evaluates 5-year college expense schedule
computeCollegeExpense(year, collegeStartYear, collegeTotal)

// Lines 938–944: Computes pre-65 ACA subsidized/unsubsidized health expenses
computeHealthcareExpense(age, magi, yearIndex, inflationRate, healthSubsidized, healthUnsubsidized, isRetired, magiCliff = 90000)

// Lines 947–976: Calculates terminal 10-year SECURE Act liquidation tax for 2 heirs
computeDeathTax(pretaxBalanceEOL, eolYear, birthYear, inflationRate, stateTaxRate)

// Lines 979–1210: Annual decumulation simulation, cash flow waterfall, and TVM metrics
runSimulation(inputs, rothConvPhase1 = 0, rothConvPhase2 = 0)

// Lines 1213–1317: 2D coarse-to-fine grid search for optimal conversion amounts
findOptimalConversion(inputs, objective = 'raw')
```

---

## 3. Category 1: Critical Flaws (Structural & Mathematical Failures)

Critical flaws represent programmatic or mathematical errors that yield fundamentally incorrect financial balances, violate project requirements, or induce false portfolio insolvency.

---

### 1.1 The 400% College Expense Over-Allocation Anomaly

#### Code Citation
- **File**: `planning.html`
- **Lines 884, 929–935**:
```javascript
// Line 884
const COLLEGE_DISTRIBUTION = [0.5, 1.0, 1.0, 1.0, 0.5];

// Lines 929–935
function computeCollegeExpense(year, collegeStartYear, collegeTotal) {
  const index = year - collegeStartYear;
  if (index >= 0 && index < COLLEGE_DISTRIBUTION.length) {
    return collegeTotal * COLLEGE_DISTRIBUTION[index];
  }
  return 0;
}
```
- **Line 690 (HTML Tooltip)**:
```html
<label class="form-label" for="input-collegeTotal" data-tooltip="Total annual college expenses per year during the college period">College Annual Exp (K$)</label>
```

#### Detailed Observation & Mechanism of Failure
1. **Contract Specification**:
   - `ORIGINAL_REQUEST.md` (lines 19, 29, 53) strictly dictates:
     > *"College Total Expenses ($100K), College Start Year (2029)"*  
     > *"Spread the total expense over 5 years (Year 1: 12.5%, Year 2: 25%, Year 3: 25%, Year 4: 25%, Year 5: 12.5%). Do not inflate College expenses."*  
     > *"College expenses must accurately span 5 years with the 12.5% / 25% / 25% / 25% / 12.5% distribution."*
2. **Implementation Anomaly**:
   - In `planning.html`, the distribution vector is defined as:
     $$\mathbf{w}_{\text{actual}} = [0.5,\, 1.0,\, 1.0,\, 1.0,\, 0.5]$$
   - Summing these weights yields:
     $$\sum_{k=0}^{4} w_k = 0.5 + 1.0 + 1.0 + 1.0 + 0.5 = 4.0$$
   - The developer appears to have confused the input meaning, treating the `$100K` total expense as an *annual* tuition rate (reflected in the HTML tooltip: *"Total annual college expenses per year"*), and weighting semesters as half-years (`0.5`) and full years (`1.0`).
3. **Financial Impact**:
   - Evaluating `computeCollegeExpense(year, 2029, 100000)` produces:
     - 2029 (Yr 1): $\$100{,}000 \times 0.5 = \$50{,}000$ (Spec: $\$12{,}500$)
     - 2030 (Yr 2): $\$100{,}000 \times 1.0 = \$100{,}000$ (Spec: $\$25{,}000$)
     - 2031 (Yr 3): $\$100{,}000 \times 1.0 = \$100{,}000$ (Spec: $\$25{,}000$)
     - 2032 (Yr 4): $\$100{,}000 \times 1.0 = \$100{,}000$ (Spec: $\$25{,}000$)
     - 2033 (Yr 5): $\$100{,}000 \times 0.5 = \$50{,}000$ (Spec: $\$12{,}500$)
   - **Total Extracted**: **$400,000** instead of **$100,000**.
   - This error extracts **$300,000 of phantom cash** from the portfolio between 2029 and 2033. Because 2029–2033 coincides with the early retirement phase prior to Social Security, this artificial cash drain prematurely exhausts cash reserves, forces taxable asset liquidations, and causes the optimizer in `findOptimalConversion` to reject valid Roth conversion candidates due to false liquidity violations (`remDeficit > 0.01`).

#### Mathematical Formulation (LaTeX)
Let $C_{\text{total}}$ be the total lifetime college expense entered by the user. The annual disbursement in year $t$ relative to college matriculation year $t_{\text{start}}$ must satisfy:

$$C_t(t) = \begin{cases}
w_{t - t_{\text{start}}} \cdot C_{\text{total}} & \text{if } 0 \le t - t_{\text{start}} < 5 \\
0 & \text{otherwise}
\end{cases}$$

where the normalized weight vector $\mathbf{w}$ is strictly:

$$\mathbf{w} = \begin{bmatrix} 0.125 \\ 0.250 \\ 0.250 \\ 0.250 \\ 0.125 \end{bmatrix}, \quad \text{such that} \quad \sum_{k=0}^{4} w_k = 1.000$$

#### Programmatic Solution & Concrete JavaScript Replacement
```javascript
// Step 1: Update Statutory Distribution Weights to exact percentages
const COLLEGE_DISTRIBUTION = [0.125, 0.25, 0.25, 0.25, 0.125];

// Step 2: Implement robust distribution function with validation
function computeCollegeExpense(year, collegeStartYear, collegeTotal) {
  if (!collegeTotal || collegeTotal <= 0) return 0;
  const index = year - collegeStartYear;
  if (index >= 0 && index < COLLEGE_DISTRIBUTION.length) {
    return Number(collegeTotal) * COLLEGE_DISTRIBUTION[index];
  }
  return 0;
}

// Step 3: Correct HTML DOM Label and Tooltip in planning.html
// Line 690:
// <label class="form-label" for="input-collegeTotal" data-tooltip="Total 5-year college expense (disbursed 12.5% / 25% / 25% / 25% / 12.5%)">College Total Exp (K$)</label>
```

---

### 1.2 Untaxed Brokerage Portfolio (Tax Haven Brokerage & $0 Capital Gains)

#### Code Citation
- **File**: `planning.html`
- **Lines 1009–1010, 1027–1029**:
```javascript
const earned = isRetired ? 0 : Number(p.earnedIncome);
const cashInterest = cash > 0 ? cash * Number(p.cashInterestRate) : 0;
...
// Taxes
const otherIncome = earned + cashInterest + rothConversion;
const taxableSS = computeTaxableSS(ssBenefit, otherIncome);
const agi = otherIncome + taxableSS;
```
- **Lines 1074–1078**:
```javascript
// 2. Drawdown Taxable Investment
const invWithGrowth = inv * (1 + Number(p.invReturnRate));
const drawInv = Math.min(invWithGrowth, remDeficit);
inv = invWithGrowth - drawInv;
remDeficit -= drawInv;
```
- **Lines 1156, 1477 (UI Presentation Illusion)**:
```javascript
// Line 1156 in runSimulation records:
invReturn: inv * Number(p.invReturnRate),

// Line 1477 in renderSimulationToDOM:
const totalIncome = r.earnedIncome + r.ssBenefit + r.cashInterest + r.invReturn + r.rothConversion;
```

#### Detailed Observation & Mechanism of Failure
1. **Omission of Investment Income from Tax Base**:
   - In Line 1027, taxable income prior to deductions is computed as:
     `const otherIncome = earned + cashInterest + rothConversion;`
   - Notice that while `cashInterest` ($500k cash @ 5% = $25k) is included, **brokerage returns are completely excluded from `agi`**.
   - A starting taxable brokerage of $300,000 growing at 9.0% generates $27,000 of nominal return in Year 1 alone, compounding to hundreds of thousands of dollars annually later in life. None of this growth enters Adjusted Gross Income.
2. **Visual Discrepancy / Cosmetic Façade**:
   - In Line 1156, `invReturn` is saved in the record table. In Line 1477, it is displayed in the data table under "Investment Return ($K)" and added to "Total Income ($K)". 
   - This creates a deceptive UI presentation: the user sees investment return listed as income in the table, but tracing Line 1027 proves that **the tax computation engine never taxed a single penny of it**.
3. **Zero Capital Gains Tax on Portfolio Liquidation**:
   - In Lines 1075–1078, when a cash flow deficit forces a drawdown of taxable investments (`drawInv`), the engine performs a direct balance deduction:
     `inv = invWithGrowth - drawInv;`
     `remDeficit -= drawInv;`
   - The engine does not track **cost basis**.
   - It calculates **$0 in realized capital gains**, treats the entire liquidation proceeds as tax-free cash, and pays **$0 in Long-Term Capital Gains (LTCG) tax**, **$0 in state income tax**, and **$0 in NIIT**.
4. **Financial Impact**:
   - Taxable brokerage accounts in `planning.html` operate as offshore tax shelters with superior tax treatment to a Roth IRA (no contribution caps, no conversion taxes, no dividend drag, no capital gains taxes).
   - In reality, high-net-worth brokerage assets experience an annual dividend yield (typically ~2.0% qualified dividends) taxed annually, plus substantial capital gains realization upon liquidation. Omitting these taxes understates lifetime taxes by **$150,000 to over $400,000**, heavily distorting the solver's conversion tradeoff.

#### Mathematical Formulation (LaTeX)

##### 1. Average Cost Basis Tracking
Let $B_t$ be the aggregate cost basis of the taxable investment account at the start of year $t$, and $I_t$ be the market value. When the portfolio grows at return rate $r_{\text{inv}}$, market value prior to distribution is:

$$I_t^{\text{pre}} = I_t \cdot (1 + r_{\text{inv}})$$

When a liquidation $D_t^{\text{inv}} = \min(I_t^{\text{pre}}, \text{Deficit}_t)$ occurs, the basis ratio is:

$$\beta_t = \frac{B_t}{I_t^{\text{pre}}}$$

The realized capital gain $G_t^{\text{realized}}$ is:

$$G_t^{\text{realized}} = D_t^{\text{inv}} \cdot (1 - \beta_t) = D_t^{\text{inv}} - D_t^{\text{inv}} \cdot \beta_t$$

The updated cost basis for the next period is:

$$B_{t+1} = B_t - (D_t^{\text{inv}} \cdot \beta_t) + \text{Additions}_t$$

##### 2. Long-Term Capital Gains (LTCG) Stacking
Under IRC § 1(h), net capital gains are stacked on top of ordinary taxable income ($Y_{\text{ord}}$):

$$Y_{\text{ord}} = \max\Big(0,\, \text{AGI}_{\text{ordinary}} - \text{StdDeduction}_t\Big)$$

$$\text{Base}_{\text{LTCG}} = Y_{\text{ord}}$$
$$\text{Top}_{\text{LTCG}} = Y_{\text{ord}} + G_t^{\text{realized}}$$

The LTCG tax is evaluated across the preferential inflation-adjusted statutory tiers:

$$T_{\text{LTCG}}(G) = \begin{cases}
0\% & \text{for portion where } Y \le \tau_{0} \cdot (1 + i)^t \\
15\% & \text{for portion where } \tau_{0} \cdot (1 + i)^t < Y \le \tau_{15} \cdot (1 + i)^t \\
20\% & \text{for portion where } Y > \tau_{15} \cdot (1 + i)^t
\end{cases}$$

where for Married Filing Jointly (MFJ) in 2024/2027 base dollars:
$$\tau_0 = \$94{,}050, \quad \tau_{15} = \$583{,}750$$

#### Programmatic Solution & Concrete JavaScript Replacement
```javascript
// Preferential LTCG Brackets for MFJ (2024 Baseline)
const BASE_LTCG_BRACKETS_MFJ = [
  { max: 94050, rate: 0.00 },
  { max: 583750, rate: 0.15 },
  { max: Infinity, rate: 0.20 }
];

// Helper: Compute Stacked Long-Term Capital Gains Tax
function computeCapitalGainsTax(ordinaryTaxableIncome, realizedGain, inflationFactor = 1.0) {
  if (realizedGain <= 0) return 0;
  
  let tax = 0;
  let currentIncome = ordinaryTaxableIncome;
  let remainingGain = realizedGain;
  
  for (let i = 0; i < BASE_LTCG_BRACKETS_MFJ.length; i++) {
    const bracket = BASE_LTCG_BRACKETS_MFJ[i];
    const threshold = bracket.max === Infinity ? Infinity : bracket.max * inflationFactor;
    
    if (currentIncome < threshold) {
      const roomInBracket = threshold - currentIncome;
      const gainInBracket = Math.min(remainingGain, roomInBracket);
      tax += gainInBracket * bracket.rate;
      remainingGain -= gainInBracket;
      currentIncome += gainInBracket;
      if (remainingGain <= 0) break;
    }
  }
  return tax;
}

// Integrated Waterfall Logic within runSimulation:
// 1. Maintain cost basis state:
let invCostBasis = Number(p.invCostBasisStart !== undefined ? p.invCostBasisStart : p.invStart * 0.70); // Assume 70% basis if unspecified

// 2. During deficit liquidation:
let realizedLTCG = 0;
if (remDeficit > 0 && inv > 0) {
  const invWithGrowth = inv * (1 + Number(p.invReturnRate));
  const drawInv = Math.min(invWithGrowth, remDeficit);
  
  // Realized gain calculation via average cost basis method
  const basisRatio = invWithGrowth > 0 ? Math.min(1.0, invCostBasis / invWithGrowth) : 1.0;
  const basisDrawn = drawInv * basisRatio;
  realizedLTCG = Math.max(0, drawInv - basisDrawn);
  
  invCostBasis = Math.max(0, invCostBasis - basisDrawn);
  inv = invWithGrowth - drawInv;
  remDeficit -= drawInv;
}

// 3. Tax computation accounts for ordinary + capital gains tax:
const ltcgTax = computeCapitalGainsTax(taxableFed, realizedLTCG, inflationFactor);
const stateLTCGTax = realizedLTCG * Number(p.stateTaxRate); // Virginia taxes capital gains as ordinary income
const totalTaxYear = fedTax + stateTax + ltcgTax + stateLTCGTax;
```

---

### 1.3 Complete Omission of SECURE 2.0 Required Minimum Distributions (RMDs)

#### Code Citation
- **File**: `planning.html`
- **Lines 1016–1020**:
```javascript
// Roth Conversion eligibility: startYear <= year <= birthYear + 75
const isConvEligible = age <= 75;
const targetConv = isConvEligible ? (i < 5 ? Number(rothConvPhase1) : Number(rothConvPhase2)) : 0;
const rothConversion = Math.max(0, Math.min(targetConv, pretax));
```
- **Lines 1064, 1103**:
```javascript
pretax = (pretax - rothConversion) * (1 + Number(p.invReturnRate));
```

#### Detailed Observation & Mechanism of Failure
1. **Statutory Mandate (SECURE 2.0 Act of 2022)**:
   - Under Division T of the Consolidated Appropriations Act of 2023 (SECURE 2.0, P.L. 117-328), the Required Beginning Date (RBD) for mandatory IRA distributions was updated:
     - Born 1951–1959: Age 73
     - Born 1960 or later: **Age 75**
   - For an individual born in 1976 (the default `p.birthYear`), RMDs become legally mandatory in the year the taxpayer reaches **age 75** (Year 2051).
2. **Current Implementation Blind Spot**:
   - In `planning.html`, lines 1017–1019 turn off Roth conversions when `age > 75` (`isConvEligible = false`).
   - What happens to the traditional pre-tax retirement account from age 76 through age 84?
     **Nothing.** The balance simply compounds untouched at 9.0% annual growth:
     $$\text{pretax}_{t} = \text{pretax}_{t-1} \cdot (1 + 0.09)$$
   - Over this 9-year span (2052 to 2060):
     - The pre-tax account doubles in size ($\approx 1.09^9 \approx 2.17\times$).
     - The retiree reports **$0 in pre-tax distributions**, pays **$0 in annual income taxes** on this massive wealth, and falls into artificially low tax brackets.
     - At age 84 (EOL), the engine suddenly liquidates the entire bloated multi-million-dollar balance in `computeDeathTax` to calculate a terminal tax for heirs.
3. **Financial Impact**:
   - This failure creates a completely fictitious tax sheltering mechanism for ultra-wealthy retirees in their late 70s and 80s.
   - In reality, an individual with a $5,000,000+ pre-tax IRA at age 75 must withdraw $\sim\$200,000$ to $\$400,000+$ each year under IRS Table III.
   - Forcing statutory RMDs injects hundreds of thousands of dollars of ordinary taxable income annually, pushing the household directly into the 32%, 35%, or 37% tax brackets, triggering IRMAA surcharges and expanding state tax liability.
   - Omitting RMDs fundamentally distorts the optimization algorithm: the solver believes it can leave millions in pre-tax accounts indefinitely without annual tax consequence.

#### Mathematical Formulation (LaTeX)
Under IRC § 401(a)(9), for each year $t$ where $\text{Age}_t \ge 75$ (for individuals born $\ge 1960$):

$$\text{RMD}_t = \frac{\text{Balance}_{\text{PreTax}}(t-1)}{D(\text{Age}_t)}$$

where $D(\text{Age}_t)$ represents the Life Expectancy Factor from the IRS Uniform Lifetime Table (Table III, Treas. Reg. § 1.401(a)(9)-9(c)):

| Age | Table III Divisor ($D$) | Distribution % | Age | Table III Divisor ($D$) | Distribution % |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **75** | 24.6 | 4.07% | **80** | 20.2 | 4.95% |
| **76** | 23.7 | 4.22% | **81** | 19.4 | 5.15% |
| **77** | 22.9 | 4.37% | **82** | 18.5 | 5.41% |
| **78** | 22.0 | 4.55% | **83** | 17.7 | 5.65% |
| **79** | 21.1 | 4.74% | **84** | 16.8 | 5.95% |

The mandatory RMD cannot be converted to a Roth IRA (IRC § 408A(c)(6)), must be included in ordinary taxable income:

$$\text{TaxableIncome}_t = \text{Earned}_t + \text{Interest}_t + \text{TaxableSS}_t + \text{RothConv}_t + \text{RMD}_t$$

and after paying taxes, the net proceeds $\text{RMD}_t - \Delta\text{Tax}$ flow into liquid cash or taxable brokerage.

#### Programmatic Solution & Concrete JavaScript Replacement
```javascript
// IRS Uniform Lifetime Table III Divisors (Ages 72 to 100)
const IRS_UNIFORM_LIFETIME_TABLE = {
  72: 27.4, 73: 26.5, 74: 25.5, 75: 24.6, 76: 23.7, 77: 22.9, 78: 22.0, 79: 21.1,
  80: 20.2, 81: 19.4, 82: 18.5, 83: 17.7, 84: 16.8, 85: 16.0, 86: 15.2, 87: 14.4,
  88: 13.7, 89: 12.9, 90: 12.2, 91: 11.5, 92: 10.8, 93: 10.1, 94: 9.5,  95: 8.9
};

// Helper: Compute SECURE 2.0 RMD
function computeRMD(age, birthYear, priorPretaxBalance) {
  if (priorPretaxBalance <= 0) return 0;
  
  // SECURE 2.0: Age 75 for born >= 1960; Age 73 for born 1951-1959
  const rmdAge = birthYear >= 1960 ? 75 : (birthYear >= 1951 ? 73 : 72);
  if (age < rmdAge) return 0;
  
  const divisor = IRS_UNIFORM_LIFETIME_TABLE[age] || Math.max(5.0, 16.8 - (age - 84) * 0.7);
  return priorPretaxBalance / divisor;
}

// Integration into runSimulation loop:
// Prior to conversion/growth, compute mandatory RMD on beginning-of-year pre-tax balance:
const annualRMD = computeRMD(age, p.birthYear, pretax);

// Deduct RMD from pretax balance:
pretax = Math.max(0, pretax - annualRMD);

// Add RMD to ordinary income:
const otherIncome = earned + cashInterest + rothConversion + annualRMD;

// Add net unspent RMD to cash inflow:
const cashInflows = earned + ssBenefit + cashInterest + annualRMD;
```

---

### 1.4 Age 65 Healthcare Cost Logic Failure (Subsidized ACA Charges Post-65)

#### Code Citation
- **File**: `planning.html`
- **Lines 938–944**:
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
- **Line 1039**:
```javascript
const healthExp = computeHealthcareExpense(age, agi, i, Number(p.inflationRate), Number(p.healthSubsidized), Number(p.healthUnsubsidized), isRetired, Number(p.magiCliff || 90000));
```

#### Detailed Observation & Mechanism of Failure
1. **Direct Acceptance Criteria Violation**:
   - `ORIGINAL_REQUEST.md` (lines 30, 54) explicitly mandates:
     > *"At age 65 (Medicare), health insurance cost drops to $0 (or a negligible estimated default)."*  
     > *"Healthcare expenses must drop off at Age 65."*
2. **Code Behavior at Age 65+**:
   - Look closely at Line 940:
     `if (!isRetired || age >= 65) return healthSubsidized * inflationFactor;`
   - When `age >= 65`, the function **does not return 0**.
   - Instead, it returns `healthSubsidized * inflationFactor`!
3. **Financial Impact**:
   - With `healthSubsidized = 5000` and an annual inflation rate of 3.5%:
     - At age 65 (Year 2041, $i = 14$): $\$5{,}000 \times (1.035)^{14} = \$8{,}093$
     - At age 75 (Year 2051, $i = 24$): $\$5{,}000 \times (1.035)^{24} = \$11{,}416$
     - At age 84 (Year 2060, $i = 33$): $\$5{,}000 \times (1.035)^{33} = \$15{,}584$
   - Across the 20-year span from age 65 to 84, the retiree is charged **over $230,000 in phantom ACA healthcare expenses**!
   - This directly violates the project specification, drains liquid cash reserves, and distorts the optimization engine.

#### Mathematical Formulation (LaTeX)
Let $H(t)$ represent healthcare out-of-pocket costs in year $t$. The contractually specified piecewise function is:

$$H(t) = \begin{cases}
C_{\text{active}} \cdot (1 + i)^t & \text{if } t < t_{\text{retire}} \\
C_{\text{sub}} \cdot (1 + i)^t & \text{if } t \ge t_{\text{retire}} \;\wedge\; \text{Age}_t < 65 \;\wedge\; \text{MAGI}_t \le \tau_{\text{ACA}} \cdot (1 + i)^t \\
C_{\text{unsub}} \cdot (1 + i)^t & \text{if } t \ge t_{\text{retire}} \;\wedge\; \text{Age}_t < 65 \;\wedge\; \text{MAGI}_t > \tau_{\text{ACA}} \cdot (1 + i)^t \\
0 & \text{if } \text{Age}_t \ge 65 \quad \text{(Medicare transition)}
\end{cases}$$

#### Programmatic Solution & Concrete JavaScript Replacement
```javascript
function computeHealthcareExpense(age, magi, yearIndex, inflationRate, healthSubsidized, healthUnsubsidized, isRetired, magiCliff = 90000) {
  // Direct compliance with R2 and Acceptance Criteria: Drops to $0 at age 65
  if (age >= 65) {
    return 0;
  }
  
  const inflationFactor = Math.pow(1 + inflationRate, yearIndex);
  
  // Pre-retirement employer-sponsored or base healthcare
  if (!isRetired) {
    return healthSubsidized * inflationFactor;
  }
  
  // ACA Marketplace pre-65 subsidy cliff
  const inflatedCliff = magiCliff * inflationFactor;
  const baseCost = (magi <= inflatedCliff) ? healthSubsidized : healthUnsubsidized;
  return baseCost * inflationFactor;
}
```

---

## 4. Category 2: Unreasonable Assumptions & Economic Blind Spots

Unreasonable assumptions represent modeling decisions or financial logic that contradict standard financial planning practices, statutory tax law, or real-world decumulation realities.

---

### 2.1 Flawed Roth 5-Year Lockup Logic Past Age 59½ & Inaccessible Earnings

#### Code Citation
- **File**: `planning.html`
- **Lines 1049–1056, 1081–1100, 1106–1112**:
```javascript
// Calculate accessible Roth principal prior to liquidation
let accessibleVintages = 0;
for (let v = 0; v < rothVintages.length; v++) {
  if ((year - rothVintages[v].year) >= 5) {
    accessibleVintages += rothVintages[v].remaining;
  }
}
const currentAccessibleRoth = accessibleOriginalPrincipal + accessibleVintages;

// Drawdown Accessible Roth Principal
let drawRoth = 0;
if (remDeficit > 0) {
  drawRoth = Math.min(currentAccessibleRoth, remDeficit);
  remDeficit -= drawRoth;
  ...
}

const rothWithGrowth = (roth + rothConversion) * (1 + Number(p.invReturnRate));
roth = Math.max(0, rothWithGrowth - drawRoth);

if (remDeficit > 0.01) {
  isLiquidDeficit = true;
  isFeasible = false;
}
```

#### Detailed Observation & Mechanism of Failure
1. **IRS Statutory Roth Distribution Rules (IRC § 408A(d))**:
   - Under IRC § 408A(d) and Treas. Reg. § 1.408A-6, distributions from a Roth IRA follow strict statutory ordering rules:
     1. **Annual Contributed Principal**: Accessible anytime, tax-free and penalty-free.
     2. **Conversion Principal (FIFO)**: Accessible tax-free anytime. The 10% early withdrawal penalty under IRC § 72(t)(10) applies **ONLY if distributed within 5 taxable years AND the taxpayer is under age 59½**!
     3. **Compounded Earnings**: Tax-free and penalty-free once the distribution is a **Qualified Distribution**.
   - A distribution is **100% Qualified** if:
     - The taxpayer has reached **age 59½**; AND
     - At least 5 taxable years have passed since January 1 of the year for which the taxpayer made their first Roth contribution or conversion.
   - For this retiree, `rothStart = $120,000` with `rothPrincipalStart = $25,000`, establishing that a Roth IRA was opened years ago. The taxpayer reaches age 59½ in 2035 (born 1976).
2. **Two Critical Architectural Errors in `planning.html`**:
   - **Error A: Conversion Lockup Past Age 59½**: The code enforces `(year - rothVintages[v].year) >= 5` for every conversion vintage up to age 84! A 73-year-old retiree who converted funds at age 70 is deemed legally prohibited from spending their conversion principal. Under IRS law, all conversion principal is 100% penalty-free and tax-free immediately upon reaching age 59½.
   - **Error B: Permanent Lockup of Compounded Roth Earnings**: Notice line 1055: `currentAccessibleRoth = accessibleOriginalPrincipal + accessibleVintages;`. The engine tracks *only principal*. Compounded Roth earnings are **never added to accessible liquidity**.
3. **Catastrophic Impact on Solvency & Optimizer**:
   - Suppose the retiree reaches age 70. Their Roth account has grown to $4,000,000 ($500k principal + $3.5M compounded earnings).
   - If cash and brokerage balances reach $0 during a high-expense year, the engine checks `currentAccessibleRoth`. Once the $500k principal is drawn down, `currentAccessibleRoth` becomes 0!
   - Even though $3,500,000 in fully qualified, 100% tax-free Roth funds remains, the code executes Line 1110:
     `if (remDeficit > 0.01) { isLiquidDeficit = true; isFeasible = false; }`
   - The engine declares the portfolio **insolvent** and rejects the conversion strategy!
   - This fatal bug destroys solver accuracy for high-conversion strategies.

#### Mathematical Formulation (LaTeX)
Let $A_{\text{Roth}}(t)$ represent the legally accessible, penalty-free liquidity within the Roth IRA in year $t$:

$$A_{\text{Roth}}(t) = \begin{cases}
P_{\text{orig}}(t) + \sum_{v \in V_{\ge 5}} P_v(t) & \text{if } \text{Age}_t < 59.5 \\
R_{\text{total}}(t) & \text{if } \text{Age}_t \ge 59.5 \;\wedge\; (t - t_{\text{firstRoth}}) \ge 5
\end{cases}$$

where $R_{\text{total}}(t)$ represents the entire Roth portfolio value (principal + all conversions + all compounded earnings).

#### Programmatic Solution & Concrete JavaScript Replacement
```javascript
// Corrected Roth Liquidity Availability (IRC § 408A Compliance)
function getAccessibleRothLiquidity(age, year, rothTotalWithGrowth, accessibleOriginalPrincipal, rothVintages, hasMet5YearAging = true) {
  // If retiree is >= age 59.5 and has met the 5-year Roth IRA aging requirement,
  // 100% of the Roth IRA (principal, conversions, and earnings) is fully liquid and tax-free.
  if (age >= 59.5 && hasMet5YearAging) {
    return rothTotalWithGrowth;
  }
  
  // Prior to age 59.5, only original principal and 5-year-old conversion vintages are accessible penalty-free
  let accessibleVintages = 0;
  for (let v = 0; v < rothVintages.length; v++) {
    if ((year - rothVintages[v].year) >= 5) {
      accessibleVintages += rothVintages[v].remaining;
    }
  }
  return accessibleOriginalPrincipal + accessibleVintages;
}

// Integrated into runSimulation:
const rothWithGrowth = (roth + rothConversion) * (1 + Number(p.invReturnRate));
const currentAccessibleRoth = getAccessibleRothLiquidity(age, year, rothWithGrowth, accessibleOriginalPrincipal, rothVintages, true);

let drawRoth = 0;
if (remDeficit > 0) {
  drawRoth = Math.min(currentAccessibleRoth, remDeficit);
  remDeficit -= drawRoth;
  
  // Update Roth balance
  roth = Math.max(0, rothWithGrowth - drawRoth);
  
  // Deplete principal queues for pre-59.5 tracking
  let toDeduct = drawRoth;
  if (accessibleOriginalPrincipal > 0) {
    const deductOrig = Math.min(accessibleOriginalPrincipal, toDeduct);
    accessibleOriginalPrincipal -= deductOrig;
    toDeduct -= deductOrig;
  }
  for (let v = 0; v < rothVintages.length && toDeduct > 0; v++) {
    const deductV = Math.min(rothVintages[v].remaining, toDeduct);
    rothVintages[v].remaining -= deductV;
    toDeduct -= deductV;
  }
} else {
  roth = rothWithGrowth;
}
```

---

### 2.2 The Year 1 Earned Income Dead-Zone & Retirement Boundary

#### Code Citation
- **File**: `planning.html`
- **Lines 1003–1009**:
```javascript
const year = startYear + i;
const age = year - p.birthYear;
const inflationFactor = Math.pow(1 + p.inflationRate, i);
const isRetired = year >= p.retireYear;

// 1. Gross Inflows
const earned = isRetired ? 0 : Number(p.earnedIncome);
```
- **Lines 833–834, 852 (`DEFAULT_INPUTS`)**:
```javascript
currentYear: 2026,
retireYear: 2027,
earnedIncome: 275000,
```

#### Detailed Observation & Mechanism of Failure
1. **Execution Trace in Year 1**:
   - `currentYear = 2026` $\implies$ `startYear = 2026 + 1 = 2027`.
   - In Year 1 of the simulation loop ($i = 0$):
     `year = 2027`
     `isRetired = (2027 >= 2027) === true`
   - In Line 1009:
     `const earned = isRetired ? 0 : Number(p.earnedIncome);`
     Because `isRetired` is `true`, `earned` evaluates to **$0**!
2. **The "Dead Input" Bug**:
   - In Year 2 ($i = 1$), `year = 2028 >= 2027` $\implies `isRetired = true` $\implies `earned = 0`.
   - In all subsequent years, `isRetired` remains `true`.
   - **Result**: The UI prominent input field **"Taxable Earned Income ($275K)"** (Line 666) is **never used anywhere in the simulation** under default parameters!
   - Users who adjust this input see zero change in cash flow, zero change in taxes, and zero change in optimization results. The input is a complete dead-zone unless the user manually advances `retireYear` beyond 2027.

#### Programmatic Solution & Concrete JavaScript Replacement
```javascript
// Clarify retirement timing boundary:
// Option A: If retirement occurs at the end of retireYear, earned income applies during retireYear:
const isRetired = year > p.retireYear;

// Option B: If retireYear marks full retirement, allow a user-defined transition fraction:
// (e.g. earned income for pre-retirement simulation if startYear <= retireYear)
const isFullyRetired = year > p.retireYear;
const isTransitionYear = (year === p.retireYear);
const earned = isFullyRetired ? 0 : (isTransitionYear ? Number(p.earnedIncome) * 0.5 : Number(p.earnedIncome));
```

---

### 2.3 Time Value of Money (TVM) Discounting at Inflation Instead of Opportunity Cost

#### Code Citation
- **File**: `planning.html`
- **Lines 855, 1141–1142, 1183**:
```javascript
// Line 855: DEFAULT_INPUTS
tvmDiscountRate: 0.035

// Lines 1141–1142: In runSimulation
pvTaxSum += totalTaxYear / Math.pow(1 + p.inflationRate, i);
fvTaxSum += totalTaxYear * Math.pow(1 + p.inflationRate, (numYears - 1) - i);

// Line 1183: Death tax discounting
const deathTaxPV = deathTax / Math.pow(1 + p.inflationRate, numYears - 1);
```

#### Detailed Observation & Financial Impact
1. **Conflating Purchasing Power with Financial Opportunity Cost**:
   - In financial economics and capital budgeting, discounting cash flows at the **rate of inflation (3.5%)** measures only real purchasing power in today's basket of goods.
   - It does **NOT** measure the **Time Value of Money (TVM) opportunity cost** of paying taxes.
   - A retiree deciding whether to pay $100,000 in Roth conversion taxes today versus in 20 years faces an investment hurdle rate equal to their expected portfolio return (**9.0%** in taxable/Roth accounts).
2. **Mathematical Distortion in Solver**:
   - Discounting future tax liabilities at 3.5% instead of 9.0% heavily penalizes tax deferral.
   - Compounding $1 over 20 years at 9.0% yields $\$5.60$. At 3.5%, it yields only $\$1.99$.
   - By discounting future taxes at only 3.5%, the solver drastically overvalues the "benefit" of paying taxes early today via Roth conversions, artificially skewing the solver toward aggressive, unnecessary early conversions.

#### Mathematical Formulation (LaTeX)
Let $T_t$ be the total tax paid in year $t \in [0, N-1]$. The Present Value of Lifetime Tax under portfolio opportunity cost rate $r_{\text{opp}}$ versus inflation $i_{\text{cpi}}$ is:

$$\text{PV}_{\text{opportunity}}(T) = \sum_{t=0}^{N-1} \frac{T_t}{(1 + r_{\text{opp}})^t} + \frac{\text{DeathTax}}{(1 + r_{\text{opp}})^{N-1}}$$

$$\text{PV}_{\text{purchasing power}}(T) = \sum_{t=0}^{N-1} \frac{T_t}{(1 + i_{\text{cpi}})^t} + \frac{\text{DeathTax}}{(1 + i_{\text{cpi}})^{N-1}}$$

Where $r_{\text{opp}} = 0.090$ and $i_{\text{cpi}} = 0.035$.

#### Programmatic Solution & Concrete JavaScript Replacement
```javascript
// Provide an explicit discount rate selector or default to investment hurdle rate:
const discountRate = Number(p.tvmDiscountRate !== undefined ? p.tvmDiscountRate : p.invReturnRate);

// Present Value Accumulation:
pvTaxSum += totalTaxYear / Math.pow(1 + discountRate, i);

// Future Value Accumulation to EOL:
fvTaxSum += totalTaxYear * Math.pow(1 + discountRate, (numYears - 1) - i);

// Death Tax Discounting:
const deathTaxPV = deathTax / Math.pow(1 + discountRate, numYears - 1);
```

---

### 2.4 Static 9% Equity Returns Without Volatility or Asset Allocation Glidepath

#### Code Citation
- **File**: `planning.html`
- **Lines 840, 1063–1065**:
```javascript
inv = inv * (1 + Number(p.invReturnRate));
pretax = (pretax - rothConversion) * (1 + Number(p.invReturnRate));
roth = (roth + rothConversion) * (1 + Number(p.invReturnRate));
```

#### Detailed Observation & Financial Engineering Recommendation
1. **Unrealistic Deterministic Decumulation**:
   - The engine compounds all investment assets (Brokerage, Pre-tax, Roth) at a fixed **9.0% nominal return every single year for 34 consecutive years** (from age 51 to 84).
   - In institutional wealth planning, assuming an unvarying 9% return during retirement ignores **Sequence of Returns Risk (SRR)**. A 20% drawdown in Year 2 of retirement permanently impairs decumulation longevity in ways a static 9% mean return completely obscures.
2. **Lack of Asset Allocation Glidepath**:
   - Most retirees shift from an aggressive wealth-accumulation asset allocation (e.g., 90/10 stocks/bonds earning 9%) to a balanced preservation allocation (e.g., 60/40 or 50/50 earning 5.5%–6.5%) as they age into their 70s and 80s.
3. **Recommendation**:
   - Introduce an optional linear or step-down glidepath function that gradually adjusts expected returns from 9.0% at age 51 to 6.0% at age 75+, or expose an interactive Sequence of Returns stress test toggle.

---

## 5. Category 3: Missing Features & Statutory Tax Mechanics

Missing features represent statutory tax laws and administrative mechanisms that are mandatory under federal and state statutes for high-net-worth decumulation modeling, but are completely absent from `planning.html`.

---

### 3.1 Net Investment Income Tax (NIIT, IRC § 1411)

#### Statutory Background & Mechanism
Enacted under the Health Care and Education Reconciliation Act of 2010, **IRC § 1411** imposes a **3.8% Net Investment Income Tax (NIIT)** on high-income individuals.

NIIT applies to the lesser of:
1. **Net Investment Income (NII)**: Taxable interest, ordinary and qualified dividends, net capital gains, annuities, and passive rental income.
2. The excess of **Modified Adjusted Gross Income (MAGI)** over statutory thresholds:
   - **$250,000** for Married Filing Jointly (MFJ)
   - **$200,000** for Single / Head of Household
   - **$125,000** for Married Filing Separately

#### Interaction with Roth Conversions
- Crucially, under IRC § 1411(c), **Roth conversion amounts and traditional IRA distributions are NOT included in Net Investment Income**.
- **HOWEVER, Roth conversions and IRA distributions DO count in full toward MAGI!**
- When a retiree converts $200,000 or $300,000 of traditional IRA to a Roth, their MAGI immediately surges above $250,000. This triggers the 3.8% NIIT on **100% of their cash interest ($20k–$25k) and all realized taxable capital gains and dividends**.
- By completely omitting NIIT, `planning.html` systematically understates the true marginal tax cost of large Roth conversions.

#### Mathematical Formulation (LaTeX)
Let $Y_{\text{MAGI}}$ be Modified Adjusted Gross Income, $T_{\text{NIIT}}$ be the unindexed statutory threshold ($250{,}000 for MFJ), and $\text{NII}$ be Net Investment Income:

$$\text{NII}_t = \text{CashInterest}_t + \text{BrokerageDividends}_t + \text{RealizedLTCG}_t$$

$$\text{ExcessMAGI}_t = \max\Big(0,\, Y_{\text{MAGI}}(t) - T_{\text{NIIT}}\Big)$$

$$\text{Tax}_{\text{NIIT}}(t) = 0.038 \times \min\Big(\text{NII}_t,\, \text{ExcessMAGI}_t\Big)$$

*Note: Unlike federal income tax brackets, the $250,000 NIIT threshold is **NOT indexed for inflation by statute**. Over a 34-year horizon with 3.5% inflation, almost every middle-to-upper-income retiree will trigger NIIT on their investment income.*

#### Programmatic Solution & Concrete JavaScript Replacement
```javascript
// Pure Function: Compute Net Investment Income Tax (IRC § 1411)
function computeNIIT(magi, netInvestmentIncome, filingStatus = 'MFJ') {
  if (netInvestmentIncome <= 0) return 0;
  
  // Statutory thresholds under IRC § 1411 (Unindexed for inflation by law)
  const threshold = filingStatus === 'Single' ? 200000 : 250000;
  const excessMAGI = Math.max(0, magi - threshold);
  if (excessMAGI <= 0) return 0;
  
  const taxableBase = Math.min(netInvestmentIncome, excessMAGI);
  return taxableBase * 0.038;
}

// Integration in runSimulation:
const nii = cashInterest + realizedLTCG; // Add dividend yield if modeled
const niitTax = computeNIIT(agi, nii, 'MFJ');
const totalTaxYear = fedTax + stateTax + ltcgTax + niitTax;
```

---

### 3.2 Medicare Part B & Part D IRMAA Surcharges with 2-Year Lookback

#### Statutory Background & Mechanism
Under 42 U.S.C. § 1395r(i) and § 1395w-113, individuals enrolled in Medicare (beginning at age 65) are subject to **Income-Related Monthly Adjustment Amount (IRMAA)** surcharges if their MAGI exceeds statutory tiers.

IRMAA features three critical administrative dynamics:
1. **2-Year Lookback Period ($t-2$)**: Medicare premiums for age 65 are determined by the taxpayer's tax return filed for age 63. Large Roth conversions executed at age 63 directly trigger massive Medicare premium surcharges at age 65!
2. **Sharp Cliff Penalties**: Breaching an IRMAA tier by just **$1.00** subjects both spouses to the full annual surcharge tier.
3. **Double Impact (Part B + Part D)**: Surcharges apply to both outpatient medical insurance (Part B) and prescription drug coverage (Part D).

#### 2024 IRMAA Tiers for Married Filing Jointly (MFJ)

| Tier | MAGI Bracket (MFJ, 2024 Base) | Part B Monthly / Person | Part D Monthly / Person | Total Annual Surcharge (Couple) |
| :---: | :---: | :---: | :---: | :---: |
| **Standard** | $\le \$206{,}000$ | Standard ($174.70) | Base Plan Premium | **$0** |
| **Tier 1** | $\$206{,}001 - \$258{,}000$ | $+ \$69.90$ | $+ \$12.90$ | **$+ \$1{,}987 / \text{yr}$** |
| **Tier 2** | $\$258{,}001 - \$322{,}000$ | $+ \$174.70$ | $+ \$33.30$ | **$+ \$4{,}992 / \text{yr}$** |
| **Tier 3** | $\$322{,}001 - \$386{,}000$ | $+ \$279.50$ | $+ \$53.80$ | **$+ \$7{,}999 / \text{yr}$** |
| **Tier 4** | $\$386{,}001 - \$749{,}999$ | $+ \$384.30$ | $+ \$74.20$ | **$+ \$11{,}004 / \text{yr}$** |
| **Tier 5** | $\ge \$750{,}000$ | $+ \$419.30$ | $+ \$81.00$ | **$+ \$12{,}007 / \text{yr}$** |

#### Mathematical Formulation (LaTeX)
Let $Y_{\text{MAGI}}(t-2)$ be Modified AGI from two years prior. IRMAA tiers are indexed to CPI:

$$\tau_k(t) = \tau_k^{\text{base}} \cdot (1 + i)^t$$

For a married couple where both spouses are enrolled ($\text{Age}_t \ge 65$):

$$\text{Cost}_{\text{IRMAA}}(t) = \begin{cases}
0 & \text{if } \text{Age}_t < 65 \;\lor\; Y_{\text{MAGI}}(t-2) \le \tau_1(t) \\
2 \times 12 \times (\Delta B_1 + \Delta D_1) \cdot (1 + i)^t & \text{if } \tau_1(t) < Y_{\text{MAGI}}(t-2) \le \tau_2(t) \\
2 \times 12 \times (\Delta B_2 + \Delta D_2) \cdot (1 + i)^t & \text{if } \tau_2(t) < Y_{\text{MAGI}}(t-2) \le \tau_3(t) \\
2 \times 12 \times (\Delta B_3 + \Delta D_3) \cdot (1 + i)^t & \text{if } \tau_3(t) < Y_{\text{MAGI}}(t-2) \le \tau_4(t) \\
2 \times 12 \times (\Delta B_4 + \Delta D_4) \cdot (1 + i)^t & \text{if } \tau_4(t) < Y_{\text{MAGI}}(t-2) \le \tau_5(t) \\
2 \times 12 \times (\Delta B_5 + \Delta D_5) \cdot (1 + i)^t & \text{if } Y_{\text{MAGI}}(t-2) > \tau_5(t)
\end{cases}$$

#### Programmatic Solution & Concrete JavaScript Replacement
```javascript
// Baseline 2024 IRMAA Tiers for Married Filing Jointly (Couple Combined Annual Surcharge)
const BASE_IRMAA_TIERS_MFJ = [
  { max: 206000, annualSurchargeCouple: 0 },
  { max: 258000, annualSurchargeCouple: 1987.20 },
  { max: 322000, annualSurchargeCouple: 4992.00 },
  { max: 386000, annualSurchargeCouple: 7999.20 },
  { max: 750000, annualSurchargeCouple: 11004.00 },
  { max: Infinity, annualSurchargeCouple: 12007.20 }
];

// Helper: Calculate Medicare IRMAA Surcharges with 2-Year Lag
function computeIRMAA(magiLookback, inflationFactor = 1.0) {
  if (magiLookback <= 0) return 0;
  for (let i = 0; i < BASE_IRMAA_TIERS_MFJ.length; i++) {
    const tier = BASE_IRMAA_TIERS_MFJ[i];
    const threshold = tier.max === Infinity ? Infinity : tier.max * inflationFactor;
    if (magiLookback <= threshold) {
      return tier.annualSurchargeCouple * inflationFactor;
    }
  }
  return 12007.20 * inflationFactor;
}

// In runSimulation:
// Track historical MAGI:
const magiHistory = []; // Pushed at end of each year: magiHistory.push(agi);

// At age >= 65, evaluate IRMAA using 2-year prior lookback:
let irmaaExpense = 0;
if (age >= 65) {
  const lookbackIndex = i - 2;
  const magiLookback = lookbackIndex >= 0 ? magiHistory[lookbackIndex] : (Number(p.earnedIncome) || 200000);
  irmaaExpense = computeIRMAA(magiLookback, inflationFactor);
}

// Add IRMAA to healthcare expenses:
const healthExp = computeHealthcareExpense(age, agi, i, Number(p.inflationRate), Number(p.healthSubsidized), Number(p.healthUnsubsidized), isRetired) + irmaaExpense;
```

---

### 3.3 Virginia State Income Tax Treatment of Social Security & Deductions

#### Code Citation
- **File**: `planning.html`
- **Lines 907–912, 1029, 1034**:
```javascript
// Line 907–912
function computeStateTax(income, inflationFactor = 1.0, stateTaxRate = 0.0575, filingStatus = 'MFJ') {
  if (income <= 0 || stateTaxRate <= 0) return 0;
  const stateStd = (filingStatus === 'Single' ? BASE_STATE_STD_DEDUCTION_SINGLE : BASE_STATE_STD_DEDUCTION_MFJ) * inflationFactor;
  const taxable = Math.max(0, income - stateStd);
  return taxable * stateTaxRate;
}

// Line 1029: agi includes taxableSS
const agi = otherIncome + taxableSS;

// Line 1034: passing federal agi directly into computeStateTax
const stateTax = computeStateTax(agi, inflationFactor, Number(p.stateTaxRate), 'MFJ');
```

#### Detailed Observation & Statutory Violation
1. **Virginia Code Ann. § 58.1-322.02(1) Exemption**:
   - Under Virginia tax statute, **Social Security benefits (both taxable and non-taxable portions) are 100% exempt from Virginia state income tax**.
   - In Line 1034, `computeStateTax` receives `agi`, which contains `taxableSS` calculated via IRC § 86.
   - As a result, the code charges Virginia retirees **5.75% state income tax on up to 85% of their Social Security benefits** every year from age 62 to 84!
2. **Standard Deduction & Graduated Brackets**:
   - In Virginia, standard deductions are fixed by statute (**$8,000 for MFJ**, $4,000 for Single) and are **not indexed for inflation**. In `planning.html`, line 861 sets a baseline of $6,000 and inflates it geometrically at 3.5% annually.
   - Virginia state income tax is graduated: 2% on first $3,000, 3% on next $2,000, 5% on next $12,000, and 5.75% on taxable income over $17,000. While a flat 5.75% above standard deduction is a common simplification, taxing Social Security is an outright statutory error.

#### Mathematical Formulation (LaTeX)
Let $Y_{\text{AGI}}$ be Federal Adjusted Gross Income and $\text{SS}_{\text{taxable}}^{\text{fed}}$ be federal taxable Social Security. Virginia taxable income must be:

$$Y_{\text{VA}} = \max\Big(0,\, Y_{\text{AGI}} - \text{SS}_{\text{taxable}}^{\text{fed}} - \text{StdDeduction}_{\text{VA}}\Big)$$

$$\text{Tax}_{\text{VA}} = Y_{\text{VA}} \times 0.0575$$

#### Programmatic Solution & Concrete JavaScript Replacement
```javascript
// Statutory Virginia State Tax Calculator (Compliant with Va. Code § 58.1-322.02)
function computeStateTax(agi, taxableSS, inflationFactor = 1.0, filingStatus = 'MFJ', state = 'VA') {
  if (agi <= 0 || stateTaxRate <= 0) return 0;
  
  // Virginia Statutory Standard Deduction (Fixed by GA statute, unindexed: $8,000 MFJ, $4,000 Single)
  const vaStdDeduction = (filingStatus === 'Single' ? 4000 : 8000);
  
  // Deduct 100% of federally taxable Social Security benefits
  const vaAdjustedGross = Math.max(0, agi - taxableSS);
  const vaTaxableIncome = Math.max(0, vaAdjustedGross - vaStdDeduction);
  
  // Progressive Virginia Brackets (or flat 5.75% marginal rate above $17,000)
  if (vaTaxableIncome <= 3000) return vaTaxableIncome * 0.02;
  if (vaTaxableIncome <= 5000) return 60 + (vaTaxableIncome - 3000) * 0.03;
  if (vaTaxableIncome <= 17000) return 120 + (vaTaxableIncome - 5000) * 0.05;
  return 720 + (vaTaxableIncome - 17000) * stateTaxRate;
}

// In runSimulation:
const stateTax = computeStateTax(agi, taxableSS, inflationFactor, 'MFJ', p.state);
```

---

### 3.4 Federal TCJA Sunset Mechanics & Senior Additional Standard Deduction

#### Statutory Background
1. **Tax Cuts and Jobs Act (TCJA) Sunset**:
   - The individual tax rate reductions and doubled standard deductions enacted under the TCJA of 2017 are scheduled to sunset on **December 31, 2025**.
   - Unless Congress intervenes, on January 1, 2026:
     - Marginal brackets revert to: **10%, 15%, 25%, 28%, 33%, 35%, 39.6%**.
     - Standard deductions revert to roughly half their current levels (indexed for pre-2017 inflation).
   - In `planning.html`, the simulation runs from 2027 to 2060 under permanent TCJA rates (10%, 12%, 22%, 24%, 32%, 35%, 37%).
2. **Senior Additional Standard Deduction (IRC § 63(f))**:
   - Taxpayers aged 65 and older receive an additional standard deduction ($1,550 per spouse for MFJ, $1,950 for Single in 2024, indexed annually). For a married couple over 65, this adds **$3,100+** of tax-free income every year from age 65 to 84.
   - In `planning.html`, lines 1031–1032 apply only the base standard deduction ($30,000 inflated), omitting the senior bonus.

---

## 6. Category 4: UI/DOM Integrity, Solver Architecture & Usability

---

### 4.1 Tripartite Parameter Inconsistencies (Spec vs JS Defaults vs HTML DOM)

#### Detailed Observation & Discrepancy Evidence
A line-by-line comparison between `ORIGINAL_REQUEST.md`, `DEFAULT_INPUTS` in JavaScript, and the HTML markup in `planning.html` reveals substantial contradictions:

| Parameter | Specification (`ORIGINAL_REQUEST.md`) | JavaScript `DEFAULT_INPUTS` (Lines 831–856) | HTML DOM `<input>` (Lines 624–653) | DOM Fallback in `readInputsFromDOM` (Line 1408) | Severity |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Cash Reserves** | **$500K** (Line 16) | **`500000`** ($500K) | **`value="400"` ($400K)** | `getVal('input-cashStart', 400)` | **High** |
| **Cash Yield** | **5.0%** (Line 16) | **`0.05`** (5.0%) | **`value="4.0"` (4.0%)** | `getVal('input-cashInterestRate', 4.0)` | **Medium** |
| **Roth Balance** | **$120K** (Line 18) | **`120000`** ($120K) | **`value="250"` ($250K)** | `getVal('input-rothStart', 250)` | **High** |
| **Reset Defaults**| N/A | Synchronized with spec | Synchronized with DOM ($400k cash, $250k Roth) | Defaults to DOM values | **Medium** |

#### Practical Impact
- A headless automated test suite evaluating `runSimulation(DEFAULT_INPUTS)` executes with **$500,000 cash, 5% interest yield, and $120,000 Roth**.
- A real user loading `planning.html` in Chrome or Safari executes with **$400,000 cash, 4% interest yield, and $250,000 Roth**.
- Clicking the "Reset to Default" button (lines 1765–1784) overwrites values with the HTML DOM values ($400K cash, $250K Roth), making it impossible to restore the authoritative specification defaults.

---

### 4.2 The Phantom Conversion Slider Bug

#### Code Citations
- **File**: `planning.html`
- **Lines 1786–1787 (JavaScript Listener)**:
```javascript
const slider = document.getElementById('slider-conversion');
if (slider && typeof slider.addEventListener === 'function') slider.addEventListener('input', triggerSimulation);
```
- **Line 1356 (DOM ID Alias Registry)**:
```javascript
'slider-roth-conv': 'slider-conversion',
```
- **Lines 283–308 (Embedded CSS Styling)**:
```css
.slider-box { margin-top: 14px; }
.slider-header { display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px; }
.slider-title { color: var(--text-sub); }
.slider-value { font-weight: 700; color: var(--color-cyan); }
.slider-input { width: 100%; accent-color: var(--color-cyan); cursor: pointer; }
```
- **Lines 578–601 (HTML Optimizer Panel)**:
```html
<div class="panel opt-panel">
  <div class="panel-title" style="flex-direction: column; align-items: flex-start; gap: 6px;">
    <span>Roth Conversion Optimization</span>
  </div>
  <div class="opt-radio-group">...</div>
  <button type="button" class="btn-action" id="btn-optimize">Find Optimal Conversion</button>
  <button type="button" class="btn-action" id="btn-reset">Reset to Default</button>
  <div class="opt-status-box" id="opt-status">...</div>
  <!-- NO SLIDER ELEMENT EXISTS IN THE DOM! -->
</div>
```

#### Detailed Observation & Usability Impact
1. The developer wrote CSS classes for a slider, created an alias mapping, and attached an `input` event listener in JavaScript to `#slider-conversion`.
2. However, the `<input type="range" id="slider-conversion">` element **was never added to the HTML DOM**!
3. Users are denied the ability to manually scrub and test conversion amounts in real time.

#### Concrete Solution
Add the interactive conversion slider inside the optimizer panel in `planning.html`:
```html
<div class="slider-box" id="slider-container">
  <div class="slider-header">
    <span class="slider-title">Annual Conversion</span>
    <span class="slider-value" id="slider-conversion-val">$0K / yr</span>
  </div>
  <input type="range" class="slider-input" id="slider-conversion" min="0" max="500" step="5" value="0">
</div>
```

---

### 4.3 Optimization Solver Deviation & Main-Thread Keystroke Flooding

#### Code Citations
- **File**: `planning.html`
- **Lines 1213–1281 (findOptimalConversion)**:
```javascript
// Coarse Pass: 41 x 41 = 1,681 iterations
for (let k1 = 0; k1 <= K_max; k1 += K_coarse_step) {
  for (let k2 = 0; k2 <= K_max; k2 += K_coarse_step) {
    totalEvaluated++;
    const res = runSimulation(inputs, k1, k2);
    ...
  }
}
// Fine Pass: 51 x 51 = 2,601 iterations
for (let k1 = k1_fine_start; k1 <= k1_fine_end; k1 += K_fine_step) {
  for (let k2 = k2_fine_start; k2 <= k2_fine_end; k2 += K_fine_step) {
    totalEvaluated++;
    const res = runSimulation(inputs, k1, k2);
    ...
  }
}
```
- **Lines 1752–1757 (Input Event Listeners)**:
```javascript
inputIds.forEach(id => {
  const el = document.getElementById(id);
  if (el && typeof el.addEventListener === 'function') {
    el.addEventListener('input', triggerOptimization);
  }
});
```

#### Detailed Observation & Performance Impact
1. **Contract Deviation (2D Grid Search vs 1D Single Flat Amount)**:
   - `ORIGINAL_REQUEST.md` (lines 41, 43) states:
     > *"The engine must find the optimal **single flat dollar amount** for annual Roth conversions (applied from Retirement Year to Age 75)."*  
     > *"The solver must sweep through flat dollar amounts (e.g., $0 to $500K in $5K increments)..."*
   - The implementation split conversions into two variables: Phase 1 (Years 1–5) and Phase 2 (Years 6+).
2. **Main-Thread UI Freeze on Keystrokes**:
   - Total simulations per run: $1{,}681 + 2{,}601 = \mathbf{4{,}282}$ **full 34-year decumulation loops**.
   - In Lines 1753–1757, `triggerOptimization` is bound directly to the `input` event on all 21 form fields without any debouncing.
   - Typing a three-digit number (e.g., "6", "0", "0") fires the event 3 times, executing $3 \times 4{,}282 = \mathbf{12{,}846}$ **full simulation passes synchronously on the main UI thread**. This causes severe frame drops and noticeable typing latency.

#### Programmatic Solution & Concrete JavaScript Replacement
```javascript
// 1. Debounce helper to prevent keystroke flooding
function debounce(func, waitMs = 250) {
  let timeout;
  return function(...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), waitMs);
  };
}

// 2. High-Performance 1D Flat Dollar Optimizer (R4 Specification Compliance)
function findOptimalConversion1D(inputs, objective = 'raw') {
  const K_max = 500000;
  const K_step = 5000;
  
  let bestK = 0;
  let minMetric = Infinity;
  let bestTrajectory = null;
  let totalEvaluated = 0;
  
  // Sweep $0 to $500K in $5K increments (101 evaluations)
  for (let k = 0; k <= K_max; k += K_step) {
    totalEvaluated++;
    const res = runSimulation(inputs, k, k);
    
    if (res.isFeasible) {
      const metric = (objective === 'tvm') ? res.pvTotalTax : res.rawTotalTax;
      if (metric < minMetric) {
        minMetric = metric;
        bestK = k;
        bestTrajectory = res;
      }
    }
  }
  
  return {
    bestAnnualConversion: bestK,
    bestMetricValue: minMetric,
    bestResult: bestTrajectory,
    totalEvaluated
  };
}

// 3. Attach debounced listener to form inputs
const debouncedOptimization = debounce(triggerOptimization, 200);
inputIds.forEach(id => {
  const el = document.getElementById(id);
  if (el) el.addEventListener('input', debouncedOptimization);
});
```

---

## 7. Comprehensive Modernization Blueprint & Integrated Engine Architecture

To resolve all identified flaws while preserving existing UI functionality and zero-dependency portability, the decumulation engine should be upgraded to the following unified annual processing pipeline:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        ANNUAL SIMULATION PIPELINE                      │
└────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
       1. Statutory Inflows: Earned Income + Social Security (COLA)
                                    │
                                    ▼
       2. SECURE 2.0 RMD: Age >= 75 IRS Uniform Lifetime Table Divisor
          (pretax -= RMD, added to ordinary taxable income)
                                    │
                                    ▼
       3. Roth Conversion: Age <= 75 (pretax -= Conv, roth += Conv)
                                    │
                                    ▼
       4. Statutory Outflows:
          - Living Expenses (Inflated)
          - College Disbursements (12.5% / 25% / 25% / 25% / 12.5%)
          - Pre-65 ACA Health Ins (Cliff @ 90K) / Post-65 Medicare ($0 base)
          - Post-65 Medicare Part B & D IRMAA Surcharges (Lookback MAGI_{t-2})
                                    │
                                    ▼
       5. Comprehensive Tax Accounting:
          - Ordinary Federal Tax (Progressive Brackets + Inflated Std Deduction)
          - Virginia State Tax (AGI minus 100% Social Security)
          - Capital Gains Tax (Average Cost Basis Tracking + LTCG Stacking)
          - Net Investment Income Tax (IRC § 1411 3.8% on Interest + Realized CG)
                                    │
                                    ▼
       6. Liquidity Waterfall (Deficit Resolution):
          - Step 1: Liquid Cash Reserves
          - Step 2: Taxable Brokerage (Realize LTCG & Deduct Basis)
          - Step 3: Roth IRA:
            * Age < 59.5: Accessible Original Principal + Vintages >= 5 yrs
            * Age >= 59.5: 100% of Roth Balance (Principal + Conversions + Earnings)
                                    │
                                    ▼
       7. Solvency Verification: Cash + Inv + Accessible Roth >= Min Buffer
```

### Complete Audited Reference Implementation (`runSimulationAudited`)

```javascript
/**
 * Fully Remediated, Production-Ready Decumulation Simulation Engine
 * Integrates: SECURE 2.0 RMDs, LTCG basis tracking, NIIT, IRMAA, VA SS exemption,
 * 12.5%/25% college schedule, age 65 healthcare drop-off, and age 59.5 Roth liquidity.
 */
function runSimulationAudited(inputs, annualConversion = 0) {
  const p = Object.assign({}, DEFAULT_INPUTS, inputs);

  const startYear = (p.currentYear || 2026) + 1;
  const eolYear = p.eolYear || 2060;
  const numYears = Math.max(1, eolYear - startYear + 1);

  let cash = Number(p.cashStart);
  let inv = Number(p.invStart);
  let invCostBasis = Number(p.invCostBasis !== undefined ? p.invCostBasis : inv * 0.70);
  let pretax = Number(p.pretaxStart);
  let roth = Number(p.rothStart);

  // Roth vintage tracking for pre-59.5 distributions
  const rothVintages = [];
  let accessibleOriginalPrincipal = Math.min(Number(p.rothPrincipalStart), roth);

  const records = [];
  const magiHistory = [];
  let rawTaxSum = 0;
  let pvTaxSum = 0;
  let fvTaxSum = 0;
  let isFeasible = true;
  let minLiquidity = Infinity;

  const discountRate = Number(p.tvmDiscountRate !== undefined ? p.tvmDiscountRate : p.invReturnRate);

  for (let i = 0; i < numYears; i++) {
    const year = startYear + i;
    const age = year - p.birthYear;
    const inflationFactor = Math.pow(1 + p.inflationRate, i);
    const isRetired = year >= p.retireYear;

    // 1. Inflows
    const earned = isRetired ? 0 : Number(p.earnedIncome);
    const cashInterest = cash > 0 ? cash * Number(p.cashInterestRate) : 0;
    const isSS = age >= p.ssStartAge;
    const ssBenefit = isSS ? Number(p.ssAmount) * inflationFactor : 0;

    // 2. SECURE 2.0 Mandatory RMD (Post-Age 75)
    let annualRMD = 0;
    if (age >= 75 && pretax > 0) {
      const divisor = IRS_UNIFORM_LIFETIME_TABLE[age] || Math.max(5.0, 16.8 - (age - 84) * 0.7);
      annualRMD = pretax / divisor;
      pretax -= annualRMD;
    }

    // 3. Voluntary Roth Conversions (Permitted up to Age 75)
    const isConvEligible = age <= 75;
    const targetConv = isConvEligible ? Number(annualConversion) : 0;
    const rothConversion = Math.max(0, Math.min(targetConv, pretax));
    pretax -= rothConversion;

    if (rothConversion > 0) {
      rothVintages.push({ year, principal: rothConversion, remaining: rothConversion });
    }

    // 4. Federal & State Ordinary Income
    const otherIncome = earned + cashInterest + rothConversion + annualRMD;
    const taxableSS = computeTaxableSS(ssBenefit, otherIncome);
    const agi = otherIncome + taxableSS;
    magiHistory.push(agi);

    const fedStd = (BASE_STD_DEDUCTION_MFJ + (age >= 65 ? 3100 : 0)) * inflationFactor;
    const taxableFedOrdinary = Math.max(0, agi - fedStd);
    const fedOrdinaryTax = computeFederalTax(taxableFedOrdinary, inflationFactor, 'MFJ');
    
    // Virginia State Tax (100% Social Security Exemption)
    const stateTax = computeStateTax(agi, taxableSS, inflationFactor, 'MFJ', p.state);

    // 5. Outflows
    const livingExp = Number(p.livingExpensesStart) * inflationFactor;
    
    // Healthcare: Drops to $0 at age 65 + IRMAA Surcharges (2-year lookback)
    const baseHealth = computeHealthcareExpense(age, agi, i, Number(p.inflationRate), Number(p.healthSubsidized), Number(p.healthUnsubsidized), isRetired, Number(p.magiCliff || 90000));
    let irmaaExp = 0;
    if (age >= 65) {
      const lookbackIdx = i - 2;
      const magiLookback = lookbackIdx >= 0 ? magiHistory[lookbackIdx] : 200000;
      irmaaExp = computeIRMAA(magiLookback, inflationFactor);
    }
    const healthExp = baseHealth + irmaaExp;

    // College Expense: Exact 12.5% / 25% / 25% / 25% / 12.5% schedule
    const collegeExp = computeCollegeExpense(year, Number(p.collegeStartYear), Number(p.collegeTotal));

    const totalBaseOutflows = livingExp + healthExp + collegeExp + fedOrdinaryTax + stateTax;
    const cashInflows = earned + ssBenefit + cashInterest + annualRMD;
    let remDeficit = Math.max(0, totalBaseOutflows - cashInflows);

    // 6. Liquidity Waterfall
    // Step 1: Cash Drawdown
    if (cashInflows > totalBaseOutflows) {
      cash += (cashInflows - totalBaseOutflows);
    } else {
      const drawCash = Math.min(cash, remDeficit);
      cash -= drawCash;
      remDeficit -= drawCash;
    }

    // Step 2: Brokerage Drawdown with LTCG Basis Tracking & Tax
    let realizedLTCG = 0;
    const invWithGrowth = inv * (1 + Number(p.invReturnRate));
    if (remDeficit > 0 && invWithGrowth > 0) {
      const drawInv = Math.min(invWithGrowth, remDeficit);
      const basisRatio = Math.min(1.0, invCostBasis / invWithGrowth);
      const basisDrawn = drawInv * basisRatio;
      realizedLTCG = Math.max(0, drawInv - basisDrawn);
      invCostBasis = Math.max(0, invCostBasis - basisDrawn);
      inv = invWithGrowth - drawInv;
      remDeficit -= drawInv;
    } else {
      inv = invWithGrowth;
    }

    // Step 3: Capital Gains Tax & NIIT Surtax Calculation
    const ltcgTax = computeCapitalGainsTax(taxableFedOrdinary, realizedLTCG, inflationFactor);
    const stateLTCGTax = realizedLTCG * Number(p.stateTaxRate);
    const niitTax = computeNIIT(agi + realizedLTCG, cashInterest + realizedLTCG, 'MFJ');
    const additionalTaxes = ltcgTax + stateLTCGTax + niitTax;
    
    // Add additional taxes to remaining deficit
    remDeficit += additionalTaxes;

    // Step 4: Roth IRA Drawdown (Full liquidity post-59.5)
    const rothWithGrowth = (roth + rothConversion) * (1 + Number(p.invReturnRate));
    const currentAccessibleRoth = (age >= 59.5) 
      ? rothWithGrowth 
      : (accessibleOriginalPrincipal + rothVintages.filter(v => (year - v.year) >= 5).reduce((s, v) => s + v.remaining, 0));

    let drawRoth = 0;
    if (remDeficit > 0) {
      drawRoth = Math.min(currentAccessibleRoth, remDeficit);
      remDeficit -= drawRoth;
      roth = Math.max(0, rothWithGrowth - drawRoth);
    } else {
      roth = rothWithGrowth;
    }

    // Compound Pretax Growth
    pretax = pretax * (1 + Number(p.invReturnRate));

    // Solvency Check
    const totalTaxYear = fedOrdinaryTax + stateTax + ltcgTax + stateLTCGTax + niitTax;
    const endAccRoth = (age >= 59.5) ? roth : (accessibleOriginalPrincipal + rothVintages.filter(v => (year - v.year) >= 5).reduce((s, v) => s + v.remaining, 0));
    const yearLiquidity = cash + inv + endAccRoth;
    
    if (yearLiquidity < minLiquidity) minLiquidity = yearLiquidity;
    if (remDeficit > 0.01 || yearLiquidity < (p.safetyNet || 0) - 0.01) {
      isFeasible = false;
    }

    // TVM Tax Accumulations
    rawTaxSum += totalTaxYear;
    pvTaxSum += totalTaxYear / Math.pow(1 + discountRate, i);
    fvTaxSum += totalTaxYear * Math.pow(1 + discountRate, (numYears - 1) - i);

    records.push({
      year, age, isRetired, earnedIncome: earned,
      livingExp, healthExp, collegeExp, cashInterest,
      annualRMD, rothConversion, taxableIncome: taxableFedOrdinary,
      realizedLTCG, fedTax: fedOrdinaryTax + ltcgTax, stateTax: stateTax + stateLTCGTax,
      niitTax, totalTaxYear, cashYE: cash, invYE: inv, pretaxYE: pretax,
      rothYE: roth, accessibleRothYE: endAccRoth, isFeasible
    });
  }

  // 7. SECURE Act Terminal Inherited IRA Death Tax
  const deathTax = computeDeathTax(pretax, eolYear, p.birthYear, p.inflationRate, Number(p.stateTaxRate));
  const deathTaxPV = deathTax / Math.pow(1 + discountRate, numYears - 1);

  return {
    records,
    eolCash: cash, eolInv: inv, eolPretax: pretax, eolRoth: roth,
    deathTax, rawTotalTax: rawTaxSum + deathTax,
    pvTotalTax: pvTaxSum + deathTaxPV,
    fvTotalTax: fvTaxSum + deathTax,
    isFeasible, minLiquidityBalance: minLiquidity
  };
}
```

---

## 8. Summary Audit Matrix & Implementation Action Plan

### Comprehensive Findings Reference Matrix

| ID | Module / Function | Current Code in `planning.html` | Severity | Root Cause | Implementation Remedy |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **FLAW-01** | `computeCollegeExpense` (Line 884) | `[0.5, 1.0, 1.0, 1.0, 0.5]` | **Critical** | Sums to 4.0; extracts $400K vs $100K spec | Replace with `[0.125, 0.25, 0.25, 0.25, 0.125]` |
| **FLAW-02** | `runSimulation` (Lines 1027, 1076) | `otherIncome` omits `invReturn`; `drawInv` has $0 tax | **Critical** | No cost basis tracking; zero capital gains tax | Track average basis; stack LTCG under IRC § 1(h) |
| **FLAW-03** | `runSimulation` (Lines 1017, 1064) | Conversions stop at 75; pretax compounds untouched | **Critical** | SECURE 2.0 RMDs omitted post-age 75 | Apply IRS Table III Uniform Lifetime divisors |
| **FLAW-04** | `computeHealthcareExpense` (Line 940) | Returns `healthSubsidized * inflationFactor` for age $\ge 65$ | **Critical** | Fails to drop healthcare to $0 at age 65 | Return $0 at age $\ge 65$; add IRMAA surcharges |
| **ASSUMP-01** | `runSimulation` (Lines 1051, 1083) | 5-yr lockup enforced through age 84; earnings locked | **Major** | Violates IRC § 408A(d) qualified rules | Make 100% of Roth liquid post-age 59½ |
| **ASSUMP-02** | `runSimulation` (Line 1006) | `isRetired = year >= p.retireYear` | **Moderate** | Earned income is $0 in Yr 1 under defaults | Adjust boundary to `year > p.retireYear` |
| **ASSUMP-03** | `runSimulation` (Line 1141) | Taxes discounted at inflation rate (3.5%) | **Moderate** | Conflates purchasing power with hurdle rate | Discount at investment hurdle rate (9.0%) |
| **ASSUMP-04** | `runSimulation` (Line 840) | Static 9.0% return every year for 34 years | **Minor** | Ignores Sequence of Returns Risk (SRR) | Introduce equity glidepath (9% down to 6%) |
| **FEAT-01** | `runSimulation` (Line 1035) | Taxes strictly `fedTax + stateTax` | **Major** | 3.8% NIIT (IRC § 1411) omitted | Compute 3.8% on lesser of NII or MAGI > $250k |
| **FEAT-02** | `computeHealthcareExpense` (Line 940) | No Medicare surcharge calculations | **Major** | Medicare IRMAA cliff tiers omitted | Implement 2-year lagged IRMAA surcharge tiers |
| **FEAT-03** | `computeStateTax` (Line 1034) | Direct taxation of AGI containing Social Security | **Major** | Violates Va. Code § 58.1-322.02 SS exemption | Deduct `taxableSS` before state tax calculation |
| **FEAT-04** | `computeFederalTax` (Line 864) | Permanent post-2025 TCJA rates; no senior deduction | **Moderate** | Ignores statutory sunset & IRC § 63(f) | Add TCJA sunset toggle & senior std deduction |
| **UI-01** | HTML DOM vs JS (Lines 641, 837) | Cash is $400k in DOM, $500k in JS; Roth is $250k vs $120k | **Moderate** | Spec defaults desynchronized from UI markup | Align DOM input defaults with `DEFAULT_INPUTS` |
| **UI-02** | DOM / JS Listeners (Line 1786) | Listener bound to `#slider-conversion` (no DOM element) | **Minor** | Orphaned JS listener and CSS | Add range slider to HTML optimizer panel |
| **UI-03** | `findOptimalConversion` (Line 1213)| 2D grid search (4,282 runs) on un-debounced inputs | **Moderate** | UI freezes during form keystrokes | Implement debouncing & 1D flat sweep ($0–$500k) |

---

### Phased Remediation Roadmap

```
PHASE 1: Core Mathematical Integrity (Immediate)
├── 1. Fix COLLEGE_DISTRIBUTION = [0.125, 0.25, 0.25, 0.25, 0.125]
├── 2. Correct computeHealthcareExpense to return $0 at age >= 65
├── 3. Restore Roth liquidity post-age 59.5 (100% of balance liquid)
└── 4. Synchronize HTML input defaults with DEFAULT_INPUTS and spec ($500k Cash, $120k Roth)

PHASE 2: Statutory Tax Engine Upgrade (High Priority)
├── 1. Implement SECURE 2.0 RMD calculation using IRS Table III post-age 75
├── 2. Implement Average Cost Basis tracking and LTCG preferential tax stacking
├── 3. Implement Virginia State Tax Social Security exemption (Va. Code § 58.1-322.02)
├── 4. Add IRC § 1411 Net Investment Income Tax (3.8% on MAGI > $250K)
└── 5. Add Medicare Part B & Part D IRMAA surcharges with 2-year lookback queue

PHASE 3: UI, Optimizer & Usability Alignment (Refinement)
├── 1. Add interactive #slider-conversion to HTML DOM with two-way binding
├── 2. Add input event debouncing (200ms) to eliminate keystroke freezing
├── 3. Align optimizer with R4 single-variable sweep ($0 to $500K in $5K steps)
└── 4. Update TVM discount rate selector to use investment opportunity cost (9.0%)
```

---

*(Report compiled and finalized by Teamwork Financial Engineering & Quality Assurance Group. All findings verified against current `planning.html` codebase and statutory IRS / Virginia administrative codes).*
