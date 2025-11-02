import requests
import json
import sys

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
def locationAccess():
    try:
        response = requests.get("http://api.ipapi.com/api/check?access_key=93fb3e7984b81454237161942fc8d80c")
        response.raise_for_status()
        
        output = response.json()

        country = output['country_code']
        region = output['region_code']
        city = output['city']
        latitude = output['latitude']
        longitude = output['longitude']

        return latitude, longitude, city
    
    except KeyError as e:
        sys.exit(f"Location: The key {e} does not exist in the dictionary.")
    except requests.exceptions.ConnectionError as e:
        sys.exit("Location: A connection error occurred.")
    except requests.exceptions.HTTPError as e:
        sys.exit("Location: An HTTP error occurred.")
    except requests.exceptions.ConnectTimeout as e:
        sys.exit("Location: The request timed out while trying to connect to the remote server.")
    except requests.exceptions.Timeout as e:
        sys.exit("Location: The request timed out.")
    except requests.exceptions.TooManyRedirects as e:
        sys.exit("Location: Too many redirects.")
    except requests.exceptions.ReadTimeout as e:
        print("Location: The server did not send any data in the allotted amount of time.")
    except json.JSONDecodeError as e:
        sys.exit("Location: Couldn't decode the text into json.")
    except requests.exceptions.RequestException as e:
        sys.exit("Location: Exception while handling request.")


if __name__ == "__main__":
    main()
