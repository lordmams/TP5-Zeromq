import zmq

context = zmq.Context()

frontend = context.socket(zmq.PULL)
frontend.bind("tcp://25.31.219.243:5555") 
backend = context.socket(zmq.PUSH)
backend.bind("tcp://25.30.255.204:5556")


print("Broker prêt : connecte les clients et les workers.")

while True:
    task = frontend.recv() 
    backend.send(task) 
