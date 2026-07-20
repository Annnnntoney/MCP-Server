# pip install fastmcp
from fastmcp import FastMCP

app=FastMCP("My MCP Server")
@app.tool
def add(n1:int, n2:int)->int:
    """Add Two Numbers"""
    return n1+n2

# fastmcp run app.py:app --transport http --port 8000