import zmq

context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.bind("tcp://25.30.255.204:5557")  
sender = context.socket(zmq.PUSH)
sender.bind("tcp://25.31.219.243:5558")  

print("Serveur de résultats prêt : envoie les résultats aux clients.")

while True:
    result = receiver.recv_pyobj()  
    sender.send_pyobj(result) 
