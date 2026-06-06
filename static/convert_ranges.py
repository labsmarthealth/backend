import json

file_path = "Testing_master_data.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    if item.get("reference_range"):
        item["reference_range"] = (
            item["reference_range"]
            .replace("; ", "\n")
            .replace(";", "\n")
        )

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Reference ranges converted successfully.")