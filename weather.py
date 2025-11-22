import location
import sys
import requests
import json

from location import locationAccess
from error import errorHandling

class Weather():
    def __init__(self, latitude, longitude, output=None):
        self.latitude = latitude
        self.longitude = longitude
        self.output = output
    
    def getWeather(self):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={self.latitude}&lon={self.longitude}&appid=ec9bfb9a31502ef8928de884db45d65d")
        response.raise_for_status()
        
        self.output = response.json()
        return self.output
    
def main():
    fetchWeather()

@errorHandling
def fetchWeather(lat, lon):
    weather = Weather(lat, lon)
    requestWeather = weather.getWeather()
    temp = requestWeather['main']['temp']
    description = requestWeather['weather'][0]['main']
    #apparently there is a "safe access" way to write this: temp = requestWeather.get("main", {}).get("temp") NEED TO LEARN THIS LATER"

    return temp, description

if __name__ == "__main__":
    main()