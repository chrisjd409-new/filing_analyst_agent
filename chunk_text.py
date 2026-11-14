import json

# Chunking the texts after extract_text.py

with open('data/apple_first_10k.txt', encoding = 'utf-8') as f:
    text = f.read()





# Use for loop to chunk -> 2000 per chunk for now
chunks = [text[i:i+2000] for i in range(0, len(text), 1800)]



# Chunking it with records
records = [{"id": f"apple_10k_{i}", "text": c} for i,c in enumerate(chunks)]



# Saving as json
with open ("data/apple_first_10k_chunks.json", "w", encoding="utf-8") as f:
    json.dump(records, f, indent=2)


# Read it to check
with open('data/apple_first_10k_chunks.json', 'r', encoding='utf-8') as f:
    loaded = json.load(f)

print(len(loaded))
print(loaded[50]['id'])
print(loaded[50]['text'][0:10])