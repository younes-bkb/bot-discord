# Bot Discord Simple

Un bot Discord simple créé avec Python et la bibliothèque discord.py, offrant des commandes de base pour interagir avec votre serveur

## Commandes disponibles

- `!bonjour` - Le bot vous salue
- `!ping` - Répond "Pong !"
- `!pileouface` - Lance une pièce (Pile ou Face)
- `!roll` - Lance un dé (1-6)
- `!clear [nombre]` - Supprime des messages (nécessite des permissions)

## Installation

1. **Installer discord.py** :
   ```bash
   pip install discord.py
   ```

2. **Créer votre bot** :
   - Allez sur https://discord.com/developers/applications
   - Créez une application → Bot → Copiez le token

3. **Configurer le script** :
   - Remplacez `"MonToken"` par votre token
   - ⚠️ Ne partagez jamais votre token !

4. **Lancer le bot** :
   ```bash
   python script.py
   ```

## Permissions nécessaires

Le bot a besoin de :
- Lire les messages
- Envoyer des messages  
- Gérer les messages (pour `!clear`)

## Utilisation

Tapez les commandes dans un salon Discord où le bot est présent :
```
!ping
!bonjour
!roll
!clear 5
```

---
**Note** : Remplacez votre token avant utilisation et gardez-le secret !
