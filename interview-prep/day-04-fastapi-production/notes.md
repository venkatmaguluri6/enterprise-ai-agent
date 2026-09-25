# Day 4 — FastAPI Production Patterns + LLM Integration

## Goal

Move from basic FastAPI endpoint development to a production-style API architecture suitable for GenAI applications.

```
Client
  ↓
FastAPI
  ↓
APIRouter
  ↓
Pydantic
  ↓
Depends()
  ↓
Service Layer
  ↓
RAG / LLM / Tools
  ↓
Response
```

## 1. APIRouter

`APIRouter` helps split a large FastAPI application into smaller route modules.

Example:

```python
router = APIRouter(prefix="/search", tags=["Search"])
```

Then:

```python
app.include_router(search_router)
```

**Memory:** APIRouter = organize APIs.

---

## 2. Service Layer

Keep HTTP concerns in routes and business logic in services.

```
Route receives
    ↓
Service thinks
    ↓
Repository / External API talks
```

For GenAI:

```
Chat Route
    ↓
Chat Service
    ↓
LLM Service
    ↓
LLM Provider
```

**Memory:** Route receives → Service thinks → Repository/API talks.

---

## 3. Dependency Injection — Depends()

FastAPI provides dependency injection through `Depends()`.

```python
def get_llm_service():
    return LLMService()

@app.post("/chat")
async def chat(
    request: ChatRequest,
    llm_service=Depends(get_llm_service),
):
    ...
```

Common uses:
- Authentication
- Database sessions
- Configuration
- Shared services
- Permission checks
- LLM clients

**Memory:** Depends = give the function what it needs.

---

## 4. Configuration and Secrets

Never hardcode API keys.

Use environment variables locally and a proper secret-management solution in production.

```
LLM_MODEL=...
LLM_API_KEY=...
```

**Interview answer:**  
"I externalize configuration and secrets from application code using environment variables and, for production, a secret-management system."

---

## 5. HTTP Errors

| Code | Meaning |
|---|---|
| 200 | Success |
| 201 | Created |
| 400 | Bad request |
| 401 | Authentication required |
| 403 | Forbidden |
| 404 | Not found |
| 422 | Validation error |
| 500 | Server error |

Example:

```python
from fastapi import HTTPException

raise HTTPException(
    status_code=404,
    detail="Document not found",
)
```

**Memory:** 400=request problem, 401=who are you?, 403=known but no, 404=not found, 422=validation, 500=server problem.

---

## 6. Middleware

Middleware wraps request/response processing.

```
Request
  ↓
Middleware
  ↓
Route
  ↓
Service
  ↓
Response
  ↓
Middleware
  ↓
Client
```

Common uses:
- Logging
- Request IDs
- Timing
- CORS
- Metrics
- Security-related processing

For our AI platform, middleware can later feed observability and tracing.

---

## 7. Async in GenAI

LLM APIs, vector databases and external tools are often I/O-bound.

```
Request A → waiting for LLM
Request B → waiting for database
Request C → executing
```

Async allows other ready tasks to make progress while I/O is waiting.

**Interview trap:** async does not automatically make blocking code non-blocking.

---

## 8. Streaming

LLMs generate responses progressively.

Normal:

```
Request → wait → complete answer
```

Streaming:

```
Request → token → token → token → ...
```

Python generators use `yield` for incremental production.

**Memory:** return = final result; yield = pieces.

---

## 9. LLM Service Abstraction

Don't put provider-specific LLM code directly in every route.

Prefer:

```
FastAPI
   ↓
Chat Router
   ↓
Chat Service
   ↓
LLM Service
   ↓
LLM Provider
```

Benefits:
- Easier testing
- Easier mocking
- Provider replacement
- Cleaner routes
- Separation of concerns

Today we use a mock LLM; later we will replace it with a real provider.

---

## 10. Pydantic in GenAI APIs

Request:

```python
class ChatRequest(BaseModel):
    message: str
```

Response:

```python
class ChatResponse(BaseModel):
    message: str
    answer: str
```

**Important distinction:**

Type hints → describe expected types.

Pydantic → parses and validates structured data at runtime.

**Memory:** Type hints describe. Pydantic validates.

---

## 11. Current Day 4 Project Architecture

```
enterprise-ai-agent/
├── app/
│   ├── api/
│   │   └── routes/
│   │       ├── health.py
│   │       ├── search.py
│   │       └── chat.py
│   ├── core/
│   │   └── config.py
│   ├── models/
│   │   └── schemas.py
│   ├── services/
│   │   ├── search_service.py
│   │   ├── chat_service.py
│   │   └── llm_service.py
│   └── main.py
└── tests/
```

### POST /chat flow

```
Client
  ↓
FastAPI
  ↓
ChatRouter
  ↓
Pydantic ChatRequest
  ↓
Depends()
  ↓
ChatService
  ↓
LLMService
  ↓
LLM
  ↓
ChatResponse
  ↓
Client
```

---

## 12. Most Important Interview Questions

### Q1. Why use APIRouter?
It separates related endpoints into modules and keeps a large FastAPI application maintainable.

### Q2. What is a service layer?
It contains business/application logic while routes handle HTTP concerns.

### Q3. What is dependency injection?
Providing required components to a function from outside rather than constructing them directly inside it.

### Q4. What is Depends()?
FastAPI's mechanism for resolving and injecting dependencies.

### Q5. How should API keys be managed?
Use environment variables or a secret-management system, never source code.

### Q6. What is middleware?
A layer around request/response processing for cross-cutting concerns such as logging, timing, CORS and request IDs.

### Q7. Why is streaming important for GenAI?
LLMs generate output progressively, so streaming lets clients receive output incrementally.

### Q8. Why use async for LLM APIs?
LLM calls are generally network I/O, so async lets the server work on other tasks while waiting.

### Q9. What happens if blocking code runs inside an async endpoint?
It can block the event-loop thread and reduce concurrency.

### Q10. Why separate LLMService from the route?
It isolates provider-specific logic and makes testing, mocking and provider replacement easier.

### Q11. How would you design a GenAI API?

```
FastAPI
  ↓
Router
  ↓
Pydantic
  ↓
Service
  ↓
RAG / Agent / Tools
  ↓
LLM
  ↓
Response
```

---

## 13. Interview Traps

1. APIRouter is for organization, not business logic.
2. Depends() = dependency injection.
3. Async does not automatically mean faster.
4. Async does not make blocking libraries non-blocking.
5. Never hardcode API keys.
6. Middleware handles cross-cutting concerns.
7. Streaming is especially important for LLM chat APIs.
8. Keep routes thin.
9. LLM provider logic belongs behind a service abstraction.

---

## 14. 30-Second Interview Answer

> I would design the FastAPI GenAI backend using APIRouter for modular endpoints, Pydantic for request and response contracts, Depends for reusable dependencies, and a service layer for business logic. Configuration and secrets would be externalized. I would use async-compatible clients for I/O-bound LLM and retrieval calls and streaming for chat responses when appropriate. The service layer would coordinate RAG, agents, tools and LLM providers while keeping the API routes thin.

---

## 15. Quick Revision Cheat Sheet

```
APIRouter  → organize
Pydantic   → validate
Depends    → inject
Service    → business logic
Config     → environment/secrets
HTTPException → errors
Middleware → cross-cutting
Async      → I/O concurrency
Streaming  → progressive output
LLMService → isolate provider
```

### GenAI

```
Route
  ↓
Service
  ↓
RAG / Agent / Tools
  ↓
LLM
```

### Final memory formula

**R-P-D-S-C-E-M-A-S-L**

- R = Router
- P = Pydantic
- D = Depends
- S = Service
- C = Config
- E = Errors
- M = Middleware
- A = Async
- S = Streaming
- L = LLM Service

Before Day 5, explain these without notes:

1. Why APIRouter?
2. Why service layer?
3. What does Depends() do?
4. How do you protect API keys?
5. Why async for LLM calls?
6. Why streaming?
7. What happens with blocking code?
8. Why have an LLMService?
9. Explain POST /chat request flow.
10. Explain FastAPI → GenAI architecture.
