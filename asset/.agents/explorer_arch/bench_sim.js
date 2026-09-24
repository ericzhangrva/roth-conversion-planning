// Benchmark 100 runs of the full 101-point sweep (10,100 full 34-year simulations = 343,400 year steps)
const TAX_BRACKETS_2026 = [
  { max: 23200, rate: 0.10 },
  { max: 94300, rate: 0.12 },
  { max: 201050, rate: 0.22 },
  { max: 383900, rate: 0.24 },
  { max: 487450, rate: 0.32 },
  { max: 731200, rate: 0.35 },
  { max: Infinity, rate: 0.37 }
];
const STD_DEDUCTION_2026 = 30000;

function computeTax(taxableIncome, inflationFactor) {
  let stdDed = STD_DEDUCTION_2026 * inflationFactor;
  let inc = Math.max(0, taxableIncome - stdDed);
  if (inc <= 0) return 0;
  
  let tax = 0;
  let prevMax = 0;
  for (let i = 0; i < TAX_BRACKETS_2026.length; i++) {
    let b = TAX_BRACKETS_2026[i];
    let bMax = b.max * inflationFactor;
    if (inc > bMax) {
      tax += (bMax - prevMax) * b.rate;
      prevMax = bMax;
    } else {
      tax += (inc - prevMax) * b.rate;
      break;
    }
  }
  return tax;
}

function simulateSweep(params) {
  let bestConv = 0;
  let minTax = Infinity;

  // Precompute inflation factors for each year (2027 to 2060)
  const yearsCount = params.endYear - params.startYear;
  const inflationFactors = new Float64Array(yearsCount + 1);
  for (let y = 0; y <= yearsCount; y++) {
    inflationFactors[y] = Math.pow(1 + params.inflationRate, y);
  }

  for (let conv = 0; conv <= 500000; conv += 5000) {
    let cash = params.initCash;
    let inv = params.initInv;
    let pretax = params.initPretax;
    let roth = params.initRoth;
    let accessibleRoth = params.initRothPrincipal;
    let rothBucket = new Float64Array(6); // 5-year pipeline
    rothBucket[0] = params.initRothPrincipal;
    
    let totalTaxPaid = 0;
    let failed = false;

    for (let yr = params.startYear + 1; yr <= params.endYear; yr++) {
      let idx = yr - params.startYear;
      let age = yr - params.birthYear;
      let inf = inflationFactors[idx];

      let living = params.livingExpenses * inf;
      let health = (age < 65) ? (params.healthSubsidized * inf) : 0;
      
      let college = 0;
      let cYear = yr - params.collegeStartYear;
      if (cYear === 0) college = params.collegeTotal * 0.125;
      else if (cYear >= 1 && cYear <= 3) college = params.collegeTotal * 0.25;
      else if (cYear === 4) college = params.collegeTotal * 0.125;

      let totalExpenses = living + health + college;
      let earnedIncome = (yr < params.retireYear) ? params.earnedIncome : 0;
      let ssIncome = (age >= params.ssStartAge) ? params.ssAmount : 0;

      let actualConv = (yr >= params.retireYear && age <= 75) ? Math.min(pretax, conv) : 0;
      let taxable = earnedIncome + actualConv + (ssIncome * 0.85);
      let fedTax = computeTax(taxable, inf);
      let stateTax = taxable * params.stateTaxRate;
      let yrTax = fedTax + stateTax;
      totalTaxPaid += yrTax;

      pretax -= actualConv;
      roth += actualConv;

      let net = earnedIncome + ssIncome - totalExpenses - yrTax;
      if (net >= 0) {
        cash += net;
      } else {
        let def = -net;
        if (cash >= def) {
          cash -= def;
        } else {
          def -= cash;
          cash = 0;
          if (inv >= def) {
            inv -= def;
          } else {
            def -= inv;
            inv = 0;
            if (accessibleRoth >= def) {
              accessibleRoth -= def;
              roth -= def;
            } else {
              // Check if pretax draw is allowed or liquidity violated
              failed = true;
              break;
            }
          }
        }
      }

      // Growth
      cash *= (1 + params.interestRate);
      inv *= (1 + params.invReturn);
      pretax *= (1 + params.invReturn);
      roth *= (1 + params.invReturn);
    }

    if (!failed && totalTaxPaid < minTax) {
      minTax = totalTaxPaid;
      bestConv = conv;
    }
  }

  return { bestConv, minTax };
}

let params = {
  birthYear: 1976,
  retireYear: 2027,
  startYear: 2026,
  endYear: 2060,
  inflationRate: 0.035,
  interestRate: 0.05,
  invReturn: 0.09,
  livingExpenses: 60000,
  healthSubsidized: 5000,
  healthUnsubsidized: 25000,
  collegeTotal: 100000,
  collegeStartYear: 2029,
  ssStartAge: 62,
  ssAmount: 60000,
  earnedIncome: 275000,
  stateTaxRate: 0.0575,
  initCash: 500000,
  initInv: 300000,
  initPretax: 5000000,
  initRoth: 120000,
  initRothPrincipal: 25000
};

// Warmup
simulateSweep(params);

let startT = Date.now();
const RUNS = 100;
for (let i = 0; i < RUNS; i++) {
  simulateSweep(params);
}
let endT = Date.now();
let totalMs = endT - startT;
print("Total for " + RUNS + " sweeps (10,100 simulations): " + totalMs + "ms");
print("Average per sweep: " + (totalMs / RUNS).toFixed(2) + "ms");
