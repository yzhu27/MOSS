import csv
import os
import random

input_folder = "./etc/data"
output_folder = "./etc/data/lownoise"
percent_noise = 1

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file in os.listdir(input_folder):
    if file.endswith(".csv"):
        # Read CSV file
        with open(os.path.join(input_folder, file), "r") as input_file:
            reader = csv.reader(input_file)
            header = next(reader)  # Get header row
            data = list(reader)  # Get data rows
        
        # Add noise to data
        num_rows = len(data)
        num_cols = len(header)
        num_noise = int(num_rows * num_cols * percent_noise / 100)
        indices = random.sample(range(num_rows * num_cols), num_noise)
        for idx in indices:
            row_idx = idx // num_cols
            col_idx = idx % num_cols
            data[row_idx][col_idx] = "?"
        
        # Write CSV file
        with open(os.path.join(output_folder, file), "w", newline="") as output_file:
            writer = csv.writer(output_file)
            writer.writerow(header)
            writer.writerows(data)
