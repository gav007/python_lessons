from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)


@app.get('/')
def show_form():
    return render_template("index.html")

@app.post("/submit")
def recieve_form():
    location = request.form.get("weather")
    
    # lat & lon
    dublin = (53.3498, 6.2603) 
    paris = (48.8566, 2.3522)
    london = (51.5074, 0.1278)
    new_york = (40.7128, -74.0060)
    
    
    if location.lower() == "dublin":
        params = dublin
    elif location.lower() == "paris":
        params = paris
    elif location.lower() == "london":
        params = london
    elif location.lower() == "new-york":
        params = new_york
        
    load_dotenv()
    api_key = os.environ.get("OPENWEATHER_API_KEY")
        
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={params[0]}&lon={params[1]}&appid={api_key}&units=metric"
        
    response = requests.get(url)
    
    weather_data = response.json()
    
    weather_des = weather_data["weather"][0]["description"]
    feels_like = weather_data["main"]["feels_like"]
    
    return render_template(
        "index.html",
        description=weather_des,
        feels_like=feels_like
)