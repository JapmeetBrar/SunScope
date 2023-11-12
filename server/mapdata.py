import googlemaps

class MapInfo:
    def __init__(self, client: googlemaps.Client):
        self.client = client

    def geocode(self, address: str) -> dict:
        return self.client.geocode(address)

    def coordinates(self, address: str) -> tuple:
        result = self.geocode(address)
        if result:
            location = result[0]['geometry']['location']
            return location['lat'], location['lng']
        else:
            return None, None
