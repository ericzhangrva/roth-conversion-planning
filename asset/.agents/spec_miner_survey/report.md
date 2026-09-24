# Lifetime Tax Simulation & Optimization Dashboard (`planning.html`)
## Formal Specification & Mathematical Requirements Formulation

**Document Version:** 1.0.0  
**Author:** `spec_miner_survey`  
**Date:** 2026-09-23  
**Status:** Approved Specification  
**Target File:** `/Users/eric/Dropbox/ai/asset/planning.html`  

---

## 1. Executive Summary & Problem Formulation

The objective is to build a standalone, single-file financial web application (`planning.html`) utilizing vanilla HTML5, modern CSS, JavaScript (ES6+), and Chart.js (via CDN). The application models the multi-decade decumulation phase of an executive household from retirement to End of Life (EOL).

The central problem solved by the engine is:
> **Find the optimal flat annual Roth conversion amount $K^*$ applied from the Retirement Year through Age 75 that minimizes total lifetime tax liability (either nominal raw tax or TVM-discounted tax), subject to the strict constraint that liquid wealth never drops below zero.**

At End of Life, any remaining pre-tax retirement balance is subject to a deferred "Death Tax" under the SECURE Act (liquidated by two heirs over 10 years). The engine must evaluate the trade-off between paying upfront income taxes during conversion years at lower marginal brackets versus leaving assets in traditional pre-tax accounts where they compound into a large terminal tax liability for the estate and heirs.

---

## 2. Requirement R1: UI Inputs, Data Types, Constraints & Defaults

The application interface must provide structured input controls grouped by category, with reactive two-way binding or an explicit "Recalculate / Optimize" trigger. All monetary inputs must support formatted display (commas, currency signs) and validate input bounds.

### R1 Input Parameters Specification Table

| # | Parameter Key | UI Label | Category | Data Type | Default Value | Valid Range | Unit / Format | Description & Behavior |
|---|---|---|---|---|---|---|---|---|
| 1 | `birthYear` | Birth Year | Timeline | Integer | `1976` | 1940 – 2010 | Year | Client's birth year. Age in year $y$ is $y - \text{birthYear}$. |
| 2 | `currentYear` | Current Year | Timeline | Integer | `2026` | 2020 – 2040 | Year | Simulation base year. Simulation runs from $y = \text{currentYear} + 1$. |
| 3 | `retirementYear` | Retirement Year | Timeline | Integer | `2027` | 2024 – 2050 | Year | Year retirement begins. Earned income drops to $0$ when $y \ge \text{retirementYear}$. Conversions begin in this year. |
| 4 | `eolYear` | End of Life Year | Timeline | Integer | `2060` | 2040 – 2100 | Year | Final simulation year (Age 84 for 1976 birth year). Death Tax is computed at the end of this year. |
| 5 | `inflationRate` | Inflation Rate | Economic | Float | `0.035` (3.5%) | 0.0% – 15.0% | Percentage | Cumulative compounding rate applied to Living Expenses, Healthcare, and Federal Tax Brackets. |
| 6 | `cashBalance` | Cash Reserves | Assets | Float | `$500,000` | $0 – $10M | USD ($) | Initial liquid cash balance at start of simulation. |
| 7 | `cashInterestRate` | Cash Interest Rate | Economic | Float | `0.05` (5.0%) | 0.0% – 15.0% | Percentage | Annual yield on cash reserves; taxed as ordinary income. |
| 8 | `invBalance` | Taxable Brokerage | Assets | Float | `$300,000` | $0 – $50M | USD ($) | Initial taxable brokerage investments at start of simulation. |
| 9 | `invReturnRate` | Investment Return | Economic | Float | `0.09` (9.0%) | 0.0% – 25.0% | Percentage | Annual return on taxable investments, pre-tax retirement, and Roth accounts. |
| 10 | `pretaxBalance` | Retirement Pre-tax | Assets | Float | `$5,000,000` | $0 – $50M | USD ($) | Traditional 401(k), 403(b), Cash Balance Plan balance. Taxed upon withdrawal/conversion and at death. |
| 11 | `rothBalance` | Retirement Roth | Assets | Float | `$120,000` | $0 – $20M | USD ($) | Total Roth account balance at start of simulation. Grows 100% tax-free. |
| 12 | `rothPrincipal` | Accessible Roth Principal | Assets | Float | `$25,000` | $0 – $rothBalance | USD ($) | Existing basis from direct contributions; accessible immediately in Year 1 without penalty or waiting period. |
| 13 | `collegeExpenses` | College Total Expense | Expenses | Float | `$100,000` | $0 – $2M | USD ($) | Total nominal college cost spread across 5 years. **Zero inflation applied.** |
| 14 | `collegeStartYear`| College Start Year | Expenses | Integer | `2029` | 2026 – 2050 | Year | Start year for the 5-year college expense schedule. |
| 15 | `healthSubsidized`| Healthcare (Subsidized) | Expenses | Float | `$5,000` | $0 – $50K | USD/yr | Annual health insurance premium if MAGI $\le$ Subsidy Cliff. Inflates annually until age 65. |
| 16 | `healthUnsubsidized`| Healthcare (Unsubsidized)| Expenses | Float | `$25,000` | $0 – $100K | USD/yr | Annual health insurance premium if MAGI $>$ Subsidy Cliff. Inflates annually until age 65. |
| 17 | `magiCliff` | Subsidy MAGI Cliff | Tax/Health | Float | `$90,000` | $30K – $300K | USD/yr | MAGI threshold switching healthcare from subsidized to unsubsidized. |
| 18 | `ssStartAge` | SS Start Age | Income | Integer | `62` | 62 – 70 | Age | Age when Social Security payments commence. |
| 19 | `ssAmount` | Social Security Amount | Income | Float | `$60,000` | $0 – $150K | USD/yr | Annual Social Security benefit at start age. Subject to annual COLA/inflation. |
| 20 | `earnedIncome` | Taxable Earned Income | Income | Float | `$275,000` | $0 – $2M | USD/yr | Pre-retirement salary/bonus. Valid only for years $y < \text{retirementYear}$. |
| 21 | `livingExpenses` | Living Expenses (Yr 1) | Expenses | Float | `$60,000` | $0 – $500K | USD/yr | Baseline living expenses in Year 1 ($y = \text{currentYear} + 1$). Inflates annually. |
| 22 | `stateTaxRate` | State Tax Rate | Tax | Float | `0.0575` (5.75%)| 0.0% – 15.0% | Percentage | Flat state income tax rate (standard Virginia top bracket baseline). |
| 23 | `filingStatus` | Tax Filing Status | Tax | Enum | `MFJ` | `MFJ`, `Single`| Option | Married Filing Jointly vs Single tax bracket schedule. |
| 24 | `tvmDiscountRate` | TVM Discount Rate | Economic | Float | `0.035` (3.5%) | 0.0% – 15.0% | Percentage | Discount rate used to calculate PV and FV of tax streams. |
| 25 | `optObjective` | Optimization Goal | Solver | Enum | `raw` | `raw`, `tvm` | Radio | Objective function: Minimize Raw Total Tax vs Minimize TVM-Adjusted Tax. |
| 26 | `manualConversion`| Manual Conversion Amount| Solver | Float | `$0` | $0 – $500K | USD/yr | User slider/input for manual scenario exploration. |

---

## 3. Requirement R2: Mathematical Specification of Simulation Engine

### 3.1 Timeline, Age Indexing & Time-Series Notation

Let simulation timeline be indexed by calendar year $y \in [Y_{\text{start}}, Y_{\text{end}}]$, where:
- Base year: $Y_0 = \text{currentYear} = 2026$.
- Start year: $Y_{\text{start}} = Y_0 + 1 = 2027$.
- End year: $Y_{\text{end}} = \text{eolYear} = 2060$.
- Total simulation span: $N = Y_{\text{end}} - Y_{\text{start}} + 1 = 2060 - 2027 + 1 = 34$ years.
- Index step: $t = y - Y_{\text{start}} \in [0, N-1]$ (where $t=0$ for 2027, $t=33$ for 2060).
- Client age in year $y$:
  $$\text{Age}(y) = y - \text{birthYear}$$
  For $y = 2027$: $\text{Age}(2027) = 2027 - 1976 = 51$.  
  For $y = 2060$: $\text{Age}(2060) = 2060 - 1976 = 84$.

---

### 3.2 Inflation Model & Tax Bracket Compounding

Let $i = \text{inflationRate} = 0.035$ (3.5%).
The cumulative inflation factor from the base year $Y_0 = 2026$ to year $y$ is:
$$\Omega(y) = (1 + i)^{y - Y_0} = (1 + i)^{t + 1}$$
The cumulative inflation factor from Year 1 ($Y_{\text{start}} = 2027$) to year $y$ is:
$$\omega(y) = (1 + i)^{y - Y_{\text{start}}} = (1 + i)^t$$

**Application Rules:**
1. **Living Expenses:** Base $L_1 = \$60,000$ is defined for Year 1 ($t=0$). For year $y$:
   $$L(y) = L_1 \times \omega(y) = \$60,000 \times (1 + i)^{y - 2027}$$
2. **Healthcare Costs:** Base costs $H_{\text{sub}}$ and $H_{\text{unsub}}$ are defined in Year 1 dollars. For year $y$:
   $$H_{\text{sub}}(y) = H_{\text{sub}} \times \omega(y), \quad H_{\text{unsub}}(y) = H_{\text{unsub}} \times \omega(y)$$
3. **Subsidy Cliff Threshold:** Base cliff $M_{\text{cliff}} = \$90,000$ scales with inflation:
   $$M_{\text{cliff}}(y) = M_{\text{cliff}} \times \omega(y)$$
4. **College Expenses:** **ZERO inflation.**
   $$E_{\text{college}}(y) \text{ does NOT inflate.}$$
5. **Federal Tax Brackets & Standard Deduction:**
   Tax bracket thresholds $T_k(y)$ and standard deduction $D_{\text{std}}(y)$ inflate cumulatively each year:
   $$T_k(y) = T_k(Y_{\text{start}}) \times \omega(y), \quad D_{\text{std}}(y) = D_{\text{std}}(Y_{\text{start}}) \times \omega(y)$$

---

### 3.3 Federal Tax Bracket Formulas & Standard Deduction

The US Federal Income Tax is modeled as a progressive piecewise linear marginal tax function.

#### Base Brackets for Married Filing Jointly (MFJ) — Year 1 ($2027$ Baseline)
- Standard Deduction: $D_{\text{std}, \text{MFJ}} = \$30,000$

| Bracket $k$ | Marginal Rate $r_k$ | Lower Bound $T_{k-1}$ | Upper Bound $T_k$ |
|---|---|---|---|
| 1 | 10% (0.10) | $0 | $23,850 |
| 2 | 12% (0.12) | $23,850 | $96,950 |
| 3 | 22% (0.22) | $96,950 | $206,700 |
| 4 | 24% (0.24) | $206,700 | $394,600 |
| 5 | 32% (0.32) | $394,600 | $501,050 |
| 6 | 35% (0.35) | $501,050 | $751,600 |
| 7 | 37% (0.37) | $751,600 | $\infty$ |

#### Base Brackets for Single Filers — Year 1 ($2027$ Baseline)
- Standard Deduction: $D_{\text{std}, \text{Single}} = \$15,000$

| Bracket $k$ | Marginal Rate $r_k$ | Lower Bound $T_{k-1}$ | Upper Bound $T_k$ |
|---|---|---|---|
| 1 | 10% (0.10) | $0 | $11,925 |
| 2 | 12% (0.12) | $11,925 | $48,475 |
| 3 | 22% (0.22) | $48,475 | $103,350 |
| 4 | 24% (0.24) | $103,350 | $197,300 |
| 5 | 32% (0.32) | $197,300 | $250,525 |
| 6 | 35% (0.35) | $250,525 | $626,350 |
| 7 | 37% (0.37) | $626,350 | $\infty$ |

#### Dynamic Indexing & Bracket Evaluation Algorithm
For any year $y$, inflated thresholds are:
$$T_k(y) = T_k \times (1 + i)^{y - Y_{\text{start}}}, \quad D_{\text{std}}(y) = D_{\text{std}} \times (1 + i)^{y - Y_{\text{start}}}$$

Given Federal Adjusted Gross Income $AGI(y)$, the Federal Taxable Income is:
$$\text{TaxableIncome}_{\text{fed}}(y) = \max\left(0, AGI(y) - D_{\text{std}}(y)\right)$$

The Federal Income Tax function $\Phi_{\text{fed}}(X, y)$ on taxable income $X = \text{TaxableIncome}_{\text{fed}}(y)$ is:
$$\Phi_{\text{fed}}(X, y) = \sum_{k=1}^{7} r_k \times \max\left(0, \min(X, T_k(y)) - T_{k-1}(y)\right)$$
where $T_0(y) = 0$ and $T_7(y) = \infty$.

---

### 3.4 State Income Tax Formulation

State income tax is computed as a flat rate on taxable income above standard deduction:
- State Tax Rate: $\tau_{\text{state}} = \text{stateTaxRate} = 0.0575$ (5.75%).
- State Standard Deduction (Virginia baseline): $D_{\text{std, state}} = \$6,000$ (MFJ) or $\$3,000$ (Single), indexed to inflation.
- State Taxable Income:
  $$\text{TaxableIncome}_{\text{state}}(y) = \max\left(0, AGI(y) - D_{\text{std, state}}(y)\right)$$
- State Income Tax:
  $$\Phi_{\text{state}}(y) = \tau_{\text{state}} \times \text{TaxableIncome}_{\text{state}}(y)$$

Total Tax for year $y$:
$$\text{Tax}(y) = \Phi_{\text{fed}}(\text{TaxableIncome}_{\text{fed}}(y), y) + \Phi_{\text{state}}(y)$$

---

### 3.5 College Funding Schedule Formulation

College total expense $C_{\text{total}} = \text{collegeExpenses} = \$100,000$.
Start year $Y_c = \text{collegeStartYear} = 2029$.
Duration = 5 years.
The annual expense distribution vector $\mathbf{w} = [0.125, 0.25, 0.25, 0.25, 0.125]$ corresponds to years $Y_c, Y_c+1, Y_c+2, Y_c+3, Y_c+4$.

Mathematical piecewise formula:
$$E_{\text{college}}(y) = \begin{cases}
0.125 \times C_{\text{total}} = \$12,500 & \text{if } y = Y_c \ (2029) \\
0.250 \times C_{\text{total}} = \$25,000 & \text{if } y \in \{Y_c+1, Y_c+2, Y_c+3\} \ (2030, 2031, 2032) \\
0.125 \times C_{\text{total}} = \$12,500 & \text{if } y = Y_c+4 \ (2033) \\
0 & \text{otherwise}
\end{cases}$$
Constraint verification: $\sum_{y} E_{\text{college}}(y) = C_{\text{total}} \times (0.125 + 0.25 + 0.25 + 0.25 + 0.125) = \$100,000$.  
**Explicit Constraint:** No inflation factor is applied to college expenses.

---

### 3.6 Healthcare Expense Model & ACA Subsidy Cliff Step Function

Healthcare expense depends on client age and Modified Adjusted Gross Income ($MAGI$):
1. **Medicare Eligibility Drop-off:**
   At age 65 ($y \ge \text{birthYear} + 65 = 2041$), private pre-Medicare health insurance drops to $\$0$:
   $$\text{HealthcareExpense}(y) = \$0 \quad \forall \ \text{Age}(y) \ge 65$$
2. **Pre-65 Subsidy Cliff ($\text{Age}(y) < 65$):**
   - Inflated Cliff: $M_{\text{cliff}}(y) = \$90,000 \times (1 + i)^{y - Y_{\text{start}}}$.
   - If $MAGI(y) \le M_{\text{cliff}}(y)$: Subsidized coverage applies.
     $$\text{BaseHC}(y) = H_{\text{sub}} = \$5,000$$
   - If $MAGI(y) > M_{\text{cliff}}(y)$: Unsubsidized coverage applies (subsidy cliff triggered).
     $$\text{BaseHC}(y) = H_{\text{unsub}} = \$25,000$$
   - Applying cumulative healthcare inflation:
     $$\text{HealthcareExpense}(y) = \text{BaseHC}(y) \times (1 + i)^{y - Y_{\text{start}}}$$

**Decoupling Insight:** $MAGI(y)$ is a function of income (earned income, cash interest, taxable investment yield, Roth conversions, taxable Social Security). It is NOT influenced by health insurance expense. Hence, $MAGI(y)$ is evaluated first, completely avoiding circular dependencies.

---

### 3.7 Social Security & IRC Section 86 Provisional Income Formula

1. **Eligibility & Timing:**
   - Social Security Start Age: $A_{\text{SS}} = \text{ssStartAge} = 62$.
   - Year SS begins: $Y_{\text{SS}} = \text{birthYear} + A_{\text{SS}} = 1976 + 62 = 2038$.
   - Annual benefit at start: $SS_0 = \text{ssAmount} = \$60,000$.
   - Prior to start age ($\text{Age}(y) < 62$): $SS(y) = 0$.
   - At and after start age ($\text{Age}(y) \ge 62$): $SS(y) = SS_0 \times (1 + i)^{y - Y_{\text{start}}}$.
2. **Taxation of Social Security (IRC § 86):**
   Provisional Income is defined as:
   $$\text{PI}(y) = AGI_{\text{other}}(y) + 0.5 \times SS(y)$$
   where $AGI_{\text{other}}(y) = W(y) + I_{\text{cash}}(y) + K(y) + \text{TaxableBrokerageIncome}(y)$.
   Under statutory IRS thresholds for MFJ:
   - Base Threshold 1: $\$32,000$
   - Base Threshold 2: $\$44,000$
   
   The taxable portion of Social Security $SS_{\text{taxable}}(y)$ is:
   $$SS_{\text{taxable}}(y) = \min\left(0.85 \times SS(y), \ 0.50 \times \max\left(0, \min(\text{PI}, 44000) - 32000\right) + 0.85 \times \max(0, \text{PI} - 44000)\right)$$
   *Note for this portfolio:* Because pre-tax assets are $\$5\text{M}$ and conversion/interest flows typically exceed $\$100\text{K}$, $\text{PI}(y)$ substantially exceeds $\$44,000$, resulting in the standard upper limit of $85\%$ of Social Security being taxable ($SS_{\text{taxable}} = 0.85 \times SS(y)$). The engine implements the exact IRS piecewise formula.

---

### 3.8 Earned Income Phase-out

Earned income represents employment salary prior to retirement:
$$W(y) = \begin{cases}
\text{earnedIncome} = \$275,000 & \text{if } y < \text{retirementYear} \\
0 & \text{if } y \ge \text{retirementYear}
\end{cases}$$
With default inputs ($Y_{\text{start}} = 2027$ and $\text{retirementYear} = 2027$), client retires at the onset of the simulation, so $W(y) = 0$ for all $y \ge 2027$. If the user adjusts $\text{retirementYear}$ to $2030$, $W(y) = \$275,000$ for $y \in \{2027, 2028, 2029\}$ and drops to $0$ in $2030$.

---

### 3.9 Asset Growth & Return Classification

At the beginning of year $y$, balances are $C_{\text{start}}(y)$ (Cash), $I_{\text{start}}(y)$ (Investment), $R_{\text{start}}(y)$ (Roth), and $P_{\text{start}}(y)$ (Pre-Tax).

1. **Cash Account:**
   - Yield: $r_{\text{cash}} = 0.05$ (5.0%).
   - Annual Interest:
     $$I_{\text{cash}}(y) = C_{\text{start}}(y) \times r_{\text{cash}}$$
   - **Tax Status:** Taxed 100% as **Ordinary Income** in the year earned.
2. **Taxable Brokerage Investment:**
   - Total Return: $r_{\text{inv}} = 0.09$ (9.0%).
   - Total Investment Growth:
     $$G_{\text{inv}}(y) = I_{\text{start}}(y) \times r_{\text{inv}}$$
   - **Tax Modeling:** In long-term portfolios, growth consists of unrealized appreciation plus dividend yield. When taxable investments are sold to cover cash flow deficits, capital gains are realized. In the simulation:
     - Realized distribution / dividend component: $2.0\%$ annual taxable dividend yield taxed at LTCG / preferential rate (or included in AGI).
     - Unrealized component: $7.0\%$ compounds tax-deferred until liquidated.
     - For clean single-file execution and conservative tax planning, taxable investment return is modeled with preferential capital gains taxation on annual realized yield plus basis tracking on liquidation.
3. **Pre-Tax Retirement Accounts:**
   - Growth: $G_{\text{pretax}}(y) = (P_{\text{start}}(y) - K(y)) \times r_{\text{inv}}$.
   - Balances compound 100% tax-deferred until converted or inherited.
4. **Roth Retirement Accounts:**
   - Growth: $G_{\text{roth}}(y) = (R_{\text{start}}(y) + K(y)) \times r_{\text{inv}}$.
   - Balances compound 100% tax-free.

---

### 3.10 Roth Conversion Mechanics & 5-Year Rule Vintage Queue

1. **Annual Conversion Amount $K(y)$:**
   Roth conversions occur from $\text{retirementYear}$ ($2027$) to Age 75 ($y = 1976 + 75 = 2051$):
   $$K(y) = \begin{cases}
   \min(K_{\text{target}}, P_{\text{start}}(y)) & \text{if } \text{retirementYear} \le y \le \text{birthYear} + 75 \\
   0 & \text{otherwise}
   \end{cases}$$
   where $K_{\text{target}}$ is the flat annual dollar conversion parameter ($0 \le K_{\text{target}} \le \$500,000$).
   - Pre-tax balance decreases by $K(y)$.
   - $K(y)$ is added to Ordinary Income in year $y$, triggering income taxes.
   - Roth balance increases by $K(y)$ at beginning of year and participates in full year's growth.

2. **The 5-Year Conversion Rule & Vintage Tracking:**
   Under IRC § 72(t)(1)(B), each conversion principal amount becomes accessible without early withdrawal penalty on January 1 of the 5th tax year following the conversion year ($y_{\text{accessible}} = y_{\text{conv}} + 5$).
   
   **Vintage State Queue:**
   Maintain an array of conversion vintage objects:
   $$\mathcal{V} = \left[ \{ \text{year}: v, \ \text{principal}: K(v), \ \text{remaining}: K(v) \} \right]$$
   Initial condition at $Y_{\text{start}} = 2027$:
   - Initial Roth Principal: $P_0 = \text{rothPrincipal} = \$25,000$.
     This is historical contribution principal and is **accessible immediately in Year 1** ($y=2027$).
   - Initial Roth Earnings: $E_0 = \text{rothBalance} - \text{rothPrincipal} = \$120,000 - \$25,000 = \$95,000$.
   
   In any simulation year $y$:
   A vintage $v \in \mathcal{V}$ is accessible if and only if:
   $$y - v \ge 5$$
   Total Accessible Roth Principal available to cover deficits in year $y$:
   $$\text{AccessibleRothPrincipal}(y) = P_{\text{orig, remaining}}(y) + \sum_{v \in \mathcal{V}, \ y - v \ge 5} v.\text{remaining}$$

---

### 3.11 Annual Cash Flow Waterfall & Liquidity Drawdown Priority

The simulation engine executes the following discrete chronological pipeline for each year $y$:

```
Step 1: Calculate Gross Inflows & AGI
        W(y) = Earned Income
        I_cash(y) = Cash_start * r_cash
        K(y) = Roth Conversion Amount
        SS(y) = Social Security Benefit
        SS_taxable(y) = IRC § 86 Formula(PI(y))
        AGI(y) = W(y) + I_cash(y) + K(y) + SS_taxable(y)

Step 2: Calculate Taxes
        Taxable_fed = max(0, AGI(y) - D_std(y))
        FedTax = ProgressiveTax(Taxable_fed, y)
        StateTax = StateRate * max(0, AGI(y) - D_std_state(y))
        TotalTax(y) = FedTax + StateTax

Step 3: Calculate Total Outflows
        Living(y) = $60,000 * (1 + i)^t
        Health(y) = Pre65_ACA(AGI(y), y) if Age < 65 else $0
        College(y) = CollegeDistribution(y)  [zero inflation]
        TotalExpenses(y) = Living(y) + Health(y) + College(y)
        TotalOutflows(y) = TotalExpenses(y) + TotalTax(y)

Step 4: Calculate Net Cash Flow
        AvailableCashInflow(y) = W(y) + SS(y) + I_cash(y)
        NetCashDeficit(y) = TotalOutflows(y) - AvailableCashInflow(y)

Step 5: Liquidity Waterfall (Deficit Drawdown Priority)
        If NetCashDeficit(y) <= 0:
            Cash_rem = Cash_start + (-NetCashDeficit)
            RemainingDeficit = 0
        Else:
            # 1. Drawdown Cash
            Draw_Cash = min(Cash_start, NetCashDeficit)
            Cash_rem = Cash_start - Draw_Cash
            RemainingDeficit = NetCashDeficit - Draw_Cash
            
            # 2. Drawdown Taxable Investment
            Inv_total = Inv_start * (1 + r_inv)
            Draw_Inv = min(Inv_total, RemainingDeficit)
            Inv_rem = Inv_total - Draw_Inv
            RemainingDeficit = RemainingDeficit - Draw_Inv
            
            # 3. Drawdown Accessible Roth Principal (FIFO by vintage)
            Draw_Roth = min(AccessibleRothPrincipal(y), RemainingDeficit)
            AccessibleRothPrincipal_rem = AccessibleRothPrincipal(y) - Draw_Roth
            Roth_rem = (Roth_start + K(y)) * (1 + r_inv) - Draw_Roth
            RemainingDeficit = RemainingDeficit - Draw_Roth

Step 6: Liquidity Constraint Evaluation
        If RemainingDeficit > 0:
            Mark Year y as INFEASIBLE: (Cash + Inv + AccessibleRoth < 0)
```

---

### 3.12 SECURE Act Inherited IRA Death Tax Formulation

At End of Life ($Y_{\text{end}} = 2060$, client age 84), remaining Pre-Tax Retirement balance $\text{PreTax}_{\text{EOL}}$ is liquidated:
- Number of Heirs: $n_{\text{heirs}} = 2$.
- Distribution Period: $T_{\text{sec}} = 10$ years (SECURE Act 10-year rule).
- Base income per heir: $Y_{\text{heir, base}} = \$150,000$/year.
- Share per heir: $\text{HeirShare} = \frac{\text{PreTax}_{\text{EOL}}}{2}$.
- Annual inherited IRA distribution per heir:
  $$W_{\text{heir}} = \frac{\text{HeirShare}}{10} = \frac{\text{PreTax}_{\text{EOL}}}{20}$$
- Annual Tax Calculation per heir (Single filer tax brackets at EOL):
  - Base Tax on heir's base income:
    $$\text{Tax}_{\text{base}} = \Phi_{\text{fed, single}}(\max(0, \$150,000 - D_{\text{single}}), Y_{\text{end}}) + \tau_{\text{state}} \times \max(0, \$150,000 - D_{\text{state}})$$
  - Combined Tax on base income + inheritance distribution:
    $$\text{Tax}_{\text{combined}} = \Phi_{\text{fed, single}}(\max(0, \$150,000 + W_{\text{heir}} - D_{\text{single}}), Y_{\text{end}}) + \tau_{\text{state}} \times \max(0, \$150,000 + W_{\text{heir}} - D_{\text{state}})$$
  - Marginal Annual Tax Attributable to Inherited IRA:
    $$\Delta \text{Tax}_{\text{heir, annual}} = \text{Tax}_{\text{combined}} - \text{Tax}_{\text{base}}$$
- Total Inherited IRA Death Tax:
  $$\text{DeathTax} = 2 \times 10 \times \Delta \text{Tax}_{\text{heir, annual}} = 20 \times \Delta \text{Tax}_{\text{heir, annual}}$$

Total Lifetime Tax Liability:
$$\text{TotalTax}_{\text{lifetime}} = \sum_{y=Y_{\text{start}}}^{Y_{\text{end}}} \text{Tax}(y) + \text{DeathTax}$$

---

### 3.13 Time Value of Money (TVM) Formulations: PV and FV

Let $r_{\text{disc}} = \text{tvmDiscountRate} = 0.035$ (3.5% inflation rate) or $r_{\text{inv}} = 0.09$ (9.0% investment opportunity cost rate). Default is inflation rate $3.5\%$, with user toggle/input.

1. **Present Value (PV) Discounted to Year 1 ($Y_{\text{start}} = 2027$):**
   For annual tax paid in year $y$:
   $$\text{PV}(\text{Tax}(y)) = \frac{\text{Tax}(y)}{(1 + r_{\text{disc}})^{y - Y_{\text{start}}}}$$
   For Death Tax incurred at EOL ($Y_{\text{end}} = 2060$):
   $$\text{PV}(\text{DeathTax}) = \frac{\text{DeathTax}}{(1 + r_{\text{disc}})^{Y_{\text{end}} - Y_{\text{start}}}}$$
   Total Lifetime Tax (PV):
   $$\text{TotalTax}_{\text{PV}} = \sum_{y=Y_{\text{start}}}^{Y_{\text{end}}} \text{PV}(\text{Tax}(y)) + \text{PV}(\text{DeathTax})$$

2. **Future Value (FV) Compounded to End of Life ($Y_{\text{end}} = 2060$):**
   For annual tax paid in year $y$:
   $$\text{FV}(\text{Tax}(y)) = \text{Tax}(y) \times (1 + r_{\text{disc}})^{Y_{\text{end}} - y}$$
   For Death Tax at EOL:
   $$\text{FV}(\text{DeathTax}) = \text{DeathTax} \times (1 + r_{\text{disc}})^0 = \text{DeathTax}$$
   Total Lifetime Tax (FV):
   $$\text{TotalTax}_{\text{FV}} = \sum_{y=Y_{\text{start}}}^{Y_{\text{end}}} \text{FV}(\text{Tax}(y)) + \text{DeathTax}$$

**Equivalence Invariant:**
$$\text{TotalTax}_{\text{FV}} = \text{TotalTax}_{\text{PV}} \times (1 + r_{\text{disc}})^{Y_{\text{end}} - Y_{\text{start}}}$$
Because $(1 + r_{\text{disc}})^{Y_{\text{end}} - Y_{\text{start}}}$ is a strictly positive constant scalar, any conversion amount $K^*$ that minimizes $\text{TotalTax}_{\text{PV}}$ also strictly minimizes $\text{TotalTax}_{\text{FV}}$.

---

## 4. Requirement R3: UI Output & Visualization Specification

### 4.1 Year-by-Year Data Table Schema

The application must render an interactive, sortable, responsive HTML data table with 34 rows ($2027$ to $2060$). Each row represents one simulated year:

| Column # | Field Header | Data Key | Format | Description |
|---|---|---|---|---|
| 1 | Year | `year` | `YYYY` | Calendar year ($2027 – 2060$) |
| 2 | Age | `age` | `##` | Client age ($51 – 84$) |
| 3 | Living Exp | `livingExp` | `$#,##0` | Inflated living expenses |
| 4 | Health Ins | `healthExp` | `$#,##0` | Pre-65 healthcare or $0 post-65 |
| 5 | College Exp | `collegeExp` | `$#,##0` | College expense (non-inflated schedule) |
| 6 | Roth Conv | `conversion` | `$#,##0` | Roth conversion amount $K(y)$ |
| 7 | Taxable Inc | `taxableInc` | `$#,##0` | Federal taxable income after deductions |
| 8 | Taxes Paid | `totalTax` | `$#,##0` | Combined Federal + State tax paid |
| 9 | YE Cash | `endCash` | `$#,##0` | Year-end liquid cash reserves |
| 10 | YE Investment | `endInv` | `$#,##0` | Year-end taxable brokerage investments |
| 11 | YE Pre-tax | `endPretax` | `$#,##0` | Year-end pre-tax retirement balance |
| 12 | YE Roth | `endRoth` | `$#,##0` | Year-end total Roth balance |
| 13 | Accessible Roth | `endAccRoth` | `$#,##0` | Accessible Roth conversion & contribution principal |

Table Features:
- Sticky header with frozen column headers during scrolling.
- Hover highlighting on rows.
- Formatted with clear typography, right-aligned monetary values.
- Color badges indicating pre-retirement vs retirement vs Medicare age.

---

### 4.2 Chart.js Dual-Axis Visualization Specification

Chart.js (v4.x via CDN) renders a composite stacked bar + line chart:
- **Canvas Element ID:** `#wealthTaxChart`
- **X-Axis:** Simulation Years ($2027$ to $2060$, 34 categorical labels).
- **Y-Axis 1 (Left - Stacked Assets):**
  - Title: "Asset Balances ($ Millions / Thousands)"
  - Stack Group: `'wealthStack'`
  - Dataset 1 (Bar): Cash Reserves — Color: `#10B981` (Emerald Green)
  - Dataset 2 (Bar): Taxable Investment — Color: `#3B82F6` (Royal Blue)
  - Dataset 3 (Bar): Retirement Pre-tax — Color: `#F59E0B` (Amber / Orange)
  - Dataset 4 (Bar): Retirement Roth — Color: `#8B5CF6` (Purple)
- **Y-Axis 2 (Right - Cumulative Tax):**
  - Title: "Cumulative Tax Paid ($)"
  - Gridlines: Disabled or subtle dashed to avoid visual clutter
  - Dataset 5 (Line): Cumulative Tax Paid — Color: `#EF4444` (Crimson Red)
  - Border Width: 3px, tension: 0.25, pointRadius: 3

Interactive Tooltips:
- Tooltip displays year, age, individual asset breakdowns, total net worth, annual tax paid, and cumulative tax paid.

---

### 4.3 Summary KPI Cards (Executive Summary)

Below the chart, a responsive grid of metric cards summarizes final portfolio outcomes:

1. **EOL Liquid Cash:** Cash balance at year 2060.
2. **EOL Taxable Investment:** Brokerage balance at year 2060.
3. **EOL Pre-tax Balance:** Pre-tax retirement balance at year 2060.
4. **EOL Roth Balance:** Roth retirement balance at year 2060.
5. **EOL Net Worth:** Sum of all 4 asset buckets at year 2060.
6. **Total Lifetime Tax (Raw):** $\sum \text{Tax}(y) + \text{DeathTax}$.
7. **Total Lifetime Tax (PV):** Present value of all lifetime taxes.
8. **Total Lifetime Tax (FV):** Future value of all lifetime taxes at EOL.
9. **Heir Death Tax:** Total SECURE Act tax paid by heirs on remaining pre-tax balance.
10. **Optimal Conversion Recommendation:** Badge displaying "$XX,000 / yr (Retirement to Age 75)".

---

## 5. Requirement R4: Optimization Engine & Solver Specification

### 5.1 Objective Functions

The user selects between two optimization modes via a radio button:
1. **Mode A (`raw`): Minimize Raw Total Tax**
   $$\min_{K \in \mathcal{K}_{\text{feasible}}} f_{\text{raw}}(K) = \sum_{y=Y_{\text{start}}}^{Y_{\text{end}}} \text{Tax}(y; K) + \text{DeathTax}(K)$$
2. **Mode B (`tvm`): Minimize TVM-Adjusted Tax**
   $$\min_{K \in \mathcal{K}_{\text{feasible}}} f_{\text{tvm}}(K) = \sum_{y=Y_{\text{start}}}^{Y_{\text{end}}} \frac{\text{Tax}(y; K)}{(1 + r_{\text{disc}})^{y - Y_{\text{start}}}} + \frac{\text{DeathTax}(K)}{(1 + r_{\text{disc}})^{Y_{\text{end}} - Y_{\text{start}}}}$$

---

### 5.2 Decision Variable & Feasibility Domain

- Decision Variable: $K \in [0, \$500,000]$, representing the flat annual Roth conversion amount applied from $y = \text{retirementYear} \ (2027)$ to $y = \text{birthYear} + 75 \ (2051)$.
- Discrete Search Grid:
  $$\mathcal{K} = \{ 0, 5000, 10000, 15000, \dots, 495000, 500000 \}$$
  Grid Size: $|\mathcal{K}| = \frac{500,000}{5,000} + 1 = 101$ evaluation points.
- **Feasibility Constraint (Liquidity Invariant):**
  A candidate conversion amount $K$ is **feasible** ($K \in \mathcal{K}_{\text{feasible}}$) if and only if for every year $y \in [Y_{\text{start}}, Y_{\text{end}}]$:
  $$\text{Cash}(y) + \text{Inv}(y) + \text{AccessibleRothPrincipal}(y) \ge 0$$
  If in any year $y$, the deficit exceeds available Cash + Investment + Accessible Roth Principal, that candidate $K$ is marked **INFEASIBLE** and discarded.

---

### 5.3 Brute-Force Grid Search Algorithm & Complexity Analysis

#### Algorithm Pseudocode
```javascript
function findOptimalConversion(inputs, objectiveMode) {
  const K_min = 0;
  const K_max = 500000;
  const K_step = 5000;
  
  let bestK = null;
  let minTax = Infinity;
  let bestTrajectory = null;
  let feasibleCount = 0;

  for (let K = K_min; K <= K_max; K += K_step) {
    const simulationResult = runSimulationEngine(inputs, K);
    
    if (simulationResult.isFeasible) {
      feasibleCount++;
      const taxScore = (objectiveMode === 'tvm') 
        ? simulationResult.totalTaxPV 
        : simulationResult.totalTaxRaw;
      
      if (taxScore < minTax) {
        minTax = taxScore;
        bestK = K;
        bestTrajectory = simulationResult;
      }
    }
  }

  return {
    optimalK: bestK,
    minTax: minTax,
    trajectory: bestTrajectory,
    feasibleCount: feasibleCount,
    totalEvaluated: 101
  };
}
```

#### Performance Complexity
- Grid Points: $M = 101$
- Years per Simulation: $N = 34$
- Total Year Evaluations: $M \times N = 101 \times 34 = 3,434$ steps.
- In JavaScript V8/SpiderMonkey, 3,434 pure arithmetic iterations execute in **under 2 milliseconds**!
- Because DOM updates are completely separated from the calculation loop, the entire optimization executes synchronously on button click or input change without any noticeable UI stutter.

---

## 6. Edge Cases & Boundary Conditions Matrix

| # | Feature / Condition | Input Scenario | Observed / Specified Engine Behavior |
|---|---|---|---|
| E1 | Zero Conversion | $K = 0$ | Feasible baseline. No upfront conversion tax. Pre-tax balance grows to max size ($\sim \$70\text{M}+$ at 9%), resulting in an enormous Death Tax on heirs at EOL. |
| E2 | Max Conversion | $K = \$500,000$ | Triggers massive early tax bills. If Cash + Inv cannot cover the early tax, liquidity constraint is violated $\implies$ marked INFEASIBLE. |
| E3 | Exhaustion of Pre-tax | $P_{\text{start}}(y) < K$ | Conversion is capped at remaining balance: $K(y) = \min(K, P_{\text{start}}(y))$. Pre-tax cannot become negative. |
| E4 | Pre-65 Subsidy Cliff Boundary | $MAGI = \$90,000 \pm \$1$ | Exactly at $\$90,000$, subsidized rate applies ($5k); at $\$90,001$, unsubsidized rate applies ($25k). Handled via strict $\le$. |
| E5 | Age 65 Medicare Transition | $\text{Age} = 64 \to 65$ | In year client turns 65, healthcare cost immediately drops from $H_{\text{sub/unsub}}$ to $\$0$. |
| E6 | College 5-Year Window Boundary | Years before 2029, 2034+ | College expenses are strictly $0$ in 2027-2028 and 2034-2060. In 2029-2033: [12.5k, 25k, 25k, 25k, 12.5k]. |
| E7 | Roth 5-Year Rule Locking | Deficit in years 2027–2031 | Conversions made in 2027 are locked until 2032. Only initial $\$25\text{K}$ principal is accessible before 2032. Deficits exceeding Cash + Inv + $25k trigger infeasibility. |
| E8 | Social Security Start Timing | $y < 2038$ vs $y \ge 2038$ | SS is exactly $\$0$ until year client reaches age 62 (2038), then starts at inflated benefit. |
| E9 | Pre-Retirement Earned Income | Retirement Year $> 2027$ | If retirement year is set to 2030, earned income of $\$275\text{K}$ applies for 2027, 2028, 2029, then becomes $0$ in 2030. |
| E10| High Inflation Sensitivity | Inflation Rate = 10% | Brackets, living expenses, and healthcare inflate aggressively. College remains static. Tests stability of floating-point compounding. |
| E11| Zero Pre-Tax Balance at EOL | Pre-tax balance is $0$ at EOL | Death Tax evaluates to exactly $\$0$. No division by zero. |
| E12| No Feasible Conversion | Extreme living expenses or zero cash/inv | Solver identifies 0 feasible points; gracefully alerts user and displays closest least-deficit trajectory. |

---

## 7. Discovered Features & Design Enhancements Matrix

| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|---|---|---|---|---|---|---|
| F1 | UI Inputs | Dual Mode Conversion Control | Allows user to either click "Optimize" to auto-find $K^*$, or drag a manual slider ($0 to $500k) to inspect any custom conversion path. | Slider value ($K$) | Real-time chart & table update | Constrained between 0 and 500k | Usability enhancement during spec review |
| F2 | Simulation | Separate Federal & State Tax Breakdown | Computes and displays Federal and State income taxes separately in table and tooltips. | AGI, deductions, rates | Federal Tax, State Tax | Clamped $\ge 0$ | Virginia 5.75% tax rule analysis |
| F3 | Simulation | IRC § 86 Tiered Social Security Taxation | Accurately models the statutory 0% / 50% / 85% provisional income formula rather than a crude flat 85%. | Other AGI, Social Security | Taxable Social Security | Clamped $\le 0.85 \times SS$ | IRC Section 86 tax code analysis |
| F4 | Optimization | Interactive Conversion vs Tax Sensitivity Curve | In addition to finding the single minimum, compute the tax curve across all 101 points to show the "U-shaped" tax optimization valley. | 101 evaluated grid points | Array of $\{K, \text{Tax}, \text{Feasible}\}$ | Highlights infeasible zone in red | Convexity analysis of tax optimization |
| F5 | Environment | Zero-Dependency Offline Polyfill & Local Storage Guard | Wraps all `localStorage` access in `try/catch` and supports standalone offline `file:///` viewing with inline SVG fallback if CDN fails. | Browser environment | Safe storage / clean render | Graceful fallback if storage throws SecurityError | Acceptance criteria R48-R49 |
| F6 | Visuals | Milestone Markers on Chart | Visual annotations on Chart.js (Retirement, College Start, Medicare Age 65, Social Security Start Age 62, Age 75 RMD/Conversion end). | Milestone year indices | Chart vertical indicator lines / badges | Ignored if outside range | Financial dashboard UX best practices |

---

## 8. Acceptance Criteria Verification Plan

| Criteria ID | Requirement Description | Verification Method & Assertion |
|---|---|---|
| **AC-01** | Single standalone `planning.html` | Inspect file count: Exactly one `.html` file containing HTML, CSS, JS; CDN for Chart.js. |
| **AC-02** | Local `file:///` execution without errors | Open `file:///Users/eric/Dropbox/ai/asset/planning.html` in browser; verify console has 0 CORS / SecurityError exceptions. |
| **AC-03** | Annual Tax Bracket Inflation Indexing | Unit test: Verify federal 22% bracket threshold in 2028 equals $96,950 \times 1.035 = \$100,343.25$. |
| **AC-04** | College 5-Year Expense Distribution | Unit test: Verify expenses in 2029-2033 are exactly $12.5k, $25k, $25k, $25k, $12.5k with 0 inflation. |
| **AC-05** | Healthcare Drop-off at Age 65 | Unit test: Verify healthcare expense at age 64 is $>0$ and at age 65 is strictly $\$0$. |
| **AC-06** | Pre-65 Subsidy Cliff at $90k MAGI | Unit test: Verify cost jumps from $\$5k$ to $\$25k$ (inflated) when MAGI crosses cliff. |
| **AC-07** | Roth 5-Year Accessibility Tracking | Unit test: Conversions in 2027 cannot be drawn until 2032; cash deficit in 2030 cannot tap 2027 conversion. |
| **AC-08** | Inherited IRA Death Tax Calculation | Unit test: Verify remaining pre-tax balance at 2060 is split by 2 heirs over 10 years with $150k base income. |
| **AC-09** | Optimization Brute-Force Sweep | Run optimization loop across 101 points; verify solver finishes in $<50$ms and identifies valid feasible minimum. |
| **AC-10** | Dual Optimization Objective Toggle | Toggle between "Minimize Raw Total Tax" and "Minimize TVM-Adjusted Tax"; verify optimal $K^*$ updates accordingly. |

---
*End of Formal Specification Report.*
