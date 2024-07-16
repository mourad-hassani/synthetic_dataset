import json
import matplotlib.pyplot as plt

def plot_distribution(values, bins=10, title="Distribution of Values", xlabel="Value", ylabel="Frequency"):
    plt.figure(figsize=(10, 6))
    plt.hist(values, bins=bins, edgecolor='black', alpha=0.7)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()
    
def apply_absolute_value(file_path):
    scores = []

    with open(file_path) as f:
        data = json.load(f)
        for d in data:
            scores.append(d[2])
    
    plot_distribution(scores)

input_file_path = 'data/date_dataset/date_dataset_close.json'

apply_absolute_value(input_file_path)

