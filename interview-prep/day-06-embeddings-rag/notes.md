# Day 6 — Embeddings, Vector Search & RAG Foundations

## 🎯 Goal

Understand the core architecture behind Retrieval-Augmented Generation (RAG) and be able to explain it clearly in an AI Engineer interview.

Today's mental model:

```
Documents
   ↓
Chunking
   ↓
Embedding
   ↓
Vector Store
   ↓
User Query
   ↓
Query Embedding
   ↓
Similarity Search
   ↓
Top-K Relevant Chunks
   ↓
LLM
   ↓
Grounded Answer
```

---

## 1. What is an embedding?

An embedding is a numerical vector that represents the meaning or characteristics of some information.

Example:

```text
"Python is a programming language"
        ↓
[0.12, -0.44, 0.81, ...]
```

The important idea is not the exact numbers. Similar meanings should generally produce vectors that are close in the embedding space.

### Memory trick

**Text → Vector → Meaning**

---

## 2. Token embedding vs document embedding

Do not confuse these in an interview.

### Token embedding

Used inside an LLM.

```
token → vector
```

Example:

```
"cat" → [0.2, -0.1, ...]
```

### Document/sentence embedding

Usually produced by an embedding model for semantic search.

```
document/chunk → vector
```

Used in RAG/vector search.

### Interview answer

> Token embeddings are representations used inside the language model, while document or sentence embeddings represent larger text units and are commonly used for semantic search and RAG.

---

## 3. What is semantic search?

Keyword search asks:

> "Do these words match?"

Semantic search asks:

> "Does this content mean something similar?"

Example:

Query:

```
How can I reset my password?
```

A keyword search may strongly prefer documents containing "reset" and "password".

Semantic search can also find:

```
Steps to recover access to your account
```

even though the wording is different.

---

## 4. What is cosine similarity?

Cosine similarity measures how similar two vectors are based on their direction.

Conceptually:

```
similar direction → high similarity
different direction → low similarity
```

Formula:

```
cosine_similarity(A, B)
= (A · B) / (||A|| ||B||)
```

For normalized vectors, this becomes especially convenient because the dot product represents cosine similarity.

### Memory trick

**Cosine = angle between vectors**

You usually do NOT need to derive the formula in an interview unless asked.

---

## 5. What is a vector database?

A vector database stores vectors and provides efficient similarity search.

Typical information:

```
ID
Text/chunk
Embedding vector
Metadata
```

Example:

```
document_id = "doc-101"
content = "AWS Lambda is serverless..."
embedding = [...]
metadata = {"source": "aws.pdf", "page": 10}
```

A production RAG system can then search for the vectors closest to the query vector.

---

## 6. Vector DB vs SQL DB

Do not say a vector database replaces SQL.

### SQL database

Best for:

- relational data
- transactions
- exact filtering
- joins
- structured queries

### Vector database

Best for:

- similarity search
- semantic retrieval
- nearest-neighbor queries
- embedding-based retrieval

In real systems they can work together.

Example:

```
Vector search → find relevant documents
SQL filter   → only documents for customer X
```

---

## 7. What is RAG?

RAG = **Retrieval-Augmented Generation**.

Instead of asking the LLM to answer only from its learned parameters:

```
Question → LLM → Answer
```

we retrieve relevant external information first:

```
Question
   ↓
Retrieve relevant knowledge
   ↓
Context
   ↓
LLM
   ↓
Answer
```

### 30-second interview answer

> RAG combines information retrieval with LLM generation. We convert documents into embeddings and store them in a vector store. For a user query, we create a query embedding, retrieve the most relevant chunks using similarity search, and provide those chunks as context to the LLM so the answer can be grounded in the retrieved information.

---

## 8. Why do we chunk documents?

Imagine a 200-page PDF.

Sending the entire PDF for every question is inefficient.

Instead:

```
Large document
      ↓
Small meaningful chunks
      ↓
Embed each chunk
      ↓
Retrieve only relevant chunks
```

Good chunking tries to preserve enough context while avoiding unnecessarily large chunks.

Chunking is a major RAG quality lever.

---

## 9. What is Top-K retrieval?

Top-K means:

> Return the K highest-ranked results.

Example:

```
query → vector search → top 5 chunks
```

If K = 5, the retriever returns its five highest-ranked candidates.

Important:

**Top-K is retrieval quantity, not automatically final answer quality.**

Too few → relevant information may be missed.

Too many → noise, cost, latency and context problems.

---

## 10. Why RAG can still hallucinate

RAG does NOT guarantee zero hallucinations.

Possible causes:

1. Wrong chunks retrieved
2. Relevant information missing
3. Poor chunking
4. Conflicting documents
5. LLM ignores or misinterprets context
6. Prompt/instruction problems
7. Untrusted retrieved content

This becomes important later when we study:

- reranking
- hybrid search
- hallucination defense
- guardrails
- document/tool poisoning defense

---

## 11. RAG vs fine-tuning

### RAG

Use when the model needs access to changing or private knowledge.

Examples:

- company policies
- internal documentation
- product manuals
- support knowledge base

### Fine-tuning

Use when you want to change model behavior/style/task performance using training examples.

Simple interview rule:

**Knowledge → RAG**

**Behavior/style/task adaptation → Fine-tuning**

This is a useful rule, but real systems can use both.

---

## 12. Basic RAG pipeline

### Offline/indexing phase

```
Documents
   ↓
Load
   ↓
Clean
   ↓
Chunk
   ↓
Embedding model
   ↓
Vector store
```

### Online/query phase

```
User query
   ↓
Query embedding
   ↓
Vector search
   ↓
Top-K chunks
   ↓
Prompt/context construction
   ↓
LLM
   ↓
Answer
```

### Interview memory trick

**Index → Embed → Store**

**Query → Embed → Retrieve → Generate**

---

## 13. What happens when retrieval is poor?

Do not immediately blame the LLM.

Debug the pipeline in this order:

```
Query quality
   ↓
Chunking
   ↓
Embedding model
   ↓
Retrieval
   ↓
Top-K
   ↓
Reranking
   ↓
Prompt/context
   ↓
LLM generation
```

This is a strong production interview answer.

---

## 14. Why not send 100 retrieved chunks?

More context is not automatically better.

Problems:

- larger token usage
- higher cost
- higher latency
- more irrelevant information
- conflicting information
- context-window pressure
- lower signal-to-noise ratio

A production system should retrieve, rank, filter and select useful context.

---

## 15. Our project connection

Our Enterprise AI Agent will eventually become:

```
FastAPI
   ↓
RAG Service
   ↓
Retriever
   ├── Vector Search
   └── Keyword Search
          ↓
      Reranking
          ↓
      LangGraph
          ↓
         MCP
          ↓
         LLM
          ↓
       Response
```

Today we are building the foundation for the Retriever.

---

## 🔥 Quick revision

Remember these 10 lines:

1. Embedding = text represented as a vector.
2. Similar meaning → generally similar vector.
3. Semantic search finds meaning, not just exact words.
4. Cosine similarity compares vector direction.
5. Vector DB stores/searches embeddings efficiently.
6. Chunking breaks large documents into useful retrieval units.
7. Top-K returns the highest-ranked candidates.
8. RAG = Retrieve → Context → Generate.
9. RAG grounds answers but does not guarantee truth.
10. More retrieved context is not always better.

### One-line memory formula

**Chunk → Embed → Store → Query → Embed → Retrieve → Ground → Generate**
