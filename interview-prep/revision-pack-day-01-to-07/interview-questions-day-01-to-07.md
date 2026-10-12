# Days 1–7: Interview Questions and Short Answers

Use active recall: answer each question aloud before reading the answer. Keep each first response to 30–60 seconds, then expand only when the interviewer asks.

## Python foundations

### 1. What is the difference between a list and a generator?
A list stores its items in memory and can be indexed/reused. A generator yields items lazily as they are requested, which can reduce memory usage for large or streaming workloads.

### 2. What is a context manager?
A context manager manages setup and cleanup around a block of code. The `with` statement ensures cleanup, such as closing a file, even when an exception occurs.

### 3. dataclass vs TypedDict vs Enum?
A dataclass defines a data-holding class; TypedDict describes a dictionary's expected keys/types for static checking; Enum defines a fixed set of named values.

### 4. Are Python type hints enforced at runtime?
Not by Python automatically. They help readability, IDEs, and static type checkers. Runtime validation requires explicit code or a library such as Pydantic.

## Async Python and concurrency

### 5. Explain concurrency vs parallelism.
Concurrency is overlapping progress among tasks; parallelism is simultaneous execution. Asyncio coordinates I/O tasks cooperatively, while multiprocessing can execute CPU-heavy work across processes.

### 6. Multithreading vs multiprocessing vs asyncio?
Asyncio is effective for many I/O operations with async-compatible libraries. Threads help integrate blocking I/O libraries. Processes can run CPU-heavy Python work in parallel but have higher overhead.

### 7. Why is time.sleep() dangerous inside async code?
It blocks the current thread and therefore can block the event loop. Use `await asyncio.sleep()` for an async wait, or move unavoidable blocking work to a thread pool.

### 8. How would you call three external APIs concurrently?
Use an async client and `asyncio.gather()` (or structured task management), with timeouts, bounded concurrency, and explicit handling for partial failures.

### 9. What does asyncio.to_thread() do?
It runs a synchronous blocking function in a separate thread so it doesn't block the event-loop thread. It's useful for blocking I/O, not generally a way to speed up CPU-bound Python code.

## FastAPI and backend design

### 10. Why FastAPI?
It supports type-driven request/response validation through Pydantic, async endpoints, dependency injection, and automatic OpenAPI documentation. It is commonly served with an ASGI server such as Uvicorn.

### 11. What is Pydantic used for?
It validates/parses incoming data against declared models and helps define response schemas. It makes API contracts explicit and testable.

### 12. Path parameter vs query parameter?
A path parameter identifies a resource, such as `/users/42`. A query parameter commonly filters or configures a result, such as `/users?active=true`.

### 13. What is dependency injection in FastAPI?
It provides reusable dependencies to endpoints, such as authentication, database sessions, configuration, or service objects. It reduces duplication and improves testability.

### 14. Why use a service layer?
It keeps business logic separate from HTTP route code. Services can be unit-tested and reused without needing to exercise the API layer.

### 15. How should an API handle external LLM failures?
Use timeouts, meaningful error mapping, bounded retries for transient failures, provider rate-limit handling, structured logging, and monitoring. Don't expose internal secrets or raw sensitive provider errors.

## LLM fundamentals

### 16. What is a token?
A tokenizer's unit of text processing. A token can represent a whole word, part of a word, punctuation, or another text unit.

### 17. What is the difference between token embeddings and document embeddings?
Token embeddings represent tokens inside a language model. Document/sentence embeddings represent larger text units for semantic search and retrieval.

### 18. Explain self-attention and Q/K/V.
Self-attention lets tokens combine information from other tokens. Queries express what a token is looking for, keys represent matchable features, and values carry information that is weighted and combined.

### 19. What is a context window?
The amount of token context a model can process in one interaction. The limit varies by model, and the prompt, retrieved chunks, and output all need to fit within the available budget.

### 20. Temperature vs top-p?
Temperature changes the sharpness/randomness of token sampling. Top-p restricts sampling to a set of likely tokens whose cumulative probability reaches a threshold. Neither guarantees truth.

### 21. What is a hallucination?
A model output that is false, fabricated, or unsupported by available evidence. Retrieval, grounding instructions, citations, abstention, and evaluation can reduce the risk but cannot guarantee elimination.

## Embeddings and RAG

### 22. What is an embedding model?
A model that maps text or other data into a numerical vector intended to capture useful semantic or task-specific relationships. Similarity between vectors can support semantic retrieval.

### 23. What is semantic search?
Search that retrieves content based on semantic similarity, not only exact keyword overlap. It can match differently worded text that expresses a similar meaning.

### 24. Why chunk documents?
To retrieve focused, relevant sections instead of passing whole documents. Chunk size balances context preservation against noise, token usage, and retrieval precision.

### 25. Explain the RAG pipeline.
Offline: load documents, clean, chunk, embed, and store vectors with text and metadata. Online: embed the question, retrieve and rank relevant chunks, build context, ask the LLM, and return an answer with sources.

### 26. Why use a vector database instead of only MySQL?
MySQL is strong for relational data, transactions, joins, and exact queries. A vector database is optimized for embedding similarity search. A system may use both, including metadata filters.

### 27. What is Top-K?
The number of highest-ranked retrieval candidates returned. A small K may miss evidence; a large K can add noise, latency, and token cost. Tune it using evaluation data.

### 28. Why can RAG still hallucinate?
The retriever may return irrelevant or incomplete evidence; documents may conflict; the prompt may be unclear; or the LLM may misinterpret or ignore context. RAG grounds the model but doesn't guarantee truth.

### 29. How would you debug an incorrect RAG answer?
Inspect retrieved chunks first. If retrieval is poor, check query, chunking, embeddings, filters, Top-K, hybrid search, and reranking. If retrieval is good, check context construction, prompt, model behavior, citations, and evaluation.

### 30. How do you reduce hallucinations?
Retrieve sufficient evidence, ground the prompt, tell the model to abstain when evidence is insufficient, return source references, and evaluate retrieval relevance, correctness, and faithfulness.

### 31. RAG vs fine-tuning?
RAG is commonly used to supply changing or private knowledge at query time. Fine-tuning adapts model behavior or task performance from examples. They solve different problems and can be combined.

## System design and production

### 32. Design a RAG question-answer endpoint.
Use a POST endpoint with Pydantic request/response models. Embed the question, retrieve and rank chunks, construct grounded context, call the LLM, and return an answer plus source references. Add auth, timeouts, rate limits, logs, metrics, and tests.

### 33. How would you improve a 15-second LLM endpoint under high concurrency?
Use an async HTTP client and non-blocking I/O; use threads only for blocking synchronous libraries. Add timeouts, connection pooling, bounded concurrency, provider rate-limit handling, caching where safe, metrics, and horizontal scaling.

### 34. Does async make the LLM generate faster?
Not necessarily. Async helps the application handle concurrent waits efficiently; it doesn't directly speed up the provider's model generation for one request.

### 35. Why not always send more chunks to the LLM?
More chunks can increase token cost and latency, introduce irrelevant or conflicting information, and crowd out useful context. Retrieve, rank, filter, and evaluate rather than maximizing quantity.

### 36. What should you monitor in a production RAG system?
API latency and errors, retrieval latency and relevance, LLM latency, token usage/cost, timeout and rate-limit frequency, answer quality/faithfulness, and source/citation quality. Avoid logging secrets or sensitive content.

---

## Day 7 mock interview — answers to rehearse

### A. Multithreading, multiprocessing, and asyncio
“Threads support concurrent I/O when using blocking libraries. Multiprocessing uses separate processes and can parallelize CPU-heavy Python work. Asyncio coordinates many I/O tasks efficiently when clients are asynchronous. For three async LLM calls, I'd use asyncio; for CPU-heavy calculations, consider multiprocessing; for a blocking sync library, use a thread pool.”

### B. Why not use time.sleep() in an async function?
“time.sleep blocks the event-loop thread, so other tasks on that loop cannot progress during the sleep. I would use await asyncio.sleep for a non-blocking wait, or move unavoidable blocking I/O to a thread pool.”

### C. Explain RAG end to end
“I'd load and clean documents, split them into meaningful chunks, embed each chunk, and store vectors with text and metadata. For each query, I'd embed the question, retrieve and rank relevant chunks, build a context with the question, and ask the LLM to generate an answer grounded in that context. I'd return source references and evaluate retrieval and answer quality separately.”

### D. Why use vector search with SQL?
“SQL is strong for structured relational data, joins, transactions, and exact filters. Vector search is optimized for retrieving semantically similar embeddings. A RAG application can use vector retrieval for relevant passages and SQL for business records or metadata constraints.”

### E. How do you debug incorrect RAG answers?
“I'd first inspect the retrieved chunks. If they don't contain the answer, I'd debug chunking, embeddings, filters, Top-K, and ranking. If they do contain the answer, I'd inspect context assembly, prompt instructions, and generation. I'd add abstention for insufficient evidence and evaluate against representative questions.”

### F. Embedding model vs LLM
“An embedding model converts text into vectors for semantic retrieval. An LLM generates text based on the question and context. In RAG, the embedding model helps find evidence and the LLM uses retrieved evidence to formulate an answer.”

### G. How do you reduce hallucination?
“I'd verify evidence quality, ground the prompt, instruct the model to abstain when evidence is insufficient, provide source references, and evaluate faithfulness and correctness. RAG reduces unsupported answers but does not guarantee truth.”

### H. Design a FastAPI RAG endpoint
“I'd create a POST endpoint with Pydantic request and response models. The service would embed the question, retrieve/rank chunks, construct context, call the LLM with a timeout, and return the answer and source metadata. I'd keep route and business logic separate and add authentication, logging, metrics, rate limiting, and tests.”

### I. Improve a slow LLM API
“I'd use async I/O to handle concurrent requests, timeouts and connection pooling to manage resources, bounded concurrency and retries to handle provider limits, caching for safe repeated work, and monitoring to identify bottlenecks. Async improves concurrency, not the model's intrinsic generation speed.”

### J. How to answer when you don't know?
Be honest and reason from fundamentals: “I haven't implemented that directly yet, but my understanding is… I'd validate it by…” Avoid pretending that a concept or implementation is production-ready when it isn't.

---

## Self-test scoring
For each answer, score yourself:
- **0:** can't explain it.
- **1:** can state a definition.
- **2:** can explain it and give a practical example.
- **3:** can explain trade-offs and failure modes.

Prioritize topics scoring 0–1 for tomorrow's revision.
