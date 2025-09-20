from mcp.server.fastmcp import FastMCP


mcp=FastMCP("math")

@mcp.tool()
def add(a:int, b:int)->int:
    """Returns the sum of a and b."""
    return a

@mcp.tool()
def multiply(a:int, b:int)->int:
    """Returns the product of a and b."""
    return a*b