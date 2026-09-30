# Enterprise AI Agent

A production-oriented GenAI application built progressively while preparing for AI Engineer / GenAI Engineer roles. The repository combines a working backend project with day-wise, interview-focused learning notes.

## Project Direction

Python → AsyncIO → FastAPI → LLM fundamentals → RAG → Hybrid Search → LangGraph → MCP → Guardrails → Observability → Docker → AWS

## Current Progress

### Day 1 — Python Foundations ✅
- Type hints, dataclasses, TypedDict and enums
- Iterators, generators and context managers
- Exceptions, JSON and pathlib
- Lazy document loading

### Day 2 — Async Python & Concurrency ✅
- Coroutines, event loop, tasks and `asyncio.gather()`
- Concurrency vs parallelism
- I/O-bound vs CPU-bound workloads
- Blocking vs non-blocking operations
- Concurrent retrieval simulation

### Day 3 — FastAPI Foundations ✅
- FastAPI routes, request validation and response models
- Query/path parameters and API testing

### Day 4 — FastAPI Production Patterns + LLM Integration ✅
- APIRouter, service layer and dependency injection
- Environment-based configuration
- Chat endpoint and provider-neutral mock LLM service
- Request validation and tests

### Day 5 — LLM Fundamentals 🧠
- Tokenization and token IDs
- Token embeddings vs document embeddings
- Transformer, self-attention and Q/K/V
- Positional information and autoregressive generation
- Context window, temperature and top-p
- Hallucination, RAG grounding, token budget and cost
- Educational mock tokenization/generation pipeline (not a real LLM)

## Run the application

```bash
uvicorn app.main:app --reload
```

Open the interactive API documentation at `/docs` while the app is running.

## Run the demos

Day 1:
```bash
python run.py
```

Day 2:
```bash
python -m app.async_demo
```

Day 5:
```bash
python -c "from app.services.llm_demo import tokenize, token_to_id, generate_response; print(tokenize('What is RAG?')); print(token_to_id(tokenize('What is RAG?'))); print(generate_response('What is RAG?', 5))"
```

The Day 5 pipeline is deliberately rule-based for learning. It is not a trained language model and does not perform real Transformer inference.

## Run tests

```bash
pytest
```

## Project structure

```text
enterprise-ai-agent/
├── app/
│   ├── api/routes/
│   ├── core/
│   ├── models/
│   ├── services/
│   │   └── llm_demo.py
│   ├── async_demo.py
│   └── main.py
├── tests/
├── interview-prep/
│   ├── day-01-python-foundations/
│   ├── day-02-async-concurrency/
│   ├── day-03-fastapi/
│   ├── day-04-fastapi-production/
│   └── day-05-llm-fundamentals/
├── data/
├── requirements.txt
└── README.md
```

Every study day contains:
- `notes.md` — daily reading and explanations
- `interview-questions.md` — important questions with answers
- `coding-practice.md` — self-contained reading, examples, revision and coding tasks

## Roadmap

- [x] Day 1 — Python foundations
- [x] Day 2 — Async Python and concurrency
- [x] Day 3 — FastAPI foundations
- [x] Day 4 — FastAPI production patterns
- [x] Day 5 — LLM fundamentals
- [ ] Day 6 — Embeddings, vector databases and RAG
- [ ] Hybrid search and reranking
- [ ] LangGraph agents and human-in-the-loop
- [ ] MCP server/client and tool security
- [ ] Guardrails and hallucination defense
- [ ] Observability and cost optimization
- [ ] Docker and AWS deployment
