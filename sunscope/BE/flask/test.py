from mapdata import MapInfo
import googlemaps
from solar_api import get_solar_data
from extract_json import import_json, find_latest_file, process_data_custom_keys, export_json
from financial_engineering import FinancialEngineering
import json
import os
import re


API_KEY = 'AIzaSyBZMtnp5vEd8vRtZb-XTkk_vfBYA4YeuVc'
client = MapInfo(googlemaps.Client(API_KEY))



address = "2905 37 Ave NE, Calgary, AB T1Y 5Z9"
coordinates = client.coordinates(address)

if coordinates:
    latitude, longitude = coordinates

    # Get solar data for these coordinates
    solar_data = get_solar_data(latitude, longitude, API_KEY)

    # Directory path where the JSON files are stored
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

else:
    print("No coordinates found for the address.")

if 'processed_data' in locals():
    fe = FinancialEngineering(processed_data)

    # Example rate per kWh and cost per panel for calculations
    rate_per_kwh = 0.10  # Adjust as needed
    cost_per_panel = 1000  # Example: $1000 per panel

    # Assuming a fixed number of panels
    number_of_panels = 10

    # Calculate revenue and payback period
    revenue = fe.calculate_revenue(number_of_panels, rate_per_kwh)
    payback_period = fe.calculate_payback_period(number_of_panels, rate_per_kwh, cost_per_panel * number_of_panels)

    # Output the results
    print(f"Revenue for {number_of_panels} panels: ${revenue}")
    print(f"Payback Period: {payback_period} years")
else:
    print("No processed data available for financial calculations.")


