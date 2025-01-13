import zmq

context = zmq.Context()

sender = context.socket(zmq.PUSH)
sender.connect("tcp://<Broker_Hamachi_IP>:5555")

receiver = context.socket(zmq.PULL)
receiver.connect("tcp://<Broker_Hamachi_IP>:5558")

sentences = ["Sentence 1", "Sentence 2"]

sender.send_pyobj(sentences)

result = receiver.recv_pyobj()
print(f"Client : embedding reçu -> {result}")
