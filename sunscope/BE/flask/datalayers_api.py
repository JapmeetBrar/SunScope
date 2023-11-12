import requests
from PIL import Image
from io import BytesIO
def get_area_solar_data(latitude, longitude, api_key, radiusMeters= 50):
    # Parameters for the API request
    params = {
        'location.latitude': latitude,
        'location.longitude': longitude,
        'requiredQuality': 'HIGH',
        'key': api_key, 
        'radiusMeters':radiusMeters
    }

    # Making the GET request to the Google Solar API
    response = requests.get('https://solar.googleapis.com/v1/dataLayers:get', params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to fetch data from Google API', 'status_code': response.status_code}

class RegionData:
    def __init__(self,latitude, longitude, api_key, radiusMeters= 60) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.api_key = api_key
        self.radiusMeters = radiusMeters
        self.params = {
            'location.latitude': latitude,
            'location.longitude': longitude,
            'requiredQuality': 'HIGH',
            'key': api_key, 
            'radiusMeters':radiusMeters
        }
        self.data = requests.get('https://solar.googleapis.com/v1/dataLayers:get', params=self.params).json()
    def rgbImage(self, saveLocation:str = None) -> Image.open:
        params = {
            'key' : self.params['key']
        }
        image = requests.get(self.data['rgbUrl'], params=params)
        img = Image.open(BytesIO(image.content))
        if saveLocation != None:
            img = img.save(saveLocation)
        return img
    def annaulFlux(self, saveLocation:str = None):
        '''params = {
            'key' : self.params['key']
        }
        flux = requests.get(self.data['annualFluxUrl'], params=params)
        img = BytesIO(flux.content)
        img.seek(0)
        print(img.read())
        img = Image.open(img.read())
        if saveLocation != None:
            img.save(saveLocation)
        return img'''
        pass #does not work
if __name__ == "__main__":

    api_key = "AIzaSyBZMtnp5vEd8vRtZb-XTkk_vfBYA4YeuVc"
    latitude = 37.4450
    longitude = -122.1310

    area = RegionData(latitude, longitude, api_key)
    area.annaulFlux(saveLocation="test2.jpg")
