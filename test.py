import requests
import json
import socket
import os

def main():
    hostname = socket.gethostname()
    ipAddress = socket.gethostbyname(hostname)

    value = os.system('ipconfig')

    response = requests.get(f"https://ipapi.co/{value}/json/")
    response.raise_for_status()

    output = response.json()

    print(output)
    
if __name__ == "__main__":
    main()