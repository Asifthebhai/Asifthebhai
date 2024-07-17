from fastapi import FastAPI

app=FastAPI()

@app.get("/index")
async def index():
    return{"Welcome !! To our Bot Page"}

@app.get("/about")
async def hello():
    return {"About !!"}

@app.get("/contact")
async def hello():
    return {"Contact !!"}

@app.get("/refererence")
async def hello():
    return {"Reference !!"}