import os
from dotenv import load_dotenv

load_dotenv()
PORT = int(os.getenv("PORT", 8000))
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

MAPS_API_KEY = os.getenv("MAPS_API_KEY")
MAPS_API_URL = "https://api.openrouteservice.org/v2/directions/driving-car"

EVENTS_API_KEY = os.getenv("EVENTS_API_KEY")
EVENTS_API_URL = "https://serpapi.com/search.json"
