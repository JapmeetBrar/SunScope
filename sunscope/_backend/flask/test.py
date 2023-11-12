from mapdata import MapInfo
import googlemaps
from solar_api import get_solar_data
from extract_json import process_data_custom_keys
from financial_engineering import FinancialEngineering


API_KEY = 'AIzaSyBZMtnp5vEd8vRtZb-XTkk_vfBYA4YeuVc'
client = MapInfo(googlemaps.Client(API_KEY))



address = "2502, 4641 128 Avenue NE Calgary, Alberta T3N1T2"
coordinates = client.cordinates(address)

if coordinates:
    latitude, longitude = coordinates
    # Step 2: Get solar data for these coordinates
    solar_data = get_solar_data(latitude, longitude, API_KEY)

    # Step 3: Process the solar data
    processed_data = process_data_custom_keys(solar_data)
    # Further processing...
else:
    print("No coordinates found for the address.")
# Step 2: Get solar data for these coordinates
solar_data = get_solar_data(latitude, longitude, API_KEY)
print(solar_data)
# Step 3: Process the solar data
processed_data = process_data_custom_keys(solar_data)

fe = FinancialEngineering(processed_data)

# Example rate per kWh and cost per panel for calculations
rate_per_kwh = 0.10  # This can be adjusted as needed
cost_per_panel = 1000  # Example: $1000 per panel

# Assuming a fixed number of panels
number_of_panels = 10

# Calculate revenue and payback period
revenue = fe.calculate_revenue(number_of_panels, rate_per_kwh)
payback_period = fe.calculate_payback_period(number_of_panels, rate_per_kwh, cost_per_panel * number_of_panels)

# Output the results
print(f"Revenue for {number_of_panels} panels: ${revenue}")
print(f"Payback Period: {payback_period} years")