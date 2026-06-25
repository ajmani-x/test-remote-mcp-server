from fastmcp import FastMCP
import random
import json

# Create the FastMCP server instance
mcp = FastMCP("Simple Calculator Server")

# Tool : Add two numbers
@mcp.tool
def add(a:int,b:int)->int:
    """Add two numbers together.
    Args:
        a (int): The first number.
        b (int): The second number.
        

    Returns:
        result (int): The sum of the two input arguments"""
    return a+b

# Tool : Generate a random number between two numbers
@mcp.tool
def random_number(min:int,max:int)->int:
    """Generate a random number between two numbers.
    Args:
        min (int): The minimum number.
        max (int): The maximum number.
        
    Returns:
        result (int): A random number between the two input arguments"""
    return random.randint(min,max)

# Resource: Server Information
@mcp.resource("info://server")
def server_info()->str:
    """Get server information."""
    info = {
        "name":"Simple Calculator Server",
        "version":"1.0.0",
        "description":"A basic MCP server with math tools",
        "tools":["add","random_number",],
        "authors":"Aryan Ajmani"
    }
    return json.dumps(info,indent=2)

# Start the server
if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8010)