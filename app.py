from fastapi import FastAPI, Form, Request, Response, File
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
import uvicorn
import os
import json


app = FastAPI()
app.mount("/static", StaticFiles(directory="templates", html = True))


@app.get("/")
async def index():
    return FileResponse("home.html")

@app.post("/submit_form")
async def submit_detail(bedrooms: int = Form(...), bathrooms: int = Form(...)):
    return {
        "bedrooms": bedrooms,
        "bathrooms": bathrooms
    }

@app.get("/")
async def get_details()


if __name__ == "__main__":
    uvicorn.run("app:app", host='0.0.0.0', port=8000, reload=True)