import requests
import random
from dotenv import load_dotenv
import os

load_dotenv()
OPENWEATHER_API = os.getenv("OPENWEATHER_API")
OMDB_API = os.getenv("OMDB_API")
