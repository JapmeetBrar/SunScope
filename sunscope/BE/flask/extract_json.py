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

    # Process 'solarPanelConfigs'
    for entry in data['solarPotential']['solarPanelConfigs']:
        key = f"yearlyEnergyDcKwh{entry['panelsCount']}"
        processed_data[key] = entry['yearlyEnergyDcKwh']

    # Recursive function to search for keys in nested dictionaries
    def find_keys(nested_dictionary, target_keys):
        found_values = {key: None for key in target_keys}
        for key, value in nested_dictionary.items():
            if key in target_keys:
                found_values[key] = value
            if isinstance(value, dict):
                deeper_values = find_keys(value, target_keys)
                for k in deeper_values:
                    if deeper_values[k] is not None:
                        found_values[k] = deeper_values[k]
        return found_values

    # Extract 'maxArrayAreaMeters2' and 'maxSunshineHoursPerYear'
    nested_keys = find_keys(data, ['maxArrayAreaMeters2', 'maxSunshineHoursPerYear'])
    processed_data.update(nested_keys)

    return processed_data

def export_json(data, dir_path, file_number):
    output_file_path = os.path.join(dir_path, f'solar_data{file_number}_proc.json')
    with open(output_file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Directory path
dir_path = 'sunscope\BE\data\JSON'

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
