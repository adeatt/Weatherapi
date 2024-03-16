import pyodbc
import csv
import urllib
from sqlalchemy import create_engine
import pandas as pd
import requests     # mithilfe von "pip install requests" im cmd installiert 



API_KEY = "1b5f6951299ca4f5fbbb95c619c374d6"
lat = "49.71754000"  # Beispiel Forchheim 
lon = "11.05877000"  # Beispiel Forchheim
requests_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"

API_antwort  = requests.get(requests_url) #befehl zum erhalten der daten von der api mit dem link(requests_url)
        
data = API_antwort.json() #json ist das ausgabe format, anscheinend wichtig für das importieren der daten
    
#print(data) # -> ausgabe aller daten
Weather = data["weather"][0]["description"]
#print(Weather)
Tempc = round(data["main"]["temp"]-273.15)# temperatur wird in kelvin angegebn daher, -273.15
#print(Tempc)
Windspeed = round(data["wind"]["speed"]*3.771)
#print(Windspeed)



with open("Wdaten.csv", mode ="w") as csvfile:  #erstellen der csv datei
    Spalten = ["WetterID", "Temperatur", "Wetter", "Windgeschwindigkeit" ]
    writer = csv.DictWriter(csvfile, fieldnames = Spalten)
    writer.writeheader()
    writer.writerow({"WetterID": "0", "Wetter": Weather, "Temperatur": Tempc, "Windgeschwindigkeit": Windspeed}) #wichtig zu beachten das eingegebne Feldnamen gleich den Namen in der access tabelle entsprechen

#csv_path = r"C:\Users\SchülerBSZFO\OneDrive\Dokumente\Projekt Wetterdaten\Code\Wdaten.csv"
#print("Öffnen der CSV...")
#Datenfeld = pd.read_csv(csv_path)  #anzeigen der csv datei
#print(Datenfeld.head(10))

#print("Importieren in Access...")
#Verb_str = (
#    r"Driver= {Microsoft Access Driver (*.mdb, *.accdb)};"
#    r"DBQ=C:\Users\SchülerBSZFO\OneDrive\Dokumente\Projekt Wetterdaten\API1.accdb"
#)
#Verb_url = f"access+pyodbc:///?odbc_connect={urllib.parse.qoute_plus(Verb_str)}"
#acc_engine = create_engine(Verb_url)
#print("Access Tabele bearbeiten")
#Datenfeld.to_sql("Wetterdaten", acc_engine, if_exists="append")
#print("Änderung Fertig")





# Zum schluss muss die csv datei wieder gelöscht werdne. Aber erst nachdem sie erfolgreich in access importiert wurde. Grund: Es wird nur die Datei Wdaten.csv gelesen. Wenn nun eine neue Abfrage beginnt ist nun die neue Datei Wdaten1.csv und damti ungültig