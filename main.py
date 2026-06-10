import os   
from dotenv import load_dotenv
load_dotenv()


import requests
from langchain.tools import tool


from langchain.agents import create_agent

from src.prompt import *

system_prompt = """
    You are a helpful AI weather Agent
    Use the tool if required
    - From the response get from the tool give the relevant info in structured Output like
    - The weather in the {city} is
    - Temeprature
    - Humidity
    - Wind speed 
    - Etc in the structured output
    - Also add your insights also
    - If you don't know say I don't know

"""


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


## Loading the API Key
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

def main():
    agent = create_agent(
        model="google_genai:gemini-3-flash-preview",
        tools=[get_weather],
        system_prompt= system_prompt
    )

    user=input("Enter:")
    response = agent.invoke({"messages": [("user", user)]})
    content = response["messages"][-1].content

    if isinstance(content, list):
        print(content[0]["text"])
    else:
        print(content)
 

if __name__ == "__main__":
    main()
