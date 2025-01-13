import zmq

context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5557")  
sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5558")  

print("Serveur de résultats prêt : envoie les résultats aux clients.")

while True:
    result = receiver.recv_pyobj()  
    sender.send_pyobj(result) 
