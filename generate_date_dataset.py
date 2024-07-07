import numpy as np
import random
from tqdm import tqdm
import os
import json

from utils.dates.to_explicit_date import to_explicit_date
from utils.dates.generate_random_date import generate_random_date
from utils.periods.generate_random_period import generate_random_period, generate_close_random_period
from utils.offsets.generate_random_offset import generate_random_offset, generate_close_random_offset
from utils.refs.generate_random_ref import generate_random_ref
from utils.intervals.generate_random_interval import generate_random_interval
from utils.dates.is_date import is_date
from utils.periods.is_period import is_period
from utils.offsets.is_offset import is_offset
from utils.refs.is_ref import is_ref
from utils.intervals.is_interval import is_interval
from utils.dates.dates_settings import START_DATE, END_DATE

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

from utils.dates.compute_similarity_dates import compute_similarity_dates, compute_similarity_dates_intervals

def generate_date_dateset():
    
    output_data = []

    DATA_FOLDER_PATH = "data/date_dataset"
    OUTPUT_FILE_NAME = "date_dataset_close.json"

    for _ in tqdm(range(20)):

        first_random_temporal_expression = generate_random_date(START_DATE, END_DATE)
        first_random_temporal_text = expression_to_text(first_random_temporal_expression)

        sentence = f"{first_random_temporal_text}"

        for _ in range(2):
            second_random_temporal_expression = generate_close_random_temporal_expression(first_random_temporal_expression, None)
            second_random_temporal_text = expression_to_text(second_random_temporal_expression)
            
            similarity = compute_similarity_dates_intervals(to_explicit_date(first_random_temporal_expression), to_explicit_date(second_random_temporal_expression))
            
            sentence_target = f"{second_random_temporal_text}"
            
            output_data.append((sentence, sentence_target, similarity))

        dates = to_explicit_date(first_random_temporal_expression)

        second_random_temporal_expression = dates[0]

        second_random_temporal_text = expression_to_text(second_random_temporal_expression)
                
        similarity = compute_similarity_dates_intervals(to_explicit_date(first_random_temporal_expression), to_explicit_date(second_random_temporal_expression))
        
        sentence_target = f"{second_random_temporal_text}"
        
        output_data.append((sentence, sentence_target, similarity))

    with open(os.path.join(DATA_FOLDER_PATH, OUTPUT_FILE_NAME), "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=4)

    count = 0
    for element in output_data:
        if element[2] < 0.1:
            count += 1

    print(f"Close similarities : {count / len(output_data)}")

if __name__ == "__main__":
    generate_date_dateset()