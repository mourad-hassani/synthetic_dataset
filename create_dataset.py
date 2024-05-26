import os
import json
from stanza.server import CoreNLPClient
from tqdm import tqdm
from utils.stanza.temporal_expressions import contains_temporal_expression

client = CoreNLPClient(
    annotators=['tokenize', 'ner'],
    be_quiet=True)

output_json = []

dataset_path = "./data"
dataset_file_names = ["HealthCareMagic-100k.json"]

for dataset_file_name in dataset_file_names:
    with open(os.path.join(dataset_path, dataset_file_name), "r", encoding="utf-8") as f:
        data = json.load(f)
        for element in tqdm(data):
            temporal_expression_bool, temporal_expressions = contains_temporal_expression(element["input"], client=client)
            if temporal_expression_bool:
                for temporal_expression in temporal_expressions:
                    output_json.append({"input": element["input"], "expression": temporal_expression.text, "value": temporal_expression.value if temporal_expression.value else temporal_expression.altValue})

    with open(os.path.join(dataset_path, f"preprocessed_questions_{dataset_file_name}"), "w", encoding="utf-8") as f:
        json.dump(output_json, f, indent=4)
        