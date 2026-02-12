# 🚀 Guide Hackathon - Jour J

## ⏰ Timeline Recommandée (24h)

### Heures 0-2: Compréhension
- [ ] Lire le brief complet
- [ ] Poser des questions au jury
- [ ] Brainstorming équipe
- [ ] Définir le MVP (Minimum Viable Product)

### Heures 2-4: Architecture
- [ ] Dessiner l'architecture système
- [ ] Choisir les technologies
- [ ] Répartir les tâches
- [ ] Setup environnement

### Heures 4-12: Développement Core
- [ ] Backend API
- [ ] Intégration données
- [ ] Algorithmes principaux
- [ ] Points d'équipe toutes les 2h

### Heures 12-18: Features & Integration
- [ ] Frontend/Dashboard
- [ ] Tests d'intégration
- [ ] Optimisations
- [ ] Debugging

### Heures 18-22: Finition
- [ ] Polish UI/UX
- [ ] Documentation code
- [ ] Préparer démo
- [ ] Slides présentation

### Heures 22-24: Présentation
- [ ] Répéter le pitch (5-10 min)
- [ ] Tester la démo 3x
- [ ] Backup du code
- [ ] Repos mental

## 🎯 Checklist Technique

### Avant de commencer
- [ ] Git configuré et repo créé
- [ ] Tous les outils installés
- [ ] Templates de code prêts
- [ ] APIs testées

### Pendant le développement
- [ ] Commits réguliers (toutes les heures)
- [ ] Code commenté
- [ ] README à jour
- [ ] Tests basiques

### Avant la présentation
- [ ] Code sur GitHub
- [ ] Démo fonctionnelle
- [ ] Plan B si démo crash
- [ ] Slides clairs et concis

## 💡 Tips Développement Rapide

### Code Quality vs Speed
✅ DO:
- Code fonctionnel > Code parfait
- Commentaires pour logique complexe
- Noms de variables clairs
- Structure de fichiers logique

❌ DON'T:
- Sur-optimiser prématurément
- Features non-essentielles
- Refactoring excessif
- Tests unitaires exhaustifs

### Gestion du Temps
- Timebox chaque tâche (max 2-3h)
- Si bloqué >30min → demander de l'aide ou changer d'approche
- Garder 6h minimum pour finition + présentation

### Collaboration
- Stand-up meetings rapides (15min max)
- Utiliser les branches Git
- Documenter les décisions importantes
- Communiquer les blocages immédiatement

## 🎤 Structure de Présentation

### 1. Le Problème (1 min)
- Quel problème avez-vous résolu?
- Pourquoi c'est important?
- Impact business/environnemental

### 2. La Solution (2 min)
- Votre approche
- Technologies utilisées
- Architecture système

### 3. La Démo (3-4 min)
- Montrer le produit fonctionnel
- Scénario d'usage concret
- Mettre en avant les features clés

### 4. Impact & Next Steps (1 min)
- Résultats/métriques
- Évolutions possibles
- Scalabilité

### 5. Q&A (2-3 min)
- Anticiper les questions techniques
- Préparer les réponses sur les choix

## 🚨 Troubleshooting Rapide

### API ne répond pas
```bash
# Vérifier si le processus tourne
ps aux | grep python

# Vérifier les ports
netstat -ano | findstr :8000

# Logs Docker
docker logs <container_id>
```

### MQTT ne fonctionne pas
```bash
# Tester la connexion
mosquitto_sub -h localhost -t test

# Vérifier le service
sudo systemctl status mosquitto
```

### Frontend ne se connecte pas au backend
- Vérifier CORS dans FastAPI
- Vérifier l'URL de l'API
- Ouvrir la console du navigateur (F12)

## 📝 Phrases Clés pour le Pitch

"Nous avons identifié que..."
"Notre solution permet de..."
"En utilisant [technologie], nous pouvons..."
"Cela se traduit par [impact mesurable]..."
"À l'échelle, cela représente..."

## 🎓 Critères d'Évaluation (Typiques)

1. **Innovation** (25%)
   - Originalité de l'approche
   - Créativité de la solution

2. **Faisabilité Technique** (25%)
   - Qualité du code
   - Architecture système
   - Scalabilité

3. **Impact Business** (25%)
   - ROI potentiel
   - Valeur ajoutée
   - Adoption possible

4. **Présentation** (15%)
   - Clarté du pitch
   - Qualité de la démo
   - Communication

5. **Travail d'Équipe** (10%)
   - Collaboration
   - Répartition des tâches
   - Complémentarité

## ⚡ Emergency Contacts

- Coach: [Nom] - [Contact]
- Support technique: [Contact]
- Équipe: [Numéros de téléphone]

---
**Remember:** Done is better than perfect! 🚀