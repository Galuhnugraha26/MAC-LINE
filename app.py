
from pathlib import Path
from typing import Literal

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(
    title="ModelServe",
    description="Lightweight machine learning inference service",
    version="0.1.0",
)

MODEL_PATH = Path(__file__).resolve().parent / "model" / "model.joblib"

# Load only the locally trained, trusted model artifact.
model = joblib.load(MODEL_PATH)


class PredictionRequest(BaseModel):
    type: Literal["L", "M", "H"]
    air_temperature: float = Field(gt=0)
    process_temperature: float = Field(gt=0)
    rotational_speed: float = Field(ge=0)
    torque: float = Field(ge=0)
    tool_wear: float = Field(ge=0)


class PredictionResponse(BaseModel):
    machine_failure: int


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    features = pd.DataFrame(
        [
            {
                "Type": request.type,
                "Air temperature": request.air_temperature,
                "Process temperature": request.process_temperature,
                "Rotational speed": request.rotational_speed,
                "Torque": request.torque,
                "Tool wear": request.tool_wear,
            }
        ]
    )

    prediction = int(model.predict(features)[0])

    return PredictionResponse(machine_failure=prediction)
