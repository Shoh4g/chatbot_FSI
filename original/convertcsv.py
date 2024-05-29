import csv
import json

def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        data = {}
        for row in reader:
            for key, value in row.items():
                if key not in data:
                    data[key] = []
                data[key].append(value)
    with open(json_file, 'w') as outfile:
        json.dump(data, outfile, indent=4)

csv_file = 'B. Funding Opportunities Database-All Funding Ops (Shared) (1).csv'  # Replace 'input.csv' with your CSV file name
json_file = 'funding.json'  # Replace 'output.json' with the desired output JSON file name
csv_to_json(csv_file, json_file)
