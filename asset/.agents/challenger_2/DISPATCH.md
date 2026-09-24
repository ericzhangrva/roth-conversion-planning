# DISPATCH — challenger_2

## Mission
Perform mathematical invariant testing and adversarial verification of `/Users/eric/Dropbox/ai/asset/planning.html`, focusing on tax calculations, TVM relationships, SECURE Act death tax math, and optimization solver consistency.

## Working Directory
`/Users/eric/Dropbox/ai/asset/.agents/challenger_2`

## Mandatory Reading
1. `/Users/eric/Dropbox/ai/asset/.agents/ORIGINAL_REQUEST.md` (authoritative user requirements)
2. `/Users/eric/Dropbox/ai/asset/PROJECT.md` (project plan, feature inventory, architecture, contracts)
3. `/Users/eric/Dropbox/ai/asset/planning.html` (the target file to stress test)
4. `/Users/eric/Dropbox/ai/asset/test_planning.js` (existing test suite)

## Scope & Duties
1. Empirically verify mathematical invariants:
   - TVM invariant: Verify $FV = PV \times (1 + r)^{T-1}$ holds across varying interest/discount rates.
   - Marginal tax monotonic non-decreasing property across progressive brackets.
   - College expense sum strictly equals total expense (12.5% + 25% + 25% + 25% + 12.5% = 100%).
   - Feasibility constraint invariant: No candidate labeled feasible may ever have `Cash + Inv + Accessible Roth < 0`.
   - SECURE Act liquidation invariance: 2 heirs $\times$ 10 years $\times$ annual tax difference accurately reflects marginal tax brackets.
2. Execute your test harnesses using JavaScriptCore or Python.
3. Formulate an explicit verdict: **APPROVE** (empirical correctness verified) or **REQUEST_CHANGES** (invariants violated).
4. Deliver `handoff.md` with your verdict and notify orchestrator.

## 2026-09-23T17:18:49Z
You are challenger_2. Your working directory is `/Users/eric/Dropbox/ai/asset/.agents/challenger_2`.
You MUST read `/Users/eric/Dropbox/ai/asset/.agents/ORIGINAL_REQUEST.md` before starting work.
Also read `/Users/eric/Dropbox/ai/asset/.agents/challenger_2/DISPATCH.md`.
Read `/Users/eric/Dropbox/ai/asset/PROJECT.md`.
Perform mathematical invariant testing and verification of `/Users/eric/Dropbox/ai/asset/planning.html` (TVM PV/FV relationships, tax monotonicity, feasibility constraint invariance, SECURE Act death tax calculations).
Deliver your handoff.md with an explicit verdict: APPROVE or REQUEST_CHANGES, and notify the orchestrator via send_message.
