from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from stock_services import StockService, CodeNotFoundError


app = FastAPI()


class StockYearlyAverage(BaseModel):
    year: int
    value: float


@app.get("/")
async def root():
    return {"message": ("Welcome! To start, please go to /yearly_average/<company> ."
                        "Example: /yearly_average/FB")}


@app.get("/yearly_average/{company_code}")
async def yearly_average(company_code: str):
    try:
        stock_service = StockService(company_code)
    except CodeNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc))

    averages = stock_service.get_yearly_average()
    return [StockYearlyAverage(year=av.year, value=av.average) for av in averages]


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
