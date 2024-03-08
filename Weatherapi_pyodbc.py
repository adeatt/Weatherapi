
import pyodbc
import pandas as pd
import requests    

API_KEY = "here should go the api key which is given by the api provider"
lat = "51.509865"  
lon = "-0.118092"   #London 

requests_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
API_answer  = requests.get(requests_url) 
data = API_answer.json() 
    
print(data) 
Weather = data["weather"][0]["description"]
Tempc = round(data["main"]["temp"]-273.15) 
Windspeed = data["wind"]["speed"]



conn_strg = r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=Path of the Access database;"
conn = pyodbc.connect(conn_strg)
cursor = conn.cursor()

apidata = (
          (0,Tempc, Weather, Windspeed)
)
cursor.executemany("INSERT INTO Weatherdata VALUES (?,?,?,?)", apidata)
df = pd.read_sql("select * from Weatherdata", conn_strg) 
print(df)   
cursor.close()
conn.close()







