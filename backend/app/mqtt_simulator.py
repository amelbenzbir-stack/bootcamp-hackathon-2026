import paho.mqtt.client as mqtt
import json
import time
import random
from datetime import datetime

class IoTSensorSimulator:
    """
    Simule des capteurs IoT industriels qui envoient des données via MQTT
    """
    
    def __init__(self, broker_address="localhost", port=1883):
        self.broker_address = broker_address
        self.port = port
        self.client = mqtt.Client(client_id="sensor_simulator")
        
        # Callbacks
        self.client.on_connect = self.on_connect
        self.client.on_publish = self.on_publish
        
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("✅ Connected to MQTT Broker successfully!")
        else:
            print(f"❌ Failed to connect, return code {rc}")
    
    def on_publish(self, client, userdata, mid):
        print(f"📤 Message {mid} published")
    
    def connect(self):
        """Connexion au broker MQTT"""
        try:
            self.client.connect(self.broker_address, self.port, keepalive=60)
            self.client.loop_start()
            print(f"🔌 Attempting connection to {self.broker_address}:{self.port}")
        except Exception as e:
            print(f"❌ Connection error: {e}")
    
    def generate_sensor_data(self, sensor_id):
        """Génère des données de capteur réalistes"""
        
        # Différents types de capteurs
        sensor_types = {
            "temperature": {
                "value": round(20 + random.uniform(-5, 15), 2),
                "unit": "°C",
                "normal_range": [15, 35]
            },
            "humidity": {
                "value": round(40 + random.uniform(-10, 30), 2),
                "unit": "%",
                "normal_range": [30, 70]
            },
            "pressure": {
                "value": round(1013 + random.uniform(-50, 50), 2),
                "unit": "hPa",
                "normal_range": [980, 1050]
            },
            "vibration": {
                "value": round(random.uniform(0, 10), 3),
                "unit": "mm/s",
                "normal_range": [0, 5]
            },
            "power_consumption": {
                "value": round(100 + random.uniform(-20, 80), 2),
                "unit": "kWh",
                "normal_range": [50, 200]
            }
        }
        
        sensor_type = random.choice(list(sensor_types.keys()))
        sensor_config = sensor_types[sensor_type]
        
        value = sensor_config["value"]
        is_anomaly = not (sensor_config["normal_range"][0] <= value <= sensor_config["normal_range"][1])
        
        data = {
            "sensor_id": sensor_id,
            "type": sensor_type,
            "value": value,
            "unit": sensor_config["unit"],
            "timestamp": datetime.now().isoformat(),
            "status": "anomaly" if is_anomaly else "normal",
            "location": f"Factory-A-Zone-{random.randint(1, 5)}"
        }
        
        return data
    
    def publish_sensor_data(self, topic, sensor_id):
        """Publie les données d'un capteur"""
        data = self.generate_sensor_data(sensor_id)
        message = json.dumps(data, indent=2)
        
        result = self.client.publish(topic, message, qos=1)
        
        # Affichage coloré selon le statut
        status_icon = "⚠️" if data["status"] == "anomaly" else "✅"
        print(f"\n{status_icon} Sensor: {sensor_id}")
        print(f"   Type: {data['type']}")
        print(f"   Value: {data['value']} {data['unit']}")
        print(f"   Status: {data['status']}")
        
        return result
    
    def simulate_multiple_sensors(self, num_sensors=5, interval=2, duration=60):
        """
        Simule plusieurs capteurs qui envoient des données
        
        Args:
            num_sensors: Nombre de capteurs à simuler
            interval: Intervalle entre chaque envoi (secondes)
            duration: Durée totale de simulation (secondes)
        """
        print(f"\n🏭 Starting simulation of {num_sensors} sensors for {duration}s")
        print(f"📊 Publishing every {interval}s\n")
        
        start_time = time.time()
        message_count = 0
        
        try:
            while (time.time() - start_time) < duration:
                for i in range(num_sensors):
                    sensor_id = f"SENSOR_{i+1:03d}"
                    topic = f"factory/sensors/{sensor_id}"
                    
                    self.publish_sensor_data(topic, sensor_id)
                    message_count += 1
                
                print(f"\n--- Total messages sent: {message_count} ---")
                time.time()
                time.sleep(interval)
        
        except KeyboardInterrupt:
            print("\n\n⏹️  Simulation stopped by user")
        
        finally:
            print(f"\n📊 Simulation Summary:")
            print(f"   Duration: {time.time() - start_time:.1f}s")
            print(f"   Messages sent: {message_count}")
            print(f"   Average rate: {message_count/(time.time() - start_time):.2f} msg/s")
    
    def disconnect(self):
        """Déconnexion propre"""
        self.client.loop_stop()
        self.client.disconnect()
        print("\n🔌 Disconnected from MQTT Broker")


# Script principal
if __name__ == "__main__":
    print("=" * 60)
    print("🏭 IoT SENSOR SIMULATOR - BOOTCAMP 5.0")
    print("=" * 60)
    
    # Créer et démarrer le simulateur
    simulator = IoTSensorSimulator(broker_address="localhost", port=1883)
    simulator.connect()
    
    # Attendre que la connexion soit établie
    time.sleep(2)
    
    # Simuler 5 capteurs pendant 60 secondes, envoi toutes les 3 secondes
    simulator.simulate_multiple_sensors(
        num_sensors=5,
        interval=3,
        duration=60
    )
    
    # Déconnexion
    simulator.disconnect()