import json
import os
import re

def find_latest_file(dir_path):
    max_number = -1
    latest_file = None
    pattern = re.compile(r'solar_data(\d+)\.json')

    for file in os.listdir(dir_path):
        match = pattern.match(file)
        if match:
            number = int(match.group(1))
            if number > max_number:
                max_number = number
                latest_file = file

    return latest_file, max_number

def import_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def process_data_custom_keys(data):
    processed_data = {}
    for entry in data['solarPotential']['solarPanelConfigs']:
        key = f"yearlyEnergyDcKwh{entry['panelsCount']}"
        processed_data[key] = entry['yearlyEnergyDcKwh']
    return processed_data

def export_json(data, dir_path, file_number):
    output_file_path = os.path.join(dir_path, f'solar_data{file_number}_proc.json')
    with open(output_file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Directory path
dir_path = 'sunscope/_backend/data/json'

# Find the latest file for importing
latest_file, file_number = find_latest_file(dir_path)
if latest_file:
    input_file_path = os.path.join(dir_path, latest_file)

    # Importing data from the JSON file
    data = import_json(input_file_path)

    # Processing the data
    processed_data = process_data_custom_keys(data)

    # Exporting the processed data to a new JSON file with corresponding naming
    export_json(processed_data, dir_path, file_number)
else:
    print("No solar data files found.")
