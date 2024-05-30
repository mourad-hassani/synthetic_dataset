from utils.generate_random_temporal_expression import generate_random_temporal_expression, generate_close_random_temporal_expression
from utils.compute_similarity_expressions import compute_similarity_expressions
from utils.mappings.expression_to_text import expression_to_text
from utils.dates.generate_random import generate_random_date_full
import os
import json
from tqdm import tqdm
from utils.dates.dates_settings import START_DATE, END_DATE

DATA_FOLDER_PATH = "data/base_dataset"
OUTPUT_FILE_NAME = "base_dataset_close.json"

output_data = []

for i in  tqdm(range(1000000)):
    first_random_temporal_expression = generate_random_temporal_expression()
    current_date = generate_random_date_full(START_DATE, END_DATE)
    year = int(current_date.split("-")[0])
    if START_DATE < year < END_DATE:
        start_year = year - 3
        end_year = year + 3
    else:
        start_year = START_DATE
        end_year = END_DATE
    current_date_target = generate_random_date_full(start_year, end_year)
    sentence = f"[CLS] {expression_to_text(first_random_temporal_expression)} [SEP] {expression_to_text(current_date)} [SEP]"
    for j in range(2):
        second_random_temporal_expression = generate_random_temporal_expression()
        similarity = compute_similarity_expressions(first_random_temporal_expression, second_random_temporal_expression, current_date, current_date_target)
        sentence_target = f"[CLS] {expression_to_text(second_random_temporal_expression)} [SEP] {expression_to_text(current_date_target)} [SEP]"
        output_data.append((sentence, sentence_target, similarity))
    for j in range(8):
        second_random_temporal_expression = generate_close_random_temporal_expression(first_random_temporal_expression)
        similarity = compute_similarity_expressions(first_random_temporal_expression, second_random_temporal_expression, current_date, current_date_target)
        sentence_target = f"[CLS] {expression_to_text(second_random_temporal_expression)} [SEP] {expression_to_text(current_date_target)} [SEP]"
        output_data.append((sentence, sentence_target, similarity))

count = 0
for element in output_data:
    if element[2] > 0.05:
        count += 1

print(f"Close similarities : {count / len(output_data)}")

with open(os.path.join(DATA_FOLDER_PATH, OUTPUT_FILE_NAME), "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=4)