from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import numpy as np
import pickle

# -----------------------------
# Load the trained model
# -----------------------------
model = pickle.load(open("model_svc.pkl", "rb"))

# -----------------------------
# FastAPI App
# -----------------------------
app = FastAPI(
    title="Menstrual Health Prediction API",
    description="API that predicts unusual bleeding using SVC model",
    version="1.0"
)

# -----------------------------
# Request Body Schema
# -----------------------------
class MenstrualFeatures(BaseModel):
    number_of_peak: float
    Age: float
    Length_of_cycle: float
    Estimated_day_of_ovulution: float
    Length_of_Leutal_Phase: float
    Length_of_menses: float
    Height: float
    Weight: float
    BMI: float
    Mean_of_length_of_cycle: float
    Menses_score: float


# -----------------------------
# Prediction Endpoint
# -----------------------------
@app.post("/predict")
def predict(data: MenstrualFeatures):

    # Convert request → numpy array
    features = np.array([
        data.number_of_peak,
        data.Age,
        data.Length_of_cycle,
        data.Estimated_day_of_ovulution,
        data.Length_of_Leutal_Phase,
        data.Length_of_menses,
        data.Height,
        data.Weight,
        data.BMI,
        data.Mean_of_length_of_cycle,
        data.Menses_score
    ]).reshape(1, -1)

    # Make prediction
    pred = model.predict(features)[0]

    # Convert numeric prediction to readable message
    result = "Unusual Bleeding Detected" if pred == 1 else "Normal"

    return {
        "prediction": int(pred),
        "result": result
    }


# -----------------------------
# Run the API (optional)
# -----------------------------
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
