from fastapi import FastAPI
import uvicorn
import calendar

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello folks!"}

@app.get("/cal/month")
async def cal(month: int):
    """Find what classes we have on day input"""
    c = calendar.TextCalendar(calendar.SUNDAY)
    print(c.prmonth(2021, month))
    
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')