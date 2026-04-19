from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from model.model import model_load,MODEL_VERSION,predict as model_predict

app = FastAPI()

@app.get('/')
def home():
    return {'message' : 'The API is Running'}
@app.get('/health')
def health():
    return{
        'status' : 'ok',
        'model version' : MODEL_VERSION,
        'model load' : model_load
    }
@app.post('/predict')
def predict(x:int):
    if 1000 <= x <= 9999:
        try :
            prediction = model_predict(x)
            return JSONResponse(status_code=200,content={f'predictted per capita income(in US$)' : f'{prediction}'})
        except Exception as e :
            return {'message' : str(e)}
    raise HTTPException(status_code=400,detail={'message' : 'Enter valid Year'})