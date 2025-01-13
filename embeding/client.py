import zmq

context = zmq.Context()

# Socket pour envoyer les tâches au broker
sender = context.socket(zmq.PUSH)
try:
    sender.connect("tcp://25.31.219.243:5555")
    print("[DEBUG] Connecté au broker sur tcp://25.31.219.243:5555.")
except Exception as e:
    print(f"[ERROR] Erreur lors de la connexion au broker : {e}")

# Socket pour recevoir les résultats des workers
receiver = context.socket(zmq.PULL)
try:
    receiver.bind("tcp://25.30.255.204:5557")
    print("[DEBUG] Liaison réussie sur tcp://25.30.255.204:5557 pour recevoir les résultats.")
except Exception as e:
    print(f"[ERROR] Erreur lors de la liaison au port pour les résultats : {e}")

# Exemple de tâche
sentences = ["Phrase 1", "Phrase 2"]

try:
    sender.send_pyobj(sentences)
    print(f"[DEBUG] Tâches envoyées au broker : {sentences}")
except Exception as e:
    print(f"[ERROR] Erreur lors de l'envoi des tâches : {e}")

try:
    result = receiver.recv_pyobj()
    print(f"[DEBUG] Résultats reçus des workers : {result}")
except Exception as e:
    print(f"[ERROR] Erreur lors de la réception des résultats : {e}")
