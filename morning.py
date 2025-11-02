from location import locationAccess
from weather import fetchWeather
from aqi import fetchAQI, postAQI

class Morning():
    def __init__(self, output=""):
        self.output = output

    def getReady(self):
        weather, description, city = fetchWeather()
        aqi = postAQI()
        self.output = f"The temperature in {city} is {round(weather-273.15)}°C with {description} and the AQI is {aqi}."

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