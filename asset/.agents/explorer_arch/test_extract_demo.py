import re
import subprocess
import json

# Demo: How a test runner can extract JS from planning.html and run it via jsc or node
html_mock = """<!DOCTYPE html>
<html>
<head><title>Test</title></head>
<body>
<div id="end-cash"></div>
<script>
const FinancialEngine = {
  version: "1.0.0",
  computeTaxBracket: function(income, inflation) {
    let b = 94300 * inflation;
    return income > b ? 0.22 : 0.12;
  },
  runOptimization: function() {
    return { bestConv: 150000, totalTax: 1200000 };
  }
};
if (typeof module !== 'undefined' && module.exports) {
  module.exports = FinancialEngine;
}
if (typeof window !== 'undefined') {
  window.FinancialEngine = FinancialEngine;
}
</script>
</body>
</html>
"""

# Extract <script> content
scripts = re.findall(r'<script>(.*?)</script>', html_mock, re.DOTALL)
js_code = "\n".join(scripts)

# Harness to run inside JSC
test_harness = f"""
{js_code}
let result = FinancialEngine.computeTaxBracket(100000, 1.0);
let opt = FinancialEngine.runOptimization();
print(JSON.stringify({{ bracketRate: result, optResult: opt }}));
"""

# Execute via JSC
res = subprocess.run(
    ["/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc", "-e", test_harness],
    capture_output=True,
    text=True,
    check=True
)

print("JSC test output:", res.stdout.strip())
parsed = json.loads(res.stdout.strip())
assert parsed["bracketRate"] == 0.22, "Bracket rate mismatch!"
assert parsed["optResult"]["bestConv"] == 150000, "Optimization mismatch!"
print("Test assertion passed perfectly!")
