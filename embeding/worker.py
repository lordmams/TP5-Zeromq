import zmq
from sentence_transformers import SentenceTransformer

# Charger le modèle d'embedding
try:
    model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    print("[DEBUG] Modèle chargé avec succès.")
except Exception as e:
    print(f"[ERROR] Erreur lors du chargement du modèle : {e}")

def get_embedding(sentences):
    try:
        embeddings = model.encode(sentences)
        print(f"[DEBUG] Embeddings calculés pour les phrases : {sentences}")
        return embeddings
    except Exception as e:
        print(f"[ERROR] Erreur lors du calcul des embeddings : {e}")
        return None

context = zmq.Context()

# Socket pour recevoir les tâches du broker
receiver = context.socket(zmq.PULL)
try:
    receiver.connect("tcp://25.31.219.243:5556")
    print("[DEBUG] Connecté au broker sur tcp://25.31.219.243:5556.")
except Exception as e:
    print(f"[ERROR] Erreur lors de la connexion au broker : {e}")

# Socket pour envoyer les résultats au client
sender = context.socket(zmq.PUSH)
try:
    sender.connect("tcp://25.30.255.204:5557")
    print("[DEBUG] Connecté au client sur tcp://25.30.255.204:5557.")
except Exception as e:
    print(f"[ERROR] Erreur lors de la connexion au client : {e}")

print("Worker prêt à traiter les tâches.")

while True:
    try:
        sentences = receiver.recv_pyobj()  # Recevoir des phrases
        print(f"[DEBUG] Tâches reçues du broker : {sentences}")

        embeddings = get_embedding(sentences)  # Calculer les embeddings

        sender.send_pyobj(embeddings)  # Envoyer les résultats au client
        print("[DEBUG] Résultats envoyés au client.")
    except Exception as e:
        print(f"[ERROR] Erreur pendant le traitement de la tâche : {e}")
