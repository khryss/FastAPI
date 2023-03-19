from fastapi import FastAPI
from pydantic import BaseModel

from stock_services import StockService


app = FastAPI()


class StockYearlyAverage(BaseModel):
    year: int
    value: float


@app.get("/")
async def root():
    return {"message": "Welcome! Please go to /yearly_average/<company> "}


@app.get("/yearly_average/{company}")
async def yearly_average(company: str):
    stock_service = StockService(company)
    averages = stock_service.get_yearly_average()

    return [StockYearlyAverage(year=av[0], value=av[1]) for av in averages]


# @app.get("/proxy_test")
# async def proxy_test():
#     return requests.get('https://data.nasdaq.com/api/v3/datasets/WIKI/FB/data.json').json()


# @app.get("/path")
# async def demo_get():
#     return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}


# @app.post("/path")
# async def demo_post(inp: Msg):
#     return {"message": inp.msg.upper()}


# @app.get("/path/{path_id}")
# async def demo_get_path_id(path_id: int):
#     return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}
