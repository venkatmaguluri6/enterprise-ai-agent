# Day 4 — FastAPI Production Patterns + LLM Integration

# Daily Reading + Interview Preparation + Coding Practice

## 1. Daily Reading

### Today's goal

Move from:

FastAPI = "I can create endpoints"

to:

FastAPI = "I can design a production-style GenAI API."

Core architecture:

```
Client
  ↓
FastAPI Route
  ↓
Dependency
  ↓
Service Layer
  ↓
RAG / LLM / External API
  ↓
Response Model
```

### APIRouter

APIRouter separates related endpoints into modules.

Example:

```python
router = APIRouter(prefix="/search", tags=["Search"])
```

**Memory:** Router = organize APIs.

### Service Layer

Keep HTTP concerns in routes and business logic in services.

```
Route receives
    ↓
Service thinks
    ↓
Repository / external API talks
```

For GenAI:

```
POST /chat
   ↓
ChatService
   ↓
LLMService
   ↓
LLM provider
```

### Dependency Injection

FastAPI uses `Depends()`.

```python
def get_llm_service():
    return LLMService()

@app.post("/chat")
async def chat(request: ChatRequest, llm_service=Depends(get_llm_service)):
    ...
```

**Memory:** Depends = give the function what it needs.

Useful for auth, DB sessions, settings and reusable services.

### Configuration and secrets

Never hardcode API keys.

Use environment variables locally and a proper secret-management system in production.

```
LLM_MODEL=...
LLM_API_KEY=...
```

**Interview phrase:** "Configuration is externalized from application code."

### HTTPException and status codes

```
200 → success
201 → created
400 → bad request
401 → authentication required
403 → forbidden
404 → not found
422 → validation error
500 → server error
```

**Memory:** 400=request problem, 401=who are you?, 403=known but not allowed, 404=not found, 422=validation problem, 500=server problem.

### Middleware

Middleware wraps request/response processing.

Uses: logging, request IDs, timing, CORS, metrics and security processing.

### Async in GenAI

LLM APIs, vector databases and external tools are often I/O-bound.

Async allows other ready tasks to make progress while I/O is waiting.

**Trap:** async does not automatically make blocking code non-blocking.

### Streaming

LLMs generate output progressively.

```
Request → token → token → token → ...
```

Python generators use `yield` to produce values incrementally.

**Memory:** return = final result; yield = pieces.

### LLM Service

Don't call the LLM directly from every route.

Prefer:

```
FastAPI
  ↓
Chat Route
  ↓
Chat Service
  ↓
LLM Service
  ↓
LLM Provider
```

This makes provider logic easier to replace, mock and test.

---

## 2. GenAI Architecture

Today's project:

```
Client
  ↓
FastAPI
  ↓
APIRouter
  ↓
Pydantic
  ↓
Service
  ↓
Mock LLM
```

Future:

```
FastAPI
  ↓
Agent Service
  ↓
LangGraph
  ├── RAG
  ├── MCP tools
  └── external APIs
       ↓
      LLM
```

---

## 3. Most Important Interview Questions

### Q1. Why use APIRouter?
It separates related endpoints into modules and keeps a large FastAPI application maintainable.

**Hack:** Router = organize APIs.

### Q2. What is a service layer?
A layer that contains business/application logic while routes handle HTTP concerns.

**Hack:** Route receives → Service thinks.

### Q3. What is dependency injection?
Providing required components to a function from outside instead of constructing them inside the function.

### Q4. What is Depends()?
FastAPI's mechanism for resolving and injecting dependencies.

### Q5. How should API keys be managed?
Use environment variables or a secret-management service, not source code.

### Q6. What is middleware?
A layer that can run around request/response processing for cross-cutting concerns such as logging, timing and CORS.

### Q7. What is HTTPException?
FastAPI's exception type for returning an HTTP error status and detail.

### Q8. Why is streaming important in GenAI?
LLMs generate progressively, so streaming lets clients receive output incrementally instead of waiting for the complete answer.

### Q9. Why use async for LLM APIs?
LLM calls are network I/O, so async lets the server work on other tasks while waiting.

### Q10. What happens if blocking code runs inside an async endpoint?
It can block the event-loop thread and reduce concurrency. Use an async-compatible library or move suitable blocking work to a worker thread.

### Q11. Why separate LLMService from the route?
It isolates provider-specific logic, improves testing and makes provider replacement easier.

### Q12. How would you design a GenAI API?
FastAPI → Router → Pydantic → Service → RAG/Agent/Tools → LLM → Response.

---

## 4. Interview Traps / Hacks

1. APIRouter is for organization, not business logic.
2. Depends() is dependency injection.
3. async does not mean every operation is non-blocking.
4. Never hardcode secrets.
5. Middleware is for cross-cutting concerns.
6. Streaming is especially relevant to LLM chat APIs.
7. Keep routes thin.
8. LLM provider code belongs behind a service abstraction.

---

## 5. 30-Second Interview Answer

> I would design the FastAPI GenAI backend with APIRouter for modular endpoints, Pydantic for request and response contracts, Depends for reusable dependencies, and a service layer for business logic. Configuration and secrets would be externalized. LLM and vector-store calls would use async-compatible clients where possible. For chat APIs, I would support streaming so generated tokens can be returned progressively. The service layer would coordinate RAG, agents, tools and LLM calls.

---

## 6. Quick Revision Structure

```
FASTAPI PRODUCTION
│
├── APIRouter → organize
├── Pydantic → validate
├── Depends → inject
├── Service → business logic
├── Config → environment/secrets
├── HTTPException → errors
├── Middleware → cross-cutting
├── Async → I/O concurrency
└── Streaming → progressive output
```

GenAI:

```
Route
  ↓
Service
  ↓
RAG / Agent / Tools
  ↓
LLM
```

---

## 7. Coding Practice

### Exercise 1 — Run the API

```bash
uvicorn app.main:app --reload
```

Check `/docs` and `/redoc`.

### Exercise 2 — Search API

GET:

```
/search/?query=What%20is%20RAG%3F&top_k=2
```

POST:

```json
{"query":"What is RAG?","top_k":2}
```

### Exercise 3 — Chat API

POST `/chat/`:

```json
{"message":"Explain RAG in simple terms"}
```

Expected shape:

```json
{"message":"Explain RAG in simple terms","answer":"Mock answer from mock-llm: ..."}
```

### Exercise 4 — Validation

Try `{}` and `{"message":""}`. Both should return HTTP 422.

### Exercise 5 — Explain the code

Without looking at notes:

```
main.py
  ↓
chat router
  ↓
Depends()
  ↓
ChatService
  ↓
LLMService
  ↓
mock response
```

### Exercise 6 — Testing

```bash
pytest
```

---

## 8. 20-Minute Daily Routine

5 min → Read today's theory.

5 min → Answer the 12 interview questions aloud.

5 min → Run `pytest` and test /search and /chat.

5 min → Explain the architecture without notes.

---

## 9. Day 4 Completion Checklist

- [ ] Understand APIRouter
- [ ] Understand service layer
- [ ] Understand Depends()
- [ ] Understand environment-based configuration
- [ ] Understand HTTP errors
- [ ] Understand middleware
- [ ] Understand async in GenAI
- [ ] Understand streaming
- [ ] Understand LLM service abstraction
- [ ] Run tests successfully
- [ ] Explain the architecture in 30 seconds
