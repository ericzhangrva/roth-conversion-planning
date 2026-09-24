# Orchestration Plan: Financial Planning & Tax Optimization Dashboard (`planning.html`)

## Objective
Build a standalone, single-file financial dashboard (`planning.html`) using vanilla HTML/JS and Chart.js to simulate and optimize lifetime tax liability from retirement to End of Life, meeting all requirements (R1 UI Inputs & Defaults, R2 Simulation Engine Rules, R3 Output Visuals, R4 Optimization Loop) and all acceptance criteria.

## Strategy & Workflow
Following the Project Pattern with Dual-Track execution:

### Step 1: Survey (Phase 0)
Spawn 3 Explorers / Spec Miners in parallel:
1. `explorer_reqs`: Spec Miner focused on ORIGINAL_REQUEST.md requirements, tax bracket rules, IRS brackets, standard deductions, MAGI cliff, Social Security taxation rules, SECURE Act 10-year rule inheritance math, PV/FV discount rate math.
2. `explorer_existing`: Codebase Explorer examining existing files in `/Users/eric/Dropbox/ai/asset` (`asset.html`, `build_dashboard.py`, `health_cost.py`, `assets_data.json`, `README.md`) to extract existing UI patterns, models, and styling.
3. `explorer_arch`: Architecture & Test Strategy Explorer defining the single-file HTML architecture, Chart.js integration, performance considerations for the 0-$500k in $5k steps optimization loop, and test harness structure.

### Step 2: Synthesis & PROJECT.md / TEST_INFRA.md Definition (Phase 1)
- Reconcile explorer findings.
- Write `PROJECT.md` at project root with Feature Inventory, Architecture, Interface Contracts, and Milestones.
- Initialize `TEST_INFRA.md` for requirement-driven E2E verification.

### Step 3: Dual-Track Execution (Phase 2)
- **Track A (E2E Testing)**: Test Writer builds comprehensive headless test runner/evaluator (`test_planning.js` or Node/Puppeteer/JSDOM runner) covering Tiers 1-4. Publishes `TEST_READY.md`.
- **Track B (Implementation)**: Worker builds `planning.html` implementing all UI inputs, simulation loop, Chart.js visuals, and the fast optimization sweep.

### Step 4: Iteration & Gate Loop (Phase 3)
- Explorer → Worker → Reviewer (2) → Challenger (2) → Forensic Auditor (1).
- Strict gate criteria: all tests pass, reviewers approve, challengers approve, auditor clean.

### Step 5: Hardening & Completion (Phase 4)
- Adversarial testing (Tier 5).
- Final forensic integrity audit.
- Submit victory claim to Sentinel.
