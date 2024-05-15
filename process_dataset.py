import os
import json
from utils.dates.is_date import is_date
from tqdm import tqdm
from utils.dates.generate_random import generate_random_date
from utils.compute_similarity import compute_similarity

data_folder_path = "data"
input_file_name = "preprocessed_questions_HealthCareMagic-100k.json"
output_file_name = "my_new_data_exp.json"

data = []

with open(os.path.join(data_folder_path, input_file_name), "r", encoding="utf-8") as f:
    input_data = json.load(f)

    for element in tqdm(input_data):
        if is_date(element["value"])[0]:
            data.append((element["input"], element["value"], 1.0))
            for i in range(10):
                random_date = generate_random_date(int(element["value"][:4]), int(element["value"][:4]) + 3)
                similarity = compute_similarity(element["value"], random_date)
                data.append((element["input"], random_date, similarity))
            for j in range(50):
                first_random_date = generate_random_date(1900, 2024)
                second_random_date = generate_random_date(int(first_random_date[:4]), int(first_random_date[:4]) + 3)
                similarity = compute_similarity(first_random_date, second_random_date)
                data.append((first_random_date, second_random_date, similarity))

with open(os.path.join(data_folder_path, output_file_name), "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(f"Dataset length : {len(data)}")