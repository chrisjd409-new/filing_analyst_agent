# Empty ChromaDB database
import chromadb
import json

client = chromadb.PersistentClient(path='data/chroma_db')
apple_10k = client.get_or_create_collection(name='apple_10k')

# Load downloaded json
with open ('data/apple_first_10k_chunks.json', 'r', encoding = 'utf-8') as f:
    loaded = json.load(f)

# Check if loaded correctly
print(len(loaded))

# Check number of collections
print(apple_10k.count())
