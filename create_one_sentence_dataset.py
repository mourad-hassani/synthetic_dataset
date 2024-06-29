from utils.text.get_sentences import split_into_sentences
import os
import json
from tqdm import tqdm
from utils.stanza.temporal_expressions import contains_temporal_expression
from stanza.server import CoreNLPClient

client = CoreNLPClient(
    annotators=['tokenize', 'ner'],
    be_quiet=True)

DATASET_PATH = "./data"
INPUT_FILE_NAME = "HealthCareMagic-100k.json"
OUTPUT_FILE = "one_sentence/one_sentence.json"

output_json = []

with open(os.path.join(DATASET_PATH, INPUT_FILE_NAME), "r", encoding="utf-8") as f:
    data = json.load(f)
    for element in tqdm(data):
        paragraph = element["input"]
        sentences = split_into_sentences(paragraph)
        for sentence in sentences:
            temporal_expression_bool, temporal_expressions = contains_temporal_expression(sentence, client=client)
            if temporal_expression_bool:
                expressions = [temporal_expression.text for temporal_expression in temporal_expressions]
                values = [temporal_expression.value if temporal_expression.value else temporal_expression.altValue for temporal_expression in temporal_expressions]
                output_json.append({"input": sentence, "expressions": expressions, "values": values})

with open(os.path.join(DATASET_PATH, OUTPUT_FILE), "w", encoding="utf-8") as f:
    json.dump(output_json, f, indent=4)