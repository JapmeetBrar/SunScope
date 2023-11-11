import requests

def get_solar_data(latitude, longitude, api_key):
    # Parameters for the API request
    params = {
        'location.latitude': latitude,
        'location.longitude': longitude,
        'requiredQuality': 'HIGH',
        'key': api_key
    }

    # Making the GET request to the Google Solar API
    response = requests.get('https://solar.googleapis.com/v1/buildingInsights:findClosest', params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to fetch data from Google API', 'status_code': response.status_code}
