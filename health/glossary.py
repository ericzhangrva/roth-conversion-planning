# Bilingual Medical Glossary for all 53 Lab Tests

TEST_GLOSSARY = {
    "WBC": {
        "name_en": "White Blood Cell Count",
        "name_zh": "白细胞计数",
        "desc_en": "Measures the total number of immune defense cells in your blood responsible for fighting infections, inflammation, and diseases.",
        "desc_zh": "血液中免疫细胞的总数，负责抵抗外界细菌、病毒感染，防御疾病及炎症反应。",
        "significance_en": "High (Leukocytosis): May indicate active bacterial/viral infection, systemic inflammation, physical stress, or bone marrow activity. Low (Leukopenia): May indicate viral illness, autoimmune conditions, or bone marrow suppression.",
        "significance_zh": "升高：常见于细菌/病毒感染、体内急性炎症、应激反应等。偏低：常见于某些病毒感染、免疫力偏低或骨髓造血功能受抑。"
    },
    "RBC": {
        "name_en": "Red Blood Cell Count",
        "name_zh": "红细胞计数",
        "desc_en": "Counts the total circulating red blood cells that transport vital oxygen from your lungs to the rest of your body.",
        "desc_zh": "血液中红细胞的总数量，主要功能是将肺部吸入的氧气输送至全身各组织和器官。",
        "significance_en": "High: Can indicate dehydration, smoking, sleep apnea, or polycythemia. Low: Classic marker of anemia, nutritional deficiency, or blood loss.",
        "significance_zh": "升高：见于血液浓缩（脱水）、长期缺氧（吸烟、高原）、睡眠呼吸暂停或红细胞增多症。偏低：提示贫血、失血或造血原料缺乏。"
    },
    "HGB": {
        "name_en": "Hemoglobin",
        "name_zh": "血红蛋白",
        "desc_en": "The iron-rich protein inside red blood cells that directly binds and carries oxygen throughout your tissues.",
        "desc_zh": "红细胞内含铁的特殊蛋白质，是人体血液中直接结合并运送氧气和二氧化碳的载体。",
        "significance_en": "High: Common with dehydration, living at high altitudes, or excessive RBC production. Low: The defining clinical criterion for anemia, fatigue, and blood loss.",
        "significance_zh": "升高：见于脱水、长期高原生活或肺部疾病。偏低：贫血的核心临床指标，可导致组织缺氧、头晕乏力。"
    },
    "HCT": {
        "name_en": "Hematocrit",
        "name_zh": "红细胞压积 / 比容",
        "desc_en": "The percentage of total blood volume made up of red blood cells. Reflects blood thickness and hydration status.",
        "desc_zh": "红细胞在全血中所占的容积百分比，反映血液粘稠度及身体水合（水分）状态。",
        "significance_en": "High: Often elevated with mild dehydration, smoking, or testosterone therapy. Low: Indicates overhydration, anemia, or blood loss.",
        "significance_zh": "升高：多见于饮水不足导致血液浓缩、吸烟、睡眠呼吸暂停或睾酮使用。偏低：见于贫血或体液潴留。"
    },
    "MCV": {
        "name_en": "Mean Corpuscular Volume",
        "name_zh": "平均红细胞体积",
        "desc_en": "Measures the average physical size of individual red blood cells.",
        "desc_zh": "单个红细胞的平均物理体积大小，用于区分不同类型的贫血。",
        "significance_en": "High (Macrocytic): Often caused by Vitamin B12 or folate deficiency, alcohol intake, or thyroid issues. Low (Microcytic): Classic for iron deficiency anemia or thalassemia trait.",
        "significance_zh": "偏大（大细胞性）：常与维生素B12/叶酸缺乏、饮酒或甲减有关。偏小（小细胞性）：常提示缺铁性贫血或地中海贫血特征。"
    },
    "MCH": {
        "name_en": "Mean Corpuscular Hemoglobin",
        "name_zh": "平均红细胞血红蛋白量",
        "desc_en": "Calculates the average weight of hemoglobin contained inside a single red blood cell.",
        "desc_zh": "每个红细胞内所含血红蛋白的平均重量。",
        "significance_en": "Tracks closely with MCV. Low in iron-deficiency anemia; high in macrocytic anemias (B12 deficiency).",
        "significance_zh": "通常与MCV变化平行。偏低提示缺铁性贫血；偏高提示巨幼细胞性贫血（如B12缺乏）。"
    },
    "MCHC": {
        "name_en": "Mean Corpuscular Hemoglobin Concentration",
        "name_zh": "平均红细胞血红蛋白浓度",
        "desc_en": "Measures the average concentration of hemoglobin packed inside a given volume of red blood cells.",
        "desc_zh": "单位容积红细胞内所含血红蛋白的平均浓度，反映红细胞内血红蛋白充盈度。",
        "significance_en": "Low indicates hypochromic anemia (pale cells due to iron deficiency). High is rare, seen in spherocytosis or cold agglutinins.",
        "significance_zh": "偏低提示低色素性贫血（缺铁导致细胞着色浅淡）；偏高较少见，见于球形红细胞增多症等。"
    },
    "RDW": {
        "name_en": "Red Cell Distribution Width",
        "name_zh": "红细胞体积分布宽度",
        "desc_en": "Measures the variation in size among red blood cells (anisocytosis). Healthy cells should all be roughly the same size.",
        "desc_zh": "反映血液中红细胞大小不均一程度的指标。正常红细胞大小相对均匀。",
        "significance_en": "High: Early sensitive sign of developing iron, B12, or folate deficiency before hemoglobin noticeably drops.",
        "significance_zh": "升高：提示红细胞大小差异显著，常是早期缺铁、叶酸或B12缺乏的敏感信号。"
    },
    "PLT": {
        "name_en": "Platelet Count",
        "name_zh": "血小板计数",
        "desc_en": "Measures small cell fragments essential for blood clotting and stopping bleeding when blood vessels are damaged.",
        "desc_zh": "血液中参与止血与凝血功能的重要细胞成分，血管破损时聚集形成血栓止血。",
        "significance_en": "High (Thrombocytosis): Inflammatory conditions, infection, iron deficiency, or marrow issues. Low (Thrombocytopenia): Viral illness, autoimmune destruction, liver disease, or medication effect.",
        "significance_zh": "升高：见于炎症感染应激、缺铁或骨髓增殖。偏低：见于病毒感染、自身免疫、药物影响或肝功能受损，过低增加出血风险。"
    },
    "MPV": {
        "name_en": "Mean Platelet Volume",
        "name_zh": "平均血小板体积",
        "desc_en": "Measures the average size of platelets. Newer, recently released platelets from bone marrow are larger.",
        "desc_zh": "单个血小板的平均体积大小。骨髓刚新生成释放的年轻血小板体积通常偏大。",
        "significance_en": "High indicates active platelet turnover and regeneration in bone marrow. Low may reflect reduced production.",
        "significance_zh": "偏大提示骨髓生成血小板活跃、更新加快；偏小提示骨髓造血功能受抑制。"
    },
    "LYM": {
        "name_en": "Lymphocytes (Absolute)",
        "name_zh": "淋巴细胞绝对值",
        "desc_en": "The absolute count of white blood cells (B cells, T cells, NK cells) that produce antibodies and fight viral infections.",
        "desc_zh": "免疫系统中核心的白细胞类别（包括B细胞、T细胞），主要负责病毒防御和抗体生成。",
        "significance_en": "High: Often elevated in response to viral infections. Low: Can occur after stress, steroid use, or immune exhaustion.",
        "significance_zh": "升高：常见于急慢性病毒感染或恢复期。偏低：常见于急性应激、免疫功能低下或皮质类固醇药物影响。"
    },
    "LYM%": {
        "name_en": "Lymphocyte Percentage",
        "name_zh": "淋巴细胞百分比",
        "desc_en": "The proportion of total white blood cells comprised of lymphocytes.",
        "desc_zh": "淋巴细胞占血液白细胞总数的百分比。",
        "significance_en": "Interpreted alongside the absolute count; shifts indicate whether the immune system is leaning toward viral or bacterial defense.",
        "significance_zh": "需结合白细胞绝对值分析，比例偏高多见于病毒感染，比例偏低常因中性粒细胞增多引起。"
    },
    "MID": {
        "name_en": "Mid-Range WBC Count (Monocytes / Eosinophils / Basophils)",
        "name_zh": "中间细胞绝对值 (单核/嗜酸/嗜碱)",
        "desc_en": "Combined count of monocytes (macrophages), eosinophils (allergy/parasite defense), and basophils.",
        "desc_zh": "单核细胞、嗜酸性粒细胞及嗜碱性粒细胞的统称，主要参与抗过敏、抗寄生虫及清理组织碎屑。",
        "significance_en": "Mild elevations are common in allergic reactions, asthma, skin conditions, or resolving infections.",
        "significance_zh": "轻微升高多见于过敏反应、鼻炎过敏、皮肤湿疹或感染恢复期清除病原。"
    },
    "MID%": {
        "name_en": "Mid-Range WBC Percentage",
        "name_zh": "中间细胞百分比",
        "desc_en": "The percentage of circulating white blood cells categorized as monocytes, eosinophils, or basophils.",
        "desc_zh": "中间细胞群在白细胞总数中所占的百分比。",
        "significance_en": "Evaluated alongside MID absolute count to assess allergic or inflammatory immune activity.",
        "significance_zh": "结合绝对值评估体内是否存在过敏反应或慢性炎性反应。"
    },
    "GRAN": {
        "name_en": "Granulocytes / Neutrophils (Absolute)",
        "name_zh": "粒细胞 / 中性粒细胞绝对值",
        "desc_en": "The body's primary first-responder white blood cells specialized in engulfing and destroying bacteria.",
        "desc_zh": "白细胞中数量最多的一类，人体对抗细菌感染的第一道防线主力军。",
        "significance_en": "High: Hallmark of acute bacterial infections, physical trauma, or acute inflammation. Low: Increases vulnerability to bacterial infection.",
        "significance_zh": "升高：急性细菌感染、创伤、手术或机体炎症的最经典标志。偏低：易导致抵抗力下降，增加细菌感染风险。"
    },
    "GRAN%": {
        "name_en": "Granulocyte Percentage",
        "name_zh": "粒细胞百分比",
        "desc_en": "The percentage of white blood cells made up of granulocytes (primarily neutrophils).",
        "desc_zh": "粒细胞（主要为中性粒细胞）占所有白细胞总数的百分比。",
        "significance_en": "Higher percentages signal acute bacterial infection or active inflammation in the body.",
        "significance_zh": "比例升高提示体内可能存在急性细菌感染或明显炎性反应。"
    },
    "Glucose": {
        "name_en": "Fasting Blood Glucose",
        "name_zh": "空腹血糖",
        "desc_en": "Measures the level of sugar (glucose) in your bloodstream after an overnight fast; the primary source of cellular energy.",
        "desc_zh": "禁食8小时后血液中的葡萄糖浓度，是人体细胞能量的主要来源及糖尿病筛查核心指标。",
        "significance_en": "High (>100): Indicates prediabetes or diabetes; elevated cardiovascular risk. Low (<65): Hypoglycemia, causing shakiness, dizziness, or weakness.",
        "significance_zh": "升高（>100 mg/dL）：提示空腹血糖受损或糖尿病风险；偏低（<65 mg/dL）：低血糖，可伴出汗、心悸、乏力。"
    },
    "BUN": {
        "name_en": "Blood Urea Nitrogen",
        "name_zh": "血尿素氮",
        "desc_en": "Waste product formed in the liver from dietary protein breakdown, normally filtered out by the kidneys.",
        "desc_zh": "体内蛋白质分解代谢产生的含氮终末产物，主要由肾小球过滤排出体外。",
        "significance_en": "High: Can be caused by mild dehydration, high-protein diet, strenuous exercise, or decreased kidney filtration. Low: Rare, seen in low-protein intake or liver disease.",
        "significance_zh": "升高：常见于饮水不足（轻度脱水）、高蛋白饮食、剧烈运动或肾功能下降。偏低：多见于低蛋白饮食或营养吸收不良。"
    },
    "Creatinine": {
        "name_en": "Serum Creatinine",
        "name_zh": "血清肌酐",
        "desc_en": "A byproduct of normal muscle breakdown that healthy kidneys continuously filter out at a steady, predictable rate.",
        "desc_zh": "肌肉代谢产生的废物，几乎完全由肾脏滤过排泄，是评估肾脏滤过功能的稳定基石指标。",
        "significance_en": "High: Signals reduced kidney filtration, dehydration, or very high muscle mass / creatine supplement use. Low: Reduced muscle mass.",
        "significance_zh": "升高：提示肾小球滤过功能减退、严重脱水或肌肉含量极高/服用肌酸补充剂。偏低：肌肉量偏少或恶液质。"
    },
    "eGFR Non-African Amer.": {
        "name_en": "Estimated Glomerular Filtration Rate (Non-African American)",
        "name_zh": "估算肾小球滤过率 (非非裔标准)",
        "desc_en": "The primary clinical calculation estimating how efficiently your kidneys filter waste from your blood each minute.",
        "desc_zh": "根据血肌酐、年龄和性别计算得出的肾脏每分钟滤过血液废物的效率，评估肾功能最核心指标。",
        "significance_en": "Values >60 are considered normal kidney function. Levels <60 over 3 months may indicate chronic kidney disease.",
        "significance_zh": ">60 mL/min/1.73m²为正常范围。持续<60提示慢性肾功能减退，数值越高代表肾脏滤过储备越充分。"
    },
    "eGFR African Amer.": {
        "name_en": "Estimated Glomerular Filtration Rate (African American)",
        "name_zh": "估算肾小球滤过率 (非裔标准)",
        "desc_en": "Historical equation adjustment factoring for average demographic muscle mass differences.",
        "desc_zh": "既往医学算法中针对不同种族肌肉平均质量差异进行的计算调整（临床现已逐渐统一）。",
        "significance_en": "Values >60 indicate normal kidney function.",
        "significance_zh": ">60为正常肾脏滤过功能。"
    },
    "Sodium": {
        "name_en": "Serum Sodium",
        "name_zh": "血清钠 (Na+)",
        "desc_en": "The major extracellular electrolyte that regulates water balance, blood pressure, and normal nerve and muscle function.",
        "desc_zh": "细胞外液中最重要的阳离子，调节体内水分平衡、渗透压、血压及神经肌肉电信号传导。",
        "significance_en": "High (Hypernatremia): Dehydration, excessive sodium intake. Low (Hyponatremia): Excessive fluid retention, diuretic medications, or hormonal imbalances.",
        "significance_zh": "升高：水分摄入过少（高渗性脱水）或钠摄入过多。偏低：稀释性低钠、水潴留、利尿剂影响或剧烈运动后大量出汗。"
    },
    "Potassium": {
        "name_en": "Serum Potassium",
        "name_zh": "血清钾 (K+)",
        "desc_en": "The primary intracellular electrolyte critical for heart rhythm, electrical conduction, and muscle contraction.",
        "desc_zh": "细胞内液最重要的阳离子，对维持心脏正常节律、心肌电生理稳定及神经传导至关重要。",
        "significance_en": "Tightly regulated. High (Hyperkalemia) or Low (Hypokalemia) can provoke dangerous cardiac arrhythmias and muscle cramping.",
        "significance_zh": "正常范围极严格。过高（高钾血症）或过低（低钾血症）均可诱发严重心律失常或肌肉痉挛无力。"
    },
    "Chloride": {
        "name_en": "Serum Chloride",
        "name_zh": "血清氯 (Cl-)",
        "desc_en": "Works hand-in-hand with sodium and potassium to maintain proper cellular fluid balance and stomach acid (HCl).",
        "desc_zh": "细胞外液中最主要的阴离子，与钠离子共同维持机体水和酸碱平衡及胃酸生成。",
        "significance_en": "High: Associated with dehydration, kidney dysfunction, or metabolic acidosis. Low: Severe vomiting, diuretic use, or overhydration.",
        "significance_zh": "升高：伴随脱水、高钠或酸碱代谢失衡。偏低：见于剧烈呕吐丢失胃酸或体液过多。"
    },
    "CO2": {
        "name_en": "Carbon Dioxide / Bicarbonate",
        "name_zh": "二氧化碳结合力 (碳酸氢根)",
        "desc_en": "Measures bicarbonate in blood; an essential indicator of acid-base (pH) balance maintained by kidneys and lungs.",
        "desc_zh": "反映血液中重碳酸根（HCO3-）离子的缓冲能力，是机体酸碱（pH）平衡的重要晴雨表。",
        "significance_en": "High: Metabolic alkalosis, breathing shallowly, or chronic lung conditions. Low: Metabolic acidosis, kidney disease, or dehydration.",
        "significance_zh": "升高：代谢性碱中毒、低钾或慢性呼吸性酸中毒。偏低：代谢性酸中毒、肾功能不全或脱水。"
    },
    "Calcium": {
        "name_en": "Serum Calcium",
        "name_zh": "血清钙 (Ca2+)",
        "desc_en": "Essential mineral required for bone and tooth strength, muscle contractions, heart beat regulation, and blood clotting.",
        "desc_zh": "人体骨骼牙齿强健不可或缺的矿物质，同时在心肌收缩、神经冲动传递和血液凝固中起核心作用。",
        "significance_en": "High: Parathyroid issues, excess Vitamin D, or bone turnover. Low: Vitamin D deficiency, malabsorption, or low albumin levels.",
        "significance_zh": "升高：甲状旁腺功能亢进、过量维生素D补充。偏低：维生素D不足、肠道吸收不良或血白蛋白水平偏低。"
    },
    "Total Protein": {
        "name_en": "Total Serum Protein",
        "name_zh": "血清总蛋白",
        "desc_en": "Measures total circulating proteins (albumin and globulins) reflecting nutrition, liver production, and immune health.",
        "desc_zh": "血液中白蛋白和球蛋白的总和，直观反映肝脏合成能力、营养状态及免疫水平。",
        "significance_en": "High: Dehydration, chronic inflammation, or bone marrow disorders. Low: Malnutrition, severe liver disease, or kidney protein leakage.",
        "significance_zh": "升高：血液浓缩脱水、慢性炎性反应或免疫球蛋白增多。偏低：营养不良、慢性肝病或肾病漏出蛋白。"
    },
    "Albumin": {
        "name_en": "Serum Albumin",
        "name_zh": "血清白蛋白",
        "desc_en": "The main protein synthesized by the liver; keeps fluid from leaking out of blood vessels (oncotic pressure) and carries hormones.",
        "desc_zh": "由肝脏合成的最主要蛋白质，维持血管内胶体渗透压防止水肿，并运载激素、药物等物质。",
        "significance_en": "High: Almost always dehydration. Low: Liver impairment, chronic kidney disease, intestinal malabsorption, or systemic inflammation.",
        "significance_zh": "升高：几乎均为体内缺水血液浓缩所致。偏低：提示肝脏合成减退、肾小球漏蛋白或肠胃营养吸收不良。"
    },
    "Total Bili": {
        "name_en": "Total Bilirubin",
        "name_zh": "总胆红素",
        "desc_en": "Orange-yellow pigment formed during normal breakdown of old red blood cells, processed and excreted by the liver.",
        "desc_zh": "衰老红细胞中血红素分解后的代谢产物，需经肝脏转化处理并通过胆道排入肠道。",
        "significance_en": "High: Liver inflammation/damage, gallbladder/bile duct obstruction, or increased red blood cell destruction (hemolysis).",
        "significance_zh": "升高：提示肝细胞受损（肝炎）、胆管阻塞（结石/息肉）或溶血性红细胞破坏过多，严重可表现为黄疸。"
    },
    "Alk Phosphatase": {
        "name_en": "Alkaline Phosphatase (ALP)",
        "name_zh": "碱性磷酸酶",
        "desc_en": "Enzyme found predominantly in the cells lining biliary ducts of the liver and in actively growing bones.",
        "desc_zh": "广泛分布于肝脏胆管上皮细胞及骨骼中的活性酶，是肝胆系统排泄与骨代谢的重要酶学指标。",
        "significance_en": "High: Gallbladder/bile duct blockage, liver disease, or rapid bone healing/growth. Low: Rare, nutritional deficiencies.",
        "significance_zh": "升高：常见于胆管排泄不畅、胆结石、肝炎或骨骼快速修复生长。偏低：见于营养严重缺乏或甲状腺功能减退。"
    },
    "AST (SGOT)": {
        "name_en": "Aspartate Aminotransferase",
        "name_zh": "谷草转氨酶 (AST)",
        "desc_en": "Enzyme concentrated in liver cells, heart muscle, skeletal muscle, and kidneys. Released into blood when tissue is injured.",
        "desc_zh": "存在于肝细胞线粒体及心肌、骨骼肌中的重要转氨酶，组织细胞受损时释放进入血液。",
        "significance_en": "High: Liver damage (fatty liver, hepatitis, alcohol, medications) or intense muscular strain/injury.",
        "significance_zh": "升高：提示肝脏细胞损伤（脂肪肝、酒精性肝损伤、药物影响）或剧烈肌肉运动与损伤。"
    },
    "ALT (SGPT)": {
        "name_en": "Alanine Aminotransferase",
        "name_zh": "谷丙转氨酶 (ALT)",
        "desc_en": "The most liver-specific enzyme. Elevated levels directly signal liver cell irritation or injury.",
        "desc_zh": "最具有肝脏特异性的酶，主要存在于肝细胞浆中，是监测肝脏炎性反应和损伤的最灵敏指标。",
        "significance_en": "High: Liver stress, non-alcoholic fatty liver disease (NAFLD), viral hepatitis, alcohol use, or medication toxicity.",
        "significance_zh": "升高：直接反映肝实质细胞炎症、脂肪肝浸润、饮酒、药物性肝损伤或病毒感染。"
    },
    "Cholesterol": {
        "name_en": "Total Cholesterol",
        "name_zh": "总胆固醇",
        "desc_en": "The total amount of cholesterol circulating in your bloodstream, combining HDL, LDL, and VLDL particles.",
        "desc_zh": "血液中所有脂蛋白所含胆固醇的总和，包括高密度、低密度和极低密度脂蛋白胆固醇。",
        "significance_en": "High (>200): Contributes to arterial plaque accumulation (atherosclerosis) and coronary heart disease risk.",
        "significance_zh": "升高（>200 mg/dL）：长期过高可加速动脉血管粥样硬化斑块形成，增加心脑血管病风险。"
    },
    "Triglycerides": {
        "name_en": "Triglycerides",
        "name_zh": "甘油三酯",
        "desc_en": "The most common form of stored fat in the body, derived from dietary fats and excess refined carbohydrates/calories.",
        "desc_zh": "人体内最主要的脂肪储存形式，由饮食摄入及多余的碳水化合物/糖分在肝脏合成转化而来。",
        "significance_en": "High (>150): Linked to insulin resistance, metabolic syndrome, fatty liver, and cardiovascular risk. Very high (>500) risks pancreatitis.",
        "significance_zh": "升高（>150 mg/dL）：与胰岛素抵抗、脂肪肝、代谢综合征及心血管疾病高度相关；极端过高可诱发胰腺炎。"
    },
    "Direct HDL": {
        "name_en": "High-Density Lipoprotein ('Good' Cholesterol)",
        "name_zh": "高密度脂蛋白胆固醇 ('好'胆固醇)",
        "desc_en": "Scavenger lipoprotein that collects excess cholesterol from peripheral arteries and transports it back to the liver for excretion.",
        "desc_zh": "被誉为血管'清道夫'，负责将血管壁和组织中多余的胆固醇运回肝脏代谢清除，具有抗动脉硬化作用。",
        "significance_en": "Higher is protective (>40 in men, >50 in women). Low levels (<40) represent an independent cardiovascular risk factor.",
        "significance_zh": "数值高具有心血管保护意义；偏低（<40 mg/dL）是心血管疾病与动脉硬化的独立危险因素。"
    },
    "LDL-Calculated": {
        "name_en": "Low-Density Lipoprotein ('Bad' Cholesterol - Calculated)",
        "name_zh": "低密度脂蛋白胆固醇 (计算值 / '坏'胆固醇)",
        "desc_en": "Primary cholesterol carrier that deposits excess lipid particles directly into arterial walls, driving plaque formation.",
        "desc_zh": "血液中运送胆固醇进入组织细胞的主要载体，过量时沉积于动脉血管壁形成粥样斑块的主因。",
        "significance_en": "Lower is better. Optimal is <100 mg/dL (<70 for high-risk cardiac patients). Elevated levels raise heart attack and stroke risk.",
        "significance_zh": "心血管防治的核心目标：越低越安全。正常理想<100 mg/dL；过高显著增加冠心病与中风风险。"
    },
    "LDL-Direct": {
        "name_en": "Direct Low-Density Lipoprotein",
        "name_zh": "直接测定低密度脂蛋白",
        "desc_en": "Directly measured laboratory assay of LDL particles, especially accurate when triglycerides are unusually high.",
        "desc_zh": "直接通过生化试剂物理测定的低密度脂蛋白水平，不受甘油三酯波动影响，比间接计算公式更精准。",
        "significance_en": "Used to confirm cardiovascular risk targets when calculated LDL may be inaccurate due to high triglycerides.",
        "significance_zh": "用于更精准评估动脉粥样硬化风险，尤其适用于血脂复杂的患者。"
    },
    "_VLDL": {
        "name_en": "Very Low-Density Lipoprotein (Calculated)",
        "name_zh": "极低密度脂蛋白 (VLDL)",
        "desc_en": "Lipoprotein made by the liver containing predominantly triglycerides, converting over time into atherogenic LDL.",
        "desc_zh": "主要由肝脏合成的大颗粒脂蛋白，富含大量甘油三酯，在血液循环中逐步代谢转化为致动脉硬化的LDL。",
        "significance_en": "Elevated with high triglyceride intake, alcohol consumption, insulin resistance, and visceral abdominal fat.",
        "significance_zh": "与甘油三酯水平高度相关，升高提示内脏脂肪代谢紊乱及胰岛素抵抗。"
    },
    "Chol/HDL Ratio": {
        "name_en": "Total Cholesterol to HDL Ratio",
        "name_zh": "总胆固醇 / 高密度脂蛋白比值",
        "desc_en": "A composite cardiovascular risk marker calculated by dividing Total Cholesterol by protective HDL.",
        "desc_zh": "总胆固醇除以'好'胆固醇的比率，综合评估动脉粥样硬化相对风险强度的经典复合指标。",
        "significance_en": "Lower is better. Optimal is <3.5; average risk is 3.5–5.0; >5.0 indicates significantly elevated cardiovascular hazard.",
        "significance_zh": "比值越低越安全。理想值<3.5；3.5–5.0为一般风险；>5.0提示心血管疾病风险明显上升。"
    },
    "uTSH": {
        "name_en": "Ultrasensitive Thyroid Stimulating Hormone",
        "name_zh": "超敏促甲状腺素 (uTSH)",
        "desc_en": "Pituitary hormone that signals the thyroid gland to produce thyroid hormones; the master metabolic speed regulator.",
        "desc_zh": "脑下垂体分泌的调控激素，调节甲状腺素合成与释放，是监控人体基础代谢率最灵敏的晴雨表。",
        "significance_en": "High: Indicates an underactive thyroid (hypothyroidism / sluggish metabolism). Low: Signals an overactive thyroid (hyperthyroidism).",
        "significance_zh": "升高：提示甲状腺功能减退（甲减，代谢变慢、畏寒易倦）。偏低：提示甲状腺功能亢进（甲亢，心悸消瘦）。"
    },
    "Free Thyroxine": {
        "name_en": "Free Thyroxine (Free T4)",
        "name_zh": "游离甲状腺素 (Free T4)",
        "desc_en": "The active, unbound thyroid hormone circulating in the blood directly responsible for controlling cellular metabolism.",
        "desc_zh": "血液中未与蛋白质结合的活性甲状腺素，直接进入细胞发挥调控机体能量代谢的核心功能。",
        "significance_en": "Interpreted alongside TSH. Low with elevated TSH confirms primary hypothyroidism; high confirms hyperthyroidism.",
        "significance_zh": "与TSH结合分析。低T4伴高TSH明确诊断为原发性甲减；高T4伴低TSH提示甲状腺功能亢进。"
    },
    "Testosterone": {
        "name_en": "Total Serum Testosterone",
        "name_zh": "总睾酮",
        "desc_en": "The primary male androgen hormone responsible for muscle mass, bone density, libido, mood, energy, and vitality.",
        "desc_zh": "男性体内最重要的雄性激素，维系肌肉力量、骨骼健康、性欲精力、情绪专注力及活力代谢。",
        "significance_en": "Low (<300 ng/dL): Hypogonadism, causing fatigue, muscle loss, brain fog, depressive symptoms, and lower libido.",
        "significance_zh": "偏低（<300 ng/dL）：雄激素不足，可引起精力疲倦、肌肉萎缩、性欲减退、情绪低落及代谢变差。"
    },
    "Free Testosterone(Direct)": {
        "name_en": "Free Bioavailable Testosterone (Direct)",
        "name_zh": "游离睾酮 (直接测定)",
        "desc_en": "The active fraction of testosterone (~1-2%) not bound to SHBG proteins, freely available to enter cells and activate receptors.",
        "desc_zh": "血液中未与性激素结合球蛋白结合的游离活性部分（约占总睾酮1-2%），能直接进入组织发挥生物学效应。",
        "significance_en": "Often provides a more accurate reflection of symptomatic androgen status than Total Testosterone when binding proteins fluctuate.",
        "significance_zh": "当结合蛋白水平波动时，游离睾酮能更真实地反映身体实际可利用的雄性激素活性水平。"
    },
    "Prolactin": {
        "name_en": "Serum Prolactin",
        "name_zh": "血清泌乳素 (催乳素)",
        "desc_en": "Hormone produced by the pituitary gland. In men, elevated levels can suppress testosterone production and blunt libido.",
        "desc_zh": "脑下垂体前叶分泌的激素。男性体内泌乳素异常升高会抑制垂体促性腺激素，进而引起睾酮降低及性欲减退。",
        "significance_en": "High: Can be triggered by chronic stress, medications (antidepressants/antacids), or pituitary microadenomas.",
        "significance_zh": "升高：常见于慢性应激疲劳、特定药物影响或脑垂体微腺瘤，可引起睾酮低下及性功能减退。"
    },
    "PSA": {
        "name_en": "Prostate-Specific Antigen",
        "name_zh": "前列腺特异性抗原",
        "desc_en": "Protein produced exclusively by prostate gland cells; the gold-standard screening benchmark for prostate health.",
        "desc_zh": "由前列腺上皮细胞特异性分泌的糖蛋白，是全球公认的前列腺健康筛查与病变监测的金标准。",
        "significance_en": "Levels <4.0 ng/mL are reassuring. Elevated levels can reflect benign enlargement (BPH), prostatitis/inflammation, or prostate cancer.",
        "significance_zh": "<4.0 ng/mL为正常安全范围。明显升高常提示良性前列腺增生（BPH）、前列腺炎或早期肿瘤病变风险。"
    },
    "Vitamin D, 25-Hydroxy": {
        "name_en": "25-Hydroxy Vitamin D (Total)",
        "name_zh": "25-羟基维生素D (总)",
        "desc_en": "The circulating storage form of Vitamin D; essential for calcium absorption, bone strength, immunity, and hormone synthesis.",
        "desc_zh": "维生素D在人体血液循环中的主要储存形式，对促进钙吸收、维持骨密度、调节免疫防病及激素平衡至关重要。",
        "significance_en": "Deficient (<20 ng/mL) or Insufficient (20–30 ng/mL): Associated with bone thinning, muscle weakness, and impaired immunity. Optimal: 30–60 ng/mL.",
        "significance_zh": "缺乏（<20 ng/mL）或不足（20-30 ng/mL）：导致骨量流失、肌肉酸痛及免疫力下降。理想健康水平：30-60 ng/mL。"
    },
    "HgbA1c": {
        "name_en": "Hemoglobin A1c (Glycated Hemoglobin)",
        "name_zh": "糖化血红蛋白 (HbA1c)",
        "desc_en": "Measures the percentage of hemoglobin coated with glucose; reflects average blood sugar control over the preceding 2–3 months.",
        "desc_zh": "血糖与血红蛋白结合的产物，不受单日饮食波动影响，真实反映过去2至3个月的平均血糖控制水平。",
        "significance_en": "Normal: <5.7%. Prediabetes: 5.7%–6.4%. Diabetes: ≥6.5%. Gold-standard benchmark for long-term metabolic health.",
        "significance_zh": "正常标准：<5.7%；糖尿病前期：5.7%-6.4%；糖尿病诊断：≥6.5%。长期代谢与防病健康管理的核心金标准。"
    },
    "Magnesium": {
        "name_en": "Serum Magnesium",
        "name_zh": "血清镁",
        "desc_en": "Vital intracellular cofactor for over 300 biochemical enzymes governing muscle contraction, nerve function, and heart rhythm.",
        "desc_zh": "人体内300余种关键生物酶的必需辅助因子，深刻影响肌肉收缩舒张、神经信号平衡及心律规整。",
        "significance_en": "Low: Can cause muscle cramps, eye twitches, cardiac palpitations, fatigue, and poor sleep quality.",
        "significance_zh": "偏低：易引发肌肉抽筋、眼皮跳动、心慌心悸、慢性疲劳及入睡困难。"
    },
    "Sed Rate": {
        "name_en": "Erythrocyte Sedimentation Rate (ESR)",
        "name_zh": "红细胞沉降率 (血沉)",
        "desc_en": "Measures how quickly red blood cells settle to the bottom of a test tube over time; a classic non-specific marker of systemic inflammation.",
        "desc_zh": "红细胞在特定时间内沉降的速率，是评估体内是否存在急慢性感染、自身免疫病或全身炎性反应的经典指标。",
        "significance_en": "High indicates active inflammation, infection, autoimmune flares, or tissue healing in the body.",
        "significance_zh": "加快升高提示体内处于活动性炎性反应状态、风湿自身免疫疾病发作或组织损伤修复期。"
    },
    "SARS-CoV-2 Spike Ab Dilution": {
        "name_en": "COVID-19 Spike Antibody Titer Dilution",
        "name_zh": "新冠刺突蛋白抗体滴度",
        "desc_en": "Quantitative numerical measurement of circulating antibodies binding the SARS-CoV-2 spike protein from vaccination or natural exposure.",
        "desc_zh": "通过血清稀释法定量测定机体由接种新冠疫苗或自然感染后产生的针对刺突蛋白（S蛋白）的保护性抗体滴度水平。",
        "significance_en": "High titers confirm a strong humoral immune response and antibody memory against the SARS-CoV-2 virus.",
        "significance_zh": "高滴度数值证实机体存在强效体液免疫保护屏障和抗体记忆。"
    },
    "SARS-CoV-2 Spike Ab Interp": {
        "name_en": "COVID-19 Antibody Interpretation",
        "name_zh": "新冠抗体定性判定",
        "desc_en": "Qualitative clinical diagnosis confirming whether SARS-CoV-2 antibodies are present (Positive) or absent (Negative).",
        "desc_zh": "实验室对新冠病毒特异性抗体检测结果给出的临床定性判断（阳性 Positive 或 阴性 Negative）。",
        "significance_en": "Positive confirms immunologic memory and antibodies from prior COVID-19 vaccination or infection.",
        "significance_zh": "阳性证实机体对新冠病毒具备既往免疫识别与保护性抗体。"
    },
    "SARS-CoV-2 Semi-Quant Spike Ab": {
        "name_en": "COVID-19 Semi-Quantitative Spike Antibody",
        "name_zh": "新冠半定量刺突抗体",
        "desc_en": "Immunoassay measuring antibody levels targeting the receptor-binding domain (RBD) of the SARS-CoV-2 virus.",
        "desc_zh": "通过化学发光免疫法检测针对新冠病毒受体结合区（RBD）的抗体水平。",
        "significance_en": "Refers to the numeric dilution score for specific antibody titer strength.",
        "significance_zh": "结合具体稀释度滴度评估抗体防护水平强度。"
    },
    "SARS-CoV-2 Semi-Quant Total Ab": {
        "name_en": "COVID-19 Semi-Quantitative Total Antibody",
        "name_zh": "新冠半定量总抗体",
        "desc_en": "Measures total circulating immunoglobulin antibodies (IgG, IgM, IgA) directed against the SARS-CoV-2 virus.",
        "desc_zh": "检测体内针对新冠病毒所产生的全谱系结合抗体总量（包含IgG、IgM等多类免疫球蛋白）。",
        "significance_en": "Demonstrates total immunologic recognition and response to SARS-CoV-2.",
        "significance_zh": "反映机体对新冠抗原的整体体液免疫应答状态。"
    }
}
