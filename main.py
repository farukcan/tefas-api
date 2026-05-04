from datetime import date

from fastapi import FastAPI, Query
from tefas import Crawler

app = FastAPI()
crawler = Crawler()


@app.get("/price")
def get_price(symbol: str = Query(...)):
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
