
import httpx


async def get_weather(city: str) -> dict:
    """Fetch current weather for a city using Open-Meteo."""

    city = city.strip()

    if not city:
        raise ValueError("City cannot be empty")

    async with httpx.AsyncClient(timeout=10.0) as client:
        # First, find the city's coordinates.
        geo_response = await client.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={
                "name": city,
                "count": 1,
                "language": "en",
                "format": "json",
            },
        )
        geo_response.raise_for_status()
        geo_data = geo_response.json()

        results = geo_data.get("results", [])
        if not results:
            raise ValueError(f"City not found: {city}")

        place = results[0]
        latitude = place["latitude"]
        longitude = place["longitude"]

        # Next, fetch the current weather for those coordinates.
        weather_response = await client.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": (
                    "temperature_2m,"
                    "relative_humidity_2m,"
                    "apparent_temperature,"
                    "wind_speed_10m,"
                    "weather_code"
                ),
                "timezone": "auto",
            },
        )
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        current = weather_data["current"]

        return {
            "city": place["name"],
            "country": place.get("country", "Unknown"),
            "temperature_c": current["temperature_2m"],
            "feels_like_c": current["apparent_temperature"],
            "humidity_percent": current["relative_humidity_2m"],
            "wind_speed_kmh": current["wind_speed_10m"],
            "weather_code": current["weather_code"],
            "time": current["time"],
        }
