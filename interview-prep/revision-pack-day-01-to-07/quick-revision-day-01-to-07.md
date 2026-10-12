# Days 1–7: 80/20 Quick Revision Pack

Use this for a 10–15 minute daily recall session. Read the question, answer aloud, then check the short answer.

## The one-minute roadmap

- **Day 1 — Python foundations:** type hints, dataclasses, TypedDict, enums, generators, context managers, exceptions, JSON, pathlib.
- **Day 2 — Async/concurrency:** event loop, coroutine, task, gather, I/O vs CPU, blocking calls, threads vs processes.
- **Day 3 — FastAPI:** routes, Pydantic validation, request/response models, dependencies, async endpoints, OpenAPI.
- **Day 4 — Production API patterns:** routers, service layer, dependency injection, configuration, HTTP errors, middleware, tests, timeouts.
- **Day 5 — LLM fundamentals:** tokens, token IDs, embeddings, Transformer, self-attention, Q/K/V, context window, temperature, top-p, hallucinations.
- **Day 6 — Embeddings and RAG:** chunking, vector search, cosine similarity, Top-K, metadata, RAG vs fine-tuning, retrieval debugging.
- **Day 7 — Mock interview:** explain concepts clearly, solve small coding problems, design a RAG API, discuss scalability.

---

## Day 1 — Python foundations

### Must remember
- **Type hints** communicate expected types; they do not enforce types at runtime by themselves.
- **dataclass** reduces boilerplate for classes mainly used to hold data.
- **TypedDict** describes the expected keys and value types of a dictionary for static type checkers.
- **Enum** represents a fixed set of named constants.
- **Generator** yields values lazily with `yield`, often reducing memory usage.
- **Context manager** manages setup/cleanup with `with`; files are closed even if an exception occurs.
- **Exceptions** should be handled specifically; don't hide unexpected failures with broad silent catches.
- **pathlib** provides object-oriented filesystem paths.

### Tiny examples
```python
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import TypedDict

class Status(str, Enum):
    PENDING = "pending"
    DONE = "done"

class SearchHit(TypedDict):
    text: str
    score: float

@dataclass
class Document:
    document_id: str
    text: str

def read_lines(path: Path):
    with path.open(encoding="utf-8") as file:
        for line in file:
            yield line.rstrip("\\n")
```

**Memory:** dataclass = data object; TypedDict = dictionary shape; Enum = fixed choices; generator = lazy values; context manager = reliable cleanup.

## Day 2 — Async Python and concurrency

### Three choices
| Approach | Best fit | Main caveat |
|---|---|---|
| `asyncio` | Many I/O waits using async-compatible clients | Blocking code still blocks the event loop |
| Threads | I/O with blocking synchronous libraries | Python threads generally don't provide parallel speedup for CPU-bound Python bytecode under the GIL |
| Multiprocessing | CPU-heavy Python work that benefits from parallel execution | Process startup, memory, and serialization overhead |

### Rules you should say aloud
- **Concurrency** means tasks make progress during overlapping time periods.
- **Parallelism** means work executes at the same time.
- `await asyncio.sleep(3)` yields control; `time.sleep(3)` blocks the current thread.
- Three async LLM/API calls: use `asyncio.gather()` with an async client.
- CPU-intensive pure-Python work: consider multiprocessing.
- Blocking sync library called from async code: use `asyncio.to_thread()` or a thread pool where appropriate.
- Use timeouts, bounded concurrency, and error handling for real external calls.

```python
import asyncio

async def call_service(client, url):
    return await client.get(url)

async def fetch_all(client, urls):
    return await asyncio.gather(
        *(call_service(client, url) for url in urls)
    )
```

**Memory:** Async = async I/O; threads = blocking I/O; processes = CPU parallelism.

## Day 3 — FastAPI foundations

- FastAPI is an ASGI framework; Uvicorn is a common ASGI server.
- Pydantic validates/parses input data and can define response schemas.
- Path parameters identify a resource; query parameters commonly filter, paginate, or configure a request.
- `Depends` provides reusable dependencies such as authentication, services, or database sessions.
- FastAPI exposes OpenAPI documentation, commonly at `/docs`.
- Use `async def` with async I/O clients. A synchronous blocking call inside an async endpoint can block the event loop.
- Test APIs with FastAPI's `TestClient` or async testing tools as appropriate.

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str = Field(min_length=1, max_length=4000)
    top_k: int = Field(default=5, ge=1, le=20)

class AnswerResponse(BaseModel):
    answer: str
    sources: list[str]

@app.post("/api/v1/chat", response_model=AnswerResponse)
async def chat(request: QuestionRequest) -> AnswerResponse:
    # Call retrieval and generation services here.
    return AnswerResponse(answer="Example answer", sources=[])
```

## Day 4 — Production API patterns

### Structure
**Router → service layer → provider/repository**, with dependencies injected rather than tightly coupling everything inside the route.

- **APIRouter:** groups related endpoints.
- **Service layer:** contains business logic and is easier to test independently.
- **Configuration:** keep environment-specific settings outside source code; never commit secrets.
- **HTTPException:** return meaningful HTTP errors for expected API failures.
- **Middleware:** cross-cutting behavior such as request IDs, timing, or CORS.
- **Timeouts:** prevent external requests from hanging indefinitely.
- **Retries:** only for appropriate transient failures; use limits/backoff and consider idempotency.
- **Tests:** test validation, success cases, failure cases, and service behavior.
- **Logging:** log useful metadata, but avoid secrets, tokens, and sensitive document contents.

## Day 5 — LLM fundamentals

- **Token:** a unit used by the model tokenizer; not necessarily one word.
- **Token ID:** integer ID assigned to a token by a tokenizer.
- **Token embedding:** vector representation used inside a model.
- **Document embedding:** vector for a sentence/chunk/document, commonly used for semantic retrieval.
- **Transformer:** architecture based on attention and feed-forward blocks.
- **Self-attention:** lets each token representation incorporate information from other tokens.
- **Q/K/V:** queries determine what a token seeks; keys represent matching features; values carry information to combine.
- **Positional information:** gives the model information about token order; RoPE is one approach.
- **Autoregressive generation:** predict the next token repeatedly, conditioning on prior tokens.
- **Context window:** amount of input/output token context a model can process; exact limits depend on the model.
- **Temperature:** affects sampling randomness; lower is generally more predictable, not guaranteed correct.
- **Top-p:** samples from a probability-mass nucleus of likely tokens.
- **Hallucination:** output that is false, unsupported, or fabricated.
- **RAG can provide evidence**, but does not guarantee that the answer is true.

**Memory:** tokenize → model processes context → predict next token repeatedly → decode output.

## Day 6 — Embeddings, vector search, and RAG

### Embedding model vs LLM
- Embedding model: text → vector for semantic similarity/retrieval.
- LLM: question + context → generated answer.
- Some model families offer both capabilities, but they are distinct tasks and may use separate models.

### RAG pipelines
**Offline/indexing:** Load → clean → chunk → embed each chunk → store vector + text + metadata.

**Online/query:** Question → embed query → retrieve candidates → rank/filter → build context → LLM → answer with sources.

### Key concepts
- **Chunking:** split long documents into useful retrieval units. Too small loses context; too large adds noise and token cost.
- **Semantic search:** finds meaning-related content even when exact wording differs.
- **Cosine similarity:** compares vector direction; it is one similarity measure, not a guarantee of factual relevance.
- **Top-K:** number of retrieved candidates. More is not always better.
- **Vector DB:** optimized for vector similarity search; can also support metadata filters.
- **SQL DB:** useful for relational data, joins, transactions, and exact conditions. SQL and vector stores can complement one another.
- **RAG vs fine-tuning:** RAG is often useful for changing/private knowledge; fine-tuning changes model behavior/task performance. They can be combined.
- **RAG failure:** inspect retrieved evidence first, then prompt/context construction and generation.

### RAG debugging checklist
1. Do the retrieved chunks actually contain evidence that answers the question?
2. Is chunking preserving the relevant context?
3. Is the query embedding/retriever appropriate?
4. Are metadata filters excluding useful documents?
5. Is Top-K too small or too large?
6. Would hybrid search or reranking improve results?
7. Is context assembled clearly and within the token budget?
8. Does the prompt tell the model to answer only from evidence and abstain when insufficient?
9. Are citations grounded in real retrieved sources?
10. Evaluate retrieval quality, answer correctness, and faithfulness separately.

**Memory formula:** Chunk → Embed → Store → Query → Embed → Retrieve → Rank → Ground → Generate.

## Day 7 — What interviewers want to hear

Use this answer structure:
1. **Define** the concept in one sentence.
2. **Explain** how it works.
3. **Give** a concrete project example.
4. **Mention** one trade-off or failure mode.

### System-design outline for a RAG API
- `POST /api/v1/chat`
- Pydantic request/response models
- Validate question and optional filters
- Embed question
- Retrieve and rank chunks
- Build grounded prompt
- Call LLM with timeout and bounded concurrency
- Return answer and source references
- Add authentication, rate limits, structured logs, metrics, tests, and caching where appropriate

### Scalability checklist for a slow LLM call
- Async HTTP client for concurrent I/O
- Thread pool only when a blocking synchronous library is required
- Connection pooling and request timeouts
- Bounded concurrency and provider rate-limit handling
- Controlled retries with backoff
- Cache embeddings or eligible repeated results
- Monitor latency, errors, token usage, and cost
- Scale API instances horizontally when needed

### Final 10-line cram sheet
1. Type hints document intent; they don't automatically validate runtime values.
2. Generators yield lazily; context managers clean up resources.
3. Async I/O yields while waiting; blocking calls can freeze the event loop.
4. Threads suit blocking I/O; processes can parallelize CPU-heavy Python work.
5. FastAPI + Pydantic gives validated API contracts.
6. A service layer separates business logic from HTTP routes.
7. Embedding model = vectors for retrieval; LLM = text generation.
8. RAG = retrieve evidence, add context, generate a grounded answer.
9. Debug retrieval before blaming the LLM.
10. RAG reduces unsupported answers only when evidence, prompts, and evaluation are sound.
