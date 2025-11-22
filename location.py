import requests
import json
import sys

from error import errorHandling

""" 
imported all the relevant packages

the program is only going to pull in the location data based on IP address so it can used by .py programs as input to access other APIs
"""

""" 
executing main
"""
def main():
    locationAccess()

""" 
pulling in the API response and pulling relevant key pair values around location
"""

@errorHandling
def locationAccess():
    response = requests.get("http://api.ipapi.com/api/check?access_key=93fb3e7984b81454237161942fc8d80c")
    response.raise_for_status()
        
    output = response.json()

    country = output['country_code']
    region = output['region_code']
    city = output['city']
    latitude = output['latitude']
    longitude = output['longitude']

    return latitude, longitude, city


if __name__ == "__main__":
    main()
