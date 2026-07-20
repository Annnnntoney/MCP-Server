# pip install fastmcp

import io
from fastmcp import FastMCP
from fastmcp.utilities.types import Image
import matplotlib.pyplot as plt

app=FastMCP("My MCP Server")
@app.tool
def add(n1:int, n2:int)->int:
    """Add Two Numbers"""
    return n1+n2

# fastmcp run app.py:app --transport http --port 8000

@app.tool
def draw_pie_chart(numbers:list[int])->Image:
    """"Draw Pie Chart"""
    plt.pie(numbers)
    buffer=io.BytesIO()
    plt.savefig(buffer, format="png")
    return Image(data=buffer, format="png")