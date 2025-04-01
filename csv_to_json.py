import csv
import json

# File paths
csv_file_path = 'student_data.csv'
json_file_path = 'student_data.json'

# Read the CSV file
data = []
with open(csv_file_path, 'r', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        data.append(row)

# Write to a JSON file
with open(json_file_path, 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)

print(f"CSV file {csv_file_path} has been converted to JSON file {json_file_path}")

