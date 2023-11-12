import requests
import json
import os
import re

def get_solar_data(latitude, longitude, api_key):
    params = {
        'location.latitude': latitude,
        'location.longitude': longitude,
        'requiredQuality': 'HIGH',
        'key': api_key
    }

    response = requests.get('https://solar.googleapis.com/v1/buildingInsights:findClosest', params=params)

    if response.status_code == 200:
        data = response.json()

        dir_path = os.path.join('sunscope','BE', 'data', 'json')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        file_number = 1
        pattern = re.compile(r'solar_data(\d+)\.json')
        for file in os.listdir(dir_path):
            match = pattern.match(file)
            if match:
                current_number = int(match.group(1))
                if current_number >= file_number:
                    file_number = current_number + 1

        file_path = os.path.join(dir_path, f'solar_data{file_number}.json')

        with open(file_path, 'w') as file:
            json.dump(data, file)

        return data
    else:
        return {'error': 'Failed to fetch data from Google API', 'status_code': response.status_code}

