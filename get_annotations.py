import os
import json
from tqdm import tqdm

folder_path = "./data"
file_name = "preprocessed_questions_HealthCareMagic-100k.json"


def get_annotations(folder_path, file_name):
    values = set()

    with open(os.path.join(folder_path, file_name), "r", encoding="utf-8") as f:
        data = json.load(f)
        for element in tqdm(data):
            values.add(element["value"])
    
    return values

values = get_annotations(folder_path=folder_path, file_name=file_name)
for value in values:
    print(value)

print(len(values))