# Enterprise AI Agent

A production-oriented GenAI application that I am building progressively while preparing for AI Engineer / GenAI Engineer roles.

The project will evolve through:

**Python → FastAPI → RAG → Hybrid Search → LangGraph → MCP → Guardrails → Observability → Docker → AWS**

## Current Progress

### Day 1 — Python Foundations

Implemented and practiced:

* Python type hints
* Dataclasses
* TypedDict
* Enums
* Generators
* Iterators
* Context managers
* Exception handling
* JSON serialization
* pathlib
* Basic Python project structure

## Project Structure

```text
enterprise-ai-agent/
├── app/
│   ├── __init__.py
│   ├── models.py
│   └── utils.py
├── data/
│   └── documents/
│       ├── rag.txt
│       ├── langgraph.txt
│       └── fastapi.txt
├── tests/
├── run.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

* Python 3.10+
* Git

No external Python packages are required for the Day 1 implementation.

## Setup

Clone the repository:

```bash
git clone <your-repository-url>
cd enterprise-ai-agent
```

Create a virtual environment.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

Run the Day 1 document generator:

```bash
python run.py
```

The application reads documents from:

```text
data/documents/
```

and generates `Document` objects lazily using a Python generator.

## What I Practiced

### Dataclass

Used dataclasses to represent structured document data.

```python
@dataclass
class Document:
    document_id: str
    content: str
    source: str
```

### TypedDict

Used `TypedDict` to define the expected structure of agent state.

```python
class AgentState(TypedDict):
    query: str
    answer: str
    documents: list[str]
```

### Generator

Documents are processed using `yield` so that they can be generated one at a time rather than loading all documents into memory.

### pathlib

Filesystem operations use Python's `pathlib` instead of manually constructing path strings.

## Roadmap

* [x] Day 1 — Python foundations
* [ ] Day 2 — Async Python and concurrency
* [ ] Day 3 — FastAPI
* [ ] Day 4 — Pydantic and API design
* [ ] Day 5 — LLM fundamentals
* [ ] RAG pipeline
* [ ] Embeddings
* [ ] Hybrid search
* [ ] LangGraph
* [ ] MCP
* [ ] Human-in-the-loop
* [ ] Guardrails
* [ ] Observability
* [ ] Cost optimization
* [ ] Docker
* [ ] AWS deployment

## Goal

Build a practical, production-oriented AI Agent platform while preparing for real-world GenAI / AI Engineer interviews.
