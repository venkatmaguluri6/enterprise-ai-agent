# Day 3 — FastAPI Interview Questions

## Highest-priority 10

1. What is FastAPI?
Answer: A modern Python API framework using type hints, Pydantic validation/serialization, automatic OpenAPI documentation and async support.

2. FastAPI vs Flask?
Both build APIs. Flask is lightweight and familiar; FastAPI emphasizes API contracts, Pydantic, automatic OpenAPI docs, dependency injection and async support.

3. What is ASGI?
ASGI = Asynchronous Server Gateway Interface. It defines communication between async-capable Python servers and applications.

4. What is Uvicorn?
Uvicorn is an ASGI server commonly used to run FastAPI.

5. What is OpenAPI?
OpenAPI is a standard description of an API contract: endpoints, parameters, request bodies and responses.

6. Swagger UI vs ReDoc?
Both are generated from OpenAPI. /docs is Swagger UI and /redoc is ReDoc. Swagger UI is interactive documentation; Postman is an API client/testing tool.

7. Path parameter vs query parameter?
Path identifies a resource: /documents/123. Query controls options/filtering: /search?query=RAG&top_k=5.

8. What is Pydantic?
A Python library for structured data parsing/validation and serialization. FastAPI uses it heavily for request/response models.

9. Why does FastAPI use Pydantic?
It gives explicit API contracts and runtime validation for structured data and integrates with OpenAPI generation.

10. What happens when request data is invalid?
FastAPI validates it before calling the endpoint and returns a validation error response, commonly HTTP 422.

## Pydantic/API Design

11. Type hints vs Pydantic?
Type hints describe expected types and help static tooling. Pydantic validates/parses structured data at runtime.
Memory: Type hints describe; Pydantic validates.

12. What is a response model?
It defines the expected output structure, validates returned data and helps prevent unintended fields from being exposed.

13. What is request body validation?
FastAPI parses JSON using a Pydantic model and checks it against the declared schema.

14. What are common request locations?
Path = resource identity; query = filtering/options; body = structured payload; headers = metadata/authentication information.

## Async FastAPI

15. Can FastAPI endpoints be async?
Yes, with async def.

16. def vs async def?
Use async def when performing asynchronous I/O with async-compatible libraries. Do not assume async automatically makes blocking code non-blocking.

17. What if blocking code runs inside an async endpoint?
It can block the event-loop thread and reduce concurrency. Use an async-compatible library or move suitable blocking work to a worker thread.

18. When is async useful in GenAI APIs?
LLM APIs, vector stores, external tools, HTTP services and async database operations are common I/O-bound cases.

## Dependency Injection

19. What is dependency injection?
The framework provides reusable dependencies to an endpoint instead of the endpoint constructing them itself.

20. What is Depends()?
It tells FastAPI to resolve a dependency and pass its result to the endpoint.

21. How would you manage DB sessions?
Use a request-scoped dependency that creates/provides a session and guarantees cleanup. With SQLAlchemy, discuss session lifecycle, transactions, rollback and cleanup.

## Production

22. How would you structure a large FastAPI application?
Separate routes, schemas, services, repositories, models and core/configuration. Keep routes thin.

23. How do you handle errors?
Use correct HTTP status codes and clear details. HTTPException handles common endpoint-level errors; centralized handlers can standardize larger applications.

24. What is middleware?
Code that wraps request/response processing. Common uses are logging, CORS, request IDs, timing and metrics.

25. How do you test FastAPI?
Use TestClient for endpoint tests and async testing tools where appropriate. Test success paths, validation failures and important business behavior.

26. How do you deploy FastAPI?
Common production patterns use containers, a reverse proxy/load balancer and ASGI server processes/workers, plus DB/cache/RAG/LLM dependencies.

## GenAI

27. How would you design a RAG API?
POST /ask → Pydantic request → FastAPI route → RAG service → retrieval/ranking → LLM → Pydantic response. Keep route logic thin.

28. How does FastAPI work with LangGraph?
FastAPI exposes the endpoint; an agent service invokes LangGraph to manage state and workflow.

29. How does FastAPI work with MCP?
FastAPI can be the HTTP API layer while MCP provides a standardized protocol layer for compatible clients/agents to interact with tools/resources. They are different layers.

30. Why is FastAPI a good fit for your project?
I already have Flask/Django API experience, so routing, HTTP methods, middleware and API design are familiar. FastAPI adds type-hint-driven contracts, Pydantic validation, automatic OpenAPI docs, dependency injection and strong async support. I can use it as the API layer in front of RAG, LangGraph, MCP tools and LLM services.

## Interview traps
1. Say OpenAPI, not OpenAI, when explaining API documentation.
2. Swagger UI is not Postman.
3. Type hints alone do not provide general runtime validation.
4. Async improves overlap of I/O waits; it does not guarantee faster execution.
5. async def does not make blocking libraries non-blocking.

## 5 answers to memorize first
1. FastAPI = API framework + type hints + Pydantic + OpenAPI + async.
2. Pydantic = runtime parsing/validation + serialization for structured data.
3. ASGI = async-capable Python web interface.
4. Uvicorn = ASGI server for running FastAPI.
5. GenAI architecture = FastAPI → service → RAG/agent/tools → LLM.