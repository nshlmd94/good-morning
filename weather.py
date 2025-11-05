import location
import sys
import requests
import json

from location import locationAccess

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

def fetchWeather(lat, lon):

    try:
        weather = Weather(lat, lon)
        requestWeather = weather.getWeather()
        temp = requestWeather['main']['temp']
        description = requestWeather['weather'][0]['main']
        #apparently there is a "safe access" way to write this: temp = requestWeather.get("main", {}).get("temp") NEED TO LEARN THIS LATER"

        return temp, description

    except KeyError as e:
        sys.exit(f"Weather: The key {e} does not exist in the dictionary.")
    except requests.exceptions.ConnectionError as e:
        sys.exit("Weather: A connection error occurred.")
    except requests.exceptions.HTTPError as e:
        sys.exit("Weather: An HTTP error occurred.")
    except requests.exceptions.ConnectTimeout as e:
        sys.exit("Weather: The request timed out while trying to connect to the remote server.")
    except requests.exceptions.Timeout as e:
        sys.exit("Weather: The request timed out.")
    except requests.exceptions.TooManyRedirects as e:
        sys.exit("Weather: Too many redirects.")
    except requests.exceptions.ReadTimeout as e:
        print("Weather: The server did not send any data in the allotted amount of time.")
    except json.JSONDecodeError as e:
        sys.exit("Weather: Couldn't decode the text into json.")
    except requests.exceptions.RequestException as e:
        sys.exit("Weather: Exception while handling request.")

if __name__ == "__main__":
    main()