import os
import json
from tqdm import tqdm
from utils.periods.generate_random_period import generate_random_period, generate_close_random_period
from utils.periods.compute_similarity_periods import compute_similarity_periods
from utils.periods.is_period import is_period

data_folder_path = "data"
input_file_name = "unique_sentences.json"
output_file_name = "unique_sentences_exp.json"

data = []

with open(os.path.join(data_folder_path, input_file_name), "r", encoding="utf-8") as f:
    input_data = json.load(f)

    for element in tqdm(input_data):
        for k, v in element.items():
            for e in v:
                sentence = f"[CLS] {k} [SEP] {e["expression"]} [SEP]"
                data.append((sentence, e["value"], 1.0))
                for i in range(2):
                    random_per = generate_random_period()
                    per_bool, per_type = is_period(e["value"])
                    per_bool1, per_type1 = is_period(random_per)
                    similarity = compute_similarity_periods(e["value"], per_type, random_per, per_type1)
                    sentence = f"[CLS] {k} [SEP] {e["expression"]} [SEP]"
                    data.append((sentence, random_per, similarity))
                for i in range(2):
                    per_bool, per_type = is_period(e["value"])
                    random_per = generate_close_random_period(e["value"], per_type)
                    per_bool1, per_type1 = is_period(random_per)
                    similarity = compute_similarity_periods(e["value"], per_type, random_per, per_type1)
                    sentence = f"[CLS] {k} [SEP] {e["expression"]} [SEP]"
                    data.append((sentence, random_per, similarity))


with open(os.path.join(data_folder_path, output_file_name), "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(f"Dataset length : {len(data)}")