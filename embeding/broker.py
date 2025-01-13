import zmq

context = zmq.Context()

# Socket pour les clients
frontend = context.socket(zmq.PULL)
try:
    frontend.bind("tcp://25.31.219.243:5555")
    print("[DEBUG] Frontend lié avec succès sur tcp://25.31.219.243:5555.")
except Exception as e:
    print(f"[ERROR] Erreur lors de la liaison du frontend : {e}")

# Socket pour les workers
backend = context.socket(zmq.PUSH)
try:
    backend.bind("tcp://25.30.255.204:5556")
    print("[DEBUG] Backend lié avec succès sur tcp://25.30.255.204:5556.")
except Exception as e:
    print(f"[ERROR] Erreur lors de la liaison du backend : {e}")

print("Broker prêt : connecte les clients et les workers.")

while True:
    try:
        task = frontend.recv()  # Recevoir une tâche du client
        print(f"[DEBUG] Tâche reçue du client : {task}")
        backend.send(task)  # Transmettre la tâche au worker
        print("[DEBUG] Tâche transmise au worker.")
    except Exception as e:
        print(f"[ERROR] Erreur pendant le traitement de la tâche : {e}")
