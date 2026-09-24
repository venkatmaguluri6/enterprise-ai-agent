# Day 3 — FastAPI
# Daily Reading + Interview Preparation + Coding Practice

## 1. Daily Reading

### What is FastAPI?

FastAPI is a modern Python framework for building APIs.

**Interview answer:**

> FastAPI uses Python type hints, Pydantic for runtime validation and serialization, automatic OpenAPI documentation, and supports async endpoints.

**Memory:** FastAPI = Type hints + Pydantic + OpenAPI + Async + Depends.

### FastAPI vs Flask

You already have Flask/Django experience.

**Interview answer:**

> I already have Flask/Django API experience, so routing, HTTP methods, middleware and API design are familiar. FastAPI adds strong type-hint-driven contracts, Pydantic validation, automatic OpenAPI documentation, dependency injection and strong async support.

### ASGI

ASGI = **Asynchronous Server Gateway Interface**.

```
Client
  ↓
Uvicorn
  ↓
ASGI
  ↓
FastAPI
```

**Remember:** WSGI = traditional synchronous interface; ASGI = async-capable interface.

### Uvicorn

Uvicorn is an ASGI server commonly used to run FastAPI.

```bash
uvicorn app.main:app --reload
```

### OpenAPI, Swagger UI, ReDoc

FastAPI automatically generates an OpenAPI schema.

```
/docs  → Swagger UI
/redoc → ReDoc
```

**Important correction:** OpenAPI, not OpenAI.

- OpenAPI = API contract/schema
- Swagger UI = interactive API documentation
- ReDoc = documentation UI
- Postman = API client/testing tool

**Memory:** Contract → OpenAPI; UI → Swagger/ReDoc; Testing client → Postman.

### Path vs Query

Path:

`GET /documents/doc-123`

Identifies which resource.

Query:

`GET /search?query=RAG&top_k=5`

Controls search/filter/options.

**Hack:** Path = WHICH. Query = HOW/FILTER.

### Request Body + Pydantic

```python
class SearchRequest(BaseModel):
    query: str
    top_k: int = 5
```

Pydantic parses/validates structured request data at runtime.

If required data is missing/invalid, FastAPI rejects the request before endpoint business logic runs. Request validation commonly returns HTTP 422.

### Response Model

```python
class SearchResponse(BaseModel):
    query: str
    results: list[str]
    total: int
```

`response_model=SearchResponse` defines the expected output contract.

**Remember:** Request model = what comes in. Response model = what goes out.

### Type Hints vs Pydantic

**Type hints describe. Pydantic validates structured data at runtime.**

### def vs async def

Use `async def` when the endpoint performs asynchronous I/O and the libraries called support async.

GenAI examples:
- LLM APIs
- vector databases
- external tools
- async DB calls

**Trap:** async def does not make blocking code non-blocking.

### Dependency Injection

FastAPI uses `Depends()`.

```python
def get_current_user():
    return {"id": 1}

@app.get("/profile")
def profile(user=Depends(get_current_user)):
    return user
```

Uses: auth, DB sessions, config, shared services.

**Memory:** Depends = give this endpoint what it needs.

### Middleware

Middleware wraps request/response processing.

Common uses: logging, CORS, request IDs, timing, metrics.

```
Request
  ↓
Middleware
  ↓
Route
  ↓
Middleware
  ↓
Response
```

### Error Handling

Use appropriate HTTP status codes and `HTTPException` for common endpoint-level errors.

### Testing

Use `TestClient` for endpoint tests.

Test:
- status codes
- JSON response
- path/query parameters
- valid request body
- invalid request body

### Production Structure

```
app/
├── main.py
├── api/
├── schemas/
├── services/
├── repositories/
├── models/
└── core/
```

Keep routes thin; business logic belongs in services.

---

## 2. GenAI Architecture

```
Client
   ↓
FastAPI
   ↓
Pydantic
   ↓
Service
   ├── RAG
   ├── LangGraph
   └── MCP
   ↓
LLM
   ↓
Response model
   ↓
Client
```

**Important:** FastAPI is the API layer. It is not the LLM.

---

## 3. Most Important Interview Questions

### Q1. What is FastAPI?
A modern Python API framework using type hints, Pydantic, automatic OpenAPI documentation and async support.

### Q2. FastAPI vs Flask?
Both build APIs. FastAPI emphasizes API contracts, Pydantic, OpenAPI, dependency injection and async support.

### Q3. What is ASGI?
Asynchronous Server Gateway Interface.

### Q4. What is Uvicorn?
An ASGI server commonly used to run FastAPI.

### Q5. What is OpenAPI?
A standard description of an API contract.

### Q6. Swagger UI vs Postman?
Swagger UI is interactive API documentation generated from OpenAPI. Postman is an API client/testing tool.

### Q7. Path vs query parameter?
Path identifies a resource; query controls filtering/options.

### Q8. What is Pydantic?
A Python library for structured data parsing/validation and serialization.

### Q9. Why Pydantic in FastAPI?
For runtime validation, parsing, serialization and explicit API contracts.

### Q10. What happens when request data is invalid?
Validation fails before endpoint logic and FastAPI returns a validation error, commonly HTTP 422.

### Q11. Type hints vs Pydantic?
Type hints describe expected types; Pydantic validates structured data at runtime.

### Q12. What is a response model?
It defines the expected output structure and makes the response contract explicit.

### Q13. def vs async def?
Use async def for asynchronous I/O with async-compatible libraries.

### Q14. What if blocking code runs inside async endpoint?
It can block the event-loop thread and reduce concurrency.

### Q15. What is dependency injection?
The framework provides reusable dependencies instead of the endpoint constructing them directly.

### Q16. What is Depends()?
FastAPI's mechanism for resolving and injecting dependencies.

### Q17. What is middleware?
Code that wraps request/response processing, useful for logging, CORS, request IDs, metrics and timing.

### Q18. How do you test FastAPI?
Use TestClient and test success, validation and important business paths.

### Q19. How would you design a RAG API?
POST /ask → Pydantic request → FastAPI route → RAG service → retrieval/ranking → LLM → Pydantic response.

### Q20. Why is FastAPI a good fit for your project?
Because it combines API contracts, runtime validation, automatic docs, dependency injection and async support, while fitting naturally in front of RAG, agents, MCP and LLM services.

---

## 4. Interview Traps / Hacks

1. **OpenAPI, not OpenAI** for API documentation.
2. Swagger UI is **not Postman**.
3. Type hints **do not equal runtime validation**.
4. async does **not automatically mean faster**.
5. async def does **not make blocking libraries non-blocking**.
6. Path = **WHICH** resource.
7. Query = **HOW/FILTER**.
8. Request model = **IN**.
9. Response model = **OUT**.
10. Depends = **give the endpoint what it needs**.

---

## 5. 30-Second Interview Answer

> I already have Flask/Django API experience, so FastAPI was mainly a shift in API design rather than learning web development from scratch. FastAPI gives me type-hint-driven API definitions, Pydantic runtime validation and serialization, automatic OpenAPI documentation, dependency injection and strong async support. For a GenAI system, I can use it as the API layer in front of RAG, LangGraph, MCP tools and LLM services.

---

## 6. Quick Revision Structure

```
HTTP request
    ↓
Path / Query / Body
    ↓
Pydantic
    ↓
FastAPI Route
    ↓
Depends / Middleware
    ↓
Service
    ↓
RAG / Agent / MCP / LLM
    ↓
Response Model
    ↓
Client
```

---

## 7. Coding Practice

### Exercise 1 — Run API

```bash
uvicorn app.main:app --reload
```

Open:
- `/docs`
- `/redoc`

### Exercise 2 — Test Endpoints

- GET /
- GET /health
- GET /documents/doc-123
- GET /search?query=What%20is%20RAG?&top_k=5
- POST /search

POST body:

```json
{"query":"What is RAG?","top_k":2}
```

### Exercise 3 — Validation

Send:

```json
{"top_k":5}
```

Explain why it fails: `query` is required by `SearchRequest`.

### Exercise 4 — RAG API Design

Design:

```
POST /ask
```

Request:

```json
{"question":"What is RAG?","top_k":5}
```

Response:

```json
{
  "question":"What is RAG?",
  "answer":"RAG combines retrieval with generation.",
  "sources":["doc-1","doc-2"]
}
```

Architecture:

```
POST /ask
 ↓
Pydantic
 ↓
FastAPI
 ↓
AI service
 ↓
RAG
 ↓
LLM
 ↓
Response model
```

### Exercise 5 — Testing

Run:

```bash
pytest
```

### 20-Minute Routine

5 min → read Daily Reading.

5 min → answer the 20 questions aloud.

5 min → run/test the API.

5 min → explain the GenAI architecture without notes.
