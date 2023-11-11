import json

def read_json(file_path):
    """ Reads a JSON file and returns the data. """
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json(data, file_path):
    """ Writes data to a JSON file. """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def extract_and_export_data(input_file_path, output_file_path):
    """ Extracts specific data and exports it to another JSON file. """
    # Reading the original JSON data
    original_data = read_json(input_file_path)
    solar_potential = original_data.get('solarPotential', {})

    # Extracting the required information
    export_data = {
        "panelsCount": solar_potential.get('panelsCount', 0),
        "yearlyEnergyDcKwh": solar_potential.get('yearlyEnergyDcKwh', 0)
    }

    # Writing the extracted data to a new JSON file
    write_json(export_data, output_file_path)

# Paths for the input and output files
input_file_path = '/path/to/your/original/json/file.json'
output_file_path = '/path/to/your/new/json/file.json'

# Extracting and exporting the data
extract_and_export_data(input_file_path, output_file_path)
