# filing_analyst_agent

An AI agent that answers questions about company 10-K filings and cites the
exact passages it used. Built from scratch in Python with the Anthropic API and
ChromaDB. No LangChain, so every part of the pipeline is visible.

## Why I built this

10-Ks run 100+ pages, and finding one number means reading a lot. This project
retrieves the relevant passages for a question and has the LLM answer only from
them, citing each source so a reader can check the claim.

## How it works

```
10-K (HTML) -> clean text -> chunks -> embeddings in ChromaDB
Question -> retrieve top chunks -> Claude answers using only those chunks -> answer + citations
```

## Stages

### Stage 1: Call an LLM from Python (done)
- Set up the repo, a virtual environment, and API key handling with `.env`
- `hello_llm.py` sends a prompt to Claude and prints the reply

### Stage 2: Plain RAG on one 10-K (in progress)
Retrieval-augmented generation (RAG) on Apple's FY2026 10-K.
1. **Extract** (`extract_text.py`): parse the HTML with BeautifulSoup, remove hidden
   XBRL blocks, clean whitespace, save plain text
2. **Chunk** (`chunk_text.py`): split into overlapping chunks (overlap keeps
   sentences from being cut in half), give each an ID such as `apple_10k_50`,
   save as JSON
3. **Embed** (`embed_chunks.py`): store every chunk in a ChromaDB collection
   (planned)
4. **Retrieve** (`search_test.py`): check that top-5 results for sample
   questions are relevant (planned)
5. **Answer** (`ask.py`): send the question plus retrieved chunks to Claude and
   cite chunk IDs (planned)

### Stage 3: Evaluation (planned)
- Write 20 questions with known answers from the filing
- Measure how many the system answers correctly and whether it cites the right chunk
- Compare chunk sizes and number of retrieved chunks

### Stage 4: Make it agentic (planned)
- Give the model tools: `search_filings(company, query)`, `calculate(expression)`,
  `list_companies()`
- Write the agent loop by hand: the model decides to call a tool, reads the
  result, and repeats until it can answer
- Re-run the Stage 3 questions and compare against plain RAG

### Stage 5: Polish (planned)
- Streamlit page for asking questions
- Write up design choices and evaluation results
- Short demo video