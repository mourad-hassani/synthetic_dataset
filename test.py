import os
import json
from tqdm import tqdm
from utils.periods.generate_random_period import generate_random_period, generate_close_random_period
from utils.periods.compute_similarity_periods import compute_similarity_periods
from utils.mappings.offset_to_text import offset_to_text
from utils.mappings.date_to_text import date_to_text
from utils.mappings.period_to_text import period_to_text
from utils.offsets.is_offset import is_offset

data_folder_path = "data"
input_file_name = "one_sentence/one_sentence.json"

data = []

with open(os.path.join(data_folder_path, input_file_name), "r", encoding="utf-8") as f:
    input_data = json.load(f)

    for element in tqdm(input_data):
        is_format_bool, text = is_offset(element["value"])
        if is_format_bool:
            print(f"=================== {element['value']} :: {text}")
        else:
            print(f"{element['value']}")