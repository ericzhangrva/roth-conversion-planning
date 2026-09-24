import json

data = {
    "metadata": {
        "patient_name_zh": "张喆",
        "patient_name_en": "Zhe Zhang",
        "gender_zh": "男",
        "gender_en": "Male",
        "age": 49,
        "dob": "1976-01-25",
        "exam_date": "2025-07-18",
        "report_date": "2025-07-31",
        "card_number": "6125094855",
        "medical_record_number": "51770971",
        "hospital_zh": "浙江大学医学院附属第二医院（浙二国际保健中心）",
        "hospital_en": "The Second Affiliated Hospital of Zhejiang University College of Medicine (International Healthcare Center)",
        "department_zh": "网络医学中心（解放路、滨江、博奥）门诊2025 (336706)",
        "department_en": "Cyber Medicine Center Outpatient Clinic (JieFang / BinJiang / BoAo)",
        "chief_doctors_zh": ["颜杨杨", "徐媛英"],
        "chief_doctors_en": ["Dr. Yangyang Yan", "Dr. Yuanying Xu"],
        "chief_auditor_zh": "贺肖洁",
        "chief_auditor_en": "Dr. Xiaojie He"
    },
    "vitals": {
        "height": {"value": 176, "unit_si": "cm", "value_us": "5 ft 9.3 in", "unit_us": "in", "ref": "--"},
        "weight": {"value": 92.7, "unit_si": "kg", "value_us": 204.4, "unit_us": "lbs", "ref": "--"},
        "bmi": {"value": 29.9, "unit_si": "kg/m²", "value_us": 29.9, "unit_us": "kg/m²", "status": "high", "ref_zh": "18.5~23.9 (≥28 肥胖)", "ref_us": "18.5 - 24.9 (25-29.9 Overweight, ≥30 Obese)"},
        "waist": {"value": 98, "unit_si": "cm", "value_us": 38.6, "unit_us": "in", "status": "high", "ref_zh": "<90 cm", "ref_us": "<40.0 in (<102 cm)"},
        "blood_pressure": {
            "systolic": {"value": 139, "unit": "mmHg", "ref": "90~140", "status": "borderline"},
            "diastolic": {"value": 87, "unit": "mmHg", "ref": "60~90", "status": "borderline"},
            "pulse": {"value": 89, "unit": "次/分 (bpm)", "ref": "60~100", "status": "normal"},
            "note_zh": "正常高值 / 治疗中高血压",
            "note_en": "Elevated / Pre-hypertensive (Under anti-hypertensive therapy)"
        },
        "vision": {
            "od_corrected": {"value": "0.8", "us": "20/25"},
            "os_corrected": {"value": "0.8", "us": "20/25"}
        }
    },
    "findings_14": [
        {
            "id": 1,
            "title_zh": "血肌酐增高、肾小球滤过率降低、胱抑素C增高",
            "title_en": "Elevated Creatinine, Reduced eGFR, and Elevated Cystatin C",
            "category_zh": "肾功能与代谢",
            "category_en": "Renal Function & Metabolism",
            "severity": "warning",
            "key_metrics": [
                {"name_zh": "血肌酐", "name_en": "Serum Creatinine", "value_si": "102.9 μmol/L", "value_us": "1.16 mg/dL", "ref_zh": "57.0-98.0 μmol/L", "ref_us": "0.70-1.30 mg/dL", "flag": "high"},
                {"name_zh": "肾小球滤过率 (eGFR)", "name_en": "eGFR (CKD-EPI)", "value_si": "73.23 mL/min", "value_us": "73.23 mL/min/1.73m²", "ref_zh": ">90.00 mL/min", "ref_us": ">90.00 mL/min/1.73m²", "flag": "low"},
                {"name_zh": "胱抑素C", "name_en": "Cystatin C", "value_si": "1.18 mg/L", "value_us": "1.18 mg/L", "ref_zh": "<1.03 mg/L", "ref_us": "0.60-1.00 mg/L", "flag": "high"}
            ],
            "explanation_zh": "肌酐是临床肾功能检验的重要指标之一，由肌肉代谢产生并经肾脏排泄。血肌酐升高见于各种原因引起的肾小球滤过功能减退，但仅一次轻度升高不一定有不可逆病理意义。肾小球滤过率（eGFR 73.23 mL/min）是早期评估肾功能减退的有效指标。胱抑素C能更早期敏感地反映肾小球滤过功能受损，但慢性炎症、甲状腺异常等也可轻度影响。",
            "explanation_en": "Serum creatinine is an established biomarker of renal excretory function. eGFR (73.23 mL/min/1.73m²) falls in the CKD Stage 2 range (60-89 mL/min). Cystatin C (1.18 mg/L) is a sensitive endogenous marker of glomerular filtration less dependent on muscle mass. Note that in US standard references, Cr 1.16 mg/dL is within the broad normal laboratory range (0.7-1.3 mg/dL), but represents a mild age- and hypertension-related reduction in GFR requiring longitudinal monitoring.",
            "recommendation_zh": "健康管理门诊 / 肾内科门诊就诊复查。避免使用肾毒性药物（如部分解热镇痛药NSAIDs、不明成分草药）。定期复查肾功能三项、尿常规及尿微量白蛋白。",
            "recommendation_en": "Consult Health Management / Nephrology Clinic for periodic surveillance. Avoid nephrotoxic agents (NSAIDs, aminoglycosides). Recheck basic metabolic panel, cystatin C, and urine microalbumin every 6-12 months."
        },
        {
            "id": 2,
            "title_zh": "高血压病、高脂血症（治疗中）、双侧颈动脉内中膜增厚、血管弹性下降、视网膜动脉细伴中轴反光增强",
            "title_en": "Hypertension, Hyperlipidemia (Treated), Carotid IMT, Decreased Arterial Elasticity, Retinal Arteriosclerosis",
            "category_zh": "心脑血管与眼底",
            "category_en": "Cardiovascular & Microvascular",
            "severity": "warning",
            "key_metrics": [
                {"name_zh": "颈动脉彩超", "name_en": "Carotid Ultrasound", "value": "双侧内中膜增厚 (IMT 0.11 cm = 1.1 mm)", "flag": "abnormal"},
                {"name_zh": "脉搏波传导速度 (baPWV)", "name_en": "baPWV", "value": "右侧 1477 cm/s (+20% vs 预测值), 左侧 1425 cm/s (+16%)", "flag": "abnormal"},
                {"name_zh": "眼底检查", "name_en": "Fundus Exam", "value": "视网膜动脉细，中轴反光增强 (I级视网膜动脉硬化改变)", "flag": "abnormal"},
                {"name_zh": "甘油三酯", "name_en": "Triglycerides", "value_si": "2.02 mmol/L", "value_us": "178.9 mg/dL", "ref_zh": "<1.70 mmol/L", "ref_us": "<150 mg/dL", "flag": "high"},
                {"name_zh": "低密度脂蛋白", "name_en": "LDL-C", "value_si": "1.90 mmol/L", "value_us": "73.5 mg/dL", "ref_zh": "<3.36 mmol/L", "ref_us": "<100 mg/dL (达标)", "flag": "normal"}
            ],
            "explanation_zh": "高血压与血脂异常是动脉粥样硬化性心血管疾病（ASCVD）的核心危险因素。检查显示颈动脉内中膜增厚（1.1mm）、右侧baPWV（1477 cm/s）轻度增快提示大中动脉弹性轻度减退，眼底镜下视网膜小动脉反光增强提示外周微血管也有轻度硬化改变。目前正规律服药（降压药与阿托伐他汀），LDL-C已控制在73.5 mg/dL（1.90 mmol/L）的理想水平，但甘油三酯仍轻度偏高。",
            "explanation_en": "Chronic hypertension and dyslipidemia contribute to systemic arterial remodeling. Subclinical macrovascular findings include bilateral carotid intima-media thickening (IMT 1.1 mm) and elevated right brachial-ankle pulse wave velocity (baPWV 1477 cm/s). Funduscopy shows grade 1 arteriolar narrowing with central light reflex. On active atorvastatin therapy, LDL-C is well-controlled at 73.5 mg/dL, while triglycerides remain mildly elevated at 178.9 mg/dL.",
            "recommendation_zh": "低盐低脂饮食，戒烟限酒，规律服用降压药及他汀类降脂药。保持心情舒畅，定期自测血压并记录。建议6-12个月复查血脂四项，半年复查颈动脉超声，每年复查眼底。",
            "recommendation_en": "Maintain low-sodium, heart-healthy diet, regular aerobic exercise. Continue current antihypertensive and statin regimens. Home blood pressure monitoring. Follow up carotid duplex ultrasound in 6-12 months and annual dilated eye exam."
        },
        {
            "id": 3,
            "title_zh": "高尿酸血症 (Hyperuricemia)",
            "title_en": "Hyperuricemia",
            "category_zh": "肾功能与代谢",
            "category_en": "Renal Function & Metabolism",
            "severity": "warning",
            "key_metrics": [
                {"name_zh": "血尿酸", "name_en": "Serum Uric Acid", "value_si": "488 μmol/L", "value_us": "8.20 mg/dL", "ref_zh": "208-428 μmol/L", "ref_us": "3.5-7.2 mg/dL", "flag": "high"}
            ],
            "explanation_zh": "日常饮食下，空腹血尿酸>420 μmol/L（7.0 mg/dL）即可诊断高尿酸血症。本次测定值为488 μmol/L（8.20 mg/dL）。高尿酸是嘌呤代谢紊乱所致，常与肥胖、代谢综合征、肾小球滤过率下降聚集发生。长期高尿酸可沉积在关节引起急性痛风，也可在肾脏沉积诱发肾间质病变与尿酸性肾结石（本次B超亦查出左肾0.5cm结石）。",
            "explanation_en": "Fasting serum uric acid is elevated at 488 μmol/L (8.20 mg/dL; US normal cutoff <7.0-7.2 mg/dL). Hyperuricemia reflects impaired purine turnover or decreased renal clearance (correlating with eGFR 73). Chronic hyperuricemia predisposes to gouty arthritis and nephrolithiasis (coinciding with the 0.5 cm left renal calculus detected on ultrasound).",
            "recommendation_zh": "忌烟限酒，少吃动物内脏、海鲜、肉汤、香肠等高嘌呤食物；杜绝高果糖含糖饮料；每日饮水2000-2500ml以上促进尿酸排出；控制体重。内分泌/风湿科随访，必要时启动降尿酸药物治疗（如别嘌醇、非布司他）。",
            "recommendation_en": "Strict dietary purine restriction (avoid organ meats, rich broths, shellfish, beer, high-fructose corn syrup). Ensure abundant hydration (>2.0-2.5 L/day). Endocrinology or rheumatology consultation to evaluate indications for uric-acid-lowering therapy."
        },
        {
            "id": 4,
            "title_zh": "左肺下叶少许小钙化灶 (Small Calcifications in Left Lower Lung Lobe)",
            "title_en": "Small Calcified Nodules in Left Lower Lobe",
            "category_zh": "呼吸与胸部影像",
            "category_en": "Pulmonary & Chest CT",
            "severity": "info",
            "key_metrics": [
                {"name_zh": "胸部CT", "name_en": "Chest CT", "value": "左肺下叶少许小钙化结节，直径约3-4mm", "flag": "benign"}
            ],
            "explanation_zh": "肺部钙化灶多属于良性陈旧性病变，通常是既往肺部感染、炎症或结核修复愈合后留下的钙化样疤痕。CT表现为边缘锐利的高密度影，无渗出或实质占位征象，恶性风险极低，一般无需药物治疗。",
            "explanation_en": "Screening chest CT demonstrates 3-4 mm well-circumscribed dense calcifications in the left lower lobe. These represent classic healed granulomatous sequelae from prior pulmonary inflammation or exposure, exhibiting completely benign characteristics.",
            "recommendation_zh": "戒烟，避免二手烟及粉尘暴露。无需特殊处理，每年健康体检低剂量胸部CT复查随访对比即可。",
            "recommendation_en": "Routine annual low-dose chest CT follow-up for stability; no intervention required."
        },
        {
            "id": 5,
            "title_zh": "脂肪肝 (Hepatic Steatosis)",
            "title_en": "Fatty Liver Disease (Hepatic Steatosis)",
            "category_zh": "消化与肝胆",
            "category_en": "Gastroenterology & Hepatobiliary",
            "severity": "attention",
            "key_metrics": [
                {"name_zh": "腹部超声", "name_en": "Abdominal Ultrasound", "value": "肝实质光点细密，回声增高，后方回声衰减，血管显示欠清", "flag": "abnormal"},
                {"name_zh": "ALT / AST", "name_en": "ALT / AST", "value": "ALT 28 U/L, AST 23 U/L, r-GT 33 U/L (肝酶完全正常)", "flag": "normal"}
            ],
            "explanation_zh": "B超显示典型轻中度脂肪肝声像。本次肝酶指标完全正常（ALT 28, AST 23, GGT 33, 胆红素均正常），提示处于单纯性脂肪浸润阶段，未发生显著脂肪性肝炎或肝细胞坏死。主要诱因为超重/肥胖（BMI 29.9）与代谢综合征相关胰岛素抵抗。",
            "explanation_en": "Abdominal ultrasound demonstrates characteristic diffuse increase in hepatic parenchymal echogenicity with deep acoustic attenuation, consistent with non-alcoholic fatty liver disease (NAFLD). Importantly, liver transaminases (ALT 28, AST 23, GGT 33) and bilirubin are completely normal, denoting simple steatosis without active steatohepatitis.",
            "recommendation_zh": "低脂低糖膳食，严格控制精制碳水和高热量食物，戒酒，坚持中等强度有氧运动，以减轻体重5%-10%为目标。6-12个月复查肝脏B超及肝生化功能。",
            "recommendation_en": "Lifestyle modification targeting 5-10% weight loss via caloric restriction and regular physical exercise. Avoid hepatotoxins/excessive alcohol. Follow up liver ultrasound and transaminases annually."
        },
        {
            "id": 6,
            "title_zh": "肥胖 (Obesity - BMI 29.9, 中心性肥胖)",
            "title_en": "Obesity (BMI 29.9 kg/m², Central Adiposity)",
            "category_zh": "营养与形体",
            "category_en": "Nutrition & Body Composition",
            "severity": "warning",
            "key_metrics": [
                {"name_zh": "身高 / 体重", "name_en": "Height / Weight", "value_si": "176 cm / 92.7 kg", "value_us": "5 ft 9 in / 204.4 lbs"},
                {"name_zh": "BMI", "name_en": "Body Mass Index", "value": "29.9 kg/m²", "ref_zh": "18.5-23.9 (≥24超重, ≥28肥胖)", "ref_us": "18.5-24.9 (≥30 Obese)", "flag": "high"},
                {"name_zh": "腰围", "name_en": "Waist Circumference", "value_si": "98 cm", "value_us": "38.6 in", "ref_zh": "<90 cm", "ref_us": "<40 in", "flag": "high"}
            ],
            "explanation_zh": "按照中国成人BMI标准，BMI≥28为肥胖（29.9已接近30）；男性腰围≥90cm（98cm）属于中心性腹型肥胖。内脏脂肪蓄积是高血压、高甘油三酯、胰岛素抵抗和动脉粥样硬化的共同病理基础。",
            "explanation_en": "A BMI of 29.9 kg/m² classifies as Class I Obesity under Asian criteria (cutoff ≥28 kg/m²) and upper Overweight / borderline Obese under WHO criteria. Waist circumference of 98 cm confirms central/visceral adiposity, the driving etiology of metabolic syndrome.",
            "recommendation_zh": "制定科学均衡的减重计划：控制总热量摄入，采用地中海或DASH饮食模式；每周进行至少150分钟快走、游泳或椭圆机等中等强度运动，配合抗阻肌力训练。营养科或健康管理门诊随诊指导。",
            "recommendation_en": "Comprehensive lifestyle intervention emphasizing DASH/Mediterranean diet, caloric deficit, and 150+ min/week moderate aerobic activity paired with resistance training. Nutritionist consultation."
        },
        {
            "id": 7,
            "title_zh": "代谢综合征 (Metabolic Syndrome)",
            "title_en": "Metabolic Syndrome",
            "category_zh": "肾功能与代谢",
            "category_en": "Renal Function & Metabolism",
            "severity": "warning",
            "key_metrics": [
                {"name_zh": "腹型肥胖", "name_en": "Abdominal Obesity", "value": "腰围 98 cm (标准 ≥90 cm) ✅ 满足"},
                {"name_zh": "血压升高/高血压病史", "name_en": "Elevated BP / Treatment", "value": "139/87 mmHg 及服药中 ✅ 满足"},
                {"name_zh": "甘油三酯升高", "name_en": "Elevated Triglycerides", "value": "2.02 mmol/L (178.9 mg/dL ≥ 1.70) ✅ 满足"},
                {"name_zh": "血糖异常/糖化血红蛋白", "name_en": "Glucose Impairment", "value": "HbA1c 5.8%, 胰岛素 172.5 pmol/L (偏高上限) ✅ 满足"}
            ],
            "explanation_zh": "代谢综合征是一组以腹型肥胖、糖脂代谢紊乱及高血压为特征的综合征。满足5项中3项即可确诊。患者同时具备腹型肥胖（腰围98cm）、高血压治疗中（139/87）、高甘油三酯（2.02 mmol/L）及糖尿病前期倾向，已完全符合代谢综合征诊断，是心脑血管病的关键危险因素。",
            "explanation_en": "The patient meets 4 out of 5 diagnostic criteria for Metabolic Syndrome: central obesity (waist 98 cm), treated hypertension, hypertriglyceridemia (2.02 mmol/L / 178.9 mg/dL), and pre-diabetic dysglycemia with borderline hyperinsulinemia (172.5 pmol/L).",
            "recommendation_zh": "综合多靶点干预：控盐（每日<5g）、控油、减糖，严格戒烟限酒，定期监测血压、血糖、血脂四项。全科/内分泌门诊综合随诊管理。",
            "recommendation_en": "Multimodal metabolic risk reduction targeting blood pressure, lipids, visceral weight loss, and insulin sensitization."
        },
        {
            "id": 8,
            "title_zh": "左肾结石 (0.5cm) (Left Renal Calculus)",
            "title_en": "Left Nephrolithiasis (0.5 cm Calculus)",
            "category_zh": "消化与肝胆",
            "category_en": "Gastroenterology & Hepatobiliary",
            "severity": "attention",
            "key_metrics": [
                {"name_zh": "左肾B超", "name_en": "Renal Ultrasound", "value": "左肾集合系统见一个强光团，大小约0.5cm，后方伴声影", "flag": "abnormal"},
                {"name_zh": "尿常规", "name_en": "Urinalysis", "value": "潜血阴性，红细胞 2/μL (正常范围)", "flag": "normal"}
            ],
            "explanation_zh": "超声发现左肾集合系统单发0.5cm结石，目前未见集合系统积水分离，双侧输尿管未扩张，尿常规红细胞正常且无潜血。结合血尿酸偏高（488 μmol/L），该结石可能为尿酸盐或草酸钙结石。0.5cm结石多数可通过多饮水和药物辅助自行排出或长期稳定观察。",
            "explanation_en": "Ultrasound reveals a solitary 0.5 cm hyperechoic stone with acoustic shadowing in the left renal collecting system. No hydronephrosis or calyceal dilation; urinalysis shows no hematuria. High serum uric acid (8.2 mg/dL) points to a uric acid or calcium oxalate composition.",
            "recommendation_zh": "每日保持充足饮水量（2000-2500ml以上），适当跳跃运动；限制高嘌呤及高草酸饮食。若突发剧烈腰痛、血尿或发热，应立即泌尿外科就诊。建议3-6个月复查泌尿系B超。",
            "recommendation_en": "Hydration therapy (>2.5 L water/day), alkalization if uric acid stones suspected, periodic renal ultrasound in 3-6 months. Seek emergency care if renal colic, hematuria, or fever occurs."
        },
        {
            "id": 9,
            "title_zh": "甲状腺双侧叶实质回声不均伴多发结节 (TI-RADS 3类)",
            "title_en": "Bilateral Thyroid Heterogeneous Echotexture with Multiple Nodules (TI-RADS 3)",
            "category_zh": "头颈与内分泌",
            "category_en": "Head, Neck & Endocrine",
            "severity": "attention",
            "key_metrics": [
                {"name_zh": "超声所见", "name_en": "Ultrasound Findings", "value": "实质回声不均匀，多个椭圆形低回声结节，右侧较大者约0.3cm，左侧较大者约0.5*0.2cm，边界清晰，CDFI未见异常血流", "flag": "abnormal"},
                {"name_zh": "TI-RADS分级", "name_en": "TI-RADS Category", "value": "TI-RADS 3类 (良性可能性大，恶性风险 <2-5%)", "flag": "info"},
                {"name_zh": "甲状腺功能全套", "name_en": "Thyroid Panel", "value": "TSH 2.90 mIU/L, FT3 4.53, FT4 12.02, TPOAb 1.28, ATGAb 0.81 (甲功五项及抗体均完全正常)", "flag": "normal"}
            ],
            "explanation_zh": "甲状腺回声不均匀常提示轻度慢性甲状腺炎样改变，但甲功五项（TSH、FT3、FT4）及自身抗体（TPOAb、ATGAb）均在理想正常范围内。双侧结节微小（最大0.5cm），形态规则，边界清晰，无微钙化或异常血流，归入TI-RADS 3类，基本属于良性病变，无需穿刺或手术。",
            "recommendation_zh": "无需特殊药物治疗，保持作息规律，避免盲目过量或极度缺碘。建议每6-12个月复查甲状腺B超和甲状腺功能。",
            "recommendation_en": "Benign ultrasound morphology and euthyroid function. No biopsy or surgical indication. Annual ultrasound surveillance."
        },
        {
            "id": 10,
            "title_zh": "糖尿病前期？ (Pre-diabetes Evaluation)",
            "title_en": "Pre-diabetes Assessment",
            "category_zh": "肾功能与代谢",
            "category_en": "Renal Function & Metabolism",
            "severity": "attention",
            "key_metrics": [
                {"name_zh": "空腹葡萄糖", "name_en": "Fasting Glucose", "value_si": "4.86 mmol/L", "value_us": "87.6 mg/dL", "ref_zh": "3.89-6.11 mmol/L", "ref_us": "70-99 mg/dL", "flag": "normal"},
                {"name_zh": "糖化血红蛋白 A1c", "name_en": "HbA1c", "value": "5.8 %", "ref_zh": "4.0-6.0 %", "ref_us": "<5.7 % Normal, 5.7-6.4% Pre-diabetes", "flag": "borderline"},
                {"name_zh": "糖化血红蛋白 F", "name_en": "HbF", "value": "2.4 %", "ref_zh": "0.1-1.3 %", "flag": "high"},
                {"name_zh": "空腹胰岛素", "name_en": "Fasting Insulin", "value_si": "172.5 pmol/L", "value_us": "24.0 μIU/mL", "ref_zh": "20.9-174.1 pmol/L", "ref_us": "2.6-24.9 μIU/mL", "flag": "normal_high"}
            ],
            "explanation_zh": "虽然本次空腹血糖正常（4.86 mmol/L / 87.6 mg/dL），但根据国际与中国糖尿病指南，HbA1c在5.7%~6.4%区间属于糖尿病前期。同时空腹胰岛素（172.5 pmol/L）位于正常参考值上限，反映存在高胰岛素代偿及外周胰岛素抵抗。",
            "explanation_en": "Fasting blood glucose is optimal at 87.6 mg/dL (4.86 mmol/L). However, HbA1c is 5.8% (American Diabetes Association defines prediabetes as HbA1c 5.7%-6.4%). Fasting insulin is at the uppermost ceiling of normal (172.5 pmol/L = 24.0 μIU/mL), indicating insulin resistance.",
            "recommendation_zh": "全科或内分泌门诊随访，可进一步行口服葡萄糖耐量试验（OGTT）评估胰岛功能。严格调整饮食碳水比例，增加运动，控制体重，每3-6个月复查HbA1c。",
            "recommendation_en": "Lifestyle modification to prevent progression to overt type 2 diabetes. Consider 75g oral glucose tolerance test (OGTT). Recheck HbA1c in 3-6 months."
        },
        {
            "id": 11,
            "title_zh": "颈椎退行性改变 (Cervical Spondylosis / Degeneration)",
            "title_en": "Cervical Spondylotic Degeneration",
            "category_zh": "骨骼与脊柱",
            "category_en": "Spine & Musculoskeletal",
            "severity": "info",
            "key_metrics": [
                {"name_zh": "颈椎CR侧位片", "name_en": "Cervical Spine X-Ray", "value": "颈椎生理曲度变直，椎体前、后缘骨质增生，椎间隙未见明显狭窄", "flag": "abnormal"}
            ],
            "explanation_zh": "CR片显示颈椎生理曲度变直伴唇样骨赘形成（骨质增生），为长期伏案、低头工作造成的早期颈椎退行性退变。椎间隙尚保持良好，未见明显椎体脱位或骨质破坏。",
            "explanation_en": "Cervical lateral radiography demonstrates straightening of physiologic lordosis with anterior/posterior marginal osteophyte formation, typical of occupational postural strain and early cervical spondylosis without severe intervertebral disc collapse.",
            "recommendation_zh": "避免长时间低头伏案或看手机；调整电脑屏幕至视线平齐；工间进行颈部肌肉拉伸放松；选择高度合适的支撑性枕头。如有上肢麻木、放射痛或眩晕，需骨科专科诊疗。",
            "recommendation_en": "Ergonomic adjustments, neck posture correction, active stretching. Avoid prolonged cervical flexion."
        },
        {
            "id": 12,
            "title_zh": "双眼豹纹状近视眼底、晶体密度增高",
            "title_en": "Bilateral Tigroid Myopic Fundus & Increased Lens Density",
            "category_zh": "眼科专科",
            "category_en": "Ophthalmology",
            "severity": "attention",
            "key_metrics": [
                {"name_zh": "眼底检查", "name_en": "Fundus Examination", "value": "双眼豹纹状近视眼底，视网膜动脉细，中轴反光增强", "flag": "abnormal"},
                {"name_zh": "裂隙灯检查", "name_en": "Slit Lamp Exam", "value": "双眼晶体密度增高（早期晶状体硬化/退行性改变）", "flag": "abnormal"},
                {"name_zh": "既往手术", "name_en": "Surgical History", "value": "右眼视网膜激光术后", "flag": "history"}
            ],
            "explanation_zh": "豹纹状眼底是高度/中度近视引起的脉络膜色素变薄透见脉络膜大血管纹理的表现。视网膜细动脉变细、反光增强提示高血压性微血管硬化改变。晶体密度增高多为中年后晶状体老化的早期表现。结合患者既往有右眼视网膜激光治疗史，需定期监测视网膜周边状况。",
            "explanation_en": "Tigroid fundus represents myopic choroidal thinning. Retinal arteriolar attenuation reflects chronic hypertensive microvascular change. Lens nuclear density increase represents early age-related crystalline lens sclerosis. Patient has a surgical history of right eye retinal photocoagulation.",
            "recommendation_zh": "养成良好用眼卫生习惯，避免剧烈头颅撞击或过度用眼。若出现眼前黑影飘动、异常闪光感或突重视力下降，需急诊眼科就诊。每年常规进行散瞳眼底检查及验光。",
            "recommendation_en": "Annual dilated fundus examination and optical refraction. Seek immediate ophthalmology attention if floaters, photopsia (flashes of light), or visual field cuts develop."
        },
        {
            "id": 13,
            "title_zh": "肌酸激酶轻度增高 (Elevated Creatine Kinase 183 U/L)",
            "title_en": "Mildly Elevated Creatine Kinase (183 U/L)",
            "category_zh": "心血管与心肌酶",
            "category_en": "Cardiovascular & Enzymes",
            "severity": "attention",
            "key_metrics": [
                {"name_zh": "肌酸激酶 (CK)", "name_en": "Creatine Kinase", "value": "183 U/L", "ref_zh": "<164 U/L", "ref_us": "30-200 U/L (US上限通常200-250)", "flag": "high"}
            ],
            "explanation_zh": "肌酸激酶（CK）在骨骼肌和心肌中高表达。本次CK为183 U/L，轻度超出中国医院参考值（<164 U/L）。但在多数欧美检验标准中，成年男性CK正常上限通常为200-250 U/L（183仍处于安全区间）。该轻度升高最常见于剧烈运动、肌肉疲劳受损，或服用他汀类降脂药（阿托伐他汀）引起的轻度肌酶波动。",
            "explanation_en": "Serum CK is mildly elevated at 183 U/L against China hospital cutoff (<164 U/L), but sits comfortably below standard US adult male upper limits (200-250 U/L). Common benign etiologies include recent strenuous muscular exertion or mild statin-induced myopathy (patient is on Atorvastatin).",
            "recommendation_zh": "近期避免过度剧烈力量训练。如无肌痛、肌肉乏力或浓茶色尿，无需过度恐慌。建议在停用剧烈运动后1个月复查CK及CK-MB心肌同工酶，评估与降脂药物的关系。",
            "recommendation_en": "Monitor for muscle soreness, tenderness, or weakness. Recheck CK in 4 weeks after resting from heavy exercise; verify liver enzymes and discuss statin regimen if symptoms appear."
        },
        {
            "id": 14,
            "title_zh": "前列腺钙化灶 (Prostatic Calcification)",
            "title_en": "Prostatic Calcification",
            "category_zh": "消化与肝胆",
            "category_en": "Gastroenterology & Hepatobiliary",
            "severity": "info",
            "key_metrics": [
                {"name_zh": "前列腺超声", "name_en": "Prostate Ultrasound", "value": "大小正常，两侧叶对称，实质内见高回声斑，未见明显占位，血流正常", "flag": "benign"},
                {"name_zh": "前列腺特异抗原 (PSA)", "name_en": "Total PSA", "value": "0.5193 ng/mL", "ref_zh": "<4.0000 ng/mL", "ref_us": "<4.0 ng/mL", "flag": "normal"}
            ],
            "explanation_zh": "前列腺钙化灶是成年男性前列腺腺管内淀粉样小体钙盐沉着形成的良性生理改变，多由既往隐匿性前列腺炎性病变消退后遗留。前列腺大小完全正常，直肠指诊未及硬结，前列腺特异性抗原（Total PSA 0.5193 ng/mL）远低于4.0警戒线，完全排除恶性征象。",
            "explanation_en": "Prostatic calcification is an incidental, benign finding resulting from quiescent prior focal inflammation. Prostate gland size is normal, and serum PSA is completely reassuring at 0.52 ng/mL (ref <4.0 ng/mL).",
            "recommendation_zh": "若无尿频、尿急、尿痛、夜尿增多或排尿等待等下尿路症状，无需任何药物或医疗干预。每年体检随访B超即可。",
            "recommendation_en": "Reassurance; no treatment required in the absence of lower urinary tract symptoms (LUTS). Annual ultrasound follow-up."
        }
    ],
    "lab_sections": [
        {
            "section_id": "glycemic",
            "title_zh": "GB212 糖化血红蛋白全套",
            "title_en": "Glycated Hemoglobin & Glycemic Panel",
            "date": "2025-07-18 07:50",
            "examiner": "陈小华",
            "auditor": "陈慧莉",
            "items": [
                {
                    "name_zh": "糖化血红蛋白 A1 (HbA1)",
                    "name_en": "Glycated Hemoglobin A1",
                    "val_si": 7.3, "unit_si": "%", "ref_si": "6.1 - 8.2",
                    "val_us": 7.3, "unit_us": "%", "ref_us": "6.1 - 8.2",
                    "status": "normal"
                },
                {
                    "name_zh": "糖化血红蛋白 A1c (HbA1c)",
                    "name_en": "Hemoglobin A1c (HbA1c)",
                    "val_si": 5.8, "unit_si": "%", "ref_si": "4.0 - 6.0",
                    "val_us": 5.8, "unit_us": "%", "ref_us": "<5.7 Normal, 5.7-6.4 Prediabetes",
                    "status": "borderline",
                    "flag": "normal"
                },
                {
                    "name_zh": "糖化血红蛋白 F (HbF / 胎儿血红蛋白)",
                    "name_en": "Fetal Hemoglobin (HbF)",
                    "val_si": 2.4, "unit_si": "%", "ref_si": "0.1 - 1.3",
                    "val_us": 2.4, "unit_us": "%", "ref_us": "0.1 - 1.3",
                    "status": "high",
                    "flag": "high"
                },
                {
                    "name_zh": "估计血浆平均葡萄糖浓度 (eAG)",
                    "name_en": "Estimated Average Glucose (eAG)",
                    "val_si": 6.6, "unit_si": "mmol/L", "ref_si": "4.2 - 7.8",
                    "val_us": 118.9, "unit_us": "mg/dL", "ref_us": "75 - 140",
                    "status": "normal"
                }
            ]
        },
        {
            "section_id": "urinary_renal",
            "title_zh": "JYK213 尿液早期肾功能系列",
            "title_en": "Urinary Early Renal Biomarker Panel",
            "date": "2025-07-18 08:58",
            "examiner": "张松照",
            "auditor": "肖于飞",
            "items": [
                {
                    "name_zh": "尿微量白蛋白 (mAlb)",
                    "name_en": "Urinary Microalbumin",
                    "val_si": "< 25.00", "unit_si": "mg/g·Cr", "ref_si": "< 25.00",
                    "val_us": "< 25.00", "unit_us": "mg/g Cr", "ref_us": "< 30.00",
                    "status": "normal"
                },
                {
                    "name_zh": "尿免疫球蛋白G (U-IgG)",
                    "name_en": "Urinary IgG",
                    "val_si": 1.90, "unit_si": "mg/g·Cr", "ref_si": "< 12.00",
                    "val_us": 1.90, "unit_us": "mg/g Cr", "ref_us": "< 12.00",
                    "status": "normal"
                },
                {
                    "name_zh": "尿转铁蛋白 (U-TRF)",
                    "name_en": "Urinary Transferrin",
                    "val_si": "< 2.90", "unit_si": "mg/g·Cr", "ref_si": "< 2.90",
                    "val_us": "< 2.90", "unit_us": "mg/g Cr", "ref_us": "< 2.90",
                    "status": "normal"
                },
                {
                    "name_zh": "尿α1微球蛋白 (α1-MG)",
                    "name_en": "Urinary α1-Microglobulin",
                    "val_si": 5.97, "unit_si": "mg/g·Cr", "ref_si": "< 15.00",
                    "val_us": 5.97, "unit_us": "mg/g Cr", "ref_us": "< 15.00",
                    "status": "normal"
                },
                {
                    "name_zh": "尿N-乙酰-β-D-氨基葡萄糖苷酶 (NAG)",
                    "name_en": "Urinary NAG Enzyme",
                    "val_si": 3.05, "unit_si": "U/g·Cr", "ref_si": "< 20.00",
                    "val_us": 3.05, "unit_us": "U/g Cr", "ref_us": "< 20.00",
                    "status": "normal"
                },
                {
                    "name_zh": "尿肌酐 (Urine Creatinine)",
                    "name_en": "Urinary Creatinine",
                    "val_si": 2.26, "unit_si": "g/L", "ref_si": "--",
                    "val_us": 226.0, "unit_us": "mg/dL", "ref_us": "20 - 320",
                    "status": "normal"
                }
            ]
        },
        {
            "section_id": "thyroid_hormones",
            "title_zh": "JYK217 T3、T4全套（甲状腺激素与抗体）",
            "title_en": "Thyroid Hormone Panel & Autoantibodies",
            "date": "2025-07-18 07:50",
            "examiner": "张松照",
            "auditor": "黄希颖",
            "items": [
                {
                    "name_zh": "总三碘甲状腺原氨酸 (TT3)",
                    "name_en": "Total Triiodothyronine (TT3)",
                    "val_si": 1.76, "unit_si": "nmol/L", "ref_si": "0.98 - 2.33",
                    "val_us": 114.6, "unit_us": "ng/dL", "ref_us": "80 - 200",
                    "status": "normal"
                },
                {
                    "name_zh": "游离三碘甲状腺原氨酸 (FT3)",
                    "name_en": "Free Triiodothyronine (FT3)",
                    "val_si": 4.53, "unit_si": "pmol/L", "ref_si": "2.43 - 6.01",
                    "val_us": 2.95, "unit_us": "pg/mL", "ref_us": "2.00 - 4.40",
                    "status": "normal"
                },
                {
                    "name_zh": "总甲状腺素 (TT4)",
                    "name_en": "Total Thyroxine (TT4)",
                    "val_si": 91.6, "unit_si": "nmol/L", "ref_si": "62.7 - 150.8",
                    "val_us": 7.12, "unit_us": "μg/dL", "ref_us": "4.5 - 12.0",
                    "status": "normal"
                },
                {
                    "name_zh": "游离甲状腺素 (FT4)",
                    "name_en": "Free Thyroxine (FT4)",
                    "val_si": 12.02, "unit_si": "pmol/L", "ref_si": "9.01 - 19.05",
                    "val_us": 0.93, "unit_us": "ng/dL", "ref_us": "0.82 - 1.77",
                    "status": "normal"
                },
                {
                    "name_zh": "高敏促甲状腺激素 (TSH)",
                    "name_en": "Thyroid Stimulating Hormone (TSH)",
                    "val_si": 2.90, "unit_si": "mIU/L", "ref_si": "0.35 - 4.94",
                    "val_us": 2.90, "unit_us": "μIU/mL", "ref_us": "0.40 - 4.50",
                    "status": "normal"
                },
                {
                    "name_zh": "甲状腺球蛋白 (TG)",
                    "name_en": "Thyroglobulin (TG)",
                    "val_si": 10.00, "unit_si": "μg/L", "ref_si": "3.50 - 77.00",
                    "val_us": 10.00, "unit_us": "ng/mL", "ref_us": "3.50 - 77.00",
                    "status": "normal"
                },
                {
                    "name_zh": "甲状腺球蛋白抗体 (ATGAb / TgAb)",
                    "name_en": "Thyroglobulin Antibody (TgAb)",
                    "val_si": 0.81, "unit_si": "IU/mL", "ref_si": "< 4.11",
                    "val_us": 0.81, "unit_us": "IU/mL", "ref_us": "< 4.00",
                    "status": "normal"
                },
                {
                    "name_zh": "甲状腺过氧化物酶抗体 (TPOAb)",
                    "name_en": "Thyroid Peroxidase Antibody (TPOAb)",
                    "val_si": 1.28, "unit_si": "IU/mL", "ref_si": "< 5.61",
                    "val_us": 1.28, "unit_us": "IU/mL", "ref_us": "< 9.00",
                    "status": "normal"
                }
            ]
        },
        {
            "section_id": "insulin",
            "title_zh": "JYK261 （空腹）胰岛素测定",
            "title_en": "Fasting Serum Insulin",
            "date": "2025-07-18 07:50",
            "examiner": "张松照",
            "auditor": "黄希颖",
            "items": [
                {
                    "name_zh": "空腹胰岛素 (Fasting Insulin)",
                    "name_en": "Fasting Serum Insulin",
                    "val_si": 172.5, "unit_si": "pmol/L", "ref_si": "20.9 - 174.1",
                    "val_us": 24.0, "unit_us": "μIU/mL", "ref_us": "2.6 - 24.9",
                    "status": "normal_high"
                }
            ]
        },
        {
            "section_id": "ebv",
            "title_zh": "鼻咽癌血清学三项 (EB病毒抗体)",
            "title_en": "Nasopharyngeal Carcinoma EBV Serology Panel",
            "date": "2025-07-18 07:50",
            "examiner": "张松照",
            "auditor": "肖于飞",
            "items": [
                {
                    "name_zh": "EBV Rta/IgG抗体",
                    "name_en": "EBV Rta IgG Antibody",
                    "val_si": "阴性 (Negative)", "unit_si": "S/CO", "ref_si": "< 1.00 (-)",
                    "val_us": "Negative", "unit_us": "S/CO", "ref_us": "< 1.00",
                    "status": "normal"
                },
                {
                    "name_zh": "EBV EA/IgA抗体",
                    "name_en": "EBV Early Antigen IgA",
                    "val_si": "阴性 (Negative)", "unit_si": "S/CO", "ref_si": "< 1.10 (-)",
                    "val_us": "Negative", "unit_us": "S/CO", "ref_us": "< 1.10",
                    "status": "normal"
                },
                {
                    "name_zh": "EBV衣壳抗原 IgA (VCA-IgA)",
                    "name_en": "EBV Viral Capsid Antigen IgA",
                    "val_si": "阴性 (Negative)", "unit_si": "S/CO", "ref_si": "< 1.10 (-)",
                    "val_us": "Negative", "unit_us": "S/CO", "ref_us": "< 1.10",
                    "status": "normal"
                }
            ]
        },
        {
            "section_id": "stool",
            "title_zh": "粪常规及隐血试验（找原虫、隐血）",
            "title_en": "Stool Routine & Occult Blood Test",
            "date": "2025-07-18 10:27",
            "examiner": "包林梅",
            "auditor": "俞爱群",
            "items": [
                {
                    "name_zh": "大便颜色", "name_en": "Stool Color",
                    "val_si": "黄色", "unit_si": "--", "ref_si": "黄色",
                    "val_us": "Yellow", "unit_us": "--", "ref_us": "Yellow", "status": "normal"
                },
                {
                    "name_zh": "大便性状", "name_en": "Stool Consistency",
                    "val_si": "软便", "unit_si": "--", "ref_si": "软",
                    "val_us": "Soft / Formed", "unit_us": "--", "ref_us": "Formed", "status": "normal"
                },
                {
                    "name_zh": "大便红细胞", "name_en": "Stool RBC",
                    "val_si": "阴性", "unit_si": "/HP", "ref_si": "阴性",
                    "val_us": "Negative", "unit_us": "/HP", "ref_us": "Negative", "status": "normal"
                },
                {
                    "name_zh": "大便白细胞", "name_en": "Stool WBC",
                    "val_si": "阴性", "unit_si": "/HP", "ref_si": "阴性",
                    "val_us": "Negative", "unit_us": "/HP", "ref_us": "Negative", "status": "normal"
                },
                {
                    "name_zh": "大便隐血 (OB)", "name_en": "Fecal Occult Blood",
                    "val_si": "阴性", "unit_si": "--", "ref_si": "阴性",
                    "val_us": "Negative", "unit_us": "--", "ref_us": "Negative", "status": "normal"
                },
                {
                    "name_zh": "寄生虫", "name_en": "Ova & Parasites",
                    "val_si": "未检到", "unit_si": "--", "ref_si": "无",
                    "val_us": "None Seen", "unit_us": "--", "ref_us": "Negative", "status": "normal"
                }
            ]
        },
        {
            "section_id": "c13",
            "title_zh": "各类呼气试验 - 幽门螺杆菌13C尿素呼气试验",
            "title_en": "Helicobacter Pylori 13C-Urea Breath Test",
            "date": "2025-07-18 13:03",
            "examiner": "徐国萍",
            "auditor": "朱永良",
            "items": [
                {
                    "name_zh": "HP尿素呼气试验 (DOB)",
                    "name_en": "H. Pylori Urea Breath Test (DOB)",
                    "val_si": 0.82, "unit_si": "DOB", "ref_si": "< 4.00",
                    "val_us": 0.82, "unit_us": "DOB", "ref_us": "< 4.00 (Negative)",
                    "status": "normal"
                }
            ]
        },
        {
            "section_id": "urinalysis",
            "title_zh": "尿常规 + 有形成分分析",
            "title_en": "Urinalysis & Microscopic Sediment Examination",
            "date": "2025-07-18 08:58",
            "examiner": "张正良",
            "auditor": "周俊",
            "items": [
                {"name_zh": "尿液颜色", "name_en": "Urine Color", "val_si": "黄色", "unit_si": "--", "ref_si": "淡黄色", "val_us": "Yellow", "unit_us": "--", "ref_us": "Yellow", "status": "normal"},
                {"name_zh": "浊度", "name_en": "Clarity / Turbidity", "val_si": "清", "unit_si": "--", "ref_si": "清", "val_us": "Clear", "unit_us": "--", "ref_us": "Clear", "status": "normal"},
                {"name_zh": "尿亚硝酸盐 (NIT)", "name_en": "Nitrite", "val_si": "阴性", "unit_si": "--", "ref_si": "阴性", "val_us": "Negative", "unit_us": "--", "ref_us": "Negative", "status": "normal"},
                {"name_zh": "尿葡萄糖 (GLU)", "name_en": "Urine Glucose", "val_si": "阴性", "unit_si": "mmol/L", "ref_si": "阴性", "val_us": "Negative", "unit_us": "mg/dL", "ref_us": "Negative", "status": "normal"},
                {"name_zh": "尿蛋白 (PRO)", "name_en": "Urine Protein", "val_si": "阴性", "unit_si": "g/L", "ref_si": "阴性", "val_us": "Negative", "unit_us": "mg/dL", "ref_us": "Negative", "status": "normal"},
                {"name_zh": "尿比重 (SG)", "name_en": "Specific Gravity", "val_si": 1.020, "unit_si": "--", "ref_si": "1.003 - 1.030", "val_us": 1.020, "unit_us": "--", "ref_us": "1.005 - 1.030", "status": "normal"},
                {"name_zh": "尿胆红素 (BIL)", "name_en": "Urine Bilirubin", "val_si": "阴性", "unit_si": "μmol/L", "ref_si": "阴性", "val_us": "Negative", "unit_us": "--", "ref_us": "Negative", "status": "normal"},
                {"name_zh": "尿酮体 (KET)", "name_en": "Urine Ketones", "val_si": "阴性", "unit_si": "mmol/L", "ref_si": "阴性", "val_us": "Negative", "unit_us": "--", "ref_us": "Negative", "status": "normal"},
                {"name_zh": "尿pH值", "name_en": "Urine pH", "val_si": 5.5, "unit_si": "--", "ref_si": "5.0 - 8.0", "val_us": 5.5, "unit_us": "--", "ref_us": "4.5 - 8.0", "status": "normal"},
                {"name_zh": "尿胆原 (URO)", "name_en": "Urobilinogen", "val_si": "弱阳性", "unit_si": "μmol/L", "ref_si": "弱阳性", "val_us": "Normal (Weak Pos)", "unit_us": "mg/dL", "ref_us": "0.2 - 1.0", "status": "normal"},
                {"name_zh": "尿潜血 (BLD)", "name_en": "Occult Blood (Hemoglobin)", "val_si": "阴性", "unit_si": "Ery/μL", "ref_si": "阴性", "val_us": "Negative", "unit_us": "--", "ref_us": "Negative", "status": "normal"},
                {"name_zh": "尿白细胞酯酶 (LEU)", "name_en": "Leukocyte Esterase", "val_si": "阴性", "unit_si": "LEU/μL", "ref_si": "阴性", "val_us": "Negative", "unit_us": "--", "ref_us": "Negative", "status": "normal"},
                {"name_zh": "尿白细胞计数", "name_en": "Urine WBC", "val_si": 1, "unit_si": "/μL", "ref_si": "≤ 10", "val_us": 1, "unit_us": "/HPF", "ref_us": "0 - 5", "status": "normal"},
                {"name_zh": "尿红细胞计数", "name_en": "Urine RBC", "val_si": 2, "unit_si": "/μL", "ref_si": "≤ 8", "val_us": 2, "unit_us": "/HPF", "ref_us": "0 - 3", "status": "normal"},
                {"name_zh": "尿鳞状上皮细胞", "name_en": "Squamous Epithelial Cells", "val_si": "< 1", "unit_si": "/μL", "ref_si": "≤ 2", "val_us": "< 1", "unit_us": "/HPF", "ref_us": "0 - 5", "status": "normal"},
                {"name_zh": "尿非鳞状上皮细胞", "name_en": "Non-squamous Epithelial Cells", "val_si": "< 1", "unit_si": "/μL", "ref_si": "≤ 4", "val_us": "< 1", "unit_us": "/HPF", "ref_us": "0 - 2", "status": "normal"},
                {"name_zh": "尿粘液丝", "name_en": "Mucus Filaments", "val_si": 8, "unit_si": "/μL", "ref_si": "≤ 137", "val_us": 8, "unit_us": "/LPF", "ref_us": "Rare/Few", "status": "normal"},
                {"name_zh": "尿草酸钙结晶", "name_en": "Calcium Oxalate Crystals", "val_si": "< 1", "unit_si": "/μL", "ref_si": "≤ 14", "val_us": "< 1", "unit_us": "/HPF", "ref_us": "Occasional", "status": "normal"},
                {"name_zh": "尿酸结晶", "name_en": "Uric Acid Crystals", "val_si": "< 1", "unit_si": "/μL", "ref_si": "≤ 14", "val_us": "< 1", "unit_us": "/HPF", "ref_us": "Occasional", "status": "normal"},
                {"name_zh": "管型计数", "name_en": "Casts", "val_si": "< 1", "unit_si": "/μL", "ref_si": "≤ 1", "val_us": "< 1", "unit_us": "/LPF", "ref_us": "0 - 1 Hyaline", "status": "normal"}
            ]
        },
        {
            "section_id": "comprehensive_metabolic",
            "title_zh": "体检生化全套（肝功、肾功、电解质、酶类、痛风、心血管生化）",
            "title_en": "Comprehensive Metabolic & Biochemical Panel",
            "date": "2025-07-18 07:50",
            "examiner": "陈小华",
            "auditor": "陈慧莉",
            "items": [
                {
                    "name_zh": "总蛋白 (TP)", "name_en": "Total Protein",
                    "val_si": 68.8, "unit_si": "g/L", "ref_si": "66.0 - 83.0",
                    "val_us": 6.88, "unit_us": "g/dL", "ref_us": "6.0 - 8.3", "status": "normal"
                },
                {
                    "name_zh": "白蛋白 (ALB)", "name_en": "Albumin",
                    "val_si": 43.1, "unit_si": "g/L", "ref_si": "35.0 - 52.0",
                    "val_us": 4.31, "unit_us": "g/dL", "ref_us": "3.5 - 5.0", "status": "normal"
                },
                {
                    "name_zh": "球蛋白 (GLB)", "name_en": "Globulin",
                    "val_si": 25.7, "unit_si": "g/L", "ref_si": "15.0 - 30.0",
                    "val_us": 2.57, "unit_us": "g/dL", "ref_us": "2.0 - 3.5", "status": "normal"
                },
                {
                    "name_zh": "白蛋白/球蛋白比值 (A/G)", "name_en": "A/G Ratio",
                    "val_si": 1.68, "unit_si": "--", "ref_si": "1.20 - 2.40",
                    "val_us": 1.68, "unit_us": "--", "ref_us": "1.1 - 2.5", "status": "normal"
                },
                {
                    "name_zh": "总胆红素 (TBIL)", "name_en": "Total Bilirubin",
                    "val_si": 15.2, "unit_si": "μmol/L", "ref_si": "< 26.0",
                    "val_us": 0.89, "unit_us": "mg/dL", "ref_us": "0.2 - 1.2", "status": "normal"
                },
                {
                    "name_zh": "直接胆红素 (DBIL)", "name_en": "Direct Bilirubin",
                    "val_si": 2.7, "unit_si": "μmol/L", "ref_si": "< 4.0",
                    "val_us": 0.16, "unit_us": "mg/dL", "ref_us": "0.0 - 0.3", "status": "normal"
                },
                {
                    "name_zh": "间接胆红素 (IBIL)", "name_en": "Indirect Bilirubin",
                    "val_si": 12.5, "unit_si": "μmol/L", "ref_si": "5.0 - 20.0",
                    "val_us": 0.73, "unit_us": "mg/dL", "ref_us": "0.2 - 0.8", "status": "normal"
                },
                {
                    "name_zh": "总胆汁酸 (TBA)", "name_en": "Total Bile Acids",
                    "val_si": 4.5, "unit_si": "μmol/L", "ref_si": "< 15.0",
                    "val_us": 4.5, "unit_us": "μmol/L", "ref_us": "< 10.0", "status": "normal"
                },
                {
                    "name_zh": "丙氨酸氨基转移酶 (ALT / GPT)", "name_en": "Alanine Aminotransferase (ALT)",
                    "val_si": 28, "unit_si": "U/L", "ref_si": "9 - 50",
                    "val_us": 28, "unit_us": "U/L", "ref_us": "7 - 56", "status": "normal"
                },
                {
                    "name_zh": "天冬氨酸氨基转移酶 (AST / GOT)", "name_en": "Aspartate Aminotransferase (AST)",
                    "val_si": 23, "unit_si": "U/L", "ref_si": "15 - 40",
                    "val_us": 23, "unit_us": "U/L", "ref_us": "10 - 40", "status": "normal"
                },
                {
                    "name_zh": "γ-谷氨酰转肽酶 (γ-GT / GGT)", "name_en": "Gamma-Glutamyl Transferase (GGT)",
                    "val_si": 33, "unit_si": "U/L", "ref_si": "10 - 60",
                    "val_us": 33, "unit_us": "U/L", "ref_us": "9 - 48", "status": "normal"
                },
                {
                    "name_zh": "碱性磷酸酶 (ALP)", "name_en": "Alkaline Phosphatase (ALP)",
                    "val_si": 83, "unit_si": "U/L", "ref_si": "30 - 120",
                    "val_us": 83, "unit_us": "U/L", "ref_us": "44 - 147", "status": "normal"
                },
                {
                    "name_zh": "α-L-岩藻糖苷酶 (AFU)", "name_en": "Alpha-L-Fucosidase (AFU)",
                    "val_si": 21.0, "unit_si": "U/L", "ref_si": "14.3 - 39.9",
                    "val_us": 21.0, "unit_us": "U/L", "ref_us": "14.0 - 40.0", "status": "normal"
                },
                {
                    "name_zh": "肌酸激酶 (CK)", "name_en": "Creatine Kinase (CK)",
                    "val_si": 183, "unit_si": "U/L", "ref_si": "< 164",
                    "val_us": 183, "unit_us": "U/L", "ref_us": "30 - 200 (US上限200-250)", "status": "high", "flag": "high"
                },
                {
                    "name_zh": "乳酸脱氢酶 (LDH)", "name_en": "Lactate Dehydrogenase (LDH)",
                    "val_si": 196, "unit_si": "U/L", "ref_si": "120 - 250",
                    "val_us": 196, "unit_us": "U/L", "ref_us": "140 - 280", "status": "normal"
                },
                {
                    "name_zh": "同型半胱氨酸 (HCY)", "name_en": "Homocysteine",
                    "val_si": 13.8, "unit_si": "μmol/L", "ref_si": "< 20.0",
                    "val_us": 13.8, "unit_us": "μmol/L", "ref_us": "< 15.0", "status": "normal"
                },
                {
                    "name_zh": "超敏C-反应蛋白 (hs-CRP)", "name_en": "High-Sensitivity CRP (hs-CRP)",
                    "val_si": 2.3, "unit_si": "mg/L", "ref_si": "< 5.0",
                    "val_us": 2.3, "unit_us": "mg/L", "ref_us": "< 3.0 (Avg risk 1-3)", "status": "normal"
                },
                {
                    "name_zh": "葡萄糖 (空腹血糖 Glu)", "name_en": "Fasting Glucose",
                    "val_si": 4.86, "unit_si": "mmol/L", "ref_si": "3.89 - 6.11",
                    "val_us": 87.6, "unit_us": "mg/dL", "ref_us": "70 - 99", "status": "normal"
                },
                {
                    "name_zh": "血肌酐 (Cr)", "name_en": "Serum Creatinine",
                    "val_si": 102.9, "unit_si": "μmol/L", "ref_si": "57.0 - 98.0",
                    "val_us": 1.16, "unit_us": "mg/dL", "ref_us": "0.70 - 1.30", "status": "high", "flag": "high"
                },
                {
                    "name_zh": "肾小球滤过率 (eGFR)", "name_en": "Estimated GFR (eGFR)",
                    "val_si": 73.23, "unit_si": "mL/min", "ref_si": "> 90.00",
                    "val_us": 73.23, "unit_us": "mL/min/1.73m²", "ref_us": "> 90.00", "status": "low", "flag": "low"
                },
                {
                    "name_zh": "尿素 (Urea / 尿素氮换算 BUN)", "name_en": "Blood Urea Nitrogen (BUN equiv)",
                    "val_si": 7.51, "unit_si": "mmol/L", "ref_si": "2.80 - 7.60",
                    "val_us": 21.0, "unit_us": "mg/dL", "ref_us": "7.0 - 20.0", "status": "borderline", "flag": "normal"
                },
                {
                    "name_zh": "尿酸 (UA)", "name_en": "Serum Uric Acid",
                    "val_si": 488, "unit_si": "μmol/L", "ref_si": "208 - 428",
                    "val_us": 8.20, "unit_us": "mg/dL", "ref_us": "3.5 - 7.2", "status": "high", "flag": "high"
                },
                {
                    "name_zh": "胱抑素C (Cys-C)", "name_en": "Cystatin C",
                    "val_si": 1.18, "unit_si": "mg/L", "ref_si": "< 1.03",
                    "val_us": 1.18, "unit_us": "mg/L", "ref_us": "0.60 - 1.00", "status": "high", "flag": "high"
                },
                {
                    "name_zh": "甘油三酯 (TG)", "name_en": "Triglycerides",
                    "val_si": 2.02, "unit_si": "mmol/L", "ref_si": "< 1.70",
                    "val_us": 178.9, "unit_us": "mg/dL", "ref_us": "< 150.0", "status": "high", "flag": "high"
                },
                {
                    "name_zh": "总胆固醇 (TC)", "name_en": "Total Cholesterol",
                    "val_si": 4.00, "unit_si": "mmol/L", "ref_si": "3.00 - 5.70",
                    "val_us": 154.7, "unit_us": "mg/dL", "ref_us": "< 200.0", "status": "normal"
                },
                {
                    "name_zh": "高密度脂蛋白胆固醇 (HDL-C)", "name_en": "HDL Cholesterol",
                    "val_si": 1.20, "unit_si": "mmol/L", "ref_si": "0.90 - 2.19",
                    "val_us": 46.4, "unit_us": "mg/dL", "ref_us": "> 40.0", "status": "normal"
                },
                {
                    "name_zh": "低密度脂蛋白胆固醇 (LDL-C)", "name_en": "LDL Cholesterol",
                    "val_si": 1.90, "unit_si": "mmol/L", "ref_si": "< 3.36",
                    "val_us": 73.5, "unit_us": "mg/dL", "ref_us": "< 100.0 (达标)", "status": "normal"
                },
                {
                    "name_zh": "载脂蛋白A1 (Apo-A1)", "name_en": "Apolipoprotein A1",
                    "val_si": 1.28, "unit_si": "g/L", "ref_si": "1.05 - 1.75",
                    "val_us": 128.0, "unit_us": "mg/dL", "ref_us": "100 - 180", "status": "normal"
                },
                {
                    "name_zh": "载脂蛋白B (Apo-B)", "name_en": "Apolipoprotein B",
                    "val_si": 0.68, "unit_si": "g/L", "ref_si": "0.60 - 1.40",
                    "val_us": 68.0, "unit_us": "mg/dL", "ref_us": "60 - 130", "status": "normal"
                },
                {
                    "name_zh": "淀粉酶 (AMY)", "name_en": "Serum Amylase",
                    "val_si": 83, "unit_si": "U/L", "ref_si": "35 - 135",
                    "val_us": 83, "unit_us": "U/L", "ref_us": "30 - 110", "status": "normal"
                },
                {
                    "name_zh": "血清钾 (K)", "name_en": "Potassium",
                    "val_si": 3.81, "unit_si": "mmol/L", "ref_si": "3.50 - 5.30",
                    "val_us": 3.81, "unit_us": "mEq/L", "ref_us": "3.5 - 5.0", "status": "normal"
                },
                {
                    "name_zh": "血清钠 (Na)", "name_en": "Sodium",
                    "val_si": 138.7, "unit_si": "mmol/L", "ref_si": "137.0 - 147.0",
                    "val_us": 138.7, "unit_us": "mEq/L", "ref_us": "136 - 145", "status": "normal"
                },
                {
                    "name_zh": "血清氯 (Cl)", "name_en": "Chloride",
                    "val_si": 106.9, "unit_si": "mmol/L", "ref_si": "99.0 - 110.0",
                    "val_us": 106.9, "unit_us": "mEq/L", "ref_us": "98 - 107", "status": "normal"
                },
                {
                    "name_zh": "血清钙 (Ca)", "name_en": "Total Calcium",
                    "val_si": 2.29, "unit_si": "mmol/L", "ref_si": "2.11 - 2.52",
                    "val_us": 9.18, "unit_us": "mg/dL", "ref_us": "8.5 - 10.5", "status": "normal"
                },
                {
                    "name_zh": "血清镁 (Mg)", "name_en": "Magnesium",
                    "val_si": 0.80, "unit_si": "mmol/L", "ref_si": "0.75 - 1.02",
                    "val_us": 1.95, "unit_us": "mg/dL", "ref_us": "1.7 - 2.4", "status": "normal"
                },
                {
                    "name_zh": "血清无机磷 (P)", "name_en": "Inorganic Phosphorus",
                    "val_si": 1.08, "unit_si": "mmol/L", "ref_si": "0.85 - 1.51",
                    "val_us": 3.34, "unit_us": "mg/dL", "ref_us": "2.5 - 4.5", "status": "normal"
                }
            ]
        },
        {
            "section_id": "vitamins",
            "title_zh": "维生素6项（体检专项）",
            "title_en": "Vitamin 6-Panel Assay",
            "date": "2025-07-18 07:50",
            "examiner": "桑奕雯",
            "auditor": "潘小艳",
            "items": [
                {
                    "name_zh": "维生素A (视黄醇)", "name_en": "Vitamin A (Retinol)",
                    "val_si": 710.69, "unit_si": "ng/mL", "ref_si": "325 - 780",
                    "val_us": 71.07, "unit_us": "μg/dL", "ref_us": "32.5 - 78.0", "status": "normal"
                },
                {
                    "name_zh": "25-羟基维生素D (总 25-OH Vit D)", "name_en": "Total 25-Hydroxyvitamin D",
                    "val_si": 37.87, "unit_si": "ng/mL", "ref_si": "正常: 20-80 (不足12-20, 缺乏<12)",
                    "val_us": 37.87, "unit_us": "ng/mL", "ref_us": "30 - 80 (Optimal)", "status": "normal"
                },
                {
                    "name_zh": "25-羟基维生素D2 (25-OH Vit D2)", "name_en": "25-OH Vitamin D2",
                    "val_si": 4.28, "unit_si": "ng/mL", "ref_si": "--",
                    "val_us": 4.28, "unit_us": "ng/mL", "ref_us": "--", "status": "normal"
                },
                {
                    "name_zh": "25-羟基维生素D3 (25-OH Vit D3)", "name_en": "25-OH Vitamin D3",
                    "val_si": 33.59, "unit_si": "ng/mL", "ref_si": "--",
                    "val_us": 33.59, "unit_us": "ng/mL", "ref_us": "--", "status": "normal"
                },
                {
                    "name_zh": "维生素K (叶绿醌)", "name_en": "Vitamin K1 (Phylloquinone)",
                    "val_si": 0.85, "unit_si": "ng/mL", "ref_si": "0.2 - 2.2",
                    "val_us": 0.85, "unit_us": "ng/mL", "ref_us": "0.2 - 2.2", "status": "normal"
                },
                {
                    "name_zh": "维生素E (α-生育酚)", "name_en": "Vitamin E (Alpha-Tocopherol)",
                    "val_si": 10.39, "unit_si": "μg/mL", "ref_si": "≥18岁: 5.5 - 17.0",
                    "val_us": 1.04, "unit_us": "mg/dL", "ref_us": "0.55 - 1.70", "status": "normal"
                }
            ]
        },
        {
            "section_id": "cbc",
            "title_zh": "血常规五分类全套",
            "title_en": "Complete Blood Count (CBC) with 5-Part Differential",
            "date": "2025-07-18 07:50",
            "examiner": "陈红兵",
            "auditor": "钟毓红",
            "items": [
                {"name_zh": "血红蛋白 (Hb)", "name_en": "Hemoglobin (Hb)", "val_si": 163, "unit_si": "g/L", "ref_si": "131 - 172", "val_us": 16.3, "unit_us": "g/dL", "ref_us": "13.8 - 17.2", "status": "normal"},
                {"name_zh": "红细胞计数 (RBC)", "name_en": "Red Blood Cell Count (RBC)", "val_si": 5.23, "unit_si": "10^12/L", "ref_si": "4.09 - 5.74", "val_us": 5.23, "unit_us": "M/μL", "ref_us": "4.10 - 5.70", "status": "normal"},
                {"name_zh": "红细胞压积 (HCT)", "name_en": "Hematocrit (HCT)", "val_si": 0.487, "unit_si": "L/L", "ref_si": "0.380 - 0.508", "val_us": 48.7, "unit_us": "%", "ref_us": "40.7 - 50.3", "status": "normal"},
                {"name_zh": "平均红细胞体积 (MCV)", "name_en": "Mean Corpuscular Volume (MCV)", "val_si": 93.2, "unit_si": "fL", "ref_si": "84.0 - 94.0", "val_us": 93.2, "unit_us": "fL", "ref_us": "80.0 - 98.0", "status": "normal"},
                {"name_zh": "平均红细胞血红蛋白量 (MCH)", "name_en": "Mean Corpuscular Hemoglobin (MCH)", "val_si": 31.1, "unit_si": "pg", "ref_si": "27.0 - 34.0", "val_us": 31.1, "unit_us": "pg", "ref_us": "27.0 - 33.0", "status": "normal"},
                {"name_zh": "平均红细胞血红蛋白浓度 (MCHC)", "name_en": "MCHC", "val_si": 335, "unit_si": "g/L", "ref_si": "320 - 380", "val_us": 33.5, "unit_us": "g/dL", "ref_us": "32.0 - 36.0", "status": "normal"},
                {"name_zh": "红细胞分布宽度 (RDW-CV)", "name_en": "RDW-CV", "val_si": 12.7, "unit_si": "%", "ref_si": "12.0 - 15.0", "val_us": 12.7, "unit_us": "%", "ref_us": "11.5 - 14.5", "status": "normal"},
                {"name_zh": "白细胞计数 (WBC)", "name_en": "White Blood Cell Count (WBC)", "val_si": 6.5, "unit_si": "10^9/L", "ref_si": "4.0 - 10.0", "val_us": 6.5, "unit_us": "K/μL", "ref_us": "4.5 - 11.0", "status": "normal"},
                {"name_zh": "中性粒细胞绝对值 (NEUT#)", "name_en": "Absolute Neutrophil Count (ANC)", "val_si": 3.41, "unit_si": "10^9/L", "ref_si": "2.00 - 7.00", "val_us": 3.41, "unit_us": "K/μL", "ref_us": "1.8 - 7.0", "status": "normal"},
                {"name_zh": "淋巴细胞绝对值 (LYMPH#)", "name_en": "Absolute Lymphocyte Count", "val_si": 2.42, "unit_si": "10^9/L", "ref_si": "0.80 - 4.00", "val_us": 2.42, "unit_us": "K/μL", "ref_us": "1.0 - 4.0", "status": "normal"},
                {"name_zh": "单核细胞绝对值 (MONO#)", "name_en": "Absolute Monocyte Count", "val_si": 0.45, "unit_si": "10^9/L", "ref_si": "0.20 - 1.20", "val_us": 0.45, "unit_us": "K/μL", "ref_us": "0.2 - 0.8", "status": "normal"},
                {"name_zh": "嗜酸性粒细胞绝对值 (EO#)", "name_en": "Absolute Eosinophil Count", "val_si": 0.19, "unit_si": "10^9/L", "ref_si": "< 1.00", "val_us": 0.19, "unit_us": "K/μL", "ref_us": "0.0 - 0.5", "status": "normal"},
                {"name_zh": "嗜碱性粒细胞绝对值 (BASO#)", "name_en": "Absolute Basophil Count", "val_si": 0.03, "unit_si": "10^9/L", "ref_si": "< 0.10", "val_us": 0.03, "unit_us": "K/μL", "ref_us": "0.0 - 0.2", "status": "normal"},
                {"name_zh": "中性粒细胞百分比 (NEUT%)", "name_en": "Neutrophil %", "val_si": 52.4, "unit_si": "%", "ref_si": "50.0 - 70.0", "val_us": 52.4, "unit_us": "%", "ref_us": "40.0 - 70.0", "status": "normal"},
                {"name_zh": "淋巴细胞百分比 (LYMPH%)", "name_en": "Lymphocyte %", "val_si": 37.3, "unit_si": "%", "ref_si": "20.0 - 40.0", "val_us": 37.3, "unit_us": "%", "ref_us": "20.0 - 45.0", "status": "normal"},
                {"name_zh": "单核细胞百分比 (MONO%)", "name_en": "Monocyte %", "val_si": 6.9, "unit_si": "%", "ref_si": "4.0 - 12.0", "val_us": 6.9, "unit_us": "%", "ref_us": "2.0 - 10.0", "status": "normal"},
                {"name_zh": "嗜酸性粒细胞百分比 (EO%)", "name_en": "Eosinophil %", "val_si": 3.0, "unit_si": "%", "ref_si": "< 10.0", "val_us": 3.0, "unit_us": "%", "ref_us": "1.0 - 5.0", "status": "normal"},
                {"name_zh": "嗜碱性粒细胞百分比 (BASO%)", "name_en": "Basophil %", "val_si": 0.4, "unit_si": "%", "ref_si": "< 1.0", "val_us": 0.4, "unit_us": "%", "ref_us": "0.0 - 1.0", "status": "normal"},
                {"name_zh": "血小板计数 (PLT)", "name_en": "Platelet Count (PLT)", "val_si": 180, "unit_si": "10^9/L", "ref_si": "100 - 300", "val_us": 180, "unit_us": "K/μL", "ref_us": "150 - 450", "status": "normal"},
                {"name_zh": "血小板压积 (PCT)", "name_en": "Plateletcrit (PCT)", "val_si": 0.197, "unit_si": "%", "ref_si": "0.106 - 0.250", "val_us": 0.197, "unit_us": "%", "ref_us": "0.106 - 0.250", "status": "normal"},
                {"name_zh": "血小板平均体积 (MPV)", "name_en": "Mean Platelet Volume (MPV)", "val_si": 11.0, "unit_si": "fL", "ref_si": "7.8 - 11.3", "val_us": 11.0, "unit_us": "fL", "ref_us": "7.5 - 11.5", "status": "normal"}
            ]
        },
        {
            "section_id": "tumor_markers",
            "title_zh": "血清肿瘤标志物全套 (10项)",
            "title_en": "Serum Tumor Marker Panel (10 Markers)",
            "date": "2025-07-18 07:50",
            "examiner": "蒋文智",
            "auditor": "方永明",
            "items": [
                {"name_zh": "癌胚抗原 (CEA)", "name_en": "Carcinoembryonic Antigen (CEA)", "val_si": 1.9, "unit_si": "ng/mL", "ref_si": "< 5.0", "val_us": 1.9, "unit_us": "ng/mL", "ref_us": "< 3.0 (Nonsmoker <3.0)", "status": "normal"},
                {"name_zh": "甲胎蛋白 (AFP)", "name_en": "Alpha-Fetoprotein (AFP)", "val_si": 3.4, "unit_si": "ng/mL", "ref_si": "< 20.0", "val_us": 3.4, "unit_us": "ng/mL", "ref_us": "< 10.0", "status": "normal"},
                {"name_zh": "糖类抗原 19-9 (CA19-9)", "name_en": "Cancer Antigen 19-9 (CA19-9)", "val_si": 5.0, "unit_si": "U/mL", "ref_si": "< 37.0", "val_us": 5.0, "unit_us": "U/mL", "ref_us": "< 37.0", "status": "normal"},
                {"name_zh": "糖类抗原 125 (CA125)", "name_en": "Cancer Antigen 125 (CA125)", "val_si": 8.1, "unit_si": "U/mL", "ref_si": "< 35.0", "val_us": 8.1, "unit_us": "U/mL", "ref_us": "< 35.0", "status": "normal"},
                {"name_zh": "糖类抗原 242 (CA242)", "name_en": "Cancer Antigen 242 (CA242)", "val_si": 1.6, "unit_si": "U/mL", "ref_si": "< 20.0", "val_us": 1.6, "unit_us": "U/mL", "ref_us": "< 20.0", "status": "normal"},
                {"name_zh": "细胞角蛋白19片段 (Cyfra21-1 / CA211)", "name_en": "Cytokeratin 19 Fragment (CA211)", "val_si": 3.8, "unit_si": "ng/mL", "ref_si": "< 5.0", "val_us": 3.8, "unit_us": "ng/mL", "ref_us": "< 3.3", "status": "normal"},
                {"name_zh": "神经元特异性烯醇化酶 (NSE)", "name_en": "Neuron-Specific Enolase (NSE)", "val_si": 15.3, "unit_si": "ng/mL", "ref_si": "< 25.0", "val_us": 15.3, "unit_us": "ng/mL", "ref_us": "< 17.0", "status": "normal"},
                {"name_zh": "鳞状细胞癌抗原 (SCC)", "name_en": "Squamous Cell Carcinoma Antigen (SCC)", "val_si": 1.0, "unit_si": "ng/mL", "ref_si": "< 1.5", "val_us": 1.0, "unit_us": "ng/mL", "ref_us": "< 1.5", "status": "normal"},
                {"name_zh": "总前列腺特异性抗原 (t-PSA)", "name_en": "Total Prostate-Specific Antigen (t-PSA)", "val_si": 0.5193, "unit_si": "ng/mL", "ref_si": "< 4.0000", "val_us": 0.52, "unit_us": "ng/mL", "ref_us": "< 4.00", "status": "normal"},
                {"name_zh": "游离前列腺特异性抗原 (f-PSA)", "name_en": "Free Prostate-Specific Antigen (f-PSA)", "val_si": 0.2620, "unit_si": "ng/mL", "ref_si": "< 1.0000", "val_us": 0.26, "unit_us": "ng/mL", "ref_us": "< 1.00", "status": "normal"},
                {"name_zh": "游离/总PSA比值 (f/T PSA)", "name_en": "Free/Total PSA Ratio", "val_si": 0.50, "unit_si": "--", "ref_si": "> 0.18", "val_us": 0.50, "unit_us": "--", "ref_us": "> 0.25", "status": "normal"}
            ]
        }
    ],
    "specialized_diagnostics": {
        "tcd": {
            "title_zh": "经颅多普勒脑血流分析 (TCD)",
            "title_en": "Transcranial Doppler (TCD) Cerebrovascular Hemodynamics",
            "date": "2025-07-18",
            "doctor": "钟国栋 / 签名: 张雪梅",
            "conclusion_zh": "双侧大脑中动脉血流速度对称、频谱形态正常；双侧椎动脉-基底动脉血流速度及频谱形态正常；双侧颈总动脉、颈内动脉颅外段、颈外动脉血流速度及频谱形态正常。TCD探及血管血流速度及频谱形态未见明显异常。",
            "conclusion_en": "Bilateral middle cerebral arteries (MCA) exhibit symmetric flow velocity and physiological waveforms. Vertebrobasilar arterial flows and extracranial carotid tree (CCA, ICA, ECA) demonstrate normal velocities and resistance indices. No significant hemodynamic stenosis or intracranial vascular abnormality detected.",
            "table": [
                {"vessel": "LCCA (左颈总动脉)", "depth": "--", "peak": 75, "mean": 35, "dias": 15, "pi": 1.71, "ri": 0.80, "sbi": 0.33, "sd": 5.00, "hr": 91},
                {"vessel": "LICA (左颈内动脉)", "depth": "--", "peak": -49, "mean": -30, "dias": -20, "pi": 0.98, "ri": 0.59, "sbi": 0.53, "sd": 2.45, "hr": 86},
                {"vessel": "LECA (左颈外动脉)", "depth": "--", "peak": -36, "mean": -17, "dias": -7, "pi": 1.74, "ri": 0.81, "sbi": 0.55, "sd": "--", "hr": 86},
                {"vessel": "RCCA (右颈总动脉)", "depth": "--", "peak": 61, "mean": 30, "dias": 15, "pi": 1.52, "ri": 0.75, "sbi": 0.37, "sd": 4.07, "hr": 83},
                {"vessel": "RICA (右颈内动脉)", "depth": "--", "peak": -51, "mean": -32, "dias": -23, "pi": 0.87, "ri": 0.55, "sbi": 0.55, "sd": 2.22, "hr": 77},
                {"vessel": "RECA (右颈外动脉)", "depth": "--", "peak": -55, "mean": -25, "dias": -10, "pi": 1.80, "ri": 0.82, "sbi": 0.57, "sd": "--", "hr": 87},
                {"vessel": "LMCA (左大脑中动脉)", "depth": 55, "peak": 95, "mean": 58, "dias": 40, "pi": 0.94, "ri": 0.58, "sbi": 0.52, "sd": 2.38, "hr": 77},
                {"vessel": "RMCA (右大脑中动脉)", "depth": 55, "peak": 89, "mean": 50, "dias": 31, "pi": 1.15, "ri": 0.65, "sbi": 0.53, "sd": 2.87, "hr": 88},
                {"vessel": "BA (基底动脉)", "depth": 90, "peak": -68, "mean": -41, "dias": -28, "pi": 0.97, "ri": 0.59, "sbi": 0.78, "sd": 2.43, "hr": 103},
                {"vessel": "LVA (左椎动脉)", "depth": 50, "peak": -34, "mean": -22, "dias": -16, "pi": 0.82, "ri": 0.53, "sbi": 0.04, "sd": 2.13, "hr": 101},
                {"vessel": "RVA (右椎动脉)", "depth": 50, "peak": -35, "mean": -21, "dias": -14, "pi": 1.00, "ri": 0.60, "sbi": 0.24, "sd": 2.50, "hr": 88}
            ]
        },
        "arteriosclerosis": {
            "title_zh": "动脉硬化检测与血管弹性分析 (PWV / ABI)",
            "title_en": "Arterial Stiffness & Ankle-Brachial Index (baPWV / ABI)",
            "date": "2025-07-18 08:22",
            "examiner": "赵娜",
            "image": "assets/arteriosclerosis_report.jpg",
            "cvd_risk_10yr": "2.5%",
            "metrics": {
                "right_arm_bp": {"systolic": 142, "diastolic": 86, "map": 103, "pulse_pressure": 56},
                "left_arm_bp": {"systolic": 143, "diastolic": 88, "map": 105, "pulse_pressure": 55},
                "right_ankle_bp": {"systolic": 160, "diastolic": 88, "map": 111, "pulse_pressure": 72},
                "left_ankle_bp": {"systolic": 157, "diastolic": 88, "map": 109, "pulse_pressure": 69},
                "right_abi": {"value": 1.12, "ref": "0.90 - 1.40", "status": "normal", "interpretation_zh": "正常", "interpretation_en": "Normal"},
                "left_abi": {"value": 1.10, "ref": "0.90 - 1.40", "status": "normal", "interpretation_zh": "正常", "interpretation_en": "Normal"},
                "right_bapwv": {"value": 1477, "predicted": 1228, "pct_diff": "+20%", "unit": "cm/s", "status": "high", "interpretation_zh": "轻度偏高，血管弹性轻度下降", "interpretation_en": "Mildly elevated, indicating mild arterial stiffness"},
                "left_bapwv": {"value": 1425, "predicted": 1228, "pct_diff": "+16%", "unit": "cm/s", "status": "normal", "interpretation_zh": "正常范围内，血管弹性良好", "interpretation_en": "Within normal range, preserved elasticity"}
            },
            "conclusion_zh": "双侧ABI值属正常范围，双下肢主干动脉血流通畅无狭窄。右侧PWV值较年龄预测值轻度偏高（1477 vs 1228 cm/s），提示大动脉壁顺应性及弹性轻度下降；左侧PWV处于该年龄段正常范围。",
            "conclusion_en": "Bilateral ABI values are within normal limits (1.12 and 1.10), ruling out peripheral artery disease (PAD) in the lower extremities. Right baPWV is mildly increased (1477 cm/s, +20% vs predicted 1228 cm/s), demonstrating mild early systemic arterial stiffening."
        },
        "bone_density": {
            "title_zh": "超声骨密度检测 (BMD)",
            "title_en": "Ultrasound Bone Mineral Densitometry (BMD)",
            "date": "2025-07-18 07:55",
            "examiner": "刘珊",
            "image": "assets/bone_density_chart.jpg",
            "site_zh": "右足跟骨 (Right Calcaneus)",
            "site_en": "Right Calcaneus",
            "sos": "1357.4 m/s",
            "bua": "47.5",
            "oi": "54.6",
            "t_score": 0.15,
            "z_score": 1.05,
            "adult_ratio": "101.4%",
            "age_matched_ratio": "110.6%",
            "conclusion_zh": "T值 +0.15（正常标准 > -1.0），骨质正常。骨密度达到健康青年成人峰值的101.4%，为同龄参考值的110.6%。未见骨质减少或骨质疏松征象。",
            "conclusion_en": "T-score is +0.15 (WHO normal criterion > -1.0 SD), consistent with normal bone mineral density. BMD is 101.4% of young adult peak and 110.6% of age-matched reference."
        },
        "ecg": {
            "title_zh": "常规12导联心电图",
            "title_en": "12-Lead Electrocardiogram (ECG)",
            "date": "2025-07-18 09:42",
            "auditor": "黄希颖 / 医师签名",
            "image": "assets/ecg_strip.jpg",
            "heart_rate": "70 bpm",
            "pr_interval": "148 ms",
            "qrs_duration": "110 ms",
            "qt_qtc": "368 / 397 ms",
            "qrs_axis": "76°",
            "rv5_sv1": "1.18 / 0.28 mV",
            "rhythm_zh": "窦性心律",
            "rhythm_en": "Normal Sinus Rhythm",
            "conclusion_zh": "窦性心律，正常范围心电图。心率70次/分，P-R间期、QRS波群时程及QTc间期均在正常生理范围，无心肌缺血、传导阻滞或心律失常特征。",
            "conclusion_en": "Normal sinus rhythm at 70 bpm. Normal PR interval (148 ms), normal QTc (397 ms), normal QRS electrical axis (76°). Normal baseline 12-lead electrocardiogram."
        },
        "ultrasound": {
            "title_zh": "高分辨率彩色超声多器官系统联合检查",
            "title_en": "Comprehensive Color Doppler Ultrasound Examination",
            "date": "2025-07-18 08:52",
            "doctor": "许俊",
            "assistant": "彭军艳",
            "organs": [
                {
                    "organ_zh": "双侧甲状腺",
                    "organ_en": "Thyroid Gland",
                    "findings_zh": "双侧叶大小、形态正常，包膜光滑，实质回声不均匀，在甲状腺实质内各见多个椭圆形低回声结节，右侧较大者约0.3cm，左侧较大者约0.5*0.2cm，边界及周边可辨，内部回声不均，CDFI示其内未见明显血流信号。实质内血流未见异常。",
                    "findings_en": "Thyroid lobes are normal in size and contour with intact capsule. Parenchymal echotexture is mildly heterogeneous. Bilateral discrete oval hypoechoic nodules: largest on right measures 0.3 cm, largest on left measures 0.5 x 0.2 cm. Margins well-defined, no microcalcifications. Color Doppler shows no pathological internal vascularity.",
                    "conclusion_zh": "甲状腺双侧叶实质回声不均伴多发结节 TI-RADS 3类",
                    "conclusion_en": "Bilateral thyroid heterogeneous echotexture with multiple small nodules (TI-RADS 3, benign appearance)",
                    "status": "attention"
                },
                {
                    "organ_zh": "双侧颈动脉",
                    "organ_en": "Carotid Arteries",
                    "findings_zh": "双侧颈动脉内径正常，内中膜增厚，较厚处约0.11cm（1.1mm），内膜不光整，动脉腔内未见明显异常回声，管腔未见狭窄，彩色多普勒血流充填良好。",
                    "findings_en": "Carotid lumen calibers are normal bilaterally. Intima-media thickening is present (max thickness 0.11 cm = 1.1 mm) with irregular intimal surface. No luminal stenosis or discrete atherosclerotic plaques. Color Doppler indicates laminar flow without filling defects.",
                    "conclusion_zh": "双侧颈动脉内中膜增厚",
                    "conclusion_en": "Bilateral carotid intima-media thickening (IMT 1.1 mm)",
                    "status": "attention"
                },
                {
                    "organ_zh": "肝脏与门静脉",
                    "organ_en": "Liver & Portal Vein",
                    "findings_zh": "肝脏大小正常，包膜光整，肝实质光点细密，回声增高，分布均匀，肝实质内未见明显占位性病变，肝实质后方回声衰减，肝内血管走行显示欠清，门静脉内径正常范围，内部透声好，CDFI显示血流充填良好。",
                    "findings_en": "Normal liver dimensions with smooth contours. Parenchymal echoes are finely increased and diffusely brightened with posterior acoustic attenuation; intrahepatic vascular architecture is mildly attenuated. Portal vein diameter and flow velocities are normal.",
                    "conclusion_zh": "脂肪肝 (Hepatic Steatosis)",
                    "conclusion_en": "Fatty liver (Diffuse hepatic steatosis)",
                    "status": "attention"
                },
                {
                    "organ_zh": "胆囊与胆管",
                    "organ_en": "Gallbladder & Bile Ducts",
                    "findings_zh": "胆囊切除术后改变。肝内胆管未见明显扩张，总胆管上段内径正常，总胆管内未见异常回声或结石嵌顿。",
                    "findings_en": "Post-cholecystectomy status. Intrahepatic and extrahepatic biliary ducts are non-dilated. Common bile duct upper caliber is normal without intraductal filling defects or residual calculi.",
                    "conclusion_zh": "胆囊切除术后，肝内外胆管不扩张",
                    "conclusion_en": "Status post cholecystectomy; no biliary tree dilatation",
                    "status": "normal"
                },
                {
                    "organ_zh": "胰腺与脾脏",
                    "organ_en": "Pancreas & Spleen",
                    "findings_zh": "胰腺大小形态正常，实质回声均匀，CDFI未见异常。脾脏大小正常，形态规则，包膜光整，脾实质回声均匀，CDFI未见异常。",
                    "findings_en": "Pancreas and spleen are normal in size, shape, and parenchymal echotexture. No focal masses or vascular anomalies.",
                    "conclusion_zh": "胰腺、脾脏未见明显异常",
                    "conclusion_en": "Unremarkable pancreas and spleen",
                    "status": "normal"
                },
                {
                    "organ_zh": "左侧肾脏",
                    "organ_en": "Left Kidney",
                    "findings_zh": "左侧肾脏大小正常，形态规则，包膜光整，实质回声均匀，皮髓质分界清晰，实质内未见占位，集合系统无积水分离。在集合系统内见一个强光团，大小约0.5cm，后方伴声影，CDFI示血流充盈良好。",
                    "findings_en": "Left kidney normal in size and cortical thickness with sharp corticomedullary differentiation. No hydronephrosis. Solitary 0.5 cm hyperechoic calculus with acoustic shadowing located within the lower collecting system. Renal vascular perfusion intact.",
                    "conclusion_zh": "左肾结石 (0.5cm)",
                    "conclusion_en": "Left nephrolithiasis (0.5 cm solitary calculus)",
                    "status": "attention"
                },
                {
                    "organ_zh": "右肾、输尿管、膀胱",
                    "organ_en": "Right Kidney, Ureters & Urinary Bladder",
                    "findings_zh": "右侧肾脏大小正常，形态规则，包膜光整，实质回声均匀，皮髓质分界清晰，集合系统未见分离，CDFI示肾血流充盈良好。双侧输尿管未见扩张。膀胱充盈后扫查，壁光整，无异常回声。",
                    "findings_en": "Right kidney unremarkable with normal parenchyma and no pelvicalyceal dilatation. Bilateral ureters not dilated. Urinary bladder wall is smooth with clear anechoic lumen.",
                    "conclusion_zh": "右肾、双侧输尿管、膀胱未见明显异常",
                    "conclusion_en": "Normal right kidney, bilateral ureters, and urinary bladder",
                    "status": "normal"
                },
                {
                    "organ_zh": "前列腺",
                    "organ_en": "Prostate Gland",
                    "findings_zh": "前列腺大小正常，两侧叶对称，包膜光整，实质内回声不均匀，并可见高回声斑，未见占位性病变，彩色多普勒未见异常血流信号。",
                    "findings_en": "Prostate gland is normal in size and symmetric. Internal echotexture shows focal hyperechoic calcification plaques without suspicious nodular masses. Normal vascularity.",
                    "conclusion_zh": "前列腺钙化灶",
                    "conclusion_en": "Prostatic parenchymal calcifications",
                    "status": "normal"
                }
            ]
        },
        "radiology": {
            "chest_ct": {
                "title_zh": "胸部低剂量CT平扫",
                "title_en": "Low-Dose Chest CT (Non-Contrast)",
                "date": "2025-07-18 07:41",
                "doctor": "汪建新",
                "findings_zh": "肺窗显示两肺支气管血管束清晰，走向分布无异常。左肺下叶少许小钙化结节，直径约3-4mm，余肺实质未见明显渗出或实质性占位性病变。纵隔居中，无淋巴结肿大。附见：胆囊术后改变。",
                "findings_en": "Bronchovascular bundles in bilateral lung fields are clear with anatomical distribution. Left lower lung lobe exhibits small calcified nodules measuring 3-4 mm in diameter. No active consolidation, ground-glass opacity, or space-occupying mass. Incidental note: post-cholecystectomy surgical changes.",
                "conclusion_zh": "左肺下叶少许小钙化灶，请随诊对比。",
                "conclusion_en": "Small calcified nodules in left lower lobe, benign sequelae; routine follow-up recommended."
            },
            "cervical_cr": {
                "title_zh": "颈椎侧位普放CR片",
                "title_en": "Cervical Spine Radiography (Lateral View)",
                "date": "2025-07-18 08:35",
                "doctor": "钱微",
                "findings_zh": "颈椎生理性曲度变直。颈椎前、后缘骨质增生（唇样骨赘）。椎体附件未见明显异常。椎间隙未见明显狭窄。",
                "findings_en": "Straightening of normal cervical lordosis. Hypertrophic osteophyte formation along anterior and posterior vertebral margins. Posterior elements intact. Intervertebral disc space heights are reasonably maintained.",
                "conclusion_zh": "颈椎退行性改变 (颈椎病)",
                "conclusion_en": "Cervical spine degenerative changes (cervical spondylosis)."
            }
        },
        "specialties": {
            "internal_medicine": {
                "title_zh": "内科常规",
                "history_zh": "高血压病（治疗中）；高脂血症（治疗中）；无烟酒嗜好；已接种新冠病毒疫苗；体质健，营养状况佳；心脏心律规整，未及病理性杂音；双肺呼吸音清；腹部平软，未及包块，肝脾肋下未触及。",
                "history_en": "Hypertension (treated); Hyperlipidemia (treated); No history of tobacco or alcohol use; Fully COVID vaccinated; General constitution fit, well nourished; Heart sounds regular without murmurs; Clear breath sounds; Abdomen soft, no tenderness or organomegaly."
            },
            "surgery": {
                "title_zh": "外科常规",
                "history_zh": "外科手术史：胆囊切除术后；甲状腺触诊无特殊；乳腺未见异常；肛门直肠指检：距肛缘4cm处未及明显异常；四肢关节活动良好；浅表淋巴结未及肿大。",
                "history_en": "Surgical history: status post cholecystectomy; Thyroid palpation normal; DRE unremarkable up to 4 cm; Peripheral joints full ROM; No lymphadenopathy."
            },
            "ophthalmology": {
                "title_zh": "眼科常规与眼底",
                "history_zh": "屈光不正；右眼视网膜激光术后；视力双眼矫正0.8；眼底：双眼豹纹状近视眼底，视网膜动脉细，中轴反光增强；裂隙灯：双眼晶状体密度增高。",
                "history_en": "Ametropia; Status post laser photocoagulation of right retina; Corrected visual acuity 0.8 (20/25) OU; Fundus: Bilateral tigroid myopic fundus, attenuated retinal arterioles with augmented central light reflex; Slit-lamp: Increased lens nuclear density."
            },
            "ent": {
                "title_zh": "耳鼻咽喉科",
                "history_zh": "既往史无特殊；初测听力正常；双耳鼓膜标志清楚；鼻腔黏膜正常，中隔无明显偏曲；咽部充血阴性，扁桃体无肿大；喉部未见明显异常。",
                "history_en": "ENT examination within normal limits. Hearing screening normal; Tympanic membranes intact; Nasal mucosa healthy; Pharynx/tonsils non-inflamed."
            },
            "stomatology": {
                "title_zh": "口腔科",
                "history_zh": "保健口腔内科：牙周组织无明显红肿萎缩，保持口腔卫生，建议定期口腔洁治与检查。",
                "history_en": "Preventive dentistry: Gingiva healthy, good dental hygiene; regular dental cleaning recommended."
            }
        }
    }
}

with open("/Users/eric/Dropbox/ai/physical/china_exam_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved china_exam_data.json successfully with", len(data["lab_sections"]), "lab sections and", len(data["findings_14"]), "findings.")
