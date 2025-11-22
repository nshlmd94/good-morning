import requests
import json
import os
import csv
import datetime

# Define a function that will handle errors across all API calls
def errorHandling(func):
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now()

        try:
            result = func(*args, **kwargs)
            status = "Success"
            message = "Successfully executed!"
            return result
            
        except Exception as e:
            status = "Failure"
            exceptionName = type(e).__name__
            errorMessage = str(e)
            message = f"{func.__name__}: An error occured: {exceptionName}, {errorMessage}"
            print("Error, check logs.")
            raise

        finally:
            logger(timestamp, func.__name__, status, message)

    return wrapper

def logger(timestamp, function, status, message):
    fileExists = os.path.exists("logs.csv")
    with open("logs.csv", "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['timestamp', 'function', 'status', 'message'])
        if not fileExists or os.path.getsize("logs.csv") == 0:
            writer.writeheader()
        writer.writerow({'timestamp': timestamp, 'function': function, 'status': status, 'message': message})