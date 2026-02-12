import paho.mqtt.client as mqtt
import json
from datetime import datetime

class IoTDataReceiver:
    """
    Reçoit et traite les données des capteurs IoT
    """
    
    def __init__(self, broker_address="localhost", port=1883):
        self.broker_address = broker_address
        self.port = port
        self.client = mqtt.Client(client_id="data_receiver")
        self.received_messages = []
        
        # Callbacks
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
    
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("✅ Receiver connected to MQTT Broker!")
            # S'abonner à tous les capteurs
            self.client.subscribe("factory/sensors/#")
            print("📡 Subscribed to: factory/sensors/#")
        else:
            print(f"❌ Connection failed with code {rc}")
    
    def on_message(self, client, userdata, msg):
        """Callback quand un message est reçu"""
        try:
            # Décoder le message JSON
            payload = json.loads(msg.payload.decode())
            
            # Ajouter à la liste des messages reçus
            self.received_messages.append({
                "topic": msg.topic,
                "data": payload,
                "received_at": datetime.now().isoformat()
            })
            
            # Affichage
            status_icon = "⚠️" if payload.get("status") == "anomaly" else "📊"
            print(f"\n{status_icon} Received from {msg.topic}")
            print(f"   Sensor: {payload.get('sensor_id')}")
            print(f"   Type: {payload.get('type')}")
            print(f"   Value: {payload.get('value')} {payload.get('unit')}")
            print(f"   Status: {payload.get('status')}")
            
            # Si anomalie, alerte!
            if payload.get("status") == "anomaly":
                print(f"   🚨 ALERT: Abnormal value detected!")
            
        except json.JSONDecodeError as e:
            print(f"❌ Error decoding message: {e}")
        except Exception as e:
            print(f"❌ Error processing message: {e}")
    
    def connect_and_listen(self):
        """Connexion et écoute des messages"""
        try:
            self.client.connect(self.broker_address, self.port, keepalive=60)
            print(f"🔌 Connecting to {self.broker_address}:{self.port}")
            print("⏳ Waiting for messages... (Press Ctrl+C to stop)\n")
            
            # Boucle d'écoute (bloquante)
            self.client.loop_forever()
            
        except KeyboardInterrupt:
            print("\n\n⏹️  Receiver stopped by user")
            self.disconnect()
        except Exception as e:
            print(f"❌ Connection error: {e}")
    
    def disconnect(self):
        """Déconnexion propre"""
        self.client.disconnect()
        print(f"\n📊 Total messages received: {len(self.received_messages)}")
        print("🔌 Disconnected from MQTT Broker")
    
    def get_statistics(self):
        """Statistiques sur les messages reçus"""
        if not self.received_messages:
            print("No messages received yet")
            return
        
        total = len(self.received_messages)
        anomalies = sum(1 for msg in self.received_messages 
                       if msg['data'].get('status') == 'anomaly')
        
        print(f"\n📊 Statistics:")
        print(f"   Total messages: {total}")
        print(f"   Normal: {total - anomalies}")
        print(f"   Anomalies: {anomalies} ({anomalies/total*100:.1f}%)")


if __name__ == "__main__":
    print("=" * 60)
    print("📡 IoT DATA RECEIVER - BOOTCAMP 5.0")
    print("=" * 60)
    
    receiver = IoTDataReceiver(broker_address="localhost", port=1883)
    receiver.connect_and_listen()