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
    if condition == "clear":
        score += 20
    if condition in {"thunderstorm", "drizzle", "rain", "snow"}:
        score -= 15
    score -= clouds * 0.25
    return max(0, min(100, score))

def year_selection(period):
    if period == "classic":
        start, end = 1930, 1969
    if period == "modern":
        start, end = 1970, 1999
    if period == "recent":
        start, end = 2000, 2025
    else:
        start, end = 1930, 2025
    return random.sample(range(start, end + 1), 3)

GENRE_SCORES = {
    "action": 55,
    "adventure": 65,
    "animation": 95,
    "biography": 45,
    "comedy": 90,
    "crime": 35,
    "documentary": 50,
    "drama": 40,
    "family": 85,
    "fantasy": 70,
    "film-noir": 25,
    "game-show": 60,
    "history": 50,
    "horror": 15,
    "music": 75,
    "musical": 80,
    "mystery": 30,
    "news": 55,
    "reality-tv": 20,
    "romance": 75,
    "scifi": 67,
    "sport": 70,
    "talk-show": 60,
    "thriller": 37,
    "war": 20,
    "western": 45
}

positive_keywords = ["friendship","friend","hero","love","dancing","singing","happy","funny"]
negative_keywords = ["fight","violence","murder","death","betrayal","health crisis","blood","crime"]

def movie_score(genres, keywords=None):
    if not genres:
        return 50
    genres_split = []
    for g in genres.split(","):
        genres_split.append(g.lower())
    total = 0
    for g in genres_split:
        total += GENRE_SCORES.get(g, 50)
    score = total / len(genres)
    if keywords:
        for word in keywords:
            word = word.lower()
            if word in positive_keywords:
                score += 5
            if word in negative_keywords:
                score -= 5
    return max(0, min(100, score))

def


