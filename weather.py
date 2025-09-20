from mcp.server.fastmcp import FastMCP

mcp=FastMCP("weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """Returns the current weather for the given location."""
    return f"Weather in Apex is rainy"
