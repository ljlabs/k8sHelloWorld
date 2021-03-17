from fastapi import FastAPI
from heavyCall import thisIsAHeavyCall

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/heavy")
async def root():
    return {"s": thisIsAHeavyCall()}