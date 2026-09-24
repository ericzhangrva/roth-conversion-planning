import json

with open("/Users/eric/Dropbox/ai/physical/china_exam_data.json", "r", encoding="utf-8") as f:
    exam_data = json.load(f)

json_str = json.dumps(exam_data, ensure_ascii=False)

with open("/Users/eric/Dropbox/ai/physical/dashboard_template.html", "r", encoding="utf-8") as f:
    template = f.read()

html_content = template.replace("__EXAM_DATA_JSON__", json_str)

with open("/Users/eric/Dropbox/ai/physical/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Updated /Users/eric/Dropbox/ai/physical/index.html successfully from template!")
