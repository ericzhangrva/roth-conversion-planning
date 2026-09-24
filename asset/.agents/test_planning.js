/**
 * ============================================================================
 * Financial Planning & Lifetime Tax Optimization Dashboard — Test Runner
 * Target File: /Users/eric/Dropbox/ai/asset/planning.html
 * Test Suite: Tiers 1-4 Comprehensive Verification & Static DOM Auditing
 * Dual-Environment Target: Node.js (`node test_planning.js`) &
 *                          macOS JavaScriptCore (`jsc test_planning.js`)
 * ============================================================================
 */

(function () {
  'use strict';

  // --------------------------------------------------------------------------
  // 1. Dual-Environment Abstraction Layer (Node.js & JavaScriptCore)
  // --------------------------------------------------------------------------
  const isNode = typeof process !== 'undefined' && process.versions && !!process.versions.node;
  let readFileContent, log, logError, exitWithCode, performanceNow;

  if (isNode) {
    const fs = require('fs');
    readFileContent = function (filePath) {
      return fs.readFileSync(filePath, 'utf8');
    };
    log = console.log.bind(console);
    logError = console.error.bind(console);
    exitWithCode = function (code) {
      process.exit(code);
    };
    performanceNow = function () {
      if (typeof performance !== 'undefined' && performance.now) {
        return performance.now();
      }
      const hr = process.hrtime();
      return hr[0] * 1000 + hr[1] / 1e6;
    };
  } else {
    // macOS JavaScriptCore (jsc) environment
    readFileContent = function (filePath) {
      if (typeof readFile === 'function') {
        return readFile(filePath);
      }
      if (typeof read === 'function') {
        return read(filePath);
      }
      throw new Error('No built-in file reader available in this JavaScriptCore shell.');
    };
    log = function (msg) {
      print(msg);
    };
    logError = function (msg) {
      print('ERROR: ' + msg);
    };
    exitWithCode = function (code) {
      quit(code);
    };
    performanceNow = function () {
      if (typeof Date.now === 'function') return Date.now();
      return new Date().getTime();
    };
    // Polyfill console for jsc
    if (typeof console === 'undefined') {
      console = {
        log: print,
        warn: print,
        error: print,
        info: print
      };
    }
  }

  // --------------------------------------------------------------------------
  // 2. ANSI Styling & Test Reporting Infrastructure
  // --------------------------------------------------------------------------
  const Colors = {
    reset: '\x1b[0m',
    bright: '\x1b[1m',
    dim: '\x1b[2m',
    green: '\x1b[32m',
    red: '\x1b[31m',
    yellow: '\x1b[33m',
    blue: '\x1b[34m',
    magenta: '\x1b[35m',
    cyan: '\x1b[36m',
    white: '\x1b[37m'
  };

  function colorize(color, text) {
    return color + text + Colors.reset;
  }

  let totalTests = 0;
  let passedTests = 0;
  let failedTests = 0;
  const failureReports = [];
  let currentSuite = '';

  function describe(suiteName, fn) {
    currentSuite = suiteName;
    log('\n' + colorize(Colors.bright + Colors.blue, '▶ ' + suiteName));
    fn();
  }

  function test(testName, fn) {
    totalTests++;
    try {
      fn();
      passedTests++;
      log('  ' + colorize(Colors.green, '✓') + ' ' + colorize(Colors.dim, testName));
    } catch (err) {
      failedTests++;
      const errorMsg = err && err.message ? err.message : String(err);
      log('  ' + colorize(Colors.red, '✗') + ' ' + testName);
      log('    ' + colorize(Colors.red, 'Assertion Error: ' + errorMsg));
      failureReports.push({
        suite: currentSuite,
        test: testName,
        error: errorMsg,
        stack: err && err.stack ? err.stack : null
      });
    }
  }

  // Assertion Primitives
  function assert(condition, message) {
    if (!condition) {
      throw new Error(message || 'Assertion failed: expected true, got false');
    }
  }

  function assertEqual(actual, expected, message) {
    if (actual !== expected) {
      throw new Error((message || 'Equality failed') + ': expected ' + JSON.stringify(expected) + ', but got ' + JSON.stringify(actual));
    }
  }

  function assertClose(actual, expected, tolerance, message) {
    const tol = typeof tolerance === 'number' ? tolerance : 0.01;
    const diff = Math.abs(actual - expected);
    if (diff > tol) {
      throw new Error((message || 'Numerical tolerance exceeded') + ': expected ' + expected + ' (±' + tol + '), got ' + actual + ' (diff: ' + diff + ')');
    }
  }

  function assertGreaterThan(actual, min, message) {
    if (actual <= min) {
      throw new Error((message || 'assertGreaterThan failed') + ': expected ' + actual + ' > ' + min);
    }
  }

  function assertLessThan(actual, max, message) {
    if (actual >= max) {
      throw new Error((message || 'assertLessThan failed') + ': expected ' + actual + ' < ' + max);
    }
  }

  function assertBetween(actual, min, max, message) {
    if (actual < min || actual > max) {
      throw new Error((message || 'assertBetween failed') + ': expected ' + actual + ' to be between ' + min + ' and ' + max);
    }
  }

  function assertThrows(fn, message) {
    let threw = false;
    try {
      fn();
    } catch (e) {
      threw = true;
    }
    if (!threw) {
      throw new Error(message || 'Expected function to throw, but it succeeded');
    }
  }

  function assertArrayEqual(actual, expected, message) {
    if (!Array.isArray(actual) || !Array.isArray(expected)) {
      throw new Error((message || 'Array equality failed') + ': one of the arguments is not an array');
    }
    if (actual.length !== expected.length) {
      throw new Error((message || 'Array length mismatch') + ': expected ' + expected.length + ', got ' + actual.length);
    }
    for (let i = 0; i < expected.length; i++) {
      if (actual[i] !== expected[i]) {
        throw new Error((message || 'Array item mismatch at index ' + i) + ': expected ' + expected[i] + ', got ' + actual[i]);
      }
    }
  }

  // --------------------------------------------------------------------------
  // 3. Target Loading & Headless Browser Sandbox Construction
  // --------------------------------------------------------------------------
  log(colorize(Colors.bright + Colors.cyan, '========================================================================'));
  log(colorize(Colors.bright + Colors.cyan, ' Financial Planning & Tax Optimization Dashboard — Test Runner'));
  log(colorize(Colors.bright + Colors.cyan, ' Running under: ') + (isNode ? 'Node.js ' + process.version : 'macOS JavaScriptCore'));
  log(colorize(Colors.bright + Colors.cyan, '========================================================================'));

  const candidatePaths = [
    'planning.html',
    './planning.html',
    '/Users/eric/Dropbox/ai/asset/planning.html'
  ];

  let targetHtmlContent = null;
  let resolvedHtmlPath = null;

  for (let i = 0; i < candidatePaths.length; i++) {
    try {
      const content = readFileContent(candidatePaths[i]);
      if (content && content.length > 0) {
        targetHtmlContent = content;
        resolvedHtmlPath = candidatePaths[i];
        break;
      }
    } catch (e) {
      // Continue search
    }
  }

  if (!targetHtmlContent) {
    logError('Target HTML file `planning.html` could not be located in workspace paths.');
    logError('Checked: ' + candidatePaths.join(', '));
    exitWithCode(1);
  }

  log('Target loaded: ' + colorize(Colors.green, resolvedHtmlPath) + ' (' + targetHtmlContent.length + ' bytes)');

  // Extract embedded JavaScript block
  const scriptRegex = /<script(?![^>]*src)[^>]*>([\s\S]*?)<\/script>/gi;
  let scriptContent = '';
  let scriptMatch;
  while ((scriptMatch = scriptRegex.exec(targetHtmlContent)) !== null) {
    scriptContent += scriptMatch[1] + '\n';
  }

  if (!scriptContent || scriptContent.trim().length === 0) {
    logError('No embedded <script> tags found in ' + resolvedHtmlPath);
    exitWithCode(1);
  }

  // Mock DOM Sandbox Environment
  const mockElements = {};
  const mockDocument = {
    getElementById: function (id) {
      if (!mockElements[id]) {
        mockElements[id] = {
          id: id,
          value: '0',
          textContent: '',
          innerHTML: '',
          checked: false,
          style: {},
          classList: {
            add: function () {},
            remove: function () {},
            contains: function () { return false; }
          },
          addEventListener: function () {},
          appendChild: function () {}
        };
      }
      return mockElements[id];
    },
    querySelectorAll: function () {
      return [];
    },
    createElement: function (tag) {
      return {
        tagName: tag,
        setAttribute: function () {},
        appendChild: function () {},
        style: {},
        classList: { add: function () {}, remove: function () {} },
        innerHTML: '',
        textContent: ''
      };
    },
    addEventListener: function () {}
  };

  const mockWindow = {
    addEventListener: function () {},
    localStorage: {
      _data: {},
      getItem: function (k) { return this._data[k] || null; },
      setItem: function (k, v) { this._data[k] = String(v); },
      removeItem: function (k) { delete this._data[k]; }
    },
    document: mockDocument
  };

  // Mock Chart.js constructor
  function MockChart(ctx, config) {
    this.ctx = ctx;
    this.config = config;
    this.data = config && config.data ? config.data : {};
    this.options = config && config.options ? config.options : {};
    this.update = function () {};
    this.destroy = function () {};
  }
  MockChart.register = function () {};

  const mockModule = { exports: {} };

  // Evaluate script inside sandbox
  let FinancialEngine = null;
  try {
    const sandboxScope = {
      window: mockWindow,
      document: mockDocument,
      Chart: MockChart,
      module: mockModule,
      exports: mockModule.exports,
      console: console,
      setTimeout: function (cb) { cb(); },
      clearTimeout: function () {},
      requestAnimationFrame: function (cb) { cb(); }
    };

    if (isNode) {
      const vm = require('vm');
      vm.createContext(sandboxScope);
      vm.runInContext(scriptContent, sandboxScope);
      FinancialEngine = sandboxScope.module.exports.FinancialEngine ||
                        sandboxScope.module.exports ||
                        sandboxScope.window.FinancialEngine ||
                        sandboxScope.FinancialEngine;
    } else {
      // JSC environment: inject into local scope and eval
      var window = mockWindow;
      var document = mockDocument;
      var Chart = MockChart;
      var module = mockModule;
      var exports = mockModule.exports;
      eval(scriptContent);
      FinancialEngine = module.exports.FinancialEngine ||
                        module.exports ||
                        window.FinancialEngine ||
                        (typeof FinancialEngine !== 'undefined' ? FinancialEngine : null);
    }
  } catch (evalErr) {
    logError('Failed to parse or execute JavaScript from ' + resolvedHtmlPath + ': ' + evalErr.message);
    if (evalErr.stack) logError(evalErr.stack);
    exitWithCode(1);
  }

  if (!FinancialEngine) {
    logError('FinancialEngine module was not exported by ' + resolvedHtmlPath);
    exitWithCode(1);
  }

  log('FinancialEngine initialized successfully. Starting test execution...\n');

  // ==========================================================================
  // SUITE 0: STATIC HTML & DOM REGISTRY AUDIT
  // ==========================================================================
  describe('Suite 0: Static Single-File Architecture & DOM Registry Verification', function () {
    test('0.1: Standalone Single-File Packaging (No local CSS/JS imports)', function () {
      assert(!/<link[^>]+rel=["']stylesheet["'][^>]*>/i.test(targetHtmlContent), 'Must not load external local stylesheet files');
      // Verify Chart.js CDN inclusion
      assert(/cdn\.jsdelivr\.net\/npm\/chart\.js/i.test(targetHtmlContent), 'Must include Chart.js via CDN');
    });

    test('0.2: SafeStorage try/catch defensive wrapper exists', function () {
      assert(typeof FinancialEngine.SafeStorage === 'object', 'SafeStorage object must be exported');
      assert(typeof FinancialEngine.SafeStorage.getItem === 'function', 'SafeStorage.getItem must be a function');
      assert(typeof FinancialEngine.SafeStorage.setItem === 'function', 'SafeStorage.setItem must be a function');
      // In-memory fallback verification: set and get
      FinancialEngine.SafeStorage.setItem('__test_key__', '42');
      assertEqual(FinancialEngine.SafeStorage.getItem('__test_key__'), '42', 'SafeStorage must store and retrieve values');
      FinancialEngine.SafeStorage.removeItem('__test_key__');
    });

    test('0.3: R1 Form Input Element IDs Present in HTML', function () {
      const requiredInputIds = [
        'input-birthYear', 'input-retireYear', 'input-eolYear', 'input-inflationRate',
        'input-cashStart', 'input-cashInterestRate', 'input-invStart', 'input-invReturnRate',
        'input-pretaxStart', 'input-rothStart', 'input-rothPrincipalStart',
        'input-collegeTotal', 'input-collegeStartYear', 'input-healthSubsidized',
        'input-healthUnsubsidized', 'input-ssStartAge', 'input-ssAmount',
        'input-earnedIncome', 'input-livingExpensesStart', 'input-stateTaxRate'
      ];
      requiredInputIds.forEach(function (id) {
        assert(targetHtmlContent.indexOf('id="' + id + '"') !== -1, 'Missing required form input element: id="' + id + '"');
      });
    });

    test('0.4: Optimization Control Element IDs Present in HTML', function () {
      const requiredOptIds = [
        'opt-obj-raw', 'opt-obj-tvm', 'btn-optimize', 'slider-conversion',
        'val-conversion', 'opt-status'
      ];
      requiredOptIds.forEach(function (id) {
        assert(targetHtmlContent.indexOf('id="' + id + '"') !== -1, 'Missing optimization control element: id="' + id + '"');
      });
    });

    test('0.5: KPI Metric Card & Visual Element IDs Present in HTML', function () {
      const requiredKpiIds = [
        'kpi-eol-cash', 'kpi-eol-inv', 'kpi-eol-pretax', 'kpi-eol-roth',
        'kpi-total-tax-raw', 'kpi-total-tax-pv', 'kpi-total-tax-fv', 'kpi-death-tax',
        'chart-canvas', 'table-simulation-body'
      ];
      requiredKpiIds.forEach(function (id) {
        assert(targetHtmlContent.indexOf('id="' + id + '"') !== -1, 'Missing output/KPI element: id="' + id + '"');
      });
    });
  });

  // ==========================================================================
  // TIER 1: FEATURE COVERAGE (>=5 tests per feature)
  // ==========================================================================

  // Feature 1: Inflation Indexing
  describe('Tier 1.1: Inflation Indexing (Feature F03)', function () {
    test('1.1.1: Standard Deduction compounds cumulatively at 3.5%/yr', function () {
      const baseStd = FinancialEngine.BASE_STD_DEDUCTION_MFJ || 30000;
      // Year 1 (t=0)
      assertEqual(baseStd, 30000, 'Baseline standard deduction in Year 1 must be $30,000');
      // Year 2 (t=1): $30,000 * 1.035 = $31,050
      const stdYr2 = baseStd * 1.035;
      assertClose(stdYr2, 31050, 0.01, 'Year 2 standard deduction should be $31,050');
      // Year 6 (t=5): $30,000 * 1.035^5
      const stdYr6 = baseStd * Math.pow(1.035, 5);
      assertClose(stdYr6, 35630.59, 1.0, 'Year 6 standard deduction should compound to ~$35,631');
    });

    test('1.1.2: Living Expenses compound annually with inflation factor', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      assert(res.records && res.records.length === 34, 'Must return 34 annual simulation records');
      // Year 1 (2027, t=0): $60,000
      assertClose(res.records[0].livingExpenses, 60000, 0.01, 'Year 1 living expenses should equal $60,000');
      // Year 2 (2028, t=1): $60,000 * 1.035 = $62,100
      assertClose(res.records[1].livingExpenses, 62100, 0.01, 'Year 2 living expenses should equal $62,100');
      // Year 11 (2037, t=10): $60,000 * 1.035^10
      const expectedYr11 = 60000 * Math.pow(1.035, 10);
      assertClose(res.records[10].livingExpenses, expectedYr11, 1.0, 'Year 11 living expenses must match 10-year compounding');
    });

    test('1.1.3: Healthcare base costs compound annually with inflation prior to age 65', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      // Pre-65 subsidized cost in Year 1 (2027, age 51): $5,000
      assertClose(res.records[0].healthExpenses, 5000, 0.01, 'Year 1 healthcare should be $5,000');
      // Year 2 (2028, t=1, age 52): $5,000 * 1.035 = $5,175
      assertClose(res.records[1].healthExpenses, 5175, 0.01, 'Year 2 healthcare should be $5,175');
      // Year 5 (2031, t=4, age 55): $5,000 * 1.035^4
      const expYr5 = 5000 * Math.pow(1.035, 4);
      assertClose(res.records[4].healthExpenses, expYr5, 1.0, 'Year 5 healthcare should be inflated');
    });

    test('1.1.4: Progressive Federal Tax Brackets compound annually by inflation', function () {
      // Bracket 22% threshold: Year 1 = $96,950
      const taxYr1 = FinancialEngine.computeFederalTax(96950, 1.0, 'MFJ');
      // In Year 2 with factor 1.035, the exact same income $96,950 should incur slightly LESS tax because thresholds shifted up
      const taxYr2 = FinancialEngine.computeFederalTax(96950, 1.035, 'MFJ');
      assertLessThan(taxYr2, taxYr1, 'Inflated brackets should reduce tax on the same nominal income');
      // If income is multiplied by 1.035, tax should scale by exactly 1.035
      const taxInflatedIncome = FinancialEngine.computeFederalTax(96950 * 1.035, 1.035, 'MFJ');
      assertClose(taxInflatedIncome, taxYr1 * 1.035, 0.5, 'Tax on scaled income in scaled bracket should match homogeneous property');
    });

    test('1.1.5: Subsidy Cliff threshold compounds annually by inflation', function () {
      // At Year 1, $90,000 is subsidized
      const hcYr1_sub = FinancialEngine.computeHealthcareExpense(55, 90000, 0, 0.035, 5000, 25000, 90000);
      assertClose(hcYr1_sub, 5000, 0.01, 'At $90,000 in Year 1, cost should be subsidized ($5,000)');
      // In Year 2 (t=1), cliff is $90,000 * 1.035 = $93,150. An income of $92,000 should be SUBSIDIZED in Year 2
      const hcYr2_sub = FinancialEngine.computeHealthcareExpense(56, 92000, 1, 0.035, 5000, 25000, 90000);
      assertClose(hcYr2_sub, 5000 * 1.035, 0.01, 'In Year 2, $92,000 is under $93,150 cliff so subsidized rate applies');
      // But $94,000 in Year 2 should exceed cliff and receive unsubsidized
      const hcYr2_unsub = FinancialEngine.computeHealthcareExpense(56, 94000, 1, 0.035, 5000, 25000, 90000);
      assertClose(hcYr2_unsub, 25000 * 1.035, 0.01, 'In Year 2, $94,000 exceeds $93,150 cliff so unsubsidized rate applies');
    });

    test('1.1.6: Custom inflation rate (e.g. 5.0%) compounds consistently', function () {
      const customInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { inflationRate: 0.05 });
      const res = FinancialEngine.runSimulation(customInputs, 0);
      const expectedYr2 = 60000 * 1.05;
      assertClose(res.records[1].livingExpenses, expectedYr2, 0.01, 'Year 2 living expenses with 5% inflation should be $63,000');
    });
  });

  // Feature 2: College Schedule
  describe('Tier 1.2: College Funding Schedule (Feature F04)', function () {
    test('1.2.1: Fixed 5-year percentage spread (12.5%, 25%, 25%, 25%, 12.5%)', function () {
      const total = 100000;
      const startYear = 2029;
      assertClose(FinancialEngine.computeCollegeExpense(2029, startYear, total), 12500, 0.01, 'Year 1 must be 12.5% ($12,500)');
      assertClose(FinancialEngine.computeCollegeExpense(2030, startYear, total), 25000, 0.01, 'Year 2 must be 25.0% ($25,000)');
      assertClose(FinancialEngine.computeCollegeExpense(2031, startYear, total), 25000, 0.01, 'Year 3 must be 25.0% ($25,000)');
      assertClose(FinancialEngine.computeCollegeExpense(2032, startYear, total), 25000, 0.01, 'Year 4 must be 25.0% ($25,000)');
      assertClose(FinancialEngine.computeCollegeExpense(2033, startYear, total), 12500, 0.01, 'Year 5 must be 12.5% ($12,500)');
    });

    test('1.2.2: Total sum across all years equals exactly collegeTotal', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      let collegeSum = 0;
      res.records.forEach(function (rec) {
        collegeSum += rec.collegeExpenses;
      });
      assertClose(collegeSum, 100000, 0.01, 'Total lifetime college sum must equal $100,000');
    });

    test('1.2.3: Zero inflation constraint on college expenses', function () {
      const highInflInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { inflationRate: 0.10 });
      const res = FinancialEngine.runSimulation(highInflInputs, 0);
      const rec2033 = res.records.find(function (r) { return r.year === 2033; });
      assert(rec2033, 'Record for 2033 must exist');
      assertEqual(rec2033.collegeExpenses, 12500, 'Year 5 college expense must remain uninflated at $12,500 even at 10% inflation');
    });

    test('1.2.4: Strictly zero outside the 5-year window', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      const rec2027 = res.records.find(function (r) { return r.year === 2027; });
      const rec2028 = res.records.find(function (r) { return r.year === 2028; });
      const rec2034 = res.records.find(function (r) { return r.year === 2034; });
      const rec2060 = res.records.find(function (r) { return r.year === 2060; });
      assertEqual(rec2027.collegeExpenses, 0, 'College in 2027 must be 0');
      assertEqual(rec2028.collegeExpenses, 0, 'College in 2028 must be 0');
      assertEqual(rec2034.collegeExpenses, 0, 'College in 2034 must be 0');
      assertEqual(rec2060.collegeExpenses, 0, 'College in 2060 must be 0');
    });

    test('1.2.5: Scaling with custom college total (e.g. $200,000)', function () {
      const customInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { collegeTotal: 200000 });
      const res = FinancialEngine.runSimulation(customInputs, 0);
      const rec2030 = res.records.find(function (r) { return r.year === 2030; });
      assertEqual(rec2030.collegeExpenses, 50000, 'Year 2 college expense on $200K total should be $50,000');
    });
  });

  // Feature 3: Healthcare Cliff & Medicare Drop
  describe('Tier 1.3: Healthcare Cliff & Age 65 Medicare Drop (Feature F05)', function () {
    test('1.3.1: Pre-65 Subsidized rate applies when MAGI <= Cliff', function () {
      const cost = FinancialEngine.computeHealthcareExpense(55, 85000, 0, 0.035, 5000, 25000, 90000);
      assertEqual(cost, 5000, 'Subsidized $5,000 should apply when MAGI <= $90K');
    });

    test('1.3.2: Pre-65 Unsubsidized rate applies when MAGI > Cliff', function () {
      const cost = FinancialEngine.computeHealthcareExpense(55, 95000, 0, 0.035, 5000, 25000, 90000);
      assertEqual(cost, 25000, 'Unsubsidized $25,000 should apply when MAGI > $90K');
    });

    test('1.3.3: Exact cliff boundary condition: $90,000 vs $90,001', function () {
      const costExact = FinancialEngine.computeHealthcareExpense(55, 90000, 0, 0.035, 5000, 25000, 90000);
      const costAbove = FinancialEngine.computeHealthcareExpense(55, 90001, 0, 0.035, 5000, 25000, 90000);
      assertEqual(costExact, 5000, 'Exact cliff boundary must qualify for subsidized rate');
      assertEqual(costAbove, 25000, '1 dollar above cliff must switch to unsubsidized rate');
    });

    test('1.3.4: Healthcare drops to strictly $0 at Age 65 (Medicare Transition)', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      // Birth 1976 => age 64 in 2040, age 65 in 2041
      const rec64 = res.records.find(function (r) { return r.age === 64; });
      const rec65 = res.records.find(function (r) { return r.age === 65; });
      assert(rec64, 'Record for age 64 must exist');
      assert(rec65, 'Record for age 65 must exist');
      assertGreaterThan(rec64.healthExpenses, 0, 'Healthcare at age 64 must be positive');
      assertEqual(rec65.healthExpenses, 0, 'Healthcare at age 65 must drop to strictly $0');
    });

    test('1.3.5: Post-65 zero healthcare persists through End of Life (Ages 66–84)', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      for (let i = 0; i < res.records.length; i++) {
        const rec = res.records[i];
        if (rec.age >= 65) {
          assertEqual(rec.healthExpenses, 0, 'Healthcare at age ' + rec.age + ' must be $0');
        }
      }
    });
  });

  // Feature 4: Social Security Modeling
  describe('Tier 1.4: Social Security Modeling & Taxation (Feature F06)', function () {
    test('1.4.1: Social Security benefit is strictly $0 prior to ssStartAge', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      // Default ssStartAge = 62. For birth 1976, age 61 is year 2037
      for (let i = 0; i < res.records.length; i++) {
        if (res.records[i].age < 62) {
          assertEqual(res.records[i].ssBenefit, 0, 'SS Benefit at age ' + res.records[i].age + ' must be 0');
        }
      }
    });

    test('1.4.2: Social Security commences exactly in the year client turns ssStartAge', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      const rec62 = res.records.find(function (r) { return r.age === 62; });
      assert(rec62, 'Record for age 62 must exist');
      assertGreaterThan(rec62.ssBenefit, 0, 'SS benefit at start age 62 must be positive');
    });

    test('1.4.3: Social Security benefit compounds with inflation', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      const rec62 = res.records.find(function (r) { return r.age === 62; });
      const rec63 = res.records.find(function (r) { return r.age === 63; });
      assert(rec62 && rec63, 'Records for age 62 and 63 must exist');
      const ratio = rec63.ssBenefit / rec62.ssBenefit;
      assertClose(ratio, 1.035, 0.001, 'SS benefit from age 62 to 63 must inflate by 3.5%');
    });

    test('1.4.4: IRC § 86 Provisional Income formula: 0% tax under $32K threshold', function () {
      // ssAmount = 20000, otherIncome = 10000 => PI = 10000 + 0.5 * 20000 = 20000 <= 32000
      const taxable = FinancialEngine.computeTaxableSS(20000, 10000);
      assertEqual(taxable, 0, 'Taxable SS should be $0 when PI <= $32K');
    });

    test('1.4.5: IRC § 86 Provisional Income formula: Tiered 50% between $32K and $44K', function () {
      // ssAmount = 20000, otherIncome = 30000 => PI = 30000 + 10000 = 40000
      // 50% of (40000 - 32000) = 4000
      const taxable = FinancialEngine.computeTaxableSS(20000, 30000);
      assertEqual(taxable, 4000, 'Taxable SS should be 50% of excess over $32K');
    });

    test('1.4.6: IRC § 86 Statutory Maximum: capped at 85% of benefit', function () {
      // High other income ($200K) pushes PI far beyond $44K
      const taxable = FinancialEngine.computeTaxableSS(60000, 200000);
      assertEqual(taxable, 0.85 * 60000, 'Taxable SS must cap at exactly 85% of gross benefit');
    });
  });

  // Feature 5: Cash Flow Waterfall & Deficit Priority
  describe('Tier 1.5: Cash Flow Waterfall & Liquidity Drawdown (Feature F08)', function () {
    test('1.5.1: Surplus cash flow accumulates in cash without depleting investments', function () {
      // High earned income with modest expenses produces cash accumulation
      const surplusInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, {
        retireYear: 2035,
        earnedIncome: 500000,
        livingExpensesStart: 40000
      });
      const res = FinancialEngine.runSimulation(surplusInputs, 0);
      // In 2027, cash should grow beyond initial $500K
      assertGreaterThan(res.records[0].cashYE, 500000, 'Surplus year must increase Year-End Cash');
    });

    test('1.5.2: Deficit Priority 1: Cash is drawn down first', function () {
      const deficitInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, {
        cashStart: 100000,
        invStart: 500000,
        livingExpensesStart: 80000
      });
      const res = FinancialEngine.runSimulation(deficitInputs, 0);
      // Cash should decrease in Year 1 while Investments grow normally at 9%
      assertLessThan(res.records[0].cashYE, 100000, 'Deficit must deplete cash first');
    });

    test('1.5.3: Deficit Priority 2: Taxable Investment drawn only after cash is exhausted', function () {
      const deficitInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, {
        cashStart: 0,
        invStart: 500000,
        livingExpensesStart: 80000
      });
      const res = FinancialEngine.runSimulation(deficitInputs, 0);
      // Cash was $0, so Investment must be drawn
      assertEqual(res.records[0].cashYE, 0, 'Cash remains $0');
      // Inv starts at 500K, grows by 9% to 545K, then covers deficit
      assertLessThan(res.records[0].invYE, 545000, 'Investment must be drawn to cover deficit');
    });

    test('1.5.4: Deficit Priority 3: Accessible Roth drawn only after Cash and Investments are 0', function () {
      const extremeDeficit = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, {
        cashStart: 0,
        invStart: 0,
        rothStart: 120000,
        rothPrincipalStart: 25000,
        livingExpensesStart: 15000
      });
      const res = FinancialEngine.runSimulation(extremeDeficit, 0);
      assertEqual(res.records[0].cashYE, 0, 'Cash is 0');
      assertEqual(res.records[0].invYE, 0, 'Investment is 0');
      // Deficit is drawn from accessible Roth principal ($25K)
      assertLessThan(res.records[0].accessibleRothYE, 25000, 'Accessible Roth principal must be tapped');
    });

    test('1.5.5: Infeasibility detected when deficit exceeds total liquidity', function () {
      const bankruptInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, {
        cashStart: 0,
        invStart: 0,
        rothStart: 0,
        rothPrincipalStart: 0,
        livingExpensesStart: 100000
      });
      const res = FinancialEngine.runSimulation(bankruptInputs, 0);
      assertEqual(res.isFeasible, false, 'Simulation must be marked infeasible if liquid deficit occurs');
      assert(res.minLiquidityBalance <= 0, 'Minimum liquidity balance must be non-positive under deficit');
    });

    test('1.5.6: Cash Interest earned on starting balance taxed as ordinary income', function () {
      const inputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, {
        cashStart: 1000000,
        cashInterestRate: 0.05
      });
      const res = FinancialEngine.runSimulation(inputs, 0);
      assertEqual(res.records[0].cashInterest, 50000, '5% interest on $1M cash is $50,000');
    });

    test('1.5.7: Taxable Brokerage 9% return compounded', function () {
      const inputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, {
        cashStart: 1000000, // Plenty of cash to cover all expenses
        invStart: 100000,
        invReturnRate: 0.09
      });
      const res = FinancialEngine.runSimulation(inputs, 0);
      // Because cash covers living expenses, investment should grow untouched: $100K * 1.09 = $109K
      assertClose(res.records[0].invYE, 109000, 0.01, 'Taxable investment should compound by 9% when untouched');
    });
  });

  // Feature 6: Roth 5-Year Rule & Vintage Queue
  describe('Tier 1.6: Roth 5-Year Rule & Vintage Queue (Feature F09)', function () {
    test('1.6.1: Initial contribution basis ($25,000) is accessible immediately in Year 1', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      assertEqual(res.records[0].accessibleRothYE, 25000, 'Year 1 accessible Roth must start with initial $25,000 principal');
    });

    test('1.6.2: Roth conversions remain locked for 5 years post-conversion', function () {
      const convAmount = 50000;
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, convAmount);
      // Conversions in 2027:
      // In 2027, 2028, 2029, 2030, 2031 (years 1 to 5), only the initial $25K principal is accessible
      for (let y = 0; y < 5; y++) {
        assertEqual(res.records[y].accessibleRothYE, 25000, 'Year ' + res.records[y].year + ' accessible Roth must remain at $25K (conversion locked)');
      }
    });

    test('1.6.3: Roth conversion from Year 1 matures and unlocks in Year 6 (2032)', function () {
      const convAmount = 50000;
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, convAmount);
      // In Year 6 (2032, year - 2027 = 5 >= 5), the 2027 conversion of $50,000 unlocks!
      // Total accessible should now be $25,000 + $50,000 = $75,000
      const rec2032 = res.records.find(function (r) { return r.year === 2032; });
      assert(rec2032, 'Record for 2032 must exist');
      assertEqual(rec2032.accessibleRothYE, 75000, 'In 2032, 2027 conversion matures giving $75,000 accessible Roth principal');
    });

    test('1.6.4: Conversions in subsequent years mature in rolling 5-year intervals', function () {
      const convAmount = 50000;
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, convAmount);
      // In 2033, 2028 conversion matures (+ $50K => $125K)
      const rec2033 = res.records.find(function (r) { return r.year === 2033; });
      assertEqual(rec2033.accessibleRothYE, 125000, 'In 2033, cumulative accessible Roth should be $125,000');
    });

    test('1.6.5: Locked conversions cannot be tapped to cover liquidity deficits', function () {
      // Setup: 0 cash, 0 inv, convert $100K in 2027, large deficit in 2029 ($60K)
      const lockInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, {
        cashStart: 0,
        invStart: 0,
        rothStart: 120000,
        rothPrincipalStart: 25000,
        livingExpensesStart: 50000
      });
      const res = FinancialEngine.runSimulation(lockInputs, 100000);
      // In 2027, $25K principal is depleted by deficit, but 2027 conversion cannot be tapped
      // Result must be marked infeasible because deficit in 2028/2029 cannot be paid
      assertEqual(res.isFeasible, false, 'Deficit exceeding accessible principal must trigger infeasibility despite locked Roth conversions');
    });

    test('1.6.6: Conversions compound tax-free inside Roth at 9%', function () {
      const convInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, {
        pretaxStart: 500000,
        cashStart: 1000000 // plenty of cash
      });
      const res = FinancialEngine.runSimulation(convInputs, 100000);
      // Roth start = $120,000. Add $100,000 conversion => $220,000. Compounded at 9% => $239,800
      assertClose(res.records[0].rothYE, 239800, 1.0, 'Year 1 Roth ending balance must reflect 9% growth on (start + conversion)');
    });
  });

  // Feature 7: SECURE Act Inherited IRA Death Tax
  describe('Tier 1.7: SECURE Act Inherited IRA Death Tax (Feature F10)', function () {
    test('1.7.1: Zero ending Pre-Tax balance yields exactly $0 Death Tax', function () {
      const tax = FinancialEngine.computeDeathTax(0, 2060, 1976, 0.035, 0.0575);
      assertEqual(tax, 0, 'Death Tax on $0 pre-tax balance must be $0');
    });

    test('1.7.2: Pre-tax balance is divided by 2 heirs over 10 years (20 portions)', function () {
      // If pretax is $2,000,000, each heir gets $100,000/yr for 10 years ($2M / 20 = $100,000)
      const tax = FinancialEngine.computeDeathTax(2000000, 2060, 1976, 0.035, 0.0575);
      assertGreaterThan(tax, 0, 'Death tax on $2M must be positive');
      // Heir base income is $150K. Combined is $250K.
      // 20 * marginal tax should be positive and bounded
      assertBetween(tax, 400000, 1500000, 'Death tax on $2M should be between $400K and $1.5M');
    });

    test('1.7.3: Death Tax calculation includes Virginia 5.75% state tax on heir shares', function () {
      // Compare 5.75% state tax vs 0% state tax
      const taxWithState = FinancialEngine.computeDeathTax(2000000, 2060, 1976, 0.035, 0.0575);
      const taxWithoutState = FinancialEngine.computeDeathTax(2000000, 2060, 1976, 0.035, 0.0);
      assertGreaterThan(taxWithState, taxWithoutState, 'State tax must increase death tax');
      // State tax difference on $2M pre-tax should be approximately $2,000,000 * 0.0575 = $115,000
      const stateDiff = taxWithState - taxWithoutState;
      assertClose(stateDiff, 115000, 5000, 'State tax component should approximate 5.75% of pretax balance');
    });

    test('1.7.4: Progressive bracket impact: higher pre-tax balance incurs higher effective death tax rate', function () {
      const taxSmall = FinancialEngine.computeDeathTax(1000000, 2060, 1976, 0.035, 0.0575);
      const taxLarge = FinancialEngine.computeDeathTax(10000000, 2060, 1976, 0.035, 0.0575);
      const rateSmall = taxSmall / 1000000;
      const rateLarge = taxLarge / 10000000;
      assertGreaterThan(rateLarge, rateSmall, 'Higher pre-tax inheritance must push heirs into higher marginal brackets');
    });

    test('1.7.5: Scaling EOL pre-tax balance in simulation directly reflects in deathTax field', function () {
      const res0 = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      const res100k = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 100000);
      // With $100K annual conversions, EOL pretax is substantially lower, so deathTax must be lower
      assertLessThan(res100k.deathTax, res0.deathTax, 'Roth conversions must reduce terminal death tax on heirs');
    });

    test('1.7.6: Total lifetime raw tax equals annual taxes plus death tax', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 50000);
      let annualTaxSum = 0;
      res.records.forEach(function (r) {
        annualTaxSum += r.totalTaxYear;
      });
      assertClose(res.rawTotalTax, annualTaxSum + res.deathTax, 0.01, 'rawTotalTax must equal sum of annual taxes + deathTax');
    });
  });

  // Feature 8: Time Value of Money (TVM) Metrics
  describe('Tier 1.8: Time Value of Money (TVM) Metrics (Feature F11)', function () {
    test('1.8.1: Raw total tax is strictly greater than PV total tax under positive discount rate', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 50000);
      assertGreaterThan(res.rawTotalTax, res.pvTotalTax, 'Nominal raw tax must exceed present value discounted tax');
    });

    test('1.8.2: FV total tax is strictly greater than Raw total tax under positive discount rate', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 50000);
      assertGreaterThan(res.fvTotalTax, res.rawTotalTax, 'Future value compounded tax must exceed raw nominal tax');
    });

    test('1.8.3: Mathematical Invariant: FV = PV * (1 + r)^(eolYear - startYear)', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 50000);
      const numYears = res.records.length; // 34
      const compoundFactor = Math.pow(1 + FinancialEngine.DEFAULT_INPUTS.inflationRate, numYears - 1);
      const expectedFV = res.pvTotalTax * compoundFactor;
      // Should match within floating point precision (0.01%)
      const relDiff = Math.abs(res.fvTotalTax - expectedFV) / res.fvTotalTax;
      assertLessThan(relDiff, 0.0001, 'FV must equal PV compounded over 33 years');
    });

    test('1.8.4: With 0% discount rate, Raw Tax == PV Tax == FV Tax', function () {
      const zeroRateInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, {
        inflationRate: 0.0
      });
      const res = FinancialEngine.runSimulation(zeroRateInputs, 50000);
      assertClose(res.rawTotalTax, res.pvTotalTax, 0.01, 'At 0% rate, Raw and PV tax must be identical');
      assertClose(res.rawTotalTax, res.fvTotalTax, 0.01, 'At 0% rate, Raw and FV tax must be identical');
    });

    test('1.8.5: Death tax PV discounting applies factor (1+r)^33', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      const deathTax = res.deathTax;
      const deathTaxPV = deathTax / Math.pow(1 + 0.035, 33);
      assertGreaterThan(res.pvTotalTax, deathTaxPV, 'Total PV tax must include discounted death tax');
    });

    test('1.8.6: Annual tax in Year 1 has PV discount factor of exactly 1.0', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      const yr1Tax = res.records[0].totalTaxYear;
      // In Year 1 (t=0), PV(Tax_1) = Tax_1 / 1.0^0 = Tax_1
      assertGreaterThan(res.pvTotalTax, yr1Tax, 'Total PV tax must be greater than Year 1 tax');
    });
  });

  // Feature 9: Optimization Solver Engine
  describe('Tier 1.9: Optimization Solver Engine (Features F15, F16)', function () {
    test('1.9.1: Evaluates exactly 101 candidate points ($0 to $500K in $5K steps)', function () {
      const opt = FinancialEngine.findOptimalConversion(FinancialEngine.DEFAULT_INPUTS, 'raw');
      assertEqual(opt.candidatesEvaluated, 101, 'Must evaluate exactly 101 candidates');
      assertEqual(opt.candidates.length, 101, 'Candidates array length must be 101');
      assertEqual(opt.candidates[0].conversion, 0, 'First candidate must be $0');
      assertEqual(opt.candidates[100].conversion, 500000, 'Last candidate must be $500,000');
    });

    test('1.9.2: Returns valid optimal conversion amount (multiple of $5,000)', function () {
      const opt = FinancialEngine.findOptimalConversion(FinancialEngine.DEFAULT_INPUTS, 'raw');
      assertBetween(opt.bestAnnualConversion, 0, 500000, 'Optimal conversion must be within [0, 500000]');
      assertEqual(opt.bestAnnualConversion % 5000, 0, 'Optimal conversion must be an integer multiple of $5,000');
    });

    test('1.9.3: Winning candidate must satisfy the liquidity feasibility constraint', function () {
      const opt = FinancialEngine.findOptimalConversion(FinancialEngine.DEFAULT_INPUTS, 'raw');
      assertEqual(opt.bestResult.isFeasible, true, 'Best candidate must be strictly feasible');
      assertGreaterThan(opt.feasibleCount, 0, 'There must be at least one feasible candidate for default inputs');
    });

    test('1.9.4: Objective "Minimize Raw Total Tax" minimizes rawTotalTax metric', function () {
      const opt = FinancialEngine.findOptimalConversion(FinancialEngine.DEFAULT_INPUTS, 'raw');
      assertEqual(opt.objective, 'raw', 'Objective must be set to "raw"');
      assertClose(opt.bestMetricValue, opt.bestResult.rawTotalTax, 0.01, 'bestMetricValue must match rawTotalTax of winning trajectory');
      // Assert that no other feasible candidate has lower rawTax
      opt.candidates.forEach(function (c) {
        if (c.isFeasible) {
          assert(c.rawTax >= opt.bestMetricValue - 0.01, 'No feasible candidate can beat optimal raw tax');
        }
      });
    });

    test('1.9.5: Objective "Minimize TVM-Adjusted Tax" minimizes pvTotalTax metric', function () {
      const opt = FinancialEngine.findOptimalConversion(FinancialEngine.DEFAULT_INPUTS, 'tvm');
      assertEqual(opt.objective, 'tvm', 'Objective must be set to "tvm"');
      assertClose(opt.bestMetricValue, opt.bestResult.pvTotalTax, 0.01, 'bestMetricValue must match pvTotalTax of winning trajectory');
      // Assert that no other feasible candidate has lower pvTax
      opt.candidates.forEach(function (c) {
        if (c.isFeasible) {
          assert(c.pvTax >= opt.bestMetricValue - 0.01, 'No feasible candidate can beat optimal TVM tax');
        }
      });
    });

    test('1.9.6: High-performance execution completes 101 sweeps in under 50ms', function () {
      const t0 = performanceNow();
      FinancialEngine.findOptimalConversion(FinancialEngine.DEFAULT_INPUTS, 'raw');
      const t1 = performanceNow();
      const elapsedMs = t1 - t0;
      log('    (Benchmark: 101-point sweep executed in ' + elapsedMs.toFixed(2) + ' ms)');
      assertLessThan(elapsedMs, 50, 'Optimization sweep must complete in under 50ms (budget < 20ms in V8)');
    });
  });

  // ==========================================================================
  // TIER 2: BOUNDARY & CORNER CASES (>=5 tests per boundary)
  // ==========================================================================

  describe('Tier 2.1: Zero Balances & Extreme Deficits', function () {
    test('2.1.1: Cash = 0, Inv = 0 handles immediate reliance on accessible Roth ($25K)', function () {
      const zeroLiquidInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, {
        cashStart: 0,
        invStart: 0,
        livingExpensesStart: 10000
      });
      const res = FinancialEngine.runSimulation(zeroLiquidInputs, 0);
      assert(res.records[0].accessibleRothYE < 25000, 'Accessible Roth must be tapped');
      assert(res.records[0].rothYE < 120000 * 1.09, 'Roth balance must decrease by draw');
    });

    test('2.1.2: All Zero Assets (Cash=0, Inv=0, Pretax=0, Roth=0) marks infeasible without NaN', function () {
      const allZero = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, {
        cashStart: 0,
        invStart: 0,
        pretaxStart: 0,
        rothStart: 0,
        rothPrincipalStart: 0
      });
      const res = FinancialEngine.runSimulation(allZero, 0);
      assertEqual(res.isFeasible, false, 'Must be marked infeasible');
      assert(!isNaN(res.rawTotalTax), 'rawTotalTax must not be NaN');
      assert(!isNaN(res.pvTotalTax), 'pvTotalTax must not be NaN');
      assertEqual(res.deathTax, 0, 'Death tax on zero pretax must be 0');
    });

    test('2.1.3: Zero Pre-Tax Start yields 0 conversions and 0 Death Tax', function () {
      const zeroPretax = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { pretaxStart: 0 });
      const res = FinancialEngine.runSimulation(zeroPretax, 100000);
      assertEqual(res.records[0].rothConversion, 0, 'Conversion must clamp to 0 when pretax balance is 0');
      assertEqual(res.deathTax, 0, 'Death tax must be 0');
      assertEqual(res.eolPretax, 0, 'EOL pretax must be 0');
    });

    test('2.1.4: Pre-Tax Balance depletion: conversion capped at available balance', function () {
      // Pretax has only $30,000, target conversion is $50,000
      const smallPretax = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { pretaxStart: 30000 });
      const res = FinancialEngine.runSimulation(smallPretax, 50000);
      assertEqual(res.records[0].rothConversion, 30000, 'Conversion must be capped at $30,000');
      assertEqual(res.records[0].pretaxYE, 0, 'Pretax ending balance must be 0');
    });

    test('2.1.5: Zero Earned Income pre-retirement gracefully handled', function () {
      const noSalary = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, {
        retireYear: 2030,
        earnedIncome: 0
      });
      const res = FinancialEngine.runSimulation(noSalary, 0);
      assertEqual(res.records[0].earnedIncome, 0, 'Earned income is 0');
    });
  });

  describe('Tier 2.2: Zero Inflation Boundary (0.0%)', function () {
    test('2.2.1: Living expenses remain static across all 34 years at 0% inflation', function () {
      const flatInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { inflationRate: 0.0 });
      const res = FinancialEngine.runSimulation(flatInputs, 0);
      for (let i = 0; i < res.records.length; i++) {
        assertEqual(res.records[i].livingExpenses, 60000, 'Living expense in year ' + res.records[i].year + ' must be $60,000');
      }
    });

    test('2.2.2: Healthcare base rate remains static pre-65 at 0% inflation', function () {
      const flatInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { inflationRate: 0.0 });
      const res = FinancialEngine.runSimulation(flatInputs, 0);
      for (let i = 0; i < res.records.length; i++) {
        if (res.records[i].age < 65) {
          assertEqual(res.records[i].healthExpenses, 5000, 'Subsidized health cost must remain $5,000');
        }
      }
    });

    test('2.2.3: Federal Tax Brackets identical in Year 1 and Year 34 at 0% inflation', function () {
      const taxYr1 = FinancialEngine.computeFederalTax(150000, 1.0, 'MFJ');
      const taxYr34 = FinancialEngine.computeFederalTax(150000, Math.pow(1.0, 33), 'MFJ');
      assertEqual(taxYr1, taxYr34, 'Taxes on same income must be identical across years under 0% inflation');
    });

    test('2.2.4: Social Security benefit remains flat at $60,000 post-62 at 0% inflation', function () {
      const flatInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { inflationRate: 0.0 });
      const res = FinancialEngine.runSimulation(flatInputs, 0);
      const rec62 = res.records.find(function (r) { return r.age === 62; });
      const rec80 = res.records.find(function (r) { return r.age === 80; });
      assertEqual(rec62.ssBenefit, 60000, 'SS at 62 must be $60,000');
      assertEqual(rec80.ssBenefit, 60000, 'SS at 80 must be $60,000');
    });

    test('2.2.5: PV Tax and FV Tax equal Raw Tax under 0% discount rate', function () {
      const flatInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { inflationRate: 0.0 });
      const res = FinancialEngine.runSimulation(flatInputs, 50000);
      assertClose(res.rawTotalTax, res.pvTotalTax, 0.01, 'Raw and PV tax must be equal');
      assertClose(res.rawTotalTax, res.fvTotalTax, 0.01, 'Raw and FV tax must be equal');
    });
  });

  describe('Tier 2.3: Extreme / High Inflation Stress (15.0%)', function () {
    test('2.3.1: Handles 15% inflation without numeric overflow or NaN', function () {
      const highInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { inflationRate: 0.15 });
      const res = FinancialEngine.runSimulation(highInputs, 0);
      assert(!isNaN(res.rawTotalTax), 'rawTotalTax must not be NaN');
      assert(!isNaN(res.pvTotalTax), 'pvTotalTax must not be NaN');
      assert(isFinite(res.rawTotalTax), 'rawTotalTax must be finite');
    });

    test('2.3.2: Living expenses in Year 34 expand by 1.15^33', function () {
      const highInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { inflationRate: 0.15 });
      const res = FinancialEngine.runSimulation(highInputs, 0);
      const expectedEnd = 60000 * Math.pow(1.15, 33);
      assertClose(res.records[33].livingExpenses, expectedEnd, 100, 'Living expenses in Year 34 must match 15% inflation formula');
    });

    test('2.3.3: College expenses remain completely uninflated at 15% inflation', function () {
      const highInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { inflationRate: 0.15 });
      const res = FinancialEngine.runSimulation(highInputs, 0);
      const rec2029 = res.records.find(function (r) { return r.year === 2029; });
      assertEqual(rec2029.collegeExpenses, 12500, 'College expense must remain $12,500');
    });

    test('2.3.4: Healthcare drops to $0 at age 65 even under 15% inflation', function () {
      const highInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { inflationRate: 0.15 });
      const res = FinancialEngine.runSimulation(highInputs, 0);
      const rec65 = res.records.find(function (r) { return r.age === 65; });
      assertEqual(rec65.healthExpenses, 0, 'Healthcare at age 65 must drop to $0 regardless of inflation rate');
    });

    test('2.3.5: Mathematical invariant FV = PV * (1+0.15)^33 holds under high inflation', function () {
      const highInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { inflationRate: 0.15 });
      const res = FinancialEngine.runSimulation(highInputs, 50000);
      const factor = Math.pow(1.15, 33);
      const expectedFV = res.pvTotalTax * factor;
      const relDiff = Math.abs(res.fvTotalTax - expectedFV) / res.fvTotalTax;
      assertLessThan(relDiff, 0.0001, 'FV/PV invariant must hold under high inflation');
    });
  });

  describe('Tier 2.4: Late Retirement & Pre-Retirement Income Gate', function () {
    test('2.4.1: Earned Income ($275K) active for all years y < retireYear (e.g. 2035)', function () {
      const lateRetireInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { retireYear: 2035 });
      const res = FinancialEngine.runSimulation(lateRetireInputs, 0);
      for (let i = 0; i < res.records.length; i++) {
        if (res.records[i].year < 2035) {
          assertEqual(res.records[i].earnedIncome, 275000, 'Earned income in year ' + res.records[i].year + ' must be $275,000');
          assertEqual(res.records[i].isRetired, false, 'Client must not be retired prior to 2035');
        } else {
          assertEqual(res.records[i].earnedIncome, 0, 'Earned income in year ' + res.records[i].year + ' must be $0');
          assertEqual(res.records[i].isRetired, true, 'Client must be retired in 2035+');
        }
      }
    });

    test('2.4.2: Roth conversions restricted to post-retirement years (2035+)', function () {
      const lateRetireInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { retireYear: 2035 });
      const res = FinancialEngine.runSimulation(lateRetireInputs, 100000);
      // For years 2027 to 2034, conversion must be 0
      for (let i = 0; i < res.records.length; i++) {
        if (res.records[i].year < 2035) {
          assertEqual(res.records[i].rothConversion, 0, 'No conversions before retirement year');
        } else if (res.records[i].age <= 75) {
          assertEqual(res.records[i].rothConversion, 100000, 'Conversions active post-retirement up to age 75');
        }
      }
    });

    test('2.4.3: Retirement year after age 75 results in 0 lifetime conversions', function () {
      // Birth 1976 => age 76 is year 2052. Set retireYear = 2053
      const superLateInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { retireYear: 2053 });
      const res = FinancialEngine.runSimulation(superLateInputs, 100000);
      res.records.forEach(function (r) {
        assertEqual(r.rothConversion, 0, 'No conversions should occur if retired after age 75');
      });
    });

    test('2.4.4: High earned income covers living expenses and builds cash reserves', function () {
      const lateRetireInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { retireYear: 2035 });
      const res = FinancialEngine.runSimulation(lateRetireInputs, 0);
      assertGreaterThan(res.records[0].cashYE, 500000, 'Year 1 cash must grow due to earned income surplus');
    });

    test('2.4.5: Immediate retirement (retireYear = 2027) has 0 earned income in Year 1', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      assertEqual(res.records[0].earnedIncome, 0, 'Year 1 earned income must be 0 with default 2027 retirement');
      assertEqual(res.records[0].isRetired, true, 'Client is retired in Year 1');
    });
  });

  describe('Tier 2.5: High Net Worth & Massive Pre-tax Balance ($50M)', function () {
    test('2.5.1: High Pre-Tax ($50M) triggers top 37% federal tax bracket consistently', function () {
      const hnwInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { pretaxStart: 50000000 });
      const res = FinancialEngine.runSimulation(hnwInputs, 500000);
      // $500K conversion puts taxable income well into top bracket
      assertGreaterThan(res.records[0].fedTax, 100000, 'Federal tax on $500K conversion must be substantial');
    });

    test('2.5.2: Death Tax scales to tens of millions without numerical overflow', function () {
      const hnwInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { pretaxStart: 50000000 });
      const res = FinancialEngine.runSimulation(hnwInputs, 0);
      assertGreaterThan(res.deathTax, 10000000, 'Death tax on $50M pre-tax compounding at 9% must exceed $10M');
      assert(isFinite(res.deathTax), 'Death tax must be finite');
    });

    test('2.5.3: Optimizer evaluates high net worth portfolio successfully', function () {
      const hnwInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { pretaxStart: 20000000 });
      const opt = FinancialEngine.findOptimalConversion(hnwInputs, 'raw');
      assertEqual(opt.candidatesEvaluated, 101, 'Optimizer must evaluate all 101 candidates');
      assertEqual(opt.bestResult.isFeasible, true, 'Best candidate must be feasible');
    });

    test('2.5.4: Substantial cash interest ($10M cash @ 5% = $500K/yr) handles properly', function () {
      const bigCashInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { cashStart: 10000000 });
      const res = FinancialEngine.runSimulation(bigCashInputs, 0);
      assertEqual(res.records[0].cashInterest, 500000, 'Cash interest should be $500,000');
      assertGreaterThan(res.records[0].totalTaxYear, 100000, 'Interest must be taxed');
    });

    test('2.5.5: Large asset returns generate surplus cash flow and maintain solvency', function () {
      const hnwInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, {
        cashStart: 2000000,
        invStart: 5000000
      });
      const res = FinancialEngine.runSimulation(hnwInputs, 100000);
      assertEqual(res.isFeasible, true, 'Large portfolio must remain fully feasible');
      assertGreaterThan(res.eolCash, 2000000, 'Cash should grow over time with strong yields');
    });
  });

  describe('Tier 2.6: Healthcare Age 65 Transition Boundaries', function () {
    test('2.6.1: Birth year 1976: turns 65 in 2041 (2040 has cost, 2041 is $0)', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      const rec2040 = res.records.find(function (r) { return r.year === 2040; });
      const rec2041 = res.records.find(function (r) { return r.year === 2041; });
      assertEqual(rec2040.age, 64, '2040 age is 64');
      assertEqual(rec2041.age, 65, '2041 age is 65');
      assertGreaterThan(rec2040.healthExpenses, 0, '2040 healthcare must be > 0');
      assertEqual(rec2041.healthExpenses, 0, '2041 healthcare must be $0');
    });

    test('2.6.2: Birth year 1962: turns 65 in 2027 (Year 1) => healthcare is $0 in ALL years', function () {
      const oldInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { birthYear: 1962 });
      const res = FinancialEngine.runSimulation(oldInputs, 0);
      res.records.forEach(function (r) {
        assertEqual(r.healthExpenses, 0, 'Healthcare must be $0 for all years when starting at age 65');
      });
    });

    test('2.6.3: Birth year 1990: turns 65 in 2055 => healthcare active for 28 years', function () {
      const youngInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { birthYear: 1990 });
      const res = FinancialEngine.runSimulation(youngInputs, 0);
      const rec2054 = res.records.find(function (r) { return r.year === 2054; });
      const rec2055 = res.records.find(function (r) { return r.year === 2055; });
      assertEqual(rec2054.age, 64, '2054 age is 64');
      assertEqual(rec2055.age, 65, '2055 age is 65');
      assertGreaterThan(rec2054.healthExpenses, 0, 'Healthcare in 2054 must be > 0');
      assertEqual(rec2055.healthExpenses, 0, 'Healthcare in 2055 must be $0');
    });

    test('2.6.4: Zero subsidized healthcare input ($0) yields $0 even pre-65', function () {
      const zeroHealthInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { healthSubsidized: 0 });
      const res = FinancialEngine.runSimulation(zeroHealthInputs, 0);
      assertEqual(res.records[0].healthExpenses, 0, 'Healthcare must be $0 if input cost is $0');
    });

    test('2.6.5: Age 65 transition functions identically under all Roth conversion levels', function () {
      const res0 = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      const res200k = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 200000);
      const rec65_0 = res0.records.find(function (r) { return r.age === 65; });
      const rec65_200k = res200k.records.find(function (r) { return r.age === 65; });
      assertEqual(rec65_0.healthExpenses, 0, 'At 0 conversion, age 65 health is 0');
      assertEqual(rec65_200k.healthExpenses, 0, 'At 200K conversion, age 65 health is 0');
    });
  });

  describe('Tier 2.7: Pre-Tax Exhaustion & Boundary Conversion Clamping', function () {
    test('2.7.1: Conversion cannot exceed pre-tax balance when balance is low', function () {
      const smallInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { pretaxStart: 10000 });
      const res = FinancialEngine.runSimulation(smallInputs, 100000);
      assertEqual(res.records[0].rothConversion, 10000, 'Conversion must clamp to starting $10,000');
    });

    test('2.7.2: Pre-tax balance is non-negative across all simulated years', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 500000);
      res.records.forEach(function (r) {
        assert(r.pretaxYE >= 0, 'Pre-tax balance in year ' + r.year + ' must be non-negative (got ' + r.pretaxYE + ')');
      });
    });

    test('2.7.3: Once pre-tax reaches 0, all future conversions are 0', function () {
      const smallInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { pretaxStart: 50000 });
      const res = FinancialEngine.runSimulation(smallInputs, 50000);
      assertEqual(res.records[0].rothConversion, 50000, 'Year 1 converts all $50,000');
      assertEqual(res.records[0].pretaxYE, 0, 'Year 1 pre-tax ends at 0');
      assertEqual(res.records[1].rothConversion, 0, 'Year 2 conversion must be 0');
      assertEqual(res.records[2].rothConversion, 0, 'Year 3 conversion must be 0');
    });

    test('2.7.4: EOL pre-tax is 0 when all pre-tax converted, resulting in $0 Death Tax', function () {
      const smallInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { pretaxStart: 50000 });
      const res = FinancialEngine.runSimulation(smallInputs, 50000);
      assertEqual(res.eolPretax, 0, 'EOL pretax is 0');
      assertEqual(res.deathTax, 0, 'Death tax is 0');
    });

    test('2.7.5: Conversion slider values outside [0, 500000] clamp defensively', function () {
      // Negative conversion
      const resNeg = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, -50000);
      assertEqual(resNeg.records[0].rothConversion, 0, 'Negative conversion must clamp to 0');
    });
  });

  // ==========================================================================
  // TIER 3: CROSS-FEATURE COMBINATIONS & PAIRWISE INTERACTIONS
  // ==========================================================================

  describe('Tier 3.1: College Crunch + Aggressive Roth Conversion', function () {
    test('3.1.1: Simultaneous college tuition and conversion taxes drawn in correct priority', function () {
      // In 2029-2033, college is active ($12.5K-$25K) while converting $150K/yr
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 150000);
      const rec2029 = res.records.find(function (r) { return r.year === 2029; });
      assertGreaterThan(rec2029.collegeExpenses, 0, 'College expense must be active in 2029');
      assertGreaterThan(rec2029.rothConversion, 0, 'Roth conversion must be active in 2029');
      assertGreaterThan(rec2029.totalTaxYear, 20000, 'Taxes on $150K conversion must be paid');
    });

    test('3.1.2: Cash buffer absorbs early college crunch without breaking liquidity', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 100000);
      assertEqual(res.isFeasible, true, 'Default portfolio must withstand college + $100K conversions');
    });

    test('3.1.3: Heavy college ($200K) + high conversion ($300K) depletes cash and draws investments', function () {
      const crunchInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, {
        collegeTotal: 200000,
        cashStart: 200000
      });
      const res = FinancialEngine.runSimulation(crunchInputs, 300000);
      // In 2030 (Year 4), cash should be exhausted and investment drawn
      const rec2030 = res.records.find(function (r) { return r.year === 2030; });
      assertEqual(rec2030.cashYE, 0, 'Cash should be depleted to 0');
    });

    test('3.1.4: Accessible Roth unlocked in 2032 provides emergency liquidity for final college year (2033)', function () {
      const crunchInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, {
        collegeTotal: 150000,
        cashStart: 350000,
        invStart: 150000
      });
      const res = FinancialEngine.runSimulation(crunchInputs, 100000);
      // In 2032, 2027 conversion matures giving access to Roth principal
      const rec2032 = res.records.find(function (r) { return r.year === 2032; });
      assertGreaterThan(rec2032.accessibleRothYE, 0, 'Accessible Roth must be positive in 2032');
    });

    test('3.1.5: Total lifetime tax reflects both conversion taxes and reduced EOL death tax', function () {
      const res0 = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      const res150k = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 150000);
      assertLessThan(res150k.deathTax, res0.deathTax, 'Aggressive conversions must substantially lower death tax');
    });
  });

  describe('Tier 3.2: Healthcare Subsidy Cliff Transitions under Conversion Spikes', function () {
    test('3.2.1: $0 conversion keeps MAGI below cliff ($5,000 subsidized)', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      // In 2027, cash interest is $25K, SS is 0, earned income is 0 => MAGI = $25K <= $90K
      assertClose(res.records[0].healthExpenses, 5000, 0.01, 'Healthcare must be $5,000 subsidized with $0 conversion');
    });

    test('3.2.2: $100K conversion pushes MAGI above cliff ($25,000 unsubsidized)', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 100000);
      // In 2027, cash interest $25K + $100K conversion = $125K > $90K cliff
      assertClose(res.records[0].healthExpenses, 25000, 0.01, 'Healthcare must jump to $25,000 unsubsidized with $100K conversion');
    });

    test('3.2.3: Healthcare cliff jump increases annual cash deficit by exactly ($25K - $5K) = $20K', function () {
      const resSub = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      const resCliff = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 70000);
      // Interest ($25K) + $70K = $95K > $90K cliff
      const diff = resCliff.records[0].healthExpenses - resSub.records[0].healthExpenses;
      assertClose(diff, 20000, 0.01, 'Healthcare expense difference must be $20,000');
    });

    test('3.2.4: Subsidy cliff effect terminates automatically at age 65 Medicare drop', function () {
      const res0 = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      const res100k = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 100000);
      const rec65_0 = res0.records.find(function (r) { return r.age === 65; });
      const rec65_100k = res100k.records.find(function (r) { return r.age === 65; });
      assertEqual(rec65_0.healthExpenses, 0, 'Post-65 healthcare is $0 at $0 conversion');
      assertEqual(rec65_100k.healthExpenses, 0, 'Post-65 healthcare is $0 at $100K conversion');
    });

    test('3.2.5: Cliff step function correctly accounts for compounding inflation threshold', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 75000);
      // In 2027, $25K interest + $75K conv = $100K > $90K cliff => unsubsidized ($25K)
      assertClose(res.records[0].healthExpenses, 25000, 0.01, 'Year 1 is unsubsidized');
    });
  });

  describe('Tier 3.3: Social Security Onset + Roth 5-Year Vintage Maturation', function () {
    test('3.3.1: In 2038 (Age 62), Social Security begins and 2027–2033 conversions have matured', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 50000);
      const rec2038 = res.records.find(function (r) { return r.year === 2038; });
      assert(rec2038, 'Record for 2038 must exist');
      assertEqual(rec2038.age, 62, 'Age in 2038 is 62');
      assertGreaterThan(rec2038.ssBenefit, 0, 'SS benefit must be active');
      // Accessible Roth includes original $25K + (2038 - 2027 >= 5) conversions
      assertGreaterThan(rec2038.accessibleRothYE, 200000, 'Accessible Roth principal must exceed $200K');
    });

    test('3.3.2: Social Security benefit increases taxable income via IRC § 86', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 100000);
      const rec2037 = res.records.find(function (r) { return r.year === 2037; });
      const rec2038 = res.records.find(function (r) { return r.year === 2038; });
      assertGreaterThan(rec2038.taxableIncome, rec2037.taxableIncome, 'Taxable income in 2038 must increase with SS onset');
    });

    test('3.3.3: Social Security cash inflow bolsters liquid cash flow balance', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      const rec2038 = res.records.find(function (r) { return r.year === 2038; });
      assertGreaterThan(rec2038.ssBenefit, 80000, 'Inflated SS benefit at 62 exceeds $80,000');
    });

    test('3.3.4: SS benefit start age user toggle (e.g. Age 67) delays benefit correctly', function () {
      const ss67Inputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, { ssStartAge: 67 });
      const res = FinancialEngine.runSimulation(ss67Inputs, 0);
      const rec62 = res.records.find(function (r) { return r.age === 62; });
      const rec67 = res.records.find(function (r) { return r.age === 67; });
      assertEqual(rec62.ssBenefit, 0, 'SS at 62 must be 0 when start age is 67');
      assertGreaterThan(rec67.ssBenefit, 0, 'SS at 67 must be active');
    });

    test('3.3.5: Conversion income and SS benefit combined in MAGI for provisional income', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 100000);
      const rec2038 = res.records.find(function (r) { return r.year === 2038; });
      // With $100K conversion, taxable SS should be capped at 85%
      const expectedTaxableSS = 0.85 * rec2038.ssBenefit;
      assertClose(FinancialEngine.computeTaxableSS(rec2038.ssBenefit, 100000), expectedTaxableSS, 0.01, 'Taxable SS should reach 85% cap');
    });
  });

  describe('Tier 3.4: Age 75 Conversion Cutoff + Pre-Tax Compounding', function () {
    test('3.4.1: Conversions occur in 2051 (Age 75) and cease in 2052 (Age 76)', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 100000);
      const rec75 = res.records.find(function (r) { return r.age === 75; });
      const rec76 = res.records.find(function (r) { return r.age === 76; });
      assert(rec75 && rec76, 'Records for age 75 and 76 must exist');
      assertEqual(rec75.rothConversion, 100000, 'Conversion at age 75 must be $100,000');
      assertEqual(rec76.rothConversion, 0, 'Conversion at age 76 must be strictly $0');
    });

    test('3.4.2: Pre-tax balance grows unhindered at 9% from Age 76 to End of Life (2060)', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 100000);
      const rec76 = res.records.find(function (r) { return r.age === 76; });
      const rec77 = res.records.find(function (r) { return r.age === 77; });
      // With 0 conversion and untouched, pretax must grow by 9%
      const ratio = rec77.pretaxYE / rec76.pretaxYE;
      assertClose(ratio, 1.09, 0.001, 'Pretax balance must compound by 9% post-age 75');
    });

    test('3.4.3: Accessible Roth pool continues to hold matured vintages after Age 75', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 100000);
      const rec75 = res.records.find(function (r) { return r.age === 75; });
      const rec80 = res.records.find(function (r) { return r.age === 80; });
      assertGreaterThan(rec80.accessibleRothYE, rec75.accessibleRothYE, 'Accessible Roth must continue to mature remaining vintages');
    });

    test('3.4.4: Taxes paid drop substantially after Age 75 as conversions cease', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 100000);
      const rec75 = res.records.find(function (r) { return r.age === 75; });
      const rec76 = res.records.find(function (r) { return r.age === 76; });
      assertLessThan(rec76.totalTaxYear, rec75.totalTaxYear, 'Tax in year 76 should drop compared to conversion year 75');
    });

    test('3.4.5: Terminal Death Tax reflects compound growth from Age 75 to Age 84', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 100000);
      assertGreaterThan(res.deathTax, 0, 'Death tax must be positive');
      assertLessThan(res.deathTax, 35000000, 'Death tax should be significantly lower than $0 conversion case');
    });
  });

  describe('Tier 3.5: Estate Planning Trade-off: $0 vs Flat Conversion Comparison', function () {
    test('3.5.1: $0 conversion results in massive EOL pre-tax balance ($70M+)', function () {
      const res0 = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      assertGreaterThan(res0.eolPretax, 70000000, 'EOL pretax at $0 conversion must exceed $70M');
    });

    test('3.5.2: $0 conversion results in massive Death Tax ($30M+) on heirs', function () {
      const res0 = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      assertGreaterThan(res0.deathTax, 30000000, 'Death tax at $0 conversion must exceed $30M');
    });

    test('3.5.3: Moderate conversion ($100K) builds tax-free Roth portfolio ($18M+)', function () {
      const res100k = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 100000);
      assertGreaterThan(res100k.eolRoth, 18000000, 'EOL Roth balance at $100K conversion must exceed $18M');
    });

    test('3.5.4: Lifetime total tax tradeoff: Raw tax exhibits dramatic reduction under conversion', function () {
      const res0 = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      const res80k = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 80000);
      const res400k = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 400000);
      // Higher conversions compound tax-free and slash the $37M death tax
      assertLessThan(res80k.rawTotalTax, res0.rawTotalTax, '$80K conversion must yield lower total tax than $0 conversion');
      assertLessThan(res400k.rawTotalTax, res80k.rawTotalTax, '$400K conversion must yield lower total tax than $80K conversion');
    });

    test('3.5.5: PV tax objective favors slightly lower conversions than Raw tax objective', function () {
      const optRaw = FinancialEngine.findOptimalConversion(FinancialEngine.DEFAULT_INPUTS, 'raw');
      const optTvm = FinancialEngine.findOptimalConversion(FinancialEngine.DEFAULT_INPUTS, 'tvm');
      // TVM discounts future death taxes, reducing the urgency to convert upfront at higher present tax cost
      assert(optTvm.bestAnnualConversion <= optRaw.bestAnnualConversion + 10000, 'TVM optimal conversion should not substantially exceed Raw optimal conversion');
    });
  });

  // ==========================================================================
  // TIER 4: REAL-WORLD APPLICATION SCENARIOS (From TEST_INFRA.md)
  // ==========================================================================

  describe('Tier 4.1: Scenario 1 — Baseline User Trajectory (Default Inputs)', function () {
    test('4.1.1: Full 34-year simulation span from 2027 (Age 51) to 2060 (Age 84)', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 75000);
      assertEqual(res.records.length, 34, 'Baseline must span exactly 34 years');
      assertEqual(res.records[0].year, 2027, 'Start year must be 2027');
      assertEqual(res.records[0].age, 51, 'Start age must be 51');
      assertEqual(res.records[33].year, 2060, 'End year must be 2060');
      assertEqual(res.records[33].age, 84, 'End age must be 84');
    });

    test('4.1.2: College active 2029–2033; Medicare drops at 2041 (Age 65); SS kicks in 2038 (Age 62)', function () {
      const res = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 75000);
      // College
      assertEqual(res.records.find(r => r.year === 2029).collegeExpenses, 12500);
      assertEqual(res.records.find(r => r.year === 2033).collegeExpenses, 12500);
      assertEqual(res.records.find(r => r.year === 2034).collegeExpenses, 0);
      // Medicare
      assertEqual(res.records.find(r => r.year === 2041).healthExpenses, 0);
      // Social Security
      assertEqual(res.records.find(r => r.year === 2037).ssBenefit, 0);
      assertGreaterThan(res.records.find(r => r.year === 2038).ssBenefit, 0);
    });

    test('4.1.3: Optimizer finds optimal flat conversion that dramatically minimizes total tax', function () {
      const opt = FinancialEngine.findOptimalConversion(FinancialEngine.DEFAULT_INPUTS, 'raw');
      assertBetween(opt.bestAnnualConversion, 50000, 450000, 'Baseline optimal conversion should be between $50K and $450K/yr');
      assertLessThan(opt.bestMetricValue, 10000000, 'Optimal tax must be under $10M (compared to $37.9M at $0 conversion)');
    });

    test('4.1.4: Baseline trajectory maintains positive liquidity across all 34 years', function () {
      const opt = FinancialEngine.findOptimalConversion(FinancialEngine.DEFAULT_INPUTS, 'raw');
      assertEqual(opt.bestResult.isFeasible, true, 'Optimal baseline trajectory must be feasible');
      assertGreaterThan(opt.bestResult.minLiquidityBalance, 0, 'Liquidity balance must remain positive');
    });

    test('4.1.5: EOL Net Worth exceeds initial net worth due to positive asset returns', function () {
      const opt = FinancialEngine.findOptimalConversion(FinancialEngine.DEFAULT_INPUTS, 'raw');
      const startNW = 500000 + 300000 + 5000000 + 120000; // $5.92M
      const eolNW = opt.bestResult.eolCash + opt.bestResult.eolInv + opt.bestResult.eolPretax + opt.bestResult.eolRoth;
      assertGreaterThan(eolNW, startNW, 'EOL Net worth must compound significantly over 34 years');
    });
  });

  describe('Tier 4.2: Scenario 2 — Early Death / Short Horizon at Age 60', function () {
    const earlyDeathInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, {
      eolYear: 2036 // 10 years: 2027 to 2036 (Age 51 to 60)
    });

    test('4.2.1: Exactly 10 annual records generated (2027 to 2036)', function () {
      const res = FinancialEngine.runSimulation(earlyDeathInputs, 50000);
      assertEqual(res.records.length, 10, 'Must contain exactly 10 records');
      assertEqual(res.records[0].year, 2027, 'Start year 2027');
      assertEqual(res.records[9].year, 2036, 'End year 2036');
      assertEqual(res.records[9].age, 60, 'End age 60');
    });

    test('4.2.2: Healthcare is active across all 10 years (client never reaches Medicare age 65)', function () {
      const res = FinancialEngine.runSimulation(earlyDeathInputs, 50000);
      res.records.forEach(function (r) {
        assertGreaterThan(r.healthExpenses, 0, 'Healthcare must be active in year ' + r.year + ' prior to age 65');
      });
    });

    test('4.2.3: Social Security benefit is strictly $0 in all years (client never reaches age 62)', function () {
      const res = FinancialEngine.runSimulation(earlyDeathInputs, 50000);
      res.records.forEach(function (r) {
        assertEqual(r.ssBenefit, 0, 'SS benefit must be $0 prior to age 62');
      });
    });

    test('4.2.4: Full SECURE Act liquidation occurs at age 60 on ending Pre-Tax balance', function () {
      const res = FinancialEngine.runSimulation(earlyDeathInputs, 50000);
      assertGreaterThan(res.deathTax, 0, 'Death tax must be calculated at EOL year 2036');
      assertLessThan(res.eolPretax, 20000000, 'Pretax balance after 10 years should be under $20M');
    });

    test('4.2.5: PV and FV discounting horizon spans 9 years (2036 - 2027)', function () {
      const res = FinancialEngine.runSimulation(earlyDeathInputs, 50000);
      const factor = Math.pow(1 + earlyDeathInputs.inflationRate, 9);
      const expectedFV = res.pvTotalTax * factor;
      const relDiff = Math.abs(res.fvTotalTax - expectedFV) / res.fvTotalTax;
      assertLessThan(relDiff, 0.0001, 'FV = PV * (1+r)^9');
    });
  });

  describe('Tier 4.3: Scenario 3 — Heavy College Cash Crunch ($400K Tuition)', function () {
    const collegeCrunchInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, {
      collegeTotal: 400000,
      collegeStartYear: 2028,
      cashStart: 150000,
      invStart: 100000
    });

    test('4.3.1: College expense vector distributes $50K, $100K, $100K, $100K, $50K', function () {
      const res = FinancialEngine.runSimulation(collegeCrunchInputs, 0);
      assertEqual(res.records.find(r => r.year === 2028).collegeExpenses, 50000); // 12.5%
      assertEqual(res.records.find(r => r.year === 2029).collegeExpenses, 100000); // 25%
      assertEqual(res.records.find(r => r.year === 2030).collegeExpenses, 100000); // 25%
      assertEqual(res.records.find(r => r.year === 2031).collegeExpenses, 100000); // 25%
      assertEqual(res.records.find(r => r.year === 2032).collegeExpenses, 50000); // 12.5%
    });

    test('4.3.2: High cash outflows deplete cash completely by Year 2 (2028)', function () {
      const res = FinancialEngine.runSimulation(collegeCrunchInputs, 0);
      const rec2028 = res.records.find(r => r.year === 2028);
      assertEqual(rec2028.cashYE, 0, 'Cash should be completely exhausted');
    });

    test('4.3.3: Brokerage investments are drawn down in Year 3 (2029)', function () {
      const res = FinancialEngine.runSimulation(collegeCrunchInputs, 0);
      const rec2029 = res.records.find(r => r.year === 2029);
      assertLessThan(rec2029.invYE, 100000, 'Brokerage investment must be drawn down');
    });

    test('4.3.4: Excessive Roth conversion ($300K) violates liquidity and triggers infeasibility', function () {
      const resExcessive = FinancialEngine.runSimulation(collegeCrunchInputs, 300000);
      assertEqual(resExcessive.isFeasible, false, 'Large conversions during college crunch must be marked infeasible');
    });

    test('4.3.5: Optimizer gracefully identifies least-deficit trajectory when cash crunch renders candidates infeasible', function () {
      const opt = FinancialEngine.findOptimalConversion(collegeCrunchInputs, 'raw');
      // Extreme cash crunch has 0 feasible points; optimizer falls back to least-deficit candidate (E12)
      assertEqual(opt.feasibleCount, 0, 'Zero candidates should be strictly feasible under extreme cash crunch');
      assertEqual(opt.bestAnnualConversion, 0, 'Least-deficit fallback chooses $0 conversion to conserve cash');
    });
  });

  describe('Tier 4.4: Scenario 4 — High Income Healthcare Cliff ($2M Cash / $5M Inv)', function () {
    const highIncomeInputs = Object.assign({}, FinancialEngine.DEFAULT_INPUTS, {
      cashStart: 2000000, // 5% = $100K/yr interest
      invStart: 5000000
    });

    test('4.4.1: Starting cash interest ($100K) exceeds $90K cliff even at $0 conversion', function () {
      const res = FinancialEngine.runSimulation(highIncomeInputs, 0);
      assertEqual(res.records[0].cashInterest, 100000, 'Cash interest is $100,000');
    });

    test('4.4.2: Healthcare premium defaults to unsubsidized ($25K inflated) in Year 1', function () {
      const res = FinancialEngine.runSimulation(highIncomeInputs, 0);
      assertClose(res.records[0].healthExpenses, 25000, 0.01, 'Must be unsubsidized rate $25,000');
    });

    test('4.4.3: Unsubsidized healthcare applies while interest exceeds inflated cliff', function () {
      const res = FinancialEngine.runSimulation(highIncomeInputs, 0);
      // In 2027-2029, cash interest ~$100K > cliff ($90K - $96.4K) => unsubsidized
      assertClose(res.records[0].healthExpenses, 25000, 0.01, '2027 healthcare is unsubsidized');
      assertClose(res.records[1].healthExpenses, 25000 * 1.035, 0.01, '2028 healthcare is unsubsidized inflated');
      assertClose(res.records[2].healthExpenses, 25000 * Math.pow(1.035, 2), 0.01, '2029 healthcare is unsubsidized inflated');
      // In 2030, inflated cliff ($99,785) crosses above interest ($99,202) => subsidized ($5,544)
      assertClose(res.records[3].healthExpenses, 5000 * Math.pow(1.035, 3), 0.01, '2030 healthcare transitions to subsidized as cliff inflates');
    });

    test('4.4.4: Healthcare drops to strictly $0 at Age 65 despite high ongoing income', function () {
      const res = FinancialEngine.runSimulation(highIncomeInputs, 0);
      const rec65 = res.records.find(r => r.age === 65);
      assertEqual(rec65.healthExpenses, 0, 'Healthcare at age 65 must drop to $0 regardless of income level');
    });

    test('4.4.5: Massive cash buffer enables high conversion capacity without liquidity risk', function () {
      const opt = FinancialEngine.findOptimalConversion(highIncomeInputs, 'raw');
      assertEqual(opt.bestResult.isFeasible, true, 'High asset scenario must be feasible');
      assertGreaterThan(opt.feasibleCount, 90, 'Nearly all 101 candidates should be feasible');
    });
  });

  describe('Tier 4.5: Scenario 5 — Zero Conversion vs $300K Flat Conversion Lifetime Contrast', function () {
    test('4.5.1: Zero conversion pays low taxes upfront but incurs massive terminal death tax', function () {
      const res0 = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      assertLessThan(res0.records[0].totalTaxYear, 10000, 'Year 1 tax at $0 conversion is low');
      assertGreaterThan(res0.deathTax, 30000000, 'Death tax on unliquidated pre-tax balance exceeds $30M');
    });

    test('4.5.2: $300K conversion pays high taxes upfront but drastically slashes death tax', function () {
      const res300k = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 300000);
      assertGreaterThan(res300k.records[0].totalTaxYear, 70000, 'Year 1 tax on $300K conversion exceeds $70K');
      assertLessThan(res300k.deathTax, 15000000, 'Death tax on pre-tax balance is slashed below $15M');
    });

    test('4.5.3: $300K conversion builds massive tax-free Roth legacy ($40M+)', function () {
      const res300k = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 300000);
      assertGreaterThan(res300k.eolRoth, 40000000, 'EOL Roth balance exceeds $40M');
    });

    test('4.5.4: Lifetime Raw Tax is lower with conversion than without conversion', function () {
      const res0 = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      const resOptimal = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 80000);
      assertLessThan(resOptimal.rawTotalTax, res0.rawTotalTax, 'Lifetime tax with optimal conversion is lower than $0 conversion');
    });

    test('4.5.5: PV discounting reflects the time-preference advantage of deferred taxes', function () {
      const res0 = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 0);
      const res300k = FinancialEngine.runSimulation(FinancialEngine.DEFAULT_INPUTS, 300000);
      // PV of death tax paid 33 years in future is discounted by 1.035^33 (~3.11x)
      assertGreaterThan(res0.pvTotalTax, 0, 'PV tax is positive');
      assertGreaterThan(res300k.pvTotalTax, 0, 'PV tax is positive');
    });
  });

  // ==========================================================================
  // FINAL REPORT & EXIT
  // ==========================================================================
  log('\n' + colorize(Colors.bright + Colors.cyan, '========================================================================'));
  log(colorize(Colors.bright + Colors.cyan, ' TEST SUITE EXECUTION SUMMARY'));
  log(colorize(Colors.bright + Colors.cyan, '========================================================================'));
  log('Total Tests Executed: ' + colorize(Colors.bright, totalTests));
  log('Passed: ' + colorize(Colors.green, passedTests));
  log('Failed: ' + (failedTests > 0 ? colorize(Colors.red, failedTests) : colorize(Colors.green, '0')));

  if (failedTests > 0) {
    log('\n' + colorize(Colors.bright + Colors.red, 'FAILURES DETAIL:'));
    failureReports.forEach(function (f, idx) {
      log('\n' + colorize(Colors.red, (idx + 1) + ') [' + f.suite + '] ' + f.test));
      log('   Error: ' + f.error);
      if (f.stack) {
        log('   Stack: ' + f.stack.split('\n').slice(0, 3).join('\n          '));
      }
    });
    log('\n' + colorize(Colors.bright + Colors.red, 'FAILED: One or more assertions failed. Exiting with code 1.'));
    exitWithCode(1);
  } else {
    log('\n' + colorize(Colors.bright + Colors.green, 'SUCCESS: 100% of tests passed across Tiers 1-4!'));
    exitWithCode(0);
  }

})();
