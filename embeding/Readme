# ZeroMQ Distributed Embedding System

## 📖 Description
Ce projet implémente un système distribué basé sur **ZeroMQ** pour calculer des embeddings de phrases à l'aide du modèle **Sentence-Transformers**. Les tâches sont envoyées par des clients, traitées par des workers, et les résultats sont retournés directement aux clients. Le système utilise une architecture simple sans serveur de résultats.

## 🚀 Fonctionnalités
- Distribution des tâches via **ZeroMQ**.
- Calcul d'embeddings à l'aide du modèle **paraphrase-multilingual-MiniLM-L12-v2**.
- Communication entre plusieurs machines via Hamachi pour simuler un réseau distribué.
- Logs de débogage pour un suivi détaillé des échanges entre les composants.

## 🏗️ Architecture
Le système comprend les composants suivants :
1. **Broker** :
   - Reçoit les tâches des clients.
   - Transmet les tâches aux workers.
2. **Worker** :
   - Reçoit les tâches du broker.
   - Calcule les embeddings et retourne les résultats directement aux clients.
3. **Client** :
   - Envoie des tâches au broker.
   - Reçoit les résultats des workers.

### Flux de données :
1. **Client** → **Broker** : Transmission des tâches.
2. **Broker** → **Worker** : Distribution des tâches.
3. **Worker** → **Client** : Envoi des résultats.

## 🛠️ Pré-requis
1. **Python 3.8+**
2. Bibliothèques Python :
   - `pyzmq`
   - `sentence-transformers`
   - `transformers`
   - `torch`
3. **Hamachi** (pour les connexions entre machines sur un réseau privé virtuel).

## 🧩 Installation
1. Clonez le dépôt :
   ```bash
   https://github.com/lordmams/TP5-Zeromq.git
   cd embeding
