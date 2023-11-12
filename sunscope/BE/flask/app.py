from flask import Flask, jsonify, request, render_template_string, redirect, url_for
from mapdata import MapInfo
import googlemaps
from solar_api import get_solar_data
from extract_json import import_json, find_latest_file, process_data_custom_keys, export_json
from financial_engineering import FinancialEngineering
import json
import os
import re

app = Flask(__name__)
API_KEY = 'AIzaSyBZMtnp5vEd8vRtZb-XTkk_vfBYA4YeuVc'
client = MapInfo(googlemaps.Client(API_KEY))

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Root route to display an HTML form for address input.
    On form submission, it redirects to the get_coordinates function.
    """
    if request.method == "POST":
        address = request.form.get("address")
        return redirect(url_for("get_coordinates", address=address))
    return '''
        <form method="post">
            Address: <input type="text" name="address"><br>
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/coordinates', methods=['GET'])
def get_coordinates():
    """
    Get geographical coordinates for a given address.
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
    Endpoint to fetch solar data based on provided coordinates.
    Expects 'latitude' and 'longitude' as query parameters.
    """
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    if latitude and longitude:
        data = get_solar_data(latitude, longitude)  # Modify as per your implementation
        return jsonify(data)
    else:
        return "Latitude and longitude required", 400

@app.route('/process_json', methods=['POST'])
def process_json_data():
    """
    Endpoint to process JSON data. Expects JSON data in the request body.
    """
    data = request.json
    processed_data = process_data_custom_keys(data)
    return jsonify(processed_data)

@app.route('/financial_analysis', methods=['GET'])
def financial_analysis():
    """
    Endpoint for performing financial analysis. 
    Expects relevant parameters as query inputs.
    """
    # Extract parameters from the request and perform financial analysis
    # Example: revenue = calculate_revenue(params)
    # return jsonify({"revenue": revenue, ...})

# Additional endpoints as required ...

if __name__ == '__main__':
    app.run(debug=True)
