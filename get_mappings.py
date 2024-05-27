import os
import json

DATA_FOLDER_PATH = "./data/"
INPUT_FILE_NAME = "one_sentence/one_sentence.json"
OUTPUT_FILE_NAME = "./utils/mappings.json"

mappings = {}

with open(os.path.join(DATA_FOLDER_PATH, INPUT_FILE_NAME), "r", encoding="utf-8") as f:
    data = json.load(f)
    for item in data:
        expression = item["expression"]
        value = item["value"]
        if value in mappings:
            exp_dict = mappings[value]
            if expression in exp_dict:
                exp_dict[expression] += 1
            else:
                exp_dict[expression] = 1
        else:
            mappings[value] = {expression: 1}

new_mappings = {}

for k, v in mappings.items():
    v = sorted(v.items(), key=lambda x: x[1], reverse=True)
    new_mappings[k] = v[0][0]

with open(OUTPUT_FILE_NAME, "w", encoding="utf-8") as f:
    json.dump(new_mappings, f, indent=4)