# Medical Laboratory Unit Conversions: China SI to US Conventional

| Clinical Analyte | China SI Unit | US Conventional Unit | Conversion Formula (SI -> US) | Standard US Reference Range | Notes |
|:---|:---:|:---:|:---:|:---:|:---|
| **Fasting Glucose** | mmol/L | mg/dL | `value * 18.0182` | 70 - 99 mg/dL | 100-125 is prediabetes |
| **Estimated Avg Glucose (eAG)** | mmol/L | mg/dL | `value * 18.0182` | 75 - 140 mg/dL | Derived from HbA1c |
| **Total Cholesterol** | mmol/L | mg/dL | `value * 38.67` | < 200 mg/dL | Desirable |
| **Triglycerides** | mmol/L | mg/dL | `value * 88.57` | < 150 mg/dL | Fasting |
| **HDL Cholesterol** | mmol/L | mg/dL | `value * 38.67` | > 40 mg/dL (M), > 50 (F) | Cardioprotective |
| **LDL Cholesterol** | mmol/L | mg/dL | `value * 38.67` | < 100 mg/dL (< 70 on statin) | Optimal target |
| **Serum Creatinine** | μmol/L | mg/dL | `value / 88.4` | 0.70 - 1.30 mg/dL (M) | China ref is narrower (57-98) |
| **Blood Urea Nitrogen (BUN)** | mmol/L Urea | mg/dL BUN | `value * 2.80` | 7 - 20 mg/dL | Urea MW 60, N2 MW 28 |
| **Serum Uric Acid** | μmol/L | mg/dL | `value / 59.48` | 3.5 - 7.2 mg/dL (M) | > 7.0 defines hyperuricemia |
| **Total Bilirubin** | μmol/L | mg/dL | `value / 17.1` | 0.2 - 1.2 mg/dL | |
| **Direct Bilirubin** | μmol/L | mg/dL | `value / 17.1` | 0.0 - 0.3 mg/dL | Conjugated |
| **Indirect Bilirubin** | μmol/L | mg/dL | `value / 17.1` | 0.2 - 0.8 mg/dL | Unconjugated |
| **Total Protein** | g/L | g/dL | `value / 10` | 6.0 - 8.3 g/dL | |
| **Serum Albumin** | g/L | g/dL | `value / 10` | 3.5 - 5.0 g/dL | |
| **Serum Globulin** | g/L | g/dL | `value / 10` | 2.0 - 3.5 g/dL | |
| **Fasting Insulin** | pmol/L | μIU/mL | `value / 7.175` | 2.6 - 24.9 μIU/mL | |
| **Total Calcium** | mmol/L | mg/dL | `value * 4.008` | 8.5 - 10.5 mg/dL | |
| **Serum Magnesium** | mmol/L | mg/dL | `value * 2.43` | 1.7 - 2.4 mg/dL | |
| **Inorganic Phosphorus** | mmol/L | mg/dL | `value * 3.097` | 2.5 - 4.5 mg/dL | |
| **Serum Potassium** | mmol/L | mEq/L | `value * 1.0` | 3.5 - 5.0 mEq/L | 1:1 equivalence |
| **Serum Sodium** | mmol/L | mEq/L | `value * 1.0` | 136 - 145 mEq/L | 1:1 equivalence |
| **Serum Chloride** | mmol/L | mEq/L | `value * 1.0` | 98 - 107 mEq/L | 1:1 equivalence |
| **Hemoglobin (Hb)** | g/L | g/dL | `value / 10` | 13.8 - 17.2 g/dL (M) | |
| **Hematocrit (Hct)** | L/L | % | `value * 100` | 40.7 - 50.3 % (M) | |
| **MCHC** | g/L | g/dL | `value / 10` | 32.0 - 36.0 g/dL | |
| **Apolipoprotein A1** | g/L | mg/dL | `value * 100` | 100 - 180 mg/dL | |
| **Apolipoprotein B** | g/L | mg/dL | `value * 100` | 60 - 130 mg/dL | |
| **Vitamin A (Retinol)** | ng/mL | μg/dL | `value / 10` | 32.5 - 78.0 μg/dL | |
| **Vitamin E** | μg/mL | mg/dL | `value / 10` | 0.55 - 1.70 mg/dL | |
| **Urine Creatinine** | g/L | mg/dL | `value * 100` | 20 - 320 mg/dL | |
| **Body Weight** | kg | lbs | `value * 2.20462` | -- | |
| **Body Height** | cm | ft / in | `value / 2.54` | -- | |
| **Waist Circumference** | cm | in | `value / 2.54` | < 40 in (M), < 35 in (F) | Asian cutoffs: 90cm/80cm |
