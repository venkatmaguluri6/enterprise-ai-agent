# Day 6 — Daily Reading + Coding Practice

This file is intentionally self-contained so it can be used for daily revision.

---

# Part 1 — Daily Reading

## Mental model

```
Document
  ↓
Chunk
  ↓
Embedding
  ↓
Vector Store

Question
  ↓
Embedding
  ↓
Similarity Search
  ↓
Top-K Chunks
  ↓
Context
  ↓
LLM
  ↓
Answer
```

### The most important idea

RAG separates two jobs:

**Retrieval:** find useful information.

**Generation:** write the answer using that information.

---

## Embedding

An embedding converts information into a vector representation.

```
"Python developer"
        ↓
[0.13, -0.27, 0.81, ...]
```

In real applications, the vector is produced by an embedding model.

Today's code uses a tiny deterministic bag-of-words vectorizer only to understand the mechanics. It is NOT a production embedding model.

---

## Similarity

If two vectors point in similar directions, their cosine similarity is high.

```
Query vector
     ↘
      ↘
       Document vector
```

This allows semantic-style retrieval.

---

## RAG

```
Question
   ↓
Retrieve
   ↓
Relevant context
   ↓
LLM
   ↓
Answer
```

### Memory

**RAG = Retrieve + Augment + Generate**

---

# Part 2 — GenAI Connection

Suppose your company has 10,000 internal documents.

A user asks:

```
"What is our production deployment approval process?"
```

We should not send all 10,000 documents to the LLM.

Instead:

```
10,000 documents
      ↓
chunk + embed
      ↓
vector store
      ↓
query embedding
      ↓
retrieve top candidates
      ↓
filter/rerank
      ↓
send useful context
      ↓
LLM
```

This is the foundation of an enterprise RAG system.

---

# Part 3 — Memory Tricks

| Concept | Remember |
|---|---|
| Embedding | Text → Vector |
| Semantic search | Meaning |
| Cosine | Angle |
| Vector DB | Store/Search vectors |
| Chunking | Big document → useful pieces |
| Top-K | Best K candidates |
| RAG | Retrieve → Context → Generate |
| Retriever | Finds |
| Generator | Writes |
| Poor RAG | Check retrieval before blaming LLM |

### RAG formula

**Chunk → Embed → Store → Query → Embed → Retrieve → Ground → Generate**

---

# Part 4 — Important Interview Questions

### Q1. What is an embedding?

An embedding is a numerical vector representation of information. Similar semantic content tends to be represented by nearby vectors.

### Q2. What is RAG?

RAG retrieves relevant external knowledge and provides it to an LLM as context before generating an answer.

### Q3. Why chunk documents?

To retrieve smaller, relevant pieces instead of sending entire documents.

### Q4. Why use Top-K?

To limit retrieval to the highest-ranked candidates and control context size, latency and cost.

### Q5. Why can RAG hallucinate?

Because retrieval can be wrong/incomplete and the LLM can still misinterpret or generate unsupported content.

### Q6. Why not retrieve everything?

More context increases cost and latency and can introduce noise, contradictions and context-window pressure.

---

# Part 5 — Coding Practice

## Exercise 1 — Create a tiny embedding

Implement a deterministic vector representation for a sentence.

Input:

```text
"python fastapi rag"
```

Output can be a simple normalized vector based on a fixed vocabulary.

Do NOT try to build a real neural embedding model.

Goal: understand:

```
text → vector
```

---

## Exercise 2 — Cosine similarity

Implement:

```
cosine_similarity(a, b)
```

Test:

```
[1, 0] vs [1, 0] → 1
[1, 0] vs [0, 1] → 0
```

Also handle zero vectors safely.

---

## Exercise 3 — Top-K retrieval

Create five document chunks:

```
"FastAPI is a Python API framework"
"RAG retrieves relevant context"
"AWS Lambda is serverless"
"Python supports async programming"
"Vector search compares embeddings"
```

Given a query:

```
"How does RAG retrieve information?"
```

Return the top 2 chunks using your similarity function.

---

## Exercise 4 — Build a tiny RAG flow

Implement:

```
query
 ↓
query vector
 ↓
retrieve_top_k
 ↓
build_context
 ↓
mock_generate
```

The final generator can simply return:

```
"Answer based on: <retrieved context>"
```

The purpose is to understand the architecture, not to create a real LLM.

---

# Part 6 — Production Thinking

Ask yourself:

### Retrieval is bad. What do I check?

```
Chunking
Embedding model
Query
Top-K
Metadata filters
Hybrid search
Reranking
```

### Retrieval is good but answer is bad?

Check:

```
Context construction
Prompt
LLM
Generation settings
Grounding/evaluation
```

This separation is very important in AI Engineer interviews.

---

# Part 7 — 20-Minute Daily Routine

### 0–5 min

Read:

- Embedding
- cosine similarity
- vector database
- RAG

### 5–10 min

Explain without looking:

> "How does RAG work?"

### 10–15 min

Implement cosine similarity and Top-K retrieval.

### 15–20 min

Answer verbally:

1. What is an embedding?
2. What is RAG?
3. Why chunk documents?
4. Why not retrieve 100 chunks?
5. Why can RAG hallucinate?

---

# Final Cheat Sheet

```
EMBEDDING
Text → Vector

VECTOR SEARCH
Query Vector → Similar Vectors

RAG
Retrieve → Context → Generate

INDEXING
Load → Chunk → Embed → Store

QUERY
Embed Query → Search → Rank → Context → LLM

DEBUG RAG
Query → Chunk → Embed → Retrieve → Rank → Context → LLM
```

### One sentence to remember

**"RAG does not make the LLM smarter; it gives the LLM better external context at inference time."**
