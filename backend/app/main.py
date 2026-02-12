from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title="Industrial IoT API",
    description="API for Industrial Hackathon",
    version="1.0.0",
)

#Configuration CORS pour permettre au frontend de communiquer
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Industrial IoT API is running!",
        "status": "healthy"
         }

@app.get("/api/health")
async def health_check():
    return {
        "status": "ok",
        "version": "1.0.0"
    }


# Endpoint pour recevoir des données de capteurs
@app.post("/api/sensor-data")
async def receive_sensor_data(data: dict):
    """
    Reçoit les données des capteurs IoT
    """
    print(f"Received sensor data: {data}")
    return {
        "status": "received",
        "data": data
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

