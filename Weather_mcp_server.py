import requests
from config import WEATHER_API_KEY, WEATHER_API_URL
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="WeatherServer", stateless_http=True)


@mcp.tool(description="Get weather information for a specific location and date")

def get_weather(location: str, date: str) -> dict:
    """Fetch weather information from OpenWeatherMap based on location and date.
        "weather": {
            "description": "Get weather forecast for a location and date",
            "endpoint": "/weather",
            "parameters": {
                "location": "string",
                "date": "string"
            }
        }  
    """
    try:
        response = requests.get(
            WEATHER_API_URL,
            params={"q": location, "date": date, "appid": WEATHER_API_KEY}
        )
        data = response.json()
        return {"success": True, "data": data}
    except Exception as e:
        return {"success": False, "error": str(e)}
