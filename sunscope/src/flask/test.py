import requests
import json

def get_solar_insight_and_save(latitude, longitude, api_key, file_path):
    url = f"https://solar.googleapis.com/v1/buildingInsights:findClosest?location.latitude={latitude}&location.longitude={longitude}&requiredQuality=HIGH&key={api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(file_path, 'w') as file:
            json.dump(response.json(), file)
        return f"Data saved to {file_path}"
    else:
        return f"Error: {response.status_code}"

# Usage
api_key = "AIzaSyBZMtnp5vEd8vRtZb-XTkk_vfBYA4YeuVc"  # Replace with your actual API key
latitude = 37.4450  # Replace with your desired latitude
longitude = -122.1390  # Replace with your desired longitude
file_path = 'sunscope\src\data\solar_insight.json'  # Specify the path where you want to save the file

result = get_solar_insight_and_save(latitude, longitude, api_key, file_path)
