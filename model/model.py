from pathlib import Path
import warnings

import joblib

warnings.filterwarnings("ignore")

MODEL_PATH = Path(__file__).resolve().parent / "model.pkl"
with open(MODEL_PATH, "rb") as f:
    model = joblib.load(f)
model_load = True if model else False
MODEL_VERSION = 1.0
def predict(X:int):
    x = [[X]]
    prediction = model.predict(x)
    return prediction[0]
print(predict(2000))