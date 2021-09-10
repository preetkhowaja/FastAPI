from fastapi import FastAPI
import uvicorn
import math

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello folks!"}

@app.get("/cal/month")
async def guards(walls: int):
    """Returns the smallest number of guards sufficient to protect your art gallery"""
    return floor(months / 3)
   
    
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
