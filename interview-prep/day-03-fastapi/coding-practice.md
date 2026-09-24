# Day 3 — FastAPI Coding Practice

## 1. Run
uvicorn app.main:app --reload

Open /docs and /redoc.

## 2. Test endpoints
GET /
GET /health
GET /documents/doc-123
GET /search?query=What%20is%20RAG?&top_k=5
POST /search

POST body:
{"query":"What is RAG?","top_k":2}

## 3. Validation challenge
Send {"top_k":5}.

Explain why it fails: query is required by SearchRequest, so validation fails before endpoint logic runs.

## 4. Interview coding challenge
Create GET /documents/{document_id} with a response model. Explain why a response model makes the API contract explicit.

## 5. GenAI coding challenge
Design POST /ask with request: question, top_k; response: question, answer, sources.

Architecture:
POST /ask → Pydantic request → FastAPI route → AI service → RAG → LLM → Pydantic response

Do not add a real LLM yet.

## 6. Testing
Run pytest.
Tests cover home, health, path parameters, query parameters, valid body, defaults and invalid body.

## 7. 20-minute routine
5 min: run API and inspect /docs.
5 min: call every endpoint.
5 min: send invalid Pydantic data.
5 min: explain the architecture aloud.

Speaking exercise:
Client sends a request to FastAPI. FastAPI extracts path/query/body data. Pydantic validates structured input. The route calls a service layer. The service will later perform RAG, agent or LLM operations. A response model defines the output contract.