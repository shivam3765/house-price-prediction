from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import pickle

app = FastAPI()
app.mount("/static", StaticFiles(directory="templates", html=True))
templates = Jinja2Templates(directory="templates")

model = pickle.load(open("model.pkl", "rb"))

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "prediction_text": ""})

@app.post("/predict_api")
async def predict_api(request: Request, 
                      House_age: float = Form(...), 
                      Distance_to_the_nearest_MRT_station: float = Form(...), 
                      Number_of_convenience_stores: float = Form(...),
                      Latitude: float = Form(...),
                      Longitude: float = Form(...),
                      ):
    try:
        prediction_result = [House_age, Distance_to_the_nearest_MRT_station,Number_of_convenience_stores,
                                      Latitude, Longitude]
        predicted_result = model.predict([prediction_result])
        return {"result": "{:.2f}".format(predicted_result[0])}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run("app:app", host='0.0.0.0', port=8000, reload=True)
