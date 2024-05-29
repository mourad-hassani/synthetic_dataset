from utils.generate_random_temporal_expression import generate_random_temporal_expression, generate_close_random_temporal_expression
from utils.compute_similarity_expressions import compute_similarity_expressions
from utils.mappings.expression_to_text import expression_to_text
from utils.dates.generate_random import generate_random_date_full
import os
import json

DATA_FOLDER_PATH = "data/base_dataset"
OUTPUT_FILE_NAME = "base_dataset.json"

output_data = []

for i in  range(1000):
    first_random_temporal_expression = generate_random_temporal_expression()
    current_date = generate_random_date_full(1900, 2050)
    sentence = f"[CLS] {expression_to_text(first_random_temporal_expression)} [SEP] {expression_to_text(current_date)} [SEP]"
    for j in range(5):
        second_random_temporal_expression = generate_random_temporal_expression()
        similarity = compute_similarity_expressions(first_random_temporal_expression, second_random_temporal_expression, current_date)
        output_data.append((sentence, expression_to_text(second_random_temporal_expression), similarity))
    for j in range(5):
        second_random_temporal_expression = generate_close_random_temporal_expression(first_random_temporal_expression)
        similarity = compute_similarity_expressions(first_random_temporal_expression, second_random_temporal_expression, current_date)
        output_data.append((sentence, expression_to_text(second_random_temporal_expression), similarity))

with open(os.path.join(DATA_FOLDER_PATH, OUTPUT_FILE_NAME), "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=4)