# Lifetime Financial & Tax Optimization Dashboard

A privacy-first, 100% client-side web application designed to help executives and retirees model asset decumulation, optimize Roth conversions, and minimize lifetime tax liability.

## Overview
This tool simulates your financial trajectory from today through your End of Life (EOL) year. By evaluating standard living expenses, healthcare cliffs, college funding, and Social Security, the engine calculates your lifetime federal and state tax burden. 

Crucially, it features a **multi-phase optimization engine** that automatically determines the mathematically optimal Roth conversion strategy to minimize your lifetime tax liability—including the SECURE 2.0 "Death Tax" passed on to your heirs.

## Key Features
* **4-Phase Roth Optimization:** The engine breaks your life into four distinct tax phases (Pre-Retirement, Pre-59½, Pre-RMD, and Post-75 RMD Active) and sweeps thousands of scenarios to find the perfect conversion amount for each phase.
* **Intelligent Liquidity Waterfall:** The simulation automatically draws down accounts in the most efficient order (Cash → Taxable Brokerage → Accessible Roth Principal) to cover cash flow deficits, rigorously enforcing the IRS 5-year Roth lockup rule.
* **Dynamic Tax & Healthcare Modeling:** Accurately models inflating Federal and State tax brackets, ACA subsidy cliffs, Medicare IRMAA surcharges, and the Net Investment Income Tax (NIIT).
* **Terminal Wealth & SECURE 2.0:** Calculates the 10-year inherited IRA liquidation tax burden on your heirs to ensure your optimization strategy preserves maximum net terminal wealth.
* **100% Private & Local:** This tool is a single-file application (`index.html`). There is no backend server, no database, and no tracking. Your sensitive financial data never leaves your browser.

## How to Use
1. **Download/Clone** this repository and simply double-click `index.html` to open it in any modern web browser (Chrome, Safari, Edge).
2. **Input your data** into the sidebar panels:
   * **Life Timeline:** Set your birth date, retirement year, and state of residence.
   * **Assets:** Input your current account balances.
   * **Incomes & Expenses:** Input your earned income, expected Social Security, and major lifetime expenses (living, healthcare, college).
3. **Optimize:** Click the **"Find Optimal Conversion"** button. The engine will instantly run through its grid search and update the interactive chart and year-by-year trajectory table with your optimal plan.
4. **Export:** Use the "Export to PDF" or "Export to JPG" buttons to save a snapshot of your optimal strategy.

## Analytics & Telemetry
This application utilizes privacy-first, cookieless [Cloudflare Web Analytics](https://dash.cloudflare.com/) via an injected beacon. This telemetry tracks basic usage metrics without compromising the core promise of zero-PII client-side computation.
