import requests
import random
from dotenv import load_dotenv
import os

load_dotenv()
OPENWEATHER_API = os.getenv("OPENWEATHER_API")
OMDB_API = os.getenv("OMDB_API")

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API}&units=imperial"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None
    return response.json()

def weather_score(weather_data):
    temp = weather_data["main"]["temp"]
    condition = weather_data["weather"][0]["main"].lower()
    clouds = weather_data["clouds"]["all"]
    score = 50
    score += (temp - 50) * 0.5
    score -= clouds * 0.25
    if condition == "clear":
        score += 20
    if condition in {"thunderstorm", "drizzle", "rain", "snow"}:
        score -= 15
    return max(0, min(100, score))
