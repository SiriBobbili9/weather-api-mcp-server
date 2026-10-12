
from fastmcp import FastMCP
from app.services.tools import get_weather

mcp = FastMCP("Weather MCP Server")


@mcp.tool()
async def get_current_weather(city: str) -> dict:
    """Get the current weather for a city by name."""
    return await get_weather(city)


if __name__ == "__main__":
    mcp.run()
