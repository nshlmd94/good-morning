import csv
import os
import datetime
from dataclasses import dataclass

from location import locationAccess
from weather import fetchWeather
from aqi import fetchAQI, postAQI

class Morning():
    def __init__(self, output=""):
        self.output = output

    def getReady(self):
        lat, lon, city = locationAccess()
        weather, description = fetchWeather(lat, lon)
        aqi = postAQI(lat, lon)

        morningData = {
            'city': city, 
            'weather': weather, 
            'description': description, 
            'aqi': aqi
        }

        # Users shouldn't call these method independently
        self._logCalls(morningData)
        self._formatOutput(morningData)

    def _logCalls(self, morningData):
        timestamp = datetime.datetime.now()

        fileExists = os.path.exists("data.csv")
        with open("data.csv", 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['timestamp', 'city', 'weather', 'description', 'aqi'])
            if not fileExists or os.path.getsize("data.csv") == 0:
                writer.writeheader()
            writer.writerow({'timestamp': timestamp, 'city': morningData['city'], 'weather': round(morningData['weather']-273.15), 'description': morningData['description'], 'aqi': morningData['aqi']})

    def _formatOutput(self, morningData):
        self.output = f"The temperature in {morningData['city']} is {round(morningData['weather']-273.15)}°C with {morningData['description']} and the AQI is {morningData['aqi']}."

    def __str__(self) -> str:
        return self.output
    
def main():
    morning = Morning()
    morning.getReady() 

    """
    choosing not do chaining here by doing Morning().getReady() because it will return None (see output was initialized as "").
    Instead doing it as: I create a Morning object → self.output = "". 
    I then call morning.getReady() 
    → it fills in self.output and then call print(morning) 
    → that calls morning.__str__() 
    → returns the string stored in self.output.
    """

    print(morning)


if __name__ == "__main__":
    main()