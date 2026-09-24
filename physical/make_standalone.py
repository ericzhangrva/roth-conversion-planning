import base64
import os

with open("/Users/eric/Dropbox/ai/physical/index.html", "r", encoding="utf-8") as f:
    html = f.read()

images = ["ecg_strip.jpg", "arteriosclerosis_report.jpg", "bone_density_chart.jpg"]
for img_name in images:
    img_path = os.path.join("/Users/eric/Dropbox/ai/physical/assets", img_name)
    if os.path.exists(img_path):
        with open(img_path, "rb") as img_file:
            b64_str = base64.b64encode(img_file.read()).decode("utf-8")
        data_uri = f"data:image/jpeg;base64,{b64_str}"
        rel_path = f"assets/{img_name}"
        html = html.replace(f'"{rel_path}"', f'"{data_uri}"')
        html = html.replace(f"'{rel_path}'", f"'{data_uri}'")
        print(f"Embedded {img_name} ({len(b64_str)} b64 chars)")

with open("/Users/eric/Dropbox/ai/physical/index.html", "w", encoding="utf-8") as f:
    f.write(html)

size_mb = os.path.getsize("/Users/eric/Dropbox/ai/physical/index.html") / (1024 * 1024)
print(f"index.html is now 100% self-contained! Total file size: {size_mb:.2f} MB")
