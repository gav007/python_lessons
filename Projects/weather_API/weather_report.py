import os
from dotenv import load_dotenv
import requests
import json
import pprint
from datetime import datetime

# load up the api
load_dotenv()
api_key = os.environ.get("OPENWEATHER_API_KEY")
lat = 53.3498
lon = -6.2603
now = datetime.now()

# test
if api_key == None:
    print("API KEY NOT SET")
else:
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    #print(response)
    weather_data = response.json()
    #pprint.pprint(weather_data)
    location = "Dublin"
    temp = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    weather_min = weather_data["main"]["temp_min"]
    weather_max = weather_data["main"]["temp_max"]
    km_hour = round(weather_data["wind"]["speed"] * 3.6, 2)
    
    
    with open("weather_report.txt", "w") as file:
        file.write("Weather Report\n")
        file.write(str(now) + "\n")
        file.write("="*30 + "\n")
        file.write("Location: " + location + "\n")
        file.write("Current Temp: " + str(temp) + "\n")
        file.write("Feels Like: " + str(feels_like) + "\n")
        file.write("Min Temp: " + str(weather_min) + "\n")
        file.write("Max Temp: " + str(weather_max) + "\n")
        file.write("Wind Speed: " + str(km_hour) + "\n")
        
        
    


