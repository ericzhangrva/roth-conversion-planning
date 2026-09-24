# DISPATCH — test_writer_e2e

## Mission
Build the comprehensive E2E test suite and test runner `/Users/eric/Dropbox/ai/asset/test_planning.js` according to `/Users/eric/Dropbox/ai/asset/TEST_INFRA.md` and `/Users/eric/Dropbox/ai/asset/PROJECT.md`.
Upon completion and verification of the test suite, publish `/Users/eric/Dropbox/ai/asset/TEST_READY.md`.

## Working Directory
`/Users/eric/Dropbox/ai/asset/.agents/test_writer_e2e`

## File Ownership
- Exclusively owns `/Users/eric/Dropbox/ai/asset/test_planning.js` and `/Users/eric/Dropbox/ai/asset/TEST_READY.md`.
- You MUST NOT modify `/Users/eric/Dropbox/ai/asset/planning.html`.

## Required Reading
1. `/Users/eric/Dropbox/ai/asset/.agents/ORIGINAL_REQUEST.md` (authoritative user requirements)
2. `/Users/eric/Dropbox/ai/asset/PROJECT.md` (project plan, feature inventory, interface contracts)
3. `/Users/eric/Dropbox/ai/asset/TEST_INFRA.md` (test methodology, 4-tier coverage plan)
4. `/Users/eric/Dropbox/ai/asset/.agents/spec_miner_survey/report.md` (exact mathematical specifications)
5. `/Users/eric/Dropbox/ai/asset/.agents/explorer_arch/report.md` (test runner architecture)

## Scope & Requirements
1. Build `/Users/eric/Dropbox/ai/asset/test_planning.js` capable of running under both Node.js (`node test_planning.js`) and macOS JavaScriptCore (`/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc test_planning.js`).
2. Implement tests spanning Tiers 1-4:
   - **Tier 1 (Feature Coverage)**: >=5 tests per feature (inflation, college, healthcare, SS, waterfall, Roth 5-yr, death tax, TVM, optimizer).
   - **Tier 2 (Boundary & Corner Cases)**: Zero balances, zero inflation, late retirement, high net worth, age 65 edge conditions.
   - **Tier 3 (Cross-Feature Combinations)**: College crunch + Roth conversions, healthcare subsidy cliff transitions under conversion income spikes.
   - **Tier 4 (Real-World Scenarios)**: 5 application scenarios from TEST_INFRA.md.
3. Test runner should test against the exported `FinancialEngine` module (via extraction from `planning.html` or evaluation) and verify DOM element IDs defined in `PROJECT.md`.
4. Run the test script to verify it functions properly.
5. Create `/Users/eric/Dropbox/ai/asset/TEST_READY.md` summarizing the test suite coverage and pass command.
6. Deliver `handoff.md` and notify the orchestrator.

## 2026-09-23T17:09:03Z
You are test_writer_e2e. Your working directory is `/Users/eric/Dropbox/ai/asset/.agents/test_writer_e2e`.
You MUST read `/Users/eric/Dropbox/ai/asset/.agents/ORIGINAL_REQUEST.md` before starting work.
Also read `/Users/eric/Dropbox/ai/asset/.agents/test_writer_e2e/DISPATCH.md`.
Read `/Users/eric/Dropbox/ai/asset/TEST_INFRA.md`, `/Users/eric/Dropbox/ai/asset/PROJECT.md`, and `/Users/eric/Dropbox/ai/asset/.agents/spec_miner_survey/report.md`.
Your mission is to construct `/Users/eric/Dropbox/ai/asset/test_planning.js` containing comprehensive tests across Tiers 1-4 for the financial planning dashboard `planning.html`.
When complete, publish `/Users/eric/Dropbox/ai/asset/TEST_READY.md`, deliver your `handoff.md`, and notify the orchestrator via send_message.
