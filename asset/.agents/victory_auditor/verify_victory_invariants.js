/**
 * Independent Victory Auditor Invariant Verification Script
 * Author: Victory Auditor (teamwork_preview_victory_auditor)
 * Date: 2026-09-23
 * Runtime: macOS JavaScriptCore (`jsc`)
 */

(function () {
  'use strict';

  var isNode = typeof process !== 'undefined' && process.versions && !!process.versions.node;
  var readFileFn = null;
  var printFn = null;
  var quitFn = null;

  if (isNode) {
    var fs = require('fs');
    readFileFn = function(p) { return fs.readFileSync(p, 'utf8'); };
    printFn = console.log.bind(console);
    quitFn = function(code) { process.exit(code); };
  } else {
    readFileFn = typeof readFile === 'function' ? readFile : read;
    printFn = print;
    quitFn = quit;
  }

  var passCount = 0;
  var failCount = 0;
  var testResults = [];

  function assert(cond, name, details) {
    if (cond) {
      passCount++;
      testResults.push({ name: name, pass: true });
      printFn('  [PASS] ' + name);
    } else {
      failCount++;
      testResults.push({ name: name, pass: false, details: details });
      printFn('  [FAIL] ' + name + (details ? ' (' + details + ')' : ''));
    }
  }

  function assertNear(val, expected, tolerancePct, name) {
    var diff = Math.abs(val - expected);
    var allowed = Math.abs(expected) * (tolerancePct / 100);
    if (allowed < 1e-6) allowed = 1e-6;
    assert(diff <= allowed, name, 'Expected ~' + expected + ', got ' + val + ' (diff: ' + diff + ')');
  }

  printFn('\n========================================================================');
  printFn(' VICTORY AUDIT INDEPENDENT INVARIANT EXECUTION & FORENSIC SUITE');
  printFn(' Target: /Users/eric/Dropbox/ai/asset/planning.html');
  printFn('========================================================================\n');

  // Load planning.html content directly
  var htmlPath = '/Users/eric/Dropbox/ai/asset/planning.html';
  var html = readFileFn(htmlPath);
  assert(html && html.length > 10000, 'HTML file loads from disk', 'Length: ' + (html ? html.length : 0));

  // Extract <script> content
  var scriptRegex = /<script(?![^>]*src)[^>]*>([\s\S]*?)<\/script>/gi;
  var scriptMatch = scriptRegex.exec(html);
  assert(scriptMatch && scriptMatch[1].length > 5000, 'Embedded JavaScript extracted from HTML');
  var scriptCode = scriptMatch ? scriptMatch[1] : '';

  // Setup Sandbox
  var mockStorage = {};
  var mockElements = {};
  var mockDocument = {
    getElementById: function (id) {
      if (!mockElements[id]) {
        mockElements[id] = {
          id: id,
          value: '0',
          textContent: '',
          innerHTML: '',
          checked: false,
          style: {},
          classList: { add: function(){}, remove: function(){}, contains: function(){ return false; } },
          addEventListener: function(){}
        };
      }
      return mockElements[id];
    }
  };

  var mockModule = { exports: {} };
  var sandboxScope = {
    window: {
      addEventListener: function(){},
      localStorage: {
        getItem: function(k){ return mockStorage[k] || null; },
        setItem: function(k, v){ mockStorage[k] = String(v); },
        removeItem: function(k){ delete mockStorage[k]; }
      },
      document: mockDocument
    },
    document: mockDocument,
    module: mockModule,
    exports: mockModule.exports,
    console: { log: function(){}, warn: function(){}, error: function(){} },
    Chart: function(){ this.update = function(){}; this.destroy = function(){}; }
  };

  // Execute inside sandbox function
  var sandboxFunc = new Function(
    'window', 'document', 'module', 'exports', 'console', 'Chart',
    scriptCode + '; return typeof FinancialEngine !== "undefined" ? FinancialEngine : module.exports;'
  );
  var engine = sandboxFunc(
    sandboxScope.window,
    sandboxScope.document,
    sandboxScope.module,
    sandboxScope.exports,
    sandboxScope.console,
    sandboxScope.Chart
  );

  assert(engine !== null && typeof engine === 'object', 'FinancialEngine successfully initialized');

  // --------------------------------------------------------------------------
  // SECTION 1: Static Architecture & AC Checks
  // --------------------------------------------------------------------------
  printFn('\n--- Section 1: Static Architecture & Acceptance Criteria ---');
  
  // Single-file check: no local .js or .css links
  var localJsLinks = (html.match(/<script\s+src=["'](?!https?:\/\/)/gi) || []).length;
  var localCssLinks = (html.match(/<link\s+[^>]*rel=["']stylesheet["'][^>]*href=["'](?!https?:\/\/)/gi) || []).length;
  assert(localJsLinks === 0, 'No local external JS scripts linked (single-file requirement)');
  assert(localCssLinks === 0, 'No local external CSS stylesheets linked (single-file requirement)');
  assert(html.indexOf('chart.umd.min.js') !== -1, 'Chart.js included via CDN link');

  // SafeStorage: test defensive behavior against localStorage SecurityError
  var safeStorage = engine.SafeStorage;
  assert(typeof safeStorage === 'object', 'SafeStorage wrapper exists');
  // Simulate throwing window.localStorage
  var origWindowLS = sandboxScope.window.localStorage;
  sandboxScope.window.localStorage = {
    getItem: function() { throw new Error('SecurityError: Access is denied for file:///'); },
    setItem: function() { throw new Error('SecurityError: Access is denied for file:///'); }
  };
  var threw = false;
  try {
    safeStorage.setItem('testKey', 'testVal');
    var retrieved = safeStorage.getItem('testKey');
    assert(retrieved === 'testVal', 'SafeStorage in-memory fallback successfully handles file:/// SecurityError');
  } catch(e) {
    threw = true;
  }
  assert(!threw, 'SafeStorage did not throw SecurityError on file:/// simulation');
  sandboxScope.window.localStorage = origWindowLS;

  // Verify all R1 Input Element IDs in HTML markup
  var requiredInputIds = [
    'input-birthYear', 'input-retireYear', 'input-eolYear', 'input-inflationRate',
    'input-cashStart', 'input-cashInterestRate', 'input-invStart', 'input-invReturnRate',
    'input-pretaxStart', 'input-rothStart', 'input-rothPrincipalStart',
    'input-collegeTotal', 'input-collegeStartYear', 'input-healthSubsidized',
    'input-healthUnsubsidized', 'input-ssStartAge', 'input-ssAmount',
    'input-earnedIncome', 'input-livingExpensesStart', 'input-stateTaxRate'
  ];
  var missingInputs = [];
  requiredInputIds.forEach(function(id) {
    if (html.indexOf('id="' + id + '"') === -1) missingInputs.push(id);
  });
  assert(missingInputs.length === 0, 'All 20 required R1 input IDs present in HTML markup', 'Missing: ' + missingInputs.join(', '));

  // Verify R4 Optimizer and R3 KPI IDs in HTML markup
  var requiredOtherIds = [
    'opt-obj-raw', 'opt-obj-tvm', 'btn-optimize', 'slider-conversion', 'val-conversion', 'opt-status',
    'kpi-eol-cash', 'kpi-eol-inv', 'kpi-eol-pretax', 'kpi-eol-roth',
    'kpi-total-tax-raw', 'kpi-total-tax-pv', 'kpi-total-tax-fv', 'kpi-death-tax',
    'table-simulation-body', 'chart-canvas'
  ];
  var missingOther = [];
  requiredOtherIds.forEach(function(id) {
    if (html.indexOf('id="' + id + '"') === -1) missingOther.push(id);
  });
  assert(missingOther.length === 0, 'All required optimizer, KPI, table, and chart IDs present in HTML markup', 'Missing: ' + missingOther.join(', '));

  // --------------------------------------------------------------------------
  // SECTION 2: R1 UI Default Parameter Invariants
  // --------------------------------------------------------------------------
  printFn('\n--- Section 2: R1 Parameter Defaults ---');
  var defs = engine.DEFAULT_INPUTS;
  assert(defs.birthYear === 1976, 'Default birthYear == 1976');
  assert(defs.retireYear === 2027, 'Default retireYear == 2027');
  assert(defs.eolYear === 2060, 'Default eolYear == 2060');
  assert(defs.inflationRate === 0.035, 'Default inflationRate == 0.035 (3.5%)');
  assert(defs.cashStart === 500000, 'Default cashStart == 500000 ($500K)');
  assert(defs.cashInterestRate === 0.05, 'Default cashInterestRate == 0.05 (5%)');
  assert(defs.invStart === 300000, 'Default invStart == 300000 ($300K)');
  assert(defs.invReturnRate === 0.09, 'Default invReturnRate == 0.09 (9%)');
  assert(defs.pretaxStart === 5000000, 'Default pretaxStart == 5000000 ($5M)');
  assert(defs.rothStart === 120000, 'Default rothStart == 120000 ($120K)');
  assert(defs.rothPrincipalStart === 25000, 'Default rothPrincipalStart == 25000 ($25K)');
  assert(defs.collegeTotal === 100000, 'Default collegeTotal == 100000 ($100K)');
  assert(defs.collegeStartYear === 2029, 'Default collegeStartYear == 2029');
  assert(defs.healthSubsidized === 5000, 'Default healthSubsidized == 5000 ($5K)');
  assert(defs.healthUnsubsidized === 25000, 'Default healthUnsubsidized == 25000 ($25K)');
  assert(defs.ssStartAge === 62, 'Default ssStartAge == 62');
  assert(defs.ssAmount === 60000, 'Default ssAmount == 60000 ($60K)');
  assert(defs.earnedIncome === 275000, 'Default earnedIncome == 275000 ($275K)');
  assert(defs.livingExpensesStart === 60000, 'Default livingExpensesStart == 60000 ($60K)');
  assert(defs.stateTaxRate === 0.0575, 'Default stateTaxRate == 0.0575 (5.75%)');

  // --------------------------------------------------------------------------
  // SECTION 3: R2 Simulation Engine Mathematical Invariants
  // --------------------------------------------------------------------------
  printFn('\n--- Section 3: R2 Simulation Engine Invariants ---');

  // 3.1 Inflation Indexation on Federal Tax Brackets
  var taxYear1 = engine.computeFederalTax(100000, 1.0, 'MFJ');
  var taxYear10 = engine.computeFederalTax(100000, Math.pow(1.035, 9), 'MFJ');
  assert(taxYear1 > taxYear10, 'Inflation indexing expands brackets: tax on $100K in Year 10 (' + taxYear10.toFixed(2) + ') < Year 1 (' + taxYear1.toFixed(2) + ')');
  // Check exact threshold scaling
  var baseMax1 = engine.BASE_FED_BRACKETS_MFJ[0].max; // 23850
  var expectedYr10Max1 = baseMax1 * Math.pow(1.035, 9);
  var taxAtYr10Threshold = engine.computeFederalTax(expectedYr10Max1, Math.pow(1.035, 9), 'MFJ');
  assertNear(taxAtYr10Threshold, expectedYr10Max1 * 0.10, 0.01, 'Federal 10% bracket expands accurately at 3.5% compounding');

  // 3.2 College 5-Year Schedule (12.5%, 25%, 25%, 25%, 12.5%) Zero Inflation
  var c2028 = engine.computeCollegeExpense(2028, 2029, 100000);
  var c2029 = engine.computeCollegeExpense(2029, 2029, 100000);
  var c2030 = engine.computeCollegeExpense(2030, 2029, 100000);
  var c2031 = engine.computeCollegeExpense(2031, 2029, 100000);
  var c2032 = engine.computeCollegeExpense(2032, 2029, 100000);
  var c2033 = engine.computeCollegeExpense(2033, 2029, 100000);
  var c2034 = engine.computeCollegeExpense(2034, 2029, 100000);

  assert(c2028 === 0, 'College expense before 2029 is strictly $0');
  assertNear(c2029, 12500, 0.01, 'College Year 1 (2029) is 12.5% ($12,500)');
  assertNear(c2030, 25000, 0.01, 'College Year 2 (2030) is 25.0% ($25,000)');
  assertNear(c2031, 25000, 0.01, 'College Year 3 (2031) is 25.0% ($25,000)');
  assertNear(c2032, 25000, 0.01, 'College Year 4 (2032) is 25.0% ($25,000)');
  assertNear(c2033, 12500, 0.01, 'College Year 5 (2033) is 12.5% ($12,500)');
  assert(c2034 === 0, 'College expense after 2033 is strictly $0');
  assert(c2029 + c2030 + c2031 + c2032 + c2033 === 100000, 'College total sum across 5 years equals exactly $100,000');

  // 3.3 Healthcare Medicare Drop-off at 65 & ACA Subsidy Cliff
  var hSubPre65 = engine.computeHealthcareExpense(64, 80000, 0, 0.035, 5000, 25000, 90000);
  var hUnsubPre65 = engine.computeHealthcareExpense(64, 100000, 0, 0.035, 5000, 25000, 90000);
  assertNear(hSubPre65, 5000, 0.01, 'Pre-65 healthcare subsidized rate ($5,000) when MAGI <= cliff');
  assertNear(hUnsubPre65, 25000, 0.01, 'Pre-65 healthcare unsubsidized rate ($25,000) when MAGI > cliff');
  var hAt65 = engine.computeHealthcareExpense(65, 50000, 5, 0.035, 5000, 25000, 90000);
  var hPost65 = engine.computeHealthcareExpense(75, 500000, 15, 0.035, 5000, 25000, 90000);
  assert(hAt65 === 0, 'Healthcare expense drops to strictly $0 at age 65 (Medicare)');
  assert(hPost65 === 0, 'Healthcare expense remains strictly $0 for all ages > 65');

  // 3.4 Social Security Start Age & IRC § 86 Formula
  var ssPre62 = engine.runSimulation({ ssStartAge: 62 }, 0).records.filter(function(r){ return r.age < 62; });
  var ssPost62 = engine.runSimulation({ ssStartAge: 62 }, 0).records.filter(function(r){ return r.age >= 62; });
  var allPre62Zero = ssPre62.every(function(r){ return r.ssBenefit === 0; });
  var allPost62Active = ssPost62.every(function(r){ return r.ssBenefit > 0; });
  assert(allPre62Zero, 'Social security benefit is strictly $0 prior to ssStartAge (62)');
  assert(allPost62Active, 'Social security benefit is active for all ages >= ssStartAge (62)');

  // IRC § 86 formula verification
  var taxableSS_0 = engine.computeTaxableSS(40000, 10000); // PI = 10000 + 20000 = 30000 <= 32000
  assert(taxableSS_0 === 0, 'IRC § 86: 0% taxable when provisional income <= $32K');
  var taxableSS_50 = engine.computeTaxableSS(40000, 20000); // PI = 20000 + 20000 = 40000 (between 32K and 44K) -> 0.5 * 8000 = 4000
  assertNear(taxableSS_50, 4000, 0.01, 'IRC § 86: 50% tier applies between $32K and $44K');
  var taxableSS_85 = engine.computeTaxableSS(40000, 100000); // Capped at 85% of $40K = $34K
  assertNear(taxableSS_85, 34000, 0.01, 'IRC § 86: 85% maximum statutory cap enforced');

  // 3.5 Roth 5-Year Rule & Liquidity Waterfall
  var simConv = engine.runSimulation({ cashStart: 500000, invStart: 300000, rothPrincipalStart: 25000 }, 100000);
  // Year 1 (2027): initial accessible principal is $25,000
  var r2027 = simConv.records[0];
  assertNear(r2027.accessibleRothYE, 25000, 0.01, 'Year 1 accessible Roth principal equals initial $25K contribution basis');
  // 2027 conversion ($100K) unlocks in 2032 (Year 6, 2032 - 2027 = 5)
  var r2031 = simConv.records.find(function(r){ return r.year === 2031; });
  var r2032 = simConv.records.find(function(r){ return r.year === 2032; });
  assert(r2032.accessibleRothYE >= r2031.accessibleRothYE + 90000, 'Roth 2027 conversion matures and unlocks in 2032 (5-year rule)');

  // 3.6 SECURE Act 10-Year Inherited IRA Death Tax
  var deathTaxZero = engine.computeDeathTax(0, 2060, 1976, 0.035, 0.0575);
  assert(deathTaxZero === 0, 'Death Tax on $0 pre-tax balance is strictly $0');
  var deathTax1M = engine.computeDeathTax(1000000, 2060, 1976, 0.035, 0.0575);
  var deathTax10M = engine.computeDeathTax(10000000, 2060, 1976, 0.035, 0.0575);
  assert(deathTax1M > 0, 'Death Tax on $1M pre-tax balance is positive (' + Math.round(deathTax1M) + ')');
  assert(deathTax10M > deathTax1M * 10, 'Death Tax is progressively higher on larger balance due to tax brackets');

  // 3.7 TVM Invariants: FV = PV * (1 + r)^(N - 1)
  var simBase = engine.runSimulation({}, 0);
  var N = simBase.records.length; // 34 years (2027 to 2060)
  var r = 0.035;
  var expectedFVFromPV = simBase.pvTotalTax * Math.pow(1 + r, N - 1);
  assertNear(simBase.fvTotalTax, expectedFVFromPV, 0.05, 'TVM invariant FV_total = PV_total * (1 + r)^(N-1) verified to <0.05%');
  assert(simBase.rawTotalTax > simBase.pvTotalTax, 'Raw total tax > PV total tax (positive discount rate)');
  assert(simBase.fvTotalTax > simBase.rawTotalTax, 'FV total tax > Raw total tax (positive compounding rate)');

  // --------------------------------------------------------------------------
  // SECTION 4: R4 Optimization Loop & Invariants
  // --------------------------------------------------------------------------
  printFn('\n--- Section 4: R4 Optimization Loop Invariants ---');
  var startTime = new Date().getTime();
  var optRaw = engine.findOptimalConversion({}, 'raw');
  var elapsedMs = new Date().getTime() - startTime;
  printFn('  Optimization execution time: ' + elapsedMs + ' ms');

  assert(optRaw.candidatesEvaluated === 101, 'Optimizer evaluated exactly 101 candidates ($0 to $500K in $5K steps)');
  assert(optRaw.bestAnnualConversion >= 0 && optRaw.bestAnnualConversion <= 500000, 'Optimal conversion within valid range [0, 500K]');
  assert(optRaw.bestAnnualConversion % 5000 === 0, 'Optimal conversion is an integer multiple of $5,000');
  assert(optRaw.bestResult.isFeasible === true, 'Optimal trajectory satisfies feasibility constraint (Cash + Inv + Accessible Roth >= 0)');
  assert(elapsedMs < 100, 'Optimization completed in < 100 ms (Actual: ' + elapsedMs + ' ms)');

  // Test TVM optimization
  var optTVM = engine.findOptimalConversion({}, 'tvm');
  assert(optTVM.candidatesEvaluated === 101, 'TVM optimizer evaluated exactly 101 candidates');
  assert(optTVM.bestResult.isFeasible === true, 'TVM optimal trajectory satisfies feasibility constraint');

  // --------------------------------------------------------------------------
  // SECTION 5: Anti-Cheating & Sensitivity Mutation Probes
  // --------------------------------------------------------------------------
  printFn('\n--- Section 5: Anti-Cheating & Dynamic Sensitivity Probes ---');

  // Probe 1: Zero conversions vs optimal conversion
  var simZero = engine.runSimulation({}, 0);
  assert(simZero.rawTotalTax > optRaw.bestMetricValue, 'Optimal conversion slashes lifetime tax vs zero conversion: ' +
    Math.round(optRaw.bestMetricValue).toLocaleString() + ' < ' + Math.round(simZero.rawTotalTax).toLocaleString());

  // Probe 2: Sensitivity to pre-tax balance
  var simPretax2M = engine.runSimulation({ pretaxStart: 2000000 }, 0);
  var simPretax10M = engine.runSimulation({ pretaxStart: 10000000 }, 0);
  assert(simPretax10M.deathTax > simPretax2M.deathTax * 5, 'Death tax scales dynamically with starting pre-tax balance');

  // Probe 3: Sensitivity to Living Expenses
  var simExpLow = engine.runSimulation({ livingExpensesStart: 40000 }, 0);
  var simExpHigh = engine.runSimulation({ livingExpensesStart: 120000 }, 0);
  assert(simExpLow.eolCash > simExpHigh.eolCash, 'EOL Cash is sensitive to living expenses');

  // Probe 4: Zero inflation parity: Raw == PV == FV
  var simZeroInf = engine.runSimulation({ inflationRate: 0 }, 0);
  assertNear(simZeroInf.pvTotalTax, simZeroInf.rawTotalTax, 0.001, 'Zero inflation produces exact parity between PV and Raw tax');
  assertNear(simZeroInf.fvTotalTax, simZeroInf.rawTotalTax, 0.001, 'Zero inflation produces exact parity between FV and Raw tax');

  // --------------------------------------------------------------------------
  // SUMMARY
  // --------------------------------------------------------------------------
  printFn('\n========================================================================');
  printFn(' VICTORY AUDITOR INDEPENDENT SUITE SUMMARY');
  printFn('========================================================================');
  printFn(' Total Invariant Probes: ' + (passCount + failCount));
  printFn(' Passed: ' + passCount);
  printFn(' Failed: ' + failCount);
  printFn(' Success Rate: ' + ((passCount / (passCount + failCount)) * 100).toFixed(1) + '%');
  printFn('========================================================================\n');

  if (failCount > 0) {
    quitFn(1);
  } else {
    quitFn(0);
  }
})();
