#!/usr/bin/env python3
"""
Reusable Medical Unit Converter: China SI <-> US Conventional Units.
"""

CONVERSION_RULES = {
    "glucose": {"factor": 18.0182, "unit_us": "mg/dL", "ref_us": "70 - 99"},
    "cholesterol": {"factor": 38.67, "unit_us": "mg/dL", "ref_us": "< 200.0"},
    "triglycerides": {"factor": 88.57, "unit_us": "mg/dL", "ref_us": "< 150.0"},
    "hdl": {"factor": 38.67, "unit_us": "mg/dL", "ref_us": "> 40.0"},
    "ldl": {"factor": 38.67, "unit_us": "mg/dL", "ref_us": "< 100.0 (< 70 on statin)"},
    "creatinine": {"formula": lambda v: v / 88.4, "unit_us": "mg/dL", "ref_us": "0.70 - 1.30"},
    "bun": {"formula": lambda urea: urea * 2.80, "unit_us": "mg/dL", "ref_us": "7.0 - 20.0"},
    "uric_acid": {"formula": lambda v: v / 59.48, "unit_us": "mg/dL", "ref_us": "3.5 - 7.2"},
    "total_bilirubin": {"formula": lambda v: v / 17.1, "unit_us": "mg/dL", "ref_us": "0.2 - 1.2"},
    "direct_bilirubin": {"formula": lambda v: v / 17.1, "unit_us": "mg/dL", "ref_us": "0.0 - 0.3"},
    "indirect_bilirubin": {"formula": lambda v: v / 17.1, "unit_us": "mg/dL", "ref_us": "0.2 - 0.8"},
    "total_protein": {"formula": lambda v: v / 10.0, "unit_us": "g/dL", "ref_us": "6.0 - 8.3"},
    "albumin": {"formula": lambda v: v / 10.0, "unit_us": "g/dL", "ref_us": "3.5 - 5.0"},
    "globulin": {"formula": lambda v: v / 10.0, "unit_us": "g/dL", "ref_us": "2.0 - 3.5"},
    "hemoglobin": {"formula": lambda v: v / 10.0, "unit_us": "g/dL", "ref_us": "13.8 - 17.2"},
    "hematocrit": {"formula": lambda v: v * 100.0, "unit_us": "%", "ref_us": "40.7 - 50.3"},
    "insulin": {"formula": lambda v: v / 7.175, "unit_us": "μIU/mL", "ref_us": "2.6 - 24.9"},
    "calcium": {"formula": lambda v: v * 4.008, "unit_us": "mg/dL", "ref_us": "8.5 - 10.5"},
    "magnesium": {"formula": lambda v: v * 2.43, "unit_us": "mg/dL", "ref_us": "1.7 - 2.4"},
    "phosphorus": {"formula": lambda v: v * 3.097, "unit_us": "mg/dL", "ref_us": "2.5 - 4.5"},
    "weight_kg": {"formula": lambda v: v * 2.20462, "unit_us": "lbs", "ref_us": "--"},
    "waist_cm": {"formula": lambda v: v / 2.54, "unit_us": "in", "ref_us": "< 40 in (< 102 cm)"}
}

def convert_metric(metric_key, val_si, decimals=2):
    rule = CONVERSION_RULES.get(metric_key)
    if not rule:
        return {"val_us": val_si, "unit_us": "--", "ref_us": "--"}
    
    if "formula" in rule:
        val_us = rule["formula"](val_si)
    else:
        val_us = val_si * rule["factor"]
    
    return {
        "val_us": round(val_us, decimals),
        "unit_us": rule["unit_us"],
        "ref_us": rule.get("ref_us", "--")
    }

if __name__ == "__main__":
    tests = [
        ("glucose", 4.86),
        ("creatinine", 102.9),
        ("uric_acid", 488),
        ("triglycerides", 2.02),
        ("ldl", 1.90),
        ("bun", 7.51),
        ("total_protein", 68.8),
        ("albumin", 43.1)
    ]
    print("Unit Conversion Validation:")
    for k, v in tests:
        res = convert_metric(k, v)
        print(f"  {k}: {v} SI -> {res['val_us']} {res['unit_us']} (Ref: {res['ref_us']})")
