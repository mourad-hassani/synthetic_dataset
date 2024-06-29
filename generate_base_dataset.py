import os
import json
from tqdm import tqdm

from utils.dates.dates_settings import START_DATE, END_DATE
from utils.refs.ref_to_date import ref_to_date
from utils.offsets.offset_to_date import offset_to_date
from utils.intervals.interval_to_date import interval_to_date
from utils.dates.to_explicit_date import to_explicit_date
from utils.refs.is_ref import is_ref
from utils.offsets.is_offset import is_offset
from utils.dates.is_date import is_date
from utils.intervals.is_interval import is_interval
from utils.generate_random_temporal_expression import generate_random_temporal_expression, generate_close_random_temporal_expression
from utils.compute_similarity_expressions import compute_similarity_expressions
from utils.mappings.expression_to_text import expression_to_text
from utils.dates.generate_random_date import generate_random_date_full

def generate_base_dataset():
    """
    generates a pure synthetic dataset (its output is in the data/base_datasetbase_dataset_close.json file). The order of generation is as follows :
    2 random expressions
    2 close random expressions
    1 close/exact date version of the anchor
    """

    DATA_FOLDER_PATH = "data/base_dataset"
    OUTPUT_FILE_NAME = "base_dataset_close.json"

    output_data = []

    for i in  tqdm(range(1000000)):
        first_random_temporal_expression = generate_random_temporal_expression()
        first_random_temporal_text = expression_to_text(first_random_temporal_expression)

        current_date = generate_random_date_full(START_DATE, END_DATE)
        current_text = expression_to_text(current_date)

        year = int(current_date.split("-")[0])
        if START_DATE < year < END_DATE:
            start_year = year - 1
            end_year = year + 1
        else:
            start_year = START_DATE
            end_year = END_DATE

        current_date_target = generate_random_date_full(start_year, end_year)
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
            
            elif is_interval(first_random_temporal_expression)[0]:
                dates = interval_to_date(first_random_temporal_expression)
            
            if dates:
                if len(dates) > 1:
                    second_random_temporal_expression = f"{dates[0]},{dates[1]}"
                
                else:
                    second_random_temporal_expression = dates[0]
            
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

if __name__ == "__main__":
    generate_base_dataset()