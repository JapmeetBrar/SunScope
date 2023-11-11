from flask import Flask, jsonify, request
from solar_api import get_solar_data  # Importing the get_solar_data function

app = Flask(__name__)

API_KEY = 'AIzaSyBZMtnp5vEd8vRtZb-XTkk_vfBYA4YeuVc'  # Replace with your actual Google API key

@app.route('/get_solar_data')
def solar_data_route():
    # Retrieving latitude and longitude from the request's query parameters
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')

    # Validate if both latitude and longitude are provided
    if not latitude or not longitude:
        return jsonify({'error': 'Latitude and longitude are required'}), 400

    # Call the get_solar_data function and store the result
    result = get_solar_data(latitude, longitude, API_KEY)

    # Check if there was an error in the API call
    if 'error' in result:
        # Return the error message and status code
        return jsonify(result), result.get('status_code', 500)

    # Return the successful result
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
