from fastapi import FastAPI
import uvicorn
import math
from imdb import IMDb

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Hello folks!"}


@app.get("/guards/walls")
async def guards(walls: int):
    """Returns the smallest number of guards sufficient to protect your art gallery"""
    return math.floor(walls / 3)

@app.get("/movie/string1")
async def movie(string1: str):
    ia = imdb.IMDb()
    name = string1
    emp_list = []
    search = ia.search_movie(name)
    for i in search:
        emp_list.append(i["title"])
    return emp_list


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
