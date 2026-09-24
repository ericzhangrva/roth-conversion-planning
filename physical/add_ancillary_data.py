import json

with open("/Users/eric/Dropbox/ai/physical/china_exam_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Add Hospital Warm Tips from Page 4
data["metadata"]["warm_tips_zh"] = [
    "体检结论仅根据本次所检项目结果所做，可能难以全面反映您的健康状况。",
    "您过去患的疾病，因这次体检范围所限未能发现到的情况，仍按原诊断及治疗。",
    "查出的疾病请及时到专科就诊治疗。",
    "若需复查相关异常体检指标，或有不明之处可来健康管理中心健康咨询门诊，我们将提供优质的健康保健指导。",
    "为了尊重和保护您的个人隐私，本保健中心在每一份体检报告上都粘有封口带，请您取到体检报告后确认封口带的完整性。",
    "放射科胶片实行自主打印，如您需要请体检当日起两个月内凭取件回单在放射科自助取片机上取片。"
]
data["metadata"]["warm_tips_en"] = [
    "The physical examination conclusions are based solely on the tests performed during this visit and may not reflect your overall health comprehensively.",
    "Previously diagnosed conditions not covered within the scope of this examination should continue to follow previous medical diagnoses and treatment plans.",
    "Please seek timely specialist consultation and treatment for any identified medical conditions or abnormalities.",
    "For repeat testing of abnormal indicators or general inquiries, please visit the Health Management Consultation Clinic.",
    "To protect your privacy, reports are sealed with security tape; please ensure the tape is intact upon receipt.",
    "Radiology films are available via self-service printing machines within two months using your receipt voucher."
]

# Add Vaccinations & Untested items
data["metadata"]["vaccinations"] = {
    "covid19_zh": "已接种",
    "covid19_en": "Vaccinated",
    "influenza_zh": "不确定",
    "influenza_en": "Uncertain",
    "pneumococcal_zh": "不确定",
    "pneumococcal_en": "Uncertain",
    "hepatitis_b_zh": "不确定",
    "hepatitis_b_en": "Uncertain"
}

data["metadata"]["untested_items"] = [
    {
        "name_zh": "人体成分检测 (体感诱发电位)",
        "name_en": "Body Composition Analysis (Somatosensory Evoked Potential)",
        "status_zh": "未检",
        "status_en": "Not Tested / Skipped"
    }
]

with open("/Users/eric/Dropbox/ai/physical/china_exam_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Added ancillary metadata, warm tips and vaccination data!")
