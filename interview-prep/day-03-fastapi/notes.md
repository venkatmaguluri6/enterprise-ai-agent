# Day 3 — FastAPI for GenAI Applications

## Goal
You already have Flask/Django web development experience, so FastAPI is not a new web-development world. Focus on the differences that matter in interviews and GenAI systems.

**FastAPI = Type hints + Pydantic + OpenAPI + Async + Dependency Injection**

## 1. What is FastAPI?
FastAPI is a modern Python framework for building APIs.

**Interview answer:** FastAPI uses Python type hints, Pydantic for runtime validation/serialization, automatic OpenAPI documentation, and supports async endpoints.

### GenAI connection
Client → FastAPI → validation → RAG/Agent service → LLM → response.

## 2. FastAPI vs Flask
You already know Flask, so explain it this way:

> I already have Flask/Django API experience, so routing, HTTP methods, middleware and API design are familiar. FastAPI adds strong type-hint-driven contracts, Pydantic validation, automatic OpenAPI documentation, dependency injection and strong async support.

| Flask | FastAPI |
|---|---|
| @app.route() | @app.get(), @app.post() |
| Type hints optional | Type hints central to API design |
| Validation often added separately | Pydantic integration |
| Docs need extra setup | OpenAPI docs generated automatically |
| Async depends on setup | ASGI-native |

## 3. ASGI
ASGI = Asynchronous Server Gateway Interface.

Think: Client → Uvicorn → ASGI → FastAPI

Memory: WSGI = traditional synchronous interface; ASGI = async-capable interface.

## 4. Uvicorn
Uvicorn is an ASGI server commonly used to run FastAPI.

uvicorn app.main:app --reload

app.main = Python module; app = FastAPI object; --reload = development reload.

## 5. OpenAPI, Swagger UI and ReDoc
FastAPI automatically generates an OpenAPI schema.

/docs → Swagger UI
/redoc → ReDoc

Important correction: say OpenAPI, not OpenAI.
OpenAPI = API contract/schema.
Swagger UI = interactive API documentation.
ReDoc = documentation UI.
Postman = API client/testing tool.

Swagger UI is useful for testing endpoints, but it is not the same product/category as Postman.

## 6. Path vs Query Parameters
Path: GET /documents/doc-123 — identifies the resource.
Query: GET /search?query=RAG&top_k=5 — controls filtering/search/options.

Memory: Path = WHICH. Query = HOW/FILTER.

## 7. Request Body + Pydantic
class SearchRequest(BaseModel):
    query: str
    top_k: int = 5

FastAPI uses the model to parse and validate JSON. Missing/invalid required input causes request validation to fail before endpoint business logic runs. Request validation errors commonly return HTTP 422.

## 8. Response Model
class SearchResponse(BaseModel):
    query: str
    results: list[str]
    total: int

response_model=SearchResponse makes the output contract explicit.

Interview answer: A response model defines the expected output structure, helps validate returned data, documents the API contract and can prevent unintended fields from being exposed.

## 9. Type Hints vs Pydantic
Type hints describe. Pydantic validates structured data at runtime.
Type hints help readability/static tooling. Pydantic parses/validates structured data and supports serialization.

## 10. def vs async def
Use async def when the endpoint performs asynchronous I/O and the libraries called support async.
GenAI examples: LLM API calls, vector DB calls, external tools, async database operations.

Trap: async def does not magically make blocking code non-blocking.

## 11. FastAPI + Day 2 AsyncIO
A future endpoint can do: POST /search → FastAPI → async service → Vector + BM25 + Metadata → combined result.

This is where your Day 2 concurrency knowledge becomes practical.

## 12. Dependency Injection
FastAPI uses Depends().

def get_current_user():
    return {"id": 1}

@app.get("/profile")
def profile(user=Depends(get_current_user)):
    return user

Real uses: authentication, authorization, DB sessions, configuration and shared services.
Memory: Depends = give this endpoint what it needs.

## 13. Error Handling
Use HTTPException for clear endpoint errors and correct status codes.

## 14. Middleware
Middleware wraps request/response processing.
Common uses: logging, CORS, request IDs, timing and metrics.
Memory: Request → Middleware → Route → Middleware → Response.

## 15. Testing
Use TestClient for endpoint tests. Test status codes, response JSON, path/query parameters, valid bodies and validation failures.
Run pytest.

## 16. Production structure
app/
  main.py
  api/
  schemas/
  services/
  repositories/
  models/
  core/

Keep routes thin. Put business logic in services.

## 17. GenAI architecture
Client → FastAPI → Pydantic → Agent/RAG service → RAG/LangGraph/MCP → LLM → Response model.

FastAPI is the API layer, not the LLM.

## 18. 30-second interview answer
> I already have Flask/Django API experience, so FastAPI was mainly a shift in API design rather than learning web development from scratch. FastAPI gives me type-hint-driven API definitions, Pydantic runtime validation and serialization, automatic OpenAPI documentation, dependency injection and strong async support. For a GenAI system, I can use it as the API layer in front of RAG, LangGraph, MCP tools and LLM services.

## Cheat sheet
FastAPI → API framework
ASGI → async-capable Python web interface
Uvicorn → ASGI server
Pydantic → validation + serialization
OpenAPI → API contract
Swagger UI → interactive API docs
ReDoc → documentation UI
Path → resource identity
Query → filtering/options
Body → structured input
Response model → output contract
Depends → dependency injection
async def → async endpoint
TestClient → API testing

## Biggest corrections from your answers
1. OpenAI → OpenAPI. OpenAPI is the API specification used for automatic docs.
2. Swagger UI ≠ Postman. Swagger UI is interactive documentation; Postman is an API client/testing tool.
3. ASGI means Asynchronous Server Gateway Interface.
4. Depends() is FastAPI's dependency-injection mechanism.
5. response_model defines the response contract.
6. async def is useful for async I/O, but does not make blocking code non-blocking.