from fastapi import FastAPI
from pydantic import BaseModel

from stock_services import StockService


app = FastAPI()


class StockYearlyAverage(BaseModel):
    year: int
    value: float


@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/yearly_average/{company}")
async def yearly_average(company: str):
    stock_service = StockService()
    year, average = stock_service.get_yearly_average(company)

    return StockYearlyAverage(year=year, value=average)


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
