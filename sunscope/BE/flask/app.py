from flask import Flask, jsonify, request
from mapdata import MapInfo
import googlemaps
from solar_api import get_solar_data
from extract_json import import_json, find_latest_file, process_data_custom_keys, export_json
from financial_engineering import FinancialEngineering
import json
import os
import re

app = Flask(__name__)
API_KEY = 'Your_Google_Maps_API_Key'
client = MapInfo(googlemaps.Client(API_KEY))

@app.route('/coordinates', methods=['GET'])
def get_coordinates():
    """
    Endpoint to get geographical coordinates for a given address.
    Expects 'address' parameter in the request.
    Returns JSON with coordinates if address is provided, else a 400 error.
    """
    address = request.args.get('address')
    if address:
        coordinates = client.coordinates(address)
        return jsonify(coordinates)
    else:
        return "No address provided", 400

@app.route('/solar_data', methods=['GET'])
def solar_data():
    """
    Endpoint to fetch solar data.
    Modify to include necessary parameters and logic based on your solar data API.
    Returns JSON with solar data.
    """
    data = get_solar_data()
    return jsonify(data)

@app.route('/import_json', methods=['POST'])
def import_json_file():
    """
    Endpoint to import a JSON file.
    Expects a file in the request.
    Process the file using 'import_json' function and return its content.
    """
    file = request.files['file']
    data = import_json(file)
    return jsonify(data)

@app.route('/find_latest_file', methods=['GET'])
def latest_file():
    """
    Endpoint to find the latest JSON file processed.
    Uses 'find_latest_file' to retrieve the file name.
    Returns the name of the latest file.
    """
    latest_file = find_latest_file()
    return jsonify({"latest_file": latest_file})

@app.route('/process_data', methods=['POST'])
def process_data():
    """
    Endpoint to process data with custom keys.
    Expects JSON data in the POST request.
    Use 'process_data_custom_keys' for processing and return the processed data.
    """
    data = request.json
    processed_data = process_data_custom_keys(data)
    return jsonify(processed_data)

@app.route('/financial_calculation', methods=['GET'])
def financial_calculation():
    """
    Endpoint for financial calculations related to solar investments.
    Modify to include specific parameters and implement the calculation logic.
    Returns the result of financial calculations.
    """
    result = FinancialEngineering().calculate()  # Modify this based on actual implementation
    return jsonify(result)

# Add additional endpoints here as required for other functionalities in test.py

if __name__ == '__main__':
    app.run(debug=True)
