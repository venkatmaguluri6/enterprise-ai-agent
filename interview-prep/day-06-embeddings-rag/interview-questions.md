# Day 6 — Important Interview Questions

## 1. What is an embedding?

### Answer

An embedding is a numerical vector representation of information such as text. It maps text into a vector space where semantically similar content tends to be closer together.

### Memory trick

**Text → Vector → Meaning**

---

## 2. What is the difference between token embedding and document embedding?

### Answer

Token embeddings represent individual tokens and are used inside an LLM. Document or sentence embeddings represent larger text units and are commonly used for semantic search and RAG.

### Trap

Do not say every embedding is used for vector databases. Token embeddings and retrieval embeddings serve different purposes.

---

## 3. What is semantic search?

### Answer

Semantic search retrieves information based on meaning rather than only matching exact keywords.

Example:

"How do I recover my account?"

can retrieve:

"Steps to regain access to your account."

---

## 4. What is cosine similarity?

### Answer

Cosine similarity measures how similar two vectors are based on the angle between them.

For normalized vectors, a higher dot product means greater similarity.

### Memory trick

**Cosine = vector angle**

---

## 5. What is a vector database?

### Answer

A vector database stores embeddings and supports efficient similarity or nearest-neighbor search. In a RAG system, it can retrieve document chunks that are semantically similar to a user's query.

---

## 6. Vector database vs SQL database?

### Answer

SQL databases are designed for structured relational operations, transactions, filtering and joins. Vector databases are optimized for similarity search over embeddings.

They are complementary rather than direct replacements.

---

## 7. What is RAG?

### Answer

RAG stands for Retrieval-Augmented Generation. It retrieves relevant external information and supplies it as context to an LLM before generation.

### 30-second answer

> In RAG, documents are chunked and converted into embeddings and stored in a vector store. When a user asks a question, the query is embedded, relevant chunks are retrieved, and those chunks are passed to the LLM as context to produce a more grounded answer.

---

## 8. Why do we need chunking?

### Answer

Large documents are divided into smaller meaningful pieces so retrieval can return only the relevant information instead of passing an entire document to the LLM.

Chunk size and overlap affect retrieval quality and context usage.

---

## 9. What is Top-K retrieval?

### Answer

Top-K retrieval returns the K highest-ranked candidates for a query.

For example, K=5 means the retriever returns its five highest-ranked chunks.

### Trap

Top-K does not mean the five chunks are guaranteed to be correct.

---

## 10. Why can RAG still hallucinate?

### Answer

RAG can hallucinate because retrieval may return irrelevant or incomplete information, documents may conflict, the LLM may misunderstand the context, or the generation/prompting layer may introduce unsupported information.

---

## 11. RAG vs fine-tuning?

### Answer

RAG is primarily useful for giving a model access to external, private or changing knowledge at inference time. Fine-tuning changes model behavior using training examples.

### Memory trick

**Knowledge → RAG**

**Behavior → Fine-tuning**

---

## 12. Why shouldn't we send 100 retrieved chunks to the LLM?

### Answer

Because more context can increase token usage, latency and cost while adding irrelevant or conflicting information. It can also put pressure on the context window and reduce the signal-to-noise ratio.

A better approach is to retrieve, filter and rerank candidates and pass only useful context.

---

## 13. What is the difference between retrieval and generation?

### Answer

Retrieval finds relevant information. Generation uses the selected information and instructions to produce the final response.

### Memory trick

**Retriever finds. Generator writes.**

---

## 14. What is a basic RAG indexing pipeline?

### Answer

```
Documents
→ Load
→ Clean
→ Chunk
→ Embed
→ Store
```

This is generally performed before users ask questions.

---

## 15. What is the query-time RAG pipeline?

### Answer

```
Query
→ Embed
→ Search
→ Rank/filter
→ Build context
→ LLM
→ Answer
```

---

## 16. How would you debug poor RAG answers?

### Strong interview answer

> I would separate retrieval quality from generation quality. First I would inspect the query, chunking and embedding model, then evaluate whether the right documents are retrieved and whether Top-K is appropriate. If retrieval is reasonable, I would inspect reranking, context construction and prompt instructions. Finally I would evaluate the LLM's grounded generation.

### Memory

**Query → Chunk → Embed → Retrieve → Rank → Context → LLM**

---

## 17. What is metadata filtering?

### Answer

Metadata filtering restricts retrieval based on structured attributes before or during similarity search.

Example:

```
customer_id = 42
document_type = "policy"
department = "HR"
```

Then semantic search runs only against permitted/relevant records.

This is important for multi-tenant systems and access control.

---

## 18. What makes a good RAG system?

### Answer

A good RAG system needs:

- good document parsing
- meaningful chunking
- suitable embeddings
- strong retrieval
- metadata filtering
- reranking when necessary
- good context construction
- grounded prompting
- evaluation and observability

### Interview trap

Do not describe RAG as "just vector database + LLM."

---

## 19. Can a vector database understand the meaning of text by itself?

### Answer

No. An embedding model converts text into vectors. The vector database primarily stores and searches those vectors.

### Memory trick

**Embedding model creates meaning representation. Vector DB searches it.**

---

## 20. What would you improve if semantic search is missing relevant documents?

### Answer

I would investigate:

1. Chunking strategy
2. Embedding model
3. Query formulation
4. Top-K
5. Metadata filters
6. Hybrid keyword + vector retrieval
7. Reranking
8. Document quality

This naturally leads to our next retrieval topic: **hybrid search**.

---

# ⭐ 5 Questions to Memorize First

1. What is an embedding?
2. What is RAG?
3. How does a RAG pipeline work?
4. Why can RAG hallucinate?
5. Why isn't more retrieved context always better?

---

# 🎯 30-Second Interview Answer

> "I would implement RAG as an indexing pipeline and a query pipeline. During indexing, I load and clean documents, split them into meaningful chunks, generate embeddings and store the vectors with metadata. At query time, I embed the user query, retrieve the most relevant chunks using similarity search, optionally filter and rerank them, construct a controlled context and pass that context to the LLM. I would separately evaluate retrieval quality and generation quality because a good LLM cannot compensate for poor retrieval."

---

# ⚠️ Interview Traps

- Embedding ≠ token ID
- Vector DB ≠ embedding model
- RAG ≠ fine-tuning
- Top-K ≠ guaranteed correctness
- RAG ≠ zero hallucinations
- More context ≠ better answer
- Semantic search ≠ exact keyword search
- Vector DB does not replace SQL
