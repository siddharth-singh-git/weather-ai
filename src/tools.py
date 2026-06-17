import requests
from langchain.tools import tool



#Documenation Link - https://open-meteo.com/
@tool
def get_weather(city:str) -> str :
    """Get the weather of the city from Weather API"""
    (lat, lon) = get_lat_lon(city)


    ## For simplicity we are using Open-Meteo - No API key required
    url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={lat}&longitude={lon}"
    f"&current=temperature_2m,relative_humidity_2m")

    data = requests.get(url).json()

    return data["current"]


# Documentation Link - "https://open-meteo.com/en/docs/geocoding-api"

def get_lat_lon(city: str) -> tuple:
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
    response = requests.get(geocoding_url).json()
    results = response.get("results", [])
    if not results:
        raise ValueError(f"City '{city}' not found.")
    lat = results[0]["latitude"]
    lon = results[0]["longitude"]
    return (lat, lon)
