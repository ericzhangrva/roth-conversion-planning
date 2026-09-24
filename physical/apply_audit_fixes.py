import json

with open("/Users/eric/Dropbox/ai/physical/china_exam_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 1. ECG Doctor
data["specialized_diagnostics"]["ecg"]["doctor"] = "沈军军"
data["specialized_diagnostics"]["ecg"]["auditor"] = "沈军军 医师 (审核并签名)"

# 2. Chest CT Doctor and Verbatim Findings
data["specialized_diagnostics"]["radiology"]["chest_ct"]["doctor"] = "周佳萍"
data["specialized_diagnostics"]["radiology"]["chest_ct"]["findings_zh"] = (
    "肺窗显示两肺支气管血管束清晰，走向分布无异常，左肺下叶少许小钙化结节，"
    "直径约3-4mm（注：医院原报告打印排版作'敬业3-4mm'），余肺实质未见明显渗出或实质性占位性病变。附见：胆囊术后改变。"
)
data["specialized_diagnostics"]["radiology"]["chest_ct"]["conclusion_zh"] = "左肺下叶少许小钙化灶，请随诊。"

# 3. Cervical Spine CR Verbatim
data["specialized_diagnostics"]["radiology"]["cervical_cr"]["doctor"] = "钱微"
data["specialized_diagnostics"]["radiology"]["cervical_cr"]["findings_zh"] = (
    "颈椎生理性曲度变直。颈椎前、后缘骨质增生。椎体附件未见明显异常。椎间隙未见明显狭窄。"
)
data["specialized_diagnostics"]["radiology"]["cervical_cr"]["conclusion_zh"] = "颈椎退行性改变。"

# 4. Ultrasound Verbatim exact alignment
us_organs = data["specialized_diagnostics"]["ultrasound"]["organs"]
for o in us_organs:
    if o["organ_zh"] == "双侧甲状腺":
        o["findings_zh"] = "甲状腺双侧叶大小、形态正常，包膜光整，实质回声不均匀，在甲状腺实质各见多个椭圆形低回声结节，右侧较大者约0.3cm，左侧较大者约0.5*0.2cm，边界及周边可辨，内部回声不均，CDFI示其内未见明显血流信号。彩色多普勒检查实质内血流未见异常。"
    elif o["organ_zh"] == "肝脏与门静脉":
        o["findings_zh"] = "肝脏大小正常，包膜光整，肝实质光点细密，回声增高，分布均匀，肝实质内未见明显占位性病变，肝实质后方回声衰减，肝内血管走行显示欠清，门静脉内径正常范围，内部透声好，CDFI显示血流充盈佳。"

with open("/Users/eric/Dropbox/ai/physical/china_exam_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Applied medical auditor fixes to china_exam_data.json!")
