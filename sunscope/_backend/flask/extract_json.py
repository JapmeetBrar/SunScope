import json

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
def export_json(data, output_file_path):
    with open(output_file_path, 'w') as file:
        json.dump(data, file, indent=4)
input_file_path = 'sunscope\_backend\data\API\get_solar_data_example_CAN.json'  # Replace with your input file path
output_file_path = 'sunscope\_backend\data\get_solar_data_example_CAN_couple.json'  # Replace with your desired output file path

# Importing data from the JSON file
data = import_json(input_file_path)

# Processing the data
processed_data = process_data_custom_keys(data)

# Exporting the processed data to a new JSON file
export_json(processed_data, output_file_path)
