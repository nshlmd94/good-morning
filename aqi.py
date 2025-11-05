import sys
import json
import requests

from location import locationAccess

class AQI():
    def __init__(self, latitude, longitude, output=None, aqi_value=None):
        self.latitude = latitude
        self.longitude = longitude
        self.output = output
        self.aqi_value = aqi_value

    def getAQI(self):
        try:
            response = requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat={self.latitude}&lon={self.longitude}&appid=ec9bfb9a31502ef8928de884db45d65d")
            response.raise_for_status()

            self.output = response.json()

            self.aqi_value = self.output['list'][0]['main']['aqi']
            return self.aqi_value
        
        except KeyError as e:
            sys.exit(f"AQI: The key {e} does not exist in the dictionary.")
        except requests.exceptions.ConnectionError as e:
            sys.exit("AQI: A connection error occurred.")
        except requests.exceptions.HTTPError as e:
            sys.exit("AQI: An HTTP error occurred.")
        except requests.exceptions.ConnectTimeout as e:
            sys.exit("AQI: The request timed out while trying to connect to the remote server.")
        except requests.exceptions.Timeout as e:
            sys.exit("AQI: The request timed out.")
        except requests.exceptions.TooManyRedirects as e:
            sys.exit("AQI: Too many redirects.")
        except requests.exceptions.ReadTimeout as e:
            print("AQI: The server did not send any data in the allotted amount of time.")
        except json.JSONDecodeError as e:
            sys.exit("AQI: Couldn't decode the text into json.")
        except requests.exceptions.RequestException as e:
            sys.exit("AQI: Exception while handling request.")

def main():
    postAQI()

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