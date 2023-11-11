import googlemaps

class MapInfo:
    def __init__(self, client: googlemaps.Client):
        self.client = client
    def geocode(self, address: str) -> dict():#Gets geocode of an address        
        return self.client.geocode(address)
    def cordinates(self, address: str) -> tuple(): #returns list of tuples of longitude and latitude in search results:
        reuslting_cordinates = []
        result = self.geocode(address)
        for location in result:
            lat = location['geometry']['location']['lat']
            long = location['geometry']['location']['lng']
            reuslting_cordinates.append((lat, long))        
        return reuslting_cordinates

if __name__ == "__main__":
    

    API_KEY = 'AIzaSyBZMtnp5vEd8vRtZb-XTkk_vfBYA4YeuVc'
    client = MapInfo(googlemaps.Client(API_KEY))
    result = client.cordinates("11335 Saskatchewan Dr NW, Edmonton, AB T6G 2M9")
    print(result)
    
