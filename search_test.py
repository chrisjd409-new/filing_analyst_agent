# Retrieval Stage
import chromadb

client = chromadb.PersistentClient(path='')


client = chromadb.PersistentClient(path='data/chroma_db')        # same folder as before
notes = client.get_collection(name="notes") 