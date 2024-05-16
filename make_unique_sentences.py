import os
import json
from utils.dates.is_date import is_date
from utils.periods.is_period import is_period
from tqdm import tqdm

data_folder_path = "./data/"
input_file_name = "preprocessed_questions_HealthCareMagic-100k.json"
output_file_name = "unique_sentences.json"

output = []

with open(os.path.join(data_folder_path, input_file_name), "r", encoding="utf-8") as f:
    data = json.load(f)
    result_dict = {}
    for element in tqdm(data):
        date_bool, date_type = is_period(element["value"])
        if date_bool:
            if element["input"] not in result_dict:
                result_dict[element["input"]] = []
            result_dict[element["input"]].append({"expression": element["expression"], "value": element["value"], "type": date_type})

    output = [{k: v} for k, v in result_dict.items()]

print(len(output))
with open(os.path.join(data_folder_path, output_file_name), "w", encoding="utf-8") as f:
    json.dump(output, f, indent=4)