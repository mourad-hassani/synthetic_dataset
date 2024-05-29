import os
import json
from tqdm import tqdm
from utils.periods.generate_random_period import generate_random_period, generate_close_random_period
from utils.dates.generate_random import generate_random_date, generate_random_date_full
from utils.offsets.generate_random_offset import generate_random_offset
from utils.periods.compute_similarity_periods import compute_similarity_periods
from utils.dates.compute_similarity_dates import compute_similarity_dates
from utils.offsets.compute_similarity_offsets import compute_similarity_offsets
from utils.periods.is_period import is_period
from utils.dates.is_date import is_date
from utils.offsets.is_offset import is_offset
from utils.mappings.date_to_text import date_to_text
from utils.mappings.period_to_text import period_to_text
from utils.mappings.offset_to_text import offset_to_text

DATA_FOLDER_PATH = "data/one_sentence"
INPUT_FILE_NAME = "one_sentence.json"
OUTPUT_FILE_NAME = "processed_one_sentence.json"

data = []

with open(os.path.join(DATA_FOLDER_PATH, INPUT_FILE_NAME), "r", encoding="utf-8") as f:
    input_data = json.load(f)

    for element in tqdm(input_data):
        if element["value"] != "":
            current_date = generate_random_date_full(2000, 2024)
            sentence = f"[CLS] {element['input']} [SEP] {date_to_text(current_date)} [SEP]"
            value_text = None
            if is_date(element["value"])[0]:
                value_text = date_to_text(element["value"])
            elif is_period(element["value"])[0]:
                value_text = period_to_text(element["value"])
            elif is_offset(element["value"])[0]:
                value_text = offset_to_text(element["value"])
            if value_text:
                data.append((sentence, value_text, 1.0))
            if is_date(element["value"])[0]:
                for i in range(5):
                    generated_dates = set()
                    generated_dates.add(element["value"])
                    date_format = is_date(element["value"])[1]
                    year = int(element["value"].split("-")[0])
                    if 1900 < year < 2100:
                        start_year = year - 3
                        end_year = year + 3
                    else:
                        start_year = 1899
                        end_year = 2099
                    random_date = generate_random_date(start_year, end_year)
                    while random_date in generated_dates:
                        random_date = generate_random_date(start_year, end_year)
                    generated_dates.add(random_date)
                    similarity = compute_similarity_dates(element["value"], random_date)
                    data.append((sentence, date_to_text(random_date), similarity))
            elif is_period(element["value"])[0]:
                generated_periods = set()
                generated_periods.add(element["value"])
                for i in range(3):
                    period_format = is_period(element["value"])[1]
                    random_period = generate_close_random_period(element["value"], period_format)
                    while random_period in generated_periods:
                        random_period = generate_close_random_period(element["value"], period_format)
                    generated_periods.add(random_period)
                    similarity = compute_similarity_periods(element["value"], period_format, random_period, period_format)
                    data.append((sentence, period_to_text(random_period), similarity))
                for i in range(3):
                    period_format = is_period(element["value"])[1]
                    random_period = generate_random_period()
                    while random_period in generated_periods:
                        random_period = generate_random_period()
                    generated_periods.add(random_period)
                    random_period_format = is_period(random_period)[1]
                    similarity = compute_similarity_periods(element["value"], period_format, random_period, random_period_format)
                    data.append((sentence, period_to_text(random_period), similarity))
            elif is_offset(element["value"])[0]:
                generated_offsets = set()
                generated_offsets.add(element["value"])
                for i in range(5):
                    offset_format = is_offset(element["value"])[1]
                    random_offset = generate_random_offset()
                    while random_offset in generated_offsets:
                        random_offset = generate_random_offset()
                    generated_offsets.add(random_offset)
                    random_offset_format = is_offset(random_offset)[1]
                    similarity = compute_similarity_offsets(element["value"], offset_format, random_offset, random_offset_format, current_date)
                    data.append((sentence, offset_to_text(random_offset), similarity))

with open(os.path.join(DATA_FOLDER_PATH, OUTPUT_FILE_NAME), "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(f"Dataset length : {len(data)}")