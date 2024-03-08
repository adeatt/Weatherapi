import requests    

API_KEY = #"here should go the api key which is given by the api provider"

lat = "51.509865"  #London
lon = "-0.118092"  # London

requests_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
API_answer = requests.get(requests_url) 
data = API_answer.json() 
    

Weather = data["weather"][0]["description"]
Tempc = round(data["main"]["temp"]-273.15) # from kelvin to celcius
Windspeed = data["wind"]["speed"]
print(data)
