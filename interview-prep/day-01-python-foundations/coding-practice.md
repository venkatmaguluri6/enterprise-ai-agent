# Day 1 — Python Foundations Coding Practice

## Exercise 1 — Document Generator

### Goal

Read files from `data/documents/` and generate `Document` objects one at a time.

### Requirements

- Use pathlib.
- Use `yield`.
- Do not load every document into memory first.
- Handle `FileNotFoundError`.
- Use the filename as the document source.

### Expected flow

```text
data/documents/
      ↓
pathlib
      ↓
one file
      ↓
read content
      ↓
Document dataclass
      ↓
yield
      ↓
next file
```

### Interview follow-up

Why use a generator instead of returning a list?

**Answer:** A generator processes documents lazily and avoids storing the complete collection in memory.

---

## Exercise 2 — Dataclass

Create:

```python
@dataclass
class Document:
    document_id: str
    content: str
    source: str
```

Explain why dataclass is useful here.

---

## Exercise 3 — TypedDict

Create:

```python
class AgentState(TypedDict):
    query: str
    answer: str
    documents: list[str]
```

Explain why this is a dictionary structure rather than a normal class object.

---

## Exercise 4 — JSON

Convert this Python dictionary to JSON and back:

```python
data = {
    "query": "What is RAG?",
    "top_k": 5,
}
```

Use:

```python
json.dumps()
json.loads()
```

Then explain the difference between `dump/dumps` and `load/loads`.

---

## Exercise 5 — pathlib

Build this path without manually concatenating strings:

```text
data/documents/rag.txt
```

Expected:

```python
Path("data") / "documents" / "rag.txt"
```

Then check whether the file exists.

---

## Exercise 6 — Context Manager

Read a text file using:

```python
with open(...) as file:
    ...
```

Explain what cleanup the context manager provides.

---

## Exercise 7 — Interview Challenge

Without looking at notes, explain this pipeline:

```text
pathlib
   ↓
generator
   ↓
dataclass
   ↓
document processing
```

Then explain how this becomes the foundation for a future RAG ingestion pipeline.
