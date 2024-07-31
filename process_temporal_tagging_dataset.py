import os
import json
from tqdm import tqdm
from utils.dates.generate_random_date import generate_random_date_full
from utils.dates.is_date import is_date
from utils.offsets.is_offset import is_offset
from utils.refs.is_ref import is_ref
from utils.intervals.is_interval import is_interval
from utils.dates.dates_settings import START_DATE, END_DATE
from utils.mappings.expression_to_text import expression_to_text
from utils.generate_random_temporal_expression import generate_random_temporal_expression, generate_close_random_temporal_expression
from utils.compute_similarity_expressions import compute_similarity_expressions
from utils.offsets.offset_to_date import offset_to_date
from utils.refs.ref_to_date import ref_to_date
from utils.dates.to_explicit_date import to_explicit_date
from utils.intervals.interval_to_date import interval_to_date

DATASET_PATH = "./data"

def process_dataset():
    INPUT_FILE_NAME = "temporal_tagging/wiki_data.json"
    OUTPUT_FILE_NAME = "temporal_tagging/processed_one_sentence_list.json"

    data = []

    with open(os.path.join(DATASET_PATH, INPUT_FILE_NAME), "r", encoding="utf-8") as f:
        input_data = json.load(f)[:100000]

        for element in tqdm(input_data):
            expressions_tmp = element["expressions"]
            values_tmp = [e if expression_to_text(e) else None for e in element["values"]]
            expressions, values = [], []
            for e, v in zip(expressions_tmp, values_tmp):
                if v and expression_to_text(v):
                    expressions.append(e)
                    values.append(v)
            for expression, value in zip(expressions, values):
                current_date = generate_random_date_full(START_DATE, END_DATE)
                current_text = expression_to_text(current_date)

                sentence = f"[CLS] {element["input"]} [SEP] {current_text} [SEP]"
                
                year = int(current_date.split("-")[0])
                if START_DATE < year < END_DATE:
                    start_year = year - 1
                    end_year = year + 1
                else:
                    start_year = START_DATE
                    end_year = END_DATE

                for j in range(2):
                    current_date_target = generate_random_date_full(start_year, end_year)
                    current_target_text = expression_to_text(current_date_target)
                    second_random_temporal_expression = generate_random_temporal_expression()
                    second_random_temporal_text = expression_to_text(second_random_temporal_expression)
                    similarity = max([compute_similarity_expressions(v, second_random_temporal_expression, current_date, current_date_target) for v in values])
                    sentence_target = f"[CLS] {second_random_temporal_text} [SEP] {current_target_text} [SEP]"
                    data.append((sentence.strip(), sentence_target.strip(), similarity))

                    if similarity >= 0.9:
                        similarity = max([compute_similarity_expressions(second_random_temporal_expression, v, current_date_target, current_date) for v in values])
                        data.append((sentence_target.strip(), sentence.strip(), similarity))

                for j in range(2):
                    current_date_target = generate_random_date_full(start_year, end_year)
                    current_target_text = expression_to_text(current_date_target)
                    second_random_temporal_expression = generate_close_random_temporal_expression(value, current_date)
                    second_random_temporal_text = expression_to_text(second_random_temporal_expression)
                    similarity = max([compute_similarity_expressions(v, second_random_temporal_expression, current_date, current_date_target) for v in values])
                    sentence_target = f"[CLS] {second_random_temporal_text} [SEP] {current_target_text} [SEP]"
                    data.append((sentence.strip(), sentence_target.strip(), similarity))

                    if similarity >= 0.9:
                        similarity = max([compute_similarity_expressions(second_random_temporal_expression, v, current_date_target, current_date) for v in values])
                        data.append((sentence_target.strip(), sentence.strip(), similarity))

                for j in range(1):
                    current_date_target = generate_random_date_full(start_year, end_year)
                    current_target_text = expression_to_text(current_date_target)
                    dates = None
                    if is_offset(value)[0]:
                        dates = offset_to_date(value, current_date)
                    elif is_ref(value)[0]:
                        dates = ref_to_date(value, current_date)
                    elif is_date(value)[0]:
                        dates = to_explicit_date(value)
                    elif is_interval(value)[0]:
                        dates = interval_to_date(value)
                    if dates:
                        if len(dates) > 1:
                            second_random_temporal_expression = f"{dates[0]},{dates[1]}"
                        else:
                            second_random_temporal_expression = dates[0]
                    else:
                        second_random_temporal_expression = generate_close_random_temporal_expression(value, current_date)
                    second_random_temporal_text = expression_to_text(second_random_temporal_expression)
                    if second_random_temporal_text:
                        similarity = max([compute_similarity_expressions(v, second_random_temporal_expression, current_date, current_date_target) for v in values])
                        sentence_target = f"[CLS] {second_random_temporal_text} [SEP] {current_target_text} [SEP]"
                        data.append((sentence.strip(), sentence_target.strip(), similarity))
                

    with open(os.path.join(DATASET_PATH, OUTPUT_FILE_NAME), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"Dataset length : {len(data)}")

process_dataset()