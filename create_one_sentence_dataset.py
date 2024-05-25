from utils.text.get_sentences import split_into_sentences
import os
import json
from tqdm import tqdm

DATASET_PATH = "./data"
INPUT_FILE_NAME = "HealthCareMagic-100k.json"
OUTPUT_FILE = "one_sentence/one_sentence.json"

output_json = []

with open(os.path.join(DATASET_PATH, INPUT_FILE_NAME), "r", encoding="utf-8") as f:
    data = json.load(f)
    for element in tqdm(data):
        paragraph = element["input"]
        sentences = split_into_sentences(paragraph)
        output_json.extend(sentences)

with open(os.path.join(DATASET_PATH, OUTPUT_FILE), "w", encoding="utf-8") as f:
    json.dump(output_json, f, indent=4)