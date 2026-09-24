# Lifetime Financial & Tax Optimization Dashboard

Welcome to the Lifetime Financial & Tax Optimization Dashboard. This application is a fully client-side, privacy-first simulation engine designed to project retirement asset decumulation, optimize Roth conversions, and calculate lifetime tax liabilities (including SECURE 2.0 Act inheritance penalties).

## Features & Logic

- **Dynamic Bracket Inflation:** Federal tax brackets, standard deductions, and state tax rules are dynamically inflated based on the assumed inflation rate to ensure future tax projections are accurate in nominal dollars.
- **Strict Liquidity Enforcement:** The drawdown engine mathematically prevents you from converting too much into a Roth IRA if you don't have enough liquid cash/taxable brokerage to pay the resulting tax bill, ensuring you never run out of spendable cash.
- **5-Year Roth Maturation (FIFO):** Roth conversions are tracked in independent 5-year buckets. You can only withdraw converted principal without penalty after 5 years have elapsed, or immediately once you cross age 59.5.
- **Medicare IRMAA & ACA Subsidies:** The simulation models the "subsidy cliff" for ACA health insurance before age 65, and calculates Medicare IRMAA surcharge tiers for ages 65+.
- **SECURE 2.0 Death Tax:** The simulator projects End-of-Life (EOL) wealth transfer, liquidating the remaining Pre-Tax 401(k) / IRA balance over the strict 10-year window mandated by the SECURE Act, adjusting for the number of heirs and their estimated baseline incomes.
- **Brute Force Optimizer:** The engine simulates every possible Roth conversion strategy (from $0 to massive sums) and plots the trajectory that mathematically minimizes your Lifetime Total Tax Liability (in both Raw and Time-Value-of-Money discounted terms).

## Usage

Simply open `index.html` in any modern web browser. Because all calculations run in JavaScript entirely on your local machine, your financial data is completely secure and is never transmitted to any server.

Use the left sidebar to tweak your starting balances, expected retirement timeline, and major living expenses. The interactive data table and charts will instantly re-simulate the rest of your life.
