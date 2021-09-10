from fastapi import FastAPI
import uvicorn
import math

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello folks!"}

@app.get("/cal/month")
<<<<<<< HEAD
async def cal(month: int):
    """Find what classes we have on day input"""
    c = calendar.TextCalendar(calendar.MONDAY)
    return c
=======
async def guards(walls: int):
    """Returns the smallest number of guards sufficient to protect your art gallery"""
    return floor(months / 3)
   
>>>>>>> 859ecf35506ed242ea6061e084040a75a5b56342
    
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
