import os
import json
from tqdm import tqdm

DATA_FOLDER_PATH = "./data"
INPUT_FILE_NAME = "preprocessed_questions_HealthCareMagic-100k.json"
OUTPUT_FILE_NAME = "annotations_dictionary.json"


def get_annotations(folder_path, file_name):
    values = {}

    with open(os.path.join(folder_path, file_name), "r", encoding="utf-8") as f:
        data = json.load(f)
        for element in tqdm(data):
            if "INTERSECT" in element["value"]:
                for sub_element in element["value"].split("INTERSECT"):
                    if sub_element.strip() in values:
                        values[sub_element.strip()] += 1
                    else:
                        values[sub_element.strip()] = 1
            else:
                if element["value"].strip() in values:
                    values[element["value"].strip()] += 1
                else:
                    values[element["value"].strip()] = 1
    
    return values

values = get_annotations(folder_path=DATA_FOLDER_PATH, file_name=INPUT_FILE_NAME)
for k, v in values.items():
    print(f"key: {k}, value: {v}")

print(len(values.keys()))

with open(os.path.join(DATA_FOLDER_PATH, OUTPUT_FILE_NAME), "w", encoding="utf-8") as f:
    sorted_values = sorted(values.items(), key=lambda x: x[1], reverse=True)
    json.dump(sorted_values, f, indent=4)