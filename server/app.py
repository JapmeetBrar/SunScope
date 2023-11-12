from flask import Flask, jsonify, request
from flask_cors import CORS
from mapdata import MapInfo
import googlemaps
import yaml
import os
import re
from solar_api import get_solar_data
from extract_json import process_data_custom_keys
from financial_engineering import FinancialEngineering

with open('server\sunscope\BE\data\json\secret.yml', 'r') as file:
    config = yaml.safe_load(file)

API_KEY = config['api_key']


app = Flask(__name__)
# THIS WILL HAVE TO BE CHANGED - CAN'T LET ALL SOURCES/ORIGINS ACCESS THE API
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})
client = MapInfo(googlemaps.Client(API_KEY))

@app.route('/get_solar_financial_data', methods=['GET'])
def get_solar_financial_data():
    """
    Endpoint to fetch and process solar data for a given address and 
    perform financial analysis.
    """
    address = request.args.get('address')
    if not address:
        return "Address is required", 400

    coordinates = client.coordinates(address)
    if not coordinates:
        return "No coordinates found for the address", 404

    latitude, longitude = coordinates
    solar_data = get_solar_data(latitude, longitude, API_KEY)
    if not solar_data:
        return "No solar data found for these coordinates", 404

    processed_data = process_data_custom_keys(solar_data)
    
    fe = FinancialEngineering(processed_data)
    rate_per_kwh = 0.10
    cost_per_panel = 1000
    number_of_panels = 10
    revenue = fe.calculate_revenue(number_of_panels, rate_per_kwh)
    payback_period = fe.calculate_payback_period(number_of_panels, rate_per_kwh, cost_per_panel * number_of_panels)

    response = {
        "address": address,
        "coordinates": coordinates,
        "solar_data": solar_data,
        "processed_data": processed_data,
        "financial_analysis": {
            "revenue": revenue,
            "payback_period": payback_period
        }
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

