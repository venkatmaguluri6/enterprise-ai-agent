# Day 1 — Python Foundations

## 1. Type Hints

Type hints tell other developers and tools what type of data a function expects.

```python
def search_documents(query: str, top_k: int = 5) -> list[str]:
    ...
```

### Remember

Type hints are mainly for readability, IDE support, and static checking. Python does not normally enforce them at runtime.

### Interview answer

> Type hints describe expected types and improve readability and static analysis, but they do not normally perform runtime validation.

---

## 2. Dataclass

A dataclass is a simple way to create a class that mainly stores data.

```python
from dataclasses import dataclass

@dataclass
class Document:
    document_id: str
    content: str
    source: str
```

Python can generate methods such as `__init__`, `__repr__`, and `__eq__`.

### Easy memory

**dataclass → Python object with data**

### Interview answer

> A dataclass reduces boilerplate for data-focused classes by automatically generating common methods such as __init__ and __repr__.

---

## 3. TypedDict

TypedDict describes the expected structure of a dictionary.

```python
from typing import TypedDict

class AgentState(TypedDict):
    query: str
    answer: str
    documents: list[str]
```

Use it like a normal dictionary:

```python
state = {
    "query": "What is RAG?",
    "answer": "",
    "documents": [],
}
```

### Remember

**TypedDict → typed dictionary structure**

TypedDict does not perform runtime validation by itself.

---

## 4. Dataclass vs TypedDict vs Pydantic

This is a high-priority interview topic.

| Concept | Simple meaning |
|---|---|
| dataclass | Structured Python object |
| TypedDict | Typed dictionary structure |
| Pydantic | Runtime validation + serialization |

Example:

```text
dataclass
    ↓
document.id

TypedDict
    ↓
document["id"]

Pydantic
    ↓
validate incoming data
```

### Interview answer

> Dataclass is mainly used for structured Python objects, TypedDict describes dictionary structures for static typing, and Pydantic performs runtime validation and serialization.

### GenAI connection

- dataclass → documents/search results
- TypedDict → agent state
- Pydantic → FastAPI request/response validation

---

## 5. Enum

Enum represents a fixed set of allowed values.

```python
from enum import Enum

class ActionStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
```

### Remember

**Enum → controlled list of valid states**

Useful for:

- Agent states
- Approval states
- Execution status
- API status values

---

## 6. Iterator

An iterator produces values one at a time.

It follows the iterator protocol:

```python
__iter__()
__next__()
```

Example:

```python
numbers = iter([1, 2, 3])

print(next(numbers))
print(next(numbers))
```

---

## 7. Generator

A generator is a simple way to create an iterator using `yield`.

```python
def generate_numbers():
    for i in range(5):
        yield i
```

The values are produced lazily.

### Easy memory

**Generator → give me the next value only when I need it.**

This is useful for:

- Large files
- Large datasets
- Document ingestion
- Streaming data
- Memory-efficient pipelines

### GenAI connection

For a RAG ingestion pipeline:

```text
1 million documents
       ↓
Generator
       ↓
one document at a time
       ↓
chunk
       ↓
embed
       ↓
store
```

We don't need to load all documents into memory at once.

---

## 8. Iterator vs Generator

### Iterator

An object that implements:

```python
__iter__()
__next__()
```

### Generator

A convenient way to create an iterator using `yield`.

### Most important interview sentence

> Every generator is an iterator, but not every iterator is a generator.

---

## 9. yield vs return

### return

Ends the function and returns a value.

```python
def get_numbers():
    return [1, 2, 3]
```

The list is created before it is returned.

### yield

Produces a value and pauses the function.

```python
def get_numbers():
    for i in range(3):
        yield i
```

The function resumes when the next value is requested.

### Remember

```text
return
  ↓
finish function + return value

yield
  ↓
produce value + pause
  ↓
resume later
```

---

## 10. Context Manager

A context manager manages the lifecycle of a resource.

```python
with open("file.txt") as file:
    data = file.read()
```

The file is automatically closed when leaving the block.

Common examples:

- Files
- Database connections
- Locks
- HTTP clients
- Temporary resources

Context managers commonly use:

```python
__enter__()
__exit__()
```

### Remember

**with → use resource safely → cleanup automatically**

---

## 11. Why use with?

Without `with`:

```python
file = open("file.txt")
try:
    data = file.read()
finally:
    file.close()
```

With:

```python
with open("file.txt") as file:
    data = file.read()
```

The second version is cleaner and ensures cleanup even if an exception occurs.

---

## 12. Exception Handling

Prefer specific exceptions.

Good:

```python
try:
    data = path.read_text()
except FileNotFoundError as exc:
    logger.error("File not found: %s", exc)
    raise
```

Avoid:

```python
try:
    process()
except:
    pass
```

A bare `except` can hide unexpected problems.

### Remember

**Catch what you know how to handle.**

---

## 13. JSON

JSON is commonly used for:

- APIs
- Frontend/backend communication
- Microservices
- Agent/tool communication
- LLM applications

### dumps

Python object → JSON string

```python
text = json.dumps({"query": "What is RAG?"})
```

### loads

JSON string → Python object

```python
data = json.loads(text)
```

### dump vs dumps

```text
dump   → write JSON to a file
dumps  → return JSON as a string
```

### load vs loads

```text
load   → read JSON from a file
loads  → read JSON from a string
```

### Easy memory

**s = string**

So:

```text
dumps → string
loads → string
```

---

## 14. pathlib

`pathlib` provides a clean, object-oriented way to work with filesystem paths.

```python
from pathlib import Path

path = Path("data") / "documents" / "rag.txt"
```

Useful methods:

```python
path.exists()
path.is_file()
path.is_dir()
path.mkdir()
path.read_text()
path.write_text()
```

### Why pathlib?

It is cleaner and more portable than manually concatenating path strings.

### Remember

```python
Path("data") / "documents" / "file.txt"
```

is preferable to manually building:

```python
"data/documents/file.txt"
```

---

## 15. Lazy Evaluation

Lazy evaluation means producing or processing something only when it is needed.

Generators are a common Python example.

```text
Normal list
→ create everything now

Generator
→ create next value when needed
```

### Why important for AI?

Large document ingestion and streaming workloads can benefit from lazy processing.

---

## 16. Day 1 GenAI Connection

The concepts we learned today already map to our future application:

```text
Documents
   ↓
pathlib
   ↓
Generator
   ↓
Document dataclass
   ↓
Typed agent state
   ↓
Pydantic API validation
   ↓
RAG
```

This is why we are strengthening Python before adding GenAI frameworks.

---

## 17. 30-Second Interview Summary

If an interviewer asks what Python concepts are important for your GenAI work:

> I use type hints and structured models to make Python code maintainable. I use dataclasses for internal data objects and TypedDict where a dictionary structure needs to be clearly defined. Pydantic is useful for runtime validation in API boundaries. Generators help process large document collections lazily, which is useful for ingestion pipelines. Context managers help manage resources safely, and pathlib provides clean filesystem handling.

---

## 18. Quick Revision Cheat Sheet

```text
Type hints
→ expected types

dataclass
→ data-focused Python object

TypedDict
→ typed dictionary structure

Pydantic
→ runtime validation + serialization

Enum
→ fixed set of valid values

Iterator
→ __iter__ + __next__

Generator
→ iterator using yield

yield
→ produce + pause

return
→ finish + return

Context manager
→ resource lifecycle

with
→ automatic cleanup

json.dumps()
→ Python → JSON string

json.loads()
→ JSON string → Python

json.dump()
→ Python → JSON file

json.load()
→ JSON file → Python

pathlib
→ clean filesystem paths
```