import pyodbc
import csv
import urllib
from sqlalchemy import create_engine
import pandas as pd
import requests     



API_KEY = "APi key"
lat = "" # Cordinates
lon = ""  
requests_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
API_answer  = requests.get(requests_url) 
data = API_answwer.json() 
    

Weather = data["weather"][0]["description"]
Tempc = round(data["main"]["temp"]-273.15)
Windspeed = round(data["wind"]["speed"]*3.771)
print(data) 



with open("Wdaten.csv", mode ="w") as csvfile:  
    fieldnames = ["WeatherID", "Tempc", "Weather", "Windspeed" ]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow({"WeatherID": "0", "Weather": Weather, "Tempc": Tempc, "Windspeed": Windspeed}) 
