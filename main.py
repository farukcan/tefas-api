from datetime import date

from fastapi import FastAPI, Query
from mcp.server.fastmcp import FastMCP
from tefas import Crawler

app = FastAPI()
crawler = Crawler()

mcp_server = FastMCP("tefas-price")


def fetch_price(symbol: str) -> dict:
    today = date.today().strftime("%Y-%m-%d")
    data = crawler.fetch(start=today, end=today, name=symbol)
    if data.empty:
        return {"error": "Data not found", "symbol": symbol, "date": today}
    row = data.iloc[0]
    return {
        "symbol": row["code"],
        "title": row["title"],
        "price": row["price"],
        "date": today,
    }


@app.get("/price")
def get_price(symbol: str = Query(...)):
    return fetch_price(symbol)


@mcp_server.tool()
def get_fund_price(symbol: str) -> dict:
    """Get today's price for a TEFAS fund. Example symbols: TLE, YAC, IPB"""
    return fetch_price(symbol)


app.mount("/mcp", mcp_server.sse_app())
