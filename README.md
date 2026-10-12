Weather API MCP server
Learn how a backend fetches real data from an external api and makes it available to an AI application

Description: Build a service that fetches current weather data and exposes it through both REST endpoints and MCP tools.
 What you will learn:
 - Call an external API using Python and HTTPX.
- Work with JSON responses from another service.
- Handle API errors and timeouts.
- Reuse the same business logic for REST and MCP.
- Test your MCP tools using an Inspector.

What we need for this project:
https://open-meteo.com/
We'll use the public Open-Meteo API, which provides weather data without requiring an API key for normal non-commercial use.

Required Packeges:
fastapi -->	Creates REST endpoints
uvicorn -->	Runs the REST API server
fastmcp -->	Registers and exposes MCP tools
httpx -->	Makes HTTP requests to external APIs
uv -->	Manages Python dependencies and the environment

tools.py --> Reusable business logic

Connecting to MCP Server:
Launch the MCP inspector:  npx -y @modelcontextprotocol/inspector uv run python -m app.mcp_server
This command will launch the http://localhost:6274.
connect using STDIO
Choose STDIO as the transport.



If the command and arguments are already populated, use the existing configuration.



Otherwise, enter the command as uv and arguments as:
run
python
-m
app.mcp_server
click connect
1. Open the Tools tab.
2. Click List Tools.
3. Select get_current_weather.
4. Enter this input:
{
  "city": "Hyderabad"
}

5. Click Run Tool.
