import requests
from config import EVENTS_API_KEY, EVENTS_API_URL

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="EventsServer", stateless_http=True)


@mcp.tool(description="Fetch events based on location and optional date range")



def get_events(location: str, date_range: str = None) -> dict:
    """Fetch events from SerpApi based on location and optional date range.
        "events": {
            "description": "Fetch events for a location and optional date range filter",
            "endpoint": "/events",
            "parameters": {
                "location": "string",     # e.g., "Austin", "Chicago"
                "date_range": "string"    # e.g., "today", "this week", "2025-10-01 to 2025-10-07"
            }
        }
    """
    try:
        print(f"Fetching events for location: {location} with date_range: {date_range}")  # Debug
        query = f"Events in {location}"
        params = {
            "engine": "google_events",
            "q": query,
            "hl": "en",
            "gl": "IN",
            "api_key": EVENTS_API_KEY
        }

        if date_range:
            params["htichips"] = f"date:{date_range}"

        response = requests.get(EVENTS_API_URL, params=params)
        data = response.json()

        print("SerpApi Raw Response:", data)  # Debug

        events_results = data.get("events_results", [])
        event_urls = [event.get("link") for event in events_results]

        return {"success": True, "data": {"events": events_results, "urls": event_urls}}
    except Exception as e:
        return {"success": False, "error": str(e)}
