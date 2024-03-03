


def wdaten():

    import requests     # mithilfe von "pip install requests" im cmd installiert 

    API_KEY = "1b5f6951299ca4f5fbbb95c619c374d6"

    lat = "49.71754000"  # Beispiel Forchheim 

    lon = "11.05877000"  # Beispiel Forchheim

    requests_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"

    API_antwort = requests.get(requests_url) #befehl zum erhalten der daten von der api mit dem link(requests_url)
        
    data = API_antwort.json() #json ist das ausgabe format, anscheinend wichtig für das importieren der daten
    
    #print(data) # -> ausgabe aller daten
    Wetter = data["weather"][0]["description"]
    print(Wetter)
    Tempc = round(data["main"]["temp"]-273.15) # temperatur wird in kelvin angegebn daher, -273.15
    print(Tempc)
    Windgeschwindigkeit = data["wind"]["speed"]
    print(Windgeschwindigkeit)

wdaten()




