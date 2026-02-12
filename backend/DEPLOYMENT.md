# 🚀 Guide de Déploiement

## Local Development

### Backend
```bash
cd backend
pip install -r requirements.txt
cd app
python main.py
```

### Frontend
```bash
cd frontend
npm install
npm start
```

### MQTT Broker
```bash
# Démarrer Mosquitto
net start mosquitto  # Windows
brew services start mosquitto  # Mac
sudo systemctl start mosquitto  # Linux
```

## Docker Deployment

### Build et Run
```bash
docker-compose up --build
```

### Arrêter
```bash
docker-compose down
```

### Voir les logs
```bash
docker-compose logs -f
```

## Production Considerations

### Environment Variables
Copier `.env.example` vers `.env` et configurer:
```
API_PORT=8000
DEBUG=False
DATABASE_URL=your_production_db_url
MQTT_BROKER=your_mqtt_broker_address
```

### Security
- [ ] Changer les mots de passe par défaut
- [ ] Configurer CORS correctement
- [ ] Activer HTTPS
- [ ] Limiter les rate limits
- [ ] Monitoring et logs

### Scaling
- Utiliser un load balancer
- Scaling horizontal avec Docker Swarm ou Kubernetes
- Message queue pour MQTT (RabbitMQ/Kafka)
- Database clustering

## Troubleshooting

### Port déjà utilisé
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:8000 | xargs kill -9
```

### Dépendances manquantes
```bash
pip install --upgrade -r requirements.txt
```
```

**3. Mettre à jour `.gitignore`:**
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.venv
pip-log.txt
pip-delete-this-directory.txt

# Node
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Environment
.env
.env.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Data
data/raw/*
!data/raw/.gitkeep
data/processed/*
!data/processed/.gitkeep
*.csv
*.xlsx
*.db

# Docker
*.log

# Jupyter
.ipynb_checkpoints/