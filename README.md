# Enterprise AI Agent

A production-oriented GenAI application that I am building progressively while preparing for AI Engineer / GenAI Engineer roles.

## Project Direction

Python → AsyncIO → FastAPI → RAG → Hybrid Search → LangGraph → MCP → Guardrails → Observability → Docker → AWS

## Current Progress

### Day 1 — Python Foundations ✅

- Type hints
- Dataclasses
- TypedDict
- Enums
- Iterators and generators
- Context managers
- Exception handling
- JSON serialization
- pathlib
- Document generator

### Day 2 — Async Python & Concurrency ✅

- async / await
- Coroutines
- Event loop
- Asyncio tasks
- asyncio.gather()
- Concurrency vs parallelism
- I/O-bound vs CPU-bound workloads
- Blocking vs non-blocking operations
- Concurrent retrieval simulation

## Run Day 1

```bash
python run.py
```

## Run Day 2

```bash
python -m app.async_demo
```

## Run Tests

```bash
pytest
```

## Project Structure

```text
enterprise-ai-agent/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── utils.py
│   └── async_demo.py
├── data/
│   └── documents/
├── tests/
├── interview-prep/
│   ├── day-01-python-foundations/
│   └── day-02-async-concurrency/
├── run.py
├── requirements.txt
└── README.md
```

## Roadmap

- [x] Day 1 — Python foundations
- [x] Day 2 — Async Python and concurrency
- [x] Day 3 — FastAPI
- [ ] Day 4 — Pydantic and API design
- [ ] Day 5 — LLM fundamentals
- [ ] RAG pipeline
- [ ] Embeddings
- [ ] Hybrid search
- [ ] LangGraph
- [ ] MCP
- [ ] Human-in-the-loop
- [ ] Guardrails
- [ ] Observability
- [ ] Cost optimization
- [ ] Docker
- [ ] AWS deployment
