from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from mqtt_subscriber import IoTDataReceiver
import threading

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

# ========== INTÉGRATION MQTT ==========
#Instance globale du receiver
mqtt_receiver = None

@app.on_event("startup")
async def startup_event():
    """Démarre le receiver MQTT au démarrage de l'API"""
    global mqtt_receiver
    
    try:
        mqtt_receiver = IoTDataReceiver(broker_address="localhost", port=1883)
        mqtt_thread = threading.Thread(target=mqtt_receiver.connect_and_listen, daemon=True)
        mqtt_thread.start()
        print("🚀 MQTT Receiver started in background")
    except Exception as e:
        print(f"⚠️ Could not start MQTT receiver: {e}")

@app.get("/api/sensor-data/latest")
async def get_latest_sensor_data():
    """Retourne les dernières données des capteurs"""
    if mqtt_receiver and mqtt_receiver.received_messages:
        return {
            "count": len(mqtt_receiver.received_messages),
            "latest": mqtt_receiver.received_messages[-10:]
        }
    return {
        "count": 0,
        "latest": [],
        "message": "No data received yet. Make sure the MQTT simulator is running."
    }

@app.get("/api/sensor-data/stats")
async def get_sensor_statistics():
    """Statistiques sur les données reçues"""
    if not mqtt_receiver or not mqtt_receiver.received_messages:
        return {
            "message": "No data received yet",
            "total_messages": 0,
            "normal": 0,
            "anomalies": 0,
            "anomaly_rate": 0
        }
    
    total = len(mqtt_receiver.received_messages)
    anomalies = sum(1 for msg in mqtt_receiver.received_messages 
                   if msg['data'].get('status') == 'anomaly')
    
    return {
        "total_messages": total,
        "normal": total - anomalies,
        "anomalies": anomalies,
        "anomaly_rate": round(anomalies/total*100, 2) if total > 0 else 0
    }

@app.get("/api/sensor-data/all")
async def get_all_sensor_data():
    """Retourne toutes les données des capteurs"""
    if mqtt_receiver and mqtt_receiver.received_messages:
        return {
            "count": len(mqtt_receiver.received_messages),
            "data": mqtt_receiver.received_messages
        }
    return {
        "count": 0,
        "data": [],
        "message": "No data received yet"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

