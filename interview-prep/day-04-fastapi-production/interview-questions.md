# Day 4 — FastAPI Production + GenAI Interview Questions

## Top 12 to memorize

1. Why APIRouter?
2. What is a service layer?
3. What is dependency injection?
4. What is Depends()?
5. How do you manage secrets?
6. What is middleware?
7. What is HTTPException?
8. Why is streaming important for GenAI?
9. Why async for LLM APIs?
10. What happens with blocking code in async endpoint?
11. Why isolate LLMService?
12. How would you design a GenAI API?

## Short answers

### 1. APIRouter
Separates related endpoints into modules so a large API remains maintainable.

### 2. Service layer
Contains business/application logic while routes handle HTTP concerns.

### 3. Dependency injection
Provides required components to a function from outside instead of constructing them inside it.

### 4. Depends()
FastAPI mechanism for resolving and injecting dependencies.

### 5. Secrets
Use environment variables or a secret manager. Never hardcode API keys in source code.

### 6. Middleware
Wraps request/response processing for cross-cutting concerns such as logging, timing, CORS and request IDs.

### 7. HTTPException
Returns an HTTP error status and detail for endpoint-level error conditions.

### 8. Streaming
Allows LLM output to be delivered incrementally as it is generated.

### 9. Async
LLM calls are usually network I/O, so async lets the server work on other tasks while waiting.

### 10. Blocking in async
Blocking operations can block the event-loop thread and reduce concurrency.

### 11. LLMService
Encapsulates provider-specific logic, making routes cleaner and testing/provider replacement easier.

### 12. GenAI API design
FastAPI → Router → Pydantic → Service → RAG/Agent/Tools → LLM → Response.

## Memory hacks

- Router = organize
- Pydantic = validate
- Depends = inject
- Service = think
- Middleware = wrap
- HTTPException = fail correctly
- Async = overlap I/O waits
- Streaming = send pieces
- LLMService = isolate provider

## 30-second answer

> I would keep FastAPI routes thin, use APIRouter for modular endpoints, Pydantic for contracts, Depends for reusable dependencies, and services for business logic. Secrets would be externalized. Async-compatible clients would be used for I/O-bound LLM and retrieval calls, and streaming would be used for chat responses when appropriate. The service layer would coordinate RAG, agents, tools and LLM providers.

## Follow-up questions to practice

- How would you inject a database session?
- How would you mock an LLM in unit tests?
- How would you add authentication?
- How would you add request IDs?
- How would you stream tokens from an LLM?
- How would you handle an LLM timeout?
- How would you structure a large FastAPI project?
