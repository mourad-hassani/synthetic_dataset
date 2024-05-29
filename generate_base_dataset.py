from utils.generate_random_temporal_expression import generate_random_temporal_expression

DATA_FOLDER_PATH = "data/base_dataset"
OUTPUT_FILE_NAME = "base_dataset.json"

output_data = []

for i in  range(1000):
    random_temporal_expression = generate_random_temporal_expression()