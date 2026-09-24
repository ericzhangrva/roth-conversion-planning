# Implementation & Orchestration Plan — Targeted Refactor of `planning.html`

## Objective
Refactor `planning.html` to implement:
1. **R1. Multi-Phase Roth Optimization**: Refactor `findOptimalConversion` to optimize across 3 liquidity phases (Phase 1: First 5 Years, Phase 2: Year 6 to Age 59.5, Phase 3: Age 59.5 to Age 75) using a fast, performant solver (e.g., coarse-to-fine sweep or sequential greedy solver) that prevents liquidity crashes and minimizes lifetime tax.
2. **R2. Input Validation Bounds**: Dynamic DOM input validation ensuring `retireYear >= currentYear + 1`, `eolYear >= retireYear`, and `eolYear >= currentYear + 1`.
3. **R3. Retirement Year Alignment**: Ensure the retirement year input is strictly the first full year retired (`isRetired = true`), aligning UI labels, table rows, and simulation logic.

## Team Topology (Small Focused Team)
- **Explorer**: Explore `planning.html`, analyze current `findOptimalConversion`, inputs, DOM event listeners, retirement year logic, and formulate concrete refactoring specification and mathematical solver design.
- **Worker**: Implement R1, R2, R3 in `planning.html`. Verify syntax, UI behavior, and simulation accuracy with automated node/js tests.
- **Reviewers (2)**: Independent code and functionality review (correctness, UI fidelity, browser responsiveness).
- **Challengers (2)**: Stress testing edge cases (boundary years, extreme inputs, liquidity crash scenarios, optimality comparison).
- **Forensic Auditor**: Integrity verification (no dummy facades, no hardcoded values, authentic algorithmic solution).

## Iteration & Verification Milestones
- **Milestone 1**: Exploration & Technical Spec Formulation
- **Milestone 2**: Worker Implementation & Automated Unit/E2E Verification
- **Milestone 3**: Gate Verification (2 Reviewers + 2 Challengers + 1 Forensic Auditor)
- **Milestone 4**: Final Synthesis & User Delivery
