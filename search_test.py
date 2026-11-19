# Retrieval Stage
import chromadb


client = chromadb.PersistentClient(path='data/chroma_db')        # same folder as before
apple_10k = client.get_collection(name="apple_10k")

questions = ['What is the total net sales of Apple?', 
             'What is the net sales of Samsung?',
             'How much did Apple spend on research?',
             "What are the risk related to China?"]

results = apple_10k.query(
    query_texts = questions,
    n_results=5
)
for i, question in enumerate(questions):
    print(f"Question: {question}")
    print("-"*40)

    ids = results['ids'][i]
    documents = results['documents'][i]
    distances = results['distances'][i]

    for chunk_ids, texts, distance in zip(ids, documents,distances):
        print(f"chunk_id: {chunk_ids} distance: {round(distance, 3)}")
        print(texts[:300])
        print("-" *40)


# list of questions
# 