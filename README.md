# MCP Weather Server

A simple Model Context Protocol (MCP) server that provides weather information using the National Weather Service API. This server exposes two tools:

1. `get_alerts`: Get weather alerts for a US state
2. `get_forecast`: Get weather forecast for a location based on latitude and longitude

## Requirements

- Python 3.10 or higher
- MCP SDK 1.2.0 or higher
- httpx for making HTTP requests

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/mcp-weather-server.git
cd mcp-weather-server
```

2. Create and activate a virtual environment:
```bash
# Using venv
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

To run the server, simply execute:

```bash
python simple_mcp_server.py
```

The server will start and listen for requests on standard input/output (stdio).

## Testing the Server

A test script is provided to verify that the server is working correctly:

```bash
python test_weather_server.py
```

This will start the server, send requests to both tools, and display the results.

## Integrating with Claude for Desktop

To use this server with Claude for Desktop:

1. Make sure you have Claude for Desktop installed and updated to the latest version.

2. Open your Claude for Desktop App configuration at:
   - MacOS/Linux: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%AppData%\Claude\claude_desktop_config.json`

3. Add your server configuration:

```json
{
    "mcpServers": {
        "weather": {
            "command": "python",
            "args": [
                "/ABSOLUTE/PATH/TO/simple_mcp_server.py"
            ]
        }
    }
}
```

4. Replace `/ABSOLUTE/PATH/TO/` with the actual path to your `simple_mcp_server.py` file.

5. Save the file and restart Claude for Desktop.

## Using the Weather Tools

Once the server is connected to Claude for Desktop, you can ask questions like:

- "What's the weather in Sacramento?"
- "What are the active weather alerts in Texas?"

Claude will automatically use the appropriate tool to fetch the information.

## Note

This server uses the US National Weather Service API, so it only works for locations within the United States.
Memory System
