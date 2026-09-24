# Audit Execution Plan: planning.html Financial & Logical Engine

## Objective
Deliver a comprehensive, mathematically rigorous, and structurally sound financial audit of `planning.html` in `/Users/eric/Dropbox/ai/asset/simulation_audit.md`, fulfilling all requirements (R1, R2, R3) and acceptance criteria with a small, focused team.

## Requirements Breakdown
- **R1: Deep Financial Audit**
  - Progressive tax brackets implementation and inflation indexation logic.
  - UI defaults & assumptions (e.g., inflation rate 3.5%, investment return 9%, interest rate 5%, living expenses $60k, earned income $275k).
  - Healthcare subsidy cliffs (ACA MAGI cliff vs ACA subsidy phase-out rules post-ARPA/IRA, drop-off at 65).
  - College distribution modeling (12.5% / 25% / 25% / 25% / 12.5% over 5 years).
  - Roth 5-year rule & ordering rules (conversions accessibility, principal vs earnings, penalty vs tax).
- **R2: Advanced Tax Mechanics & Blind Spots**
  - Preferential Capital Gains tax brackets (0%, 15%, 20%) and cost basis tracking (vs ordinary income taxation of investment growth).
  - Net Investment Income Tax (NIIT, 3.8% on lesser of NII or MAGI over $200k/$250k).
  - Medicare Part B/D IRMAA surcharges (MAGI tiered cliffs, 2-year lookback).
  - Required Minimum Distributions (RMDs, SECURE 2.0 Uniform Lifetime Table starting at 73/75) vs voluntary Roth conversions post-75.
- **R3: Deliverable Report Structure (`simulation_audit.md`)**
  - Section 1: Executive Summary
  - Section 2: Critical Flaws (Structural & mathematical errors in current logic, with JS citations & replacement formulas)
  - Section 3: Unreasonable Assumptions (Unrealistic UI defaults & behavioral models, with JS citations & recommended adjustments)
  - Section 4: Missing Features (Capital gains, NIIT, IRMAA, RMDs, with programmatic algorithms & integration points)
  - Section 5: Implementation Blueprint (Concrete JavaScript helper functions and step-by-step logic flows for future integration)

## Acceptance Criteria Checklist
- [ ] At least 3 distinct structural or mathematical limitations identified.
- [ ] Concrete, programmatic solutions and mathematical formulas provided for each flaw.
- [ ] Exact citations of JavaScript functions, variable names, and math currently in `planning.html`.
- [ ] Code in `planning.html` remains completely untouched (read-only audit).
- [ ] Report placed at `/Users/eric/Dropbox/ai/asset/simulation_audit.md`.

## Team Roles & Phased Execution
1. **Phase 1: Exploration & Code Mining**
   - Subagent: `teamwork_preview_explorer` (conv: explorer_audit)
   - Scope: Analyze `planning.html` exhaustively. Identify exact functions, line numbers, formulas, variables, tax logic, and blind spots.
2. **Phase 2: Report Drafting**
   - Subagent: `teamwork_preview_worker` (conv: worker_audit)
   - Scope: Author `/Users/eric/Dropbox/ai/asset/simulation_audit.md` using explorer findings, detailing formulas, citations, and flows.
3. **Phase 3: Review & Adversarial Check**
   - Subagent: `teamwork_preview_reviewer` (conv: reviewer_audit)
   - Scope: Verify report accuracy against `planning.html` code and acceptance criteria.
4. **Phase 4: Forensic Integrity Audit**
   - Subagent: `teamwork_preview_auditor` (conv: auditor_audit)
   - Scope: Audit report authenticity, ensuring zero fabrication and complete rigor.
5. **Phase 5: Gate Check & Victory Handoff**
   - Orchestrator evaluates gate, compiles final summary, and messages Sentinel.
