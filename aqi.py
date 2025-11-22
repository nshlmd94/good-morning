import sys
import json
import requests

from location import locationAccess
from error import errorHandling

class AQI():
    def __init__(self, latitude, longitude, output=None, aqi_value=None):
        self.latitude = latitude
        self.longitude = longitude
        self.output = output
        self.aqi_value = aqi_value

    def getAQI(self):
        response = requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat={self.latitude}&lon={self.longitude}&appid=ec9bfb9a31502ef8928de884db45d65d")
        response.raise_for_status()

        self.output = response.json()

        self.aqi_value = self.output['list'][0]['main']['aqi']
        return self.aqi_value

def main():
    postAQI()

@errorHandling
def fetchAQI(lat, lon):
    accessAQI = AQI(lat, lon).getAQI()
    return accessAQI

def postAQI(lat, lon):
    aqi = str(fetchAQI(lat, lon))

    aqiLookup = {
            "1": "Good",
            "2": "Fair",
            "3": "Moderate",
            "4": "Poor",
            "5": "Very Poor",
        }

    return aqiLookup[aqi]


if __name__ == "__main__":
    main()