from utils.generate_random_temporal_expression import generate_random_temporal_expression, generate_close_random_temporal_expression
from utils.compute_similarity_expressions import compute_similarity_expressions
from utils.mappings.expression_to_text import expression_to_text
from utils.dates.generate_random_date import generate_random_date_full
import os
import json
from tqdm import tqdm
from utils.dates.dates_settings import START_DATE, END_DATE
from utils.refs.ref_to_date import ref_to_date
from utils.offsets.offset_to_date import offset_to_date
from utils.dates.to_explicit_date import to_explicit_date
from utils.refs.is_ref import is_ref
from utils.offsets.is_offset import is_offset
from utils.dates.is_date import is_date

DATA_FOLDER_PATH = "data/base_dataset"
OUTPUT_FILE_NAME = "base_dataset_close.json"

output_data = []

for i in  tqdm(range(100)):
    first_random_temporal_expression = generate_random_temporal_expression()
    current_date = generate_random_date_full(START_DATE, END_DATE)
    year = int(current_date.split("-")[0])
    if START_DATE < year < END_DATE:
        start_year = year - 1
        end_year = year + 1
    else:
        start_year = START_DATE
        end_year = END_DATE
    current_date_target = generate_random_date_full(start_year, end_year)
    first_random_temporal_text = expression_to_text(first_random_temporal_expression)
    current_text = expression_to_text(current_date)
    current_target_text = expression_to_text(current_date_target)
    sentence = f"[CLS] {first_random_temporal_text} [SEP] {current_text} [SEP]"
    for j in range(2):
        second_random_temporal_expression = generate_random_temporal_expression()
        second_random_temporal_text = expression_to_text(second_random_temporal_expression)
        similarity = compute_similarity_expressions(first_random_temporal_expression, second_random_temporal_expression, current_date, current_date_target)
        sentence_target = f"[CLS] {second_random_temporal_text} [SEP] {current_target_text} [SEP]"
        output_data.append((sentence, sentence_target, similarity))
    for j in range(2):
        second_random_temporal_expression = generate_close_random_temporal_expression(first_random_temporal_expression, current_date)
        second_random_temporal_text = expression_to_text(second_random_temporal_expression)
        similarity = compute_similarity_expressions(first_random_temporal_expression, second_random_temporal_expression, current_date, current_date_target)
        sentence_target = f"[CLS] {second_random_temporal_text} [SEP] {current_target_text} [SEP]"
        output_data.append((sentence, sentence_target, similarity))
    for j in range(1):
        dates = None
        if is_offset(first_random_temporal_expression)[0]:
            dates = offset_to_date(first_random_temporal_expression, current_date)
        elif is_ref(first_random_temporal_expression)[0]:
            dates = ref_to_date(first_random_temporal_expression, current_date)
        elif is_date(first_random_temporal_expression)[0]:
            dates = to_explicit_date(first_random_temporal_expression)
        if dates:
            start_date = dates[0]
            end_date = dates[1] if len(dates) > 1 else start_date
            start_year = int(start_date.split("-")[0])
            end_year = int(end_date.split("-")[0])
            start_month = int(start_date.split("-")[1])
            end_month = int(end_date.split("-")[1])
            start_day = int(start_date.split("-")[2])
            end_day = int(end_date.split("-")[2])
            second_random_temporal_expression = generate_random_date_full(start_year, end_year, start_month, end_month, start_day, end_day)
        else:
            second_random_temporal_expression = generate_close_random_temporal_expression(first_random_temporal_expression, current_date)
        second_random_temporal_text = expression_to_text(second_random_temporal_expression)
        similarity = compute_similarity_expressions(first_random_temporal_expression, second_random_temporal_expression, current_date, current_date_target)
        sentence_target = f"[CLS] {second_random_temporal_text} [SEP] {current_target_text} [SEP]"
        output_data.append((sentence, sentence_target, similarity))

with open(os.path.join(DATA_FOLDER_PATH, OUTPUT_FILE_NAME), "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=4)

count = 0
for element in output_data:
    if element[2] > 0.1:
        count += 1

print(f"Close similarities : {count / len(output_data)}")