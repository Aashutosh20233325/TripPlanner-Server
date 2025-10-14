import requests
from config import MAPS_API_KEY, MAPS_API_URL
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="Map", stateless_http=True)

@mcp.tool(description="Get route between origin and destination")
def get_route(origin: str, destination: str) -> dict:
    """Fetch route from OpenRouteService based on origin and destination.
        "map": {
            "description": "Get driving directions between two locations",
            "endpoint": "/map",
            "parameters": {
                "origin": "string",        # e.g., "40.712776,-74.005974" (latitude,longitude)
                "destination": "string"    # e.g., "34.052235,-118.243683" (latitude,longitude)
            }
        }
    """
    try:
        headers = {
            "Authorization": MAPS_API_KEY
        }
        params = {
            "start": origin,       # must be lon,lat
            "end": destination     # must be lon,lat
        }
        response = requests.get(MAPS_API_URL, headers=headers, params=params)
        data = response.json()
        return {"success": True, "data": data}
    except Exception as e:
        return {"success": False, "error": str(e)}
