import zmq
from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")


def get_embedding(sentences):
   
    embeddings = model.encode(sentences)
    return embeddings

context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.connect("tcp://25.30.255.204:5556") 

sender = context.socket(zmq.PUSH)
sender.connect("tcp://25.30.255.204:5557")
print("Worker is ready to process tasks.")

while True:
   
    sentences = receiver.recv_pyobj()
    print(f"Worker received sentences: {sentences}")

    
    embeddings = get_embedding(sentences)

    
    sender.send_pyobj(embeddings)
    print("Worker sent embeddings back to the broker.")
