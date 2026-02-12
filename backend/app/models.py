from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SensorData(BaseModel):
    sensor_id: str
    timestamp: datetime
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    pressure: Optional[float] = None
    value: Optional[float] = None

class PredictionRequest(BaseModel):
    features: list[float]

class PredictionResponse(BaseModel):
    prediction: float
    confidence: float
    timestamp: datetime

