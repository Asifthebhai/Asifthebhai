from fastapi import FastAPI

app=FastAPI()

@app.get("/welcome")
async def welcome():
    return{"Welcome !! To our Bot Page"}

@app.get("/hello")
async def hello():
    return {"Hello !!"}