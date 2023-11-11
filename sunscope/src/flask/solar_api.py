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

    # Check if the response is successful
    if response.status_code == 200:
        # Return the JSON data from the response
        return response.json()
    else:
        # Return an error message if the request was unsuccessful
        return {'error': 'Failed to fetch data from Google API', 'status_code': response.status_code}
