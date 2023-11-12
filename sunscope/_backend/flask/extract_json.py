import json
import os
import re

# Function to import data from a JSON file
def import_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to process the data with custom keys
def process_data_custom_keys(data):
    processed_data = {}
    for entry in data['solarPotential']['solarPanelConfigs']:
        key = f"yearlyEnergyDcKwh{entry['panelsCount']}"
        processed_data[key] = entry['yearlyEnergyDcKwh']
    return processed_data



# Function to export data to a JSON file
def export_json(data, dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Find the next available file number
    file_number = 1
    pattern = re.compile(r'solar_data(\d+)\.json')
    for file in os.listdir(dir_path):
        match = pattern.match(file)
        if match:
            current_number = int(match.group(1))
            if current_number >= file_number:
                file_number = current_number + 1

    # Define the file path with the new number
    output_file_path = os.path.join(dir_path, f'solar_data{file_number}.json')

    with open(output_file_path, 'w') as file:
        json.dump(data, file, indent=4)

input_file_path = 'sunscope_backend/data/API/get_solar_data_example_CAN.json'  # Replace with your input file path
dir_path = 'sunscope_backend/data/API/json'

# Importing data from the JSON file
data = import_json(input_file_path)

# Processing the data
processed_data = process_data_custom_keys(data)

# Exporting the processed data to a new JSON file
export_json(processed_data, output_file_path)
