import requests
import json

def find_closest_solar_insight(latitude, longitude, api_key):
    url = f"https://solar.googleapis.com/v1/buildingInsights:findClosest?location.latitude={latitude}&location.longitude={longitude}&key={api_key}"
    response = requests.get(url)

    # Save the response to a file
    file_path = 'sunscope/src/data/solar_data.json'  # Update the path as needed
    with open(file_path, 'w') as file:
        json.dump(response.json(), file)

    return response.json()
