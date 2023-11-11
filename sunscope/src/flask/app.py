from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        api_key = "AIzaSyBZMtnp5vEd8vRtZb-XTkk_vfBYA4YeuVc"
        result = get_solar_insight(latitude, longitude, api_key)
        return render_template('results.html', result=result)
    return render_template('index.html')

def get_solar_insight(latitude, longitude, api_key):
    url = f"https://solar.googleapis.com/v1/buildingInsights:findClosest?location.latitude={latitude}&location.longitude={longitude}&requiredQuality=HIGH&key={api_key}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

if __name__ == '__main__':
    app.run(debug=True)
