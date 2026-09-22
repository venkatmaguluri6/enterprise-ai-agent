# Day 1 — Python Foundations for GenAI Engineering

## 1. Day 1 Objective

Strengthen Python concepts that are frequently used in:

* FastAPI
* RAG pipelines
* LangGraph
* MCP
* AI/LLM applications
* Data processing
* Production backend systems

The goal is not to relearn Python from scratch, but to explain Python concepts clearly and connect them to real-world AI/backend systems.

---

# 2. Type Hints

## What are type hints?

Type hints specify the expected type of variables, function parameters, and return values.

```python
def search_documents(query: str, top_k: int = 5) -> list[str]:
    ...
```

They improve:

* Code readability
* IDE support
* Static analysis
* Maintainability
* Collaboration

### Important

Type hints generally **do not perform runtime validation** by themselves.

For runtime validation, tools such as **Pydantic** are commonly used.

### Interview Question

**Q: Do Python type hints enforce types at runtime?**

**Answer:**

> No. Python type hints primarily provide metadata for developers, IDEs, and static type checkers. Python itself generally does not enforce them at runtime. Frameworks such as Pydantic can perform runtime validation.

---

# 3. Dataclass

A dataclass is useful when a class primarily represents structured data.

```python
from dataclasses import dataclass

@dataclass
class Document:
    document_id: str
    content: str
    source: str
```

Python automatically generates methods such as:

* `__init__`
* `__repr__`
* `__eq__`

depending on the dataclass configuration.

### Why use dataclass?

Instead of manually writing:

```python
class Document:

    def __init__(self, document_id, content, source):
        self.document_id = document_id
        self.content = content
        self.source = source
```

we can use:

```python
@dataclass
class Document:
    document_id: str
    content: str
    source: str
```

### GenAI use case

Representing:

* Documents
* Search results
* Configuration objects
* Agent-related data
* Internal application models

### Interview Questions

**Q: Why use a dataclass?**

> A dataclass reduces boilerplate when creating classes that primarily store data. It automatically generates common methods such as `__init__` and `__repr__`.

**Q: Dataclass vs normal class?**

> A normal class gives complete control over behavior and initialization, while a dataclass is convenient when the class mainly represents structured data.

---

# 4. TypedDict

`TypedDict` describes the expected structure of a dictionary.

```python
from typing import TypedDict

class AgentState(TypedDict):
    query: str
    answer: str
    documents: list[str]
```

Usage:

```python
state = {
    "query": "What is RAG?",
    "answer": "",
    "documents": []
}
```

### Important

`TypedDict` provides type information but **does not perform runtime validation**.

### Why important for GenAI?

It is particularly useful when defining structured state for workflows such as LangGraph.

---

# 5. Dataclass vs TypedDict vs Pydantic

This is a **high-priority interview topic**.

| Feature               | Dataclass         | TypedDict          | Pydantic            |
| --------------------- | ----------------- | ------------------ | ------------------- |
| Main purpose          | Structured object | Typed dictionary   | Validation/modeling |
| Access                | `obj.name`        | `obj["name"]`      | `obj.name`          |
| Runtime validation    | No                | No                 | Yes                 |
| Serialization         | Basic/manual      | Dictionary already | Built-in support    |
| API validation        | Not primarily     | Not primarily      | Excellent           |
| LangGraph state       | Possible          | Very common        | Possible            |
| FastAPI request model | Possible          | Not ideal          | Very common         |

### Interview Answer

> Dataclass is mainly used to represent structured Python objects. TypedDict describes the expected structure of dictionaries and is primarily useful for static type checking. Pydantic models perform runtime validation and serialization, making them especially useful for FastAPI APIs.

### Remember

```text
dataclass  → object
TypedDict  → dictionary structure
Pydantic   → runtime validation
```

---

# 6. Enum

Enums represent a fixed set of allowed values.

```python
from enum import Enum

class ActionStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
```

Useful for:

* Workflow states
* API status values
* Agent actions
* Approval states
* Execution states

### GenAI example

```text
PENDING
   ↓
APPROVED
   ↓
EXECUTED
```

or:

```text
PENDING
   ↓
REJECTED
```

### Interview Question

**Q: Why use Enum instead of strings?**

> Enums provide a controlled set of valid values, improve readability, reduce accidental invalid values, and make application states easier to manage.

---

# 7. Iterator

An iterator is an object that produces values one at a time.

The iterator protocol uses:

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

Output:

```text
1
2
```

---

# 8. Generator

A generator is a convenient way of creating an iterator using `yield`.

```python
def generate_numbers():
    for i in range(5):
        yield i
```

Usage:

```python
for number in generate_numbers():
    print(number)
```

### Key advantage

**Lazy evaluation.**

Values are produced only when requested.

This can reduce memory usage when processing:

* Large files
* Large datasets
* Database records
* Document collections
* Streaming data

### GenAI use case

Imagine processing 1 million documents.

Instead of:

```python
documents = load_all_documents()
```

we can process them incrementally:

```python
for document in generate_documents():
    process(document)
```

---

# 9. Iterator vs Generator

### Iterator

An object implementing:

```python
__iter__()
__next__()
```

### Generator

A simpler way to create an iterator using `yield`.

### Most important interview statement

> Every generator is an iterator, but not every iterator is a generator.

---

# 10. `yield` vs `return`

### `return`

Terminates the function and returns a value.

```python
def get_numbers():
    return [1, 2, 3]
```

The list is created before being returned.

### `yield`

Produces a value and pauses the function.

```python
def get_numbers():
    for i in range(3):
        yield i
```

The function resumes when the next value is requested.

### Interview Answer

> `return` terminates a function and returns a value, while `yield` pauses a function and produces values lazily. Generators using `yield` are useful for memory-efficient processing of large or streaming data.

---

# 11. Context Manager

A context manager manages the lifecycle of a resource.

Example:

```python
with open("file.txt") as file:
    data = file.read()
```

The resource is automatically cleaned up.

Conceptually:

```text
Enter context
     ↓
Use resource
     ↓
Exit context
     ↓
Cleanup
```

### Important methods

Context managers commonly implement:

```python
__enter__()
__exit__()
```

### Real-world examples

* Files
* Database connections
* Locks
* HTTP sessions
* Temporary resources

### GenAI/backend relevance

Context managers become important when working with:

* Database sessions
* HTTP clients
* Async resources
* MCP sessions
* Temporary files

---

# 12. Why use `with`?

Without context manager:

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

The resource is automatically cleaned up.

### Interview Answer

> The `with` statement ensures deterministic resource cleanup and makes code safer and easier to read. Cleanup happens even if an exception occurs inside the block.

---

# 13. Exception Handling

Basic structure:

```python
try:
    result = process_data()

except ValueError as e:
    print(e)

finally:
    cleanup()
```

### Good practice

Prefer specific exceptions:

```python
except FileNotFoundError:
```

instead of:

```python
except:
```

Avoid silently swallowing errors.

Bad:

```python
try:
    process()
except:
    pass
```

Better:

```python
try:
    process()
except FileNotFoundError as e:
    logger.error("File not found: %s", e)
    raise
```

### Interview Question

**Q: Why should we avoid bare `except`?**

> A bare `except` catches almost every exception, including unexpected errors, which can hide bugs and make debugging difficult. It is better to catch specific exceptions.

---

# 14. JSON Serialization

JSON is commonly used for communication between:

* Frontend and backend
* APIs
* Microservices
* LLM applications
* Agent/tool communication

## `json.dumps()`

Python object → JSON string

```python
import json

data = {
    "query": "What is RAG?",
    "top_k": 5
}

text = json.dumps(data)
```

## `json.loads()`

JSON string → Python object

```python
data = json.loads(text)
```

### Memorize

```text
Python object
     ↓
json.dumps()
     ↓
JSON string
     ↓
json.loads()
     ↓
Python object
```

### Common interview question

**Q: Difference between `dump` and `dumps`?**

Important distinction:

```text
dump  → write JSON to a file
dumps → return JSON as a string
```

Similarly:

```text
load  → read JSON from a file
loads → read JSON from a string
```

---

# 15. pathlib

`pathlib` provides an object-oriented way of working with filesystem paths.

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

### Why use pathlib?

It provides cleaner and more platform-independent path handling.

Instead of manually:

```python
"data/" + "documents/" + "rag.txt"
```

use:

```python
Path("data") / "documents" / "rag.txt"
```

---

# 16. Python Memory & Lazy Processing

This is important for GenAI engineering.

Suppose we have:

```text
1,000,000 documents
```

Loading everything:

```python
documents = load_all_documents()
```

can consume significant memory.

A generator:

```python
def generate_documents():
    for file in files:
        yield process(file)
```

allows:

```python
for document in generate_documents():
    process(document)
```

Only the required data is processed at a time.

### Interview connection

This concept is useful when discussing:

* RAG ingestion
* Data pipelines
* Streaming
* Large files
* Batch processing
* LLM response streaming

---

# 17. High-Priority Day 1 Interview Questions

## Python Fundamentals

### Q1. What is a dataclass?

Know:

> A convenient way to create data-focused classes with automatically generated methods such as `__init__` and `__repr__`.

### Q2. Dataclass vs normal class?

Know:

> Dataclass reduces boilerplate for data-centric classes; normal classes provide more manual control.

### Q3. What is TypedDict?

Know:

> It describes the expected structure and types of dictionary keys and values.

### Q4. TypedDict vs Pydantic?

Know:

> TypedDict mainly provides static typing information; Pydantic performs runtime validation and serialization.

### Q5. What is a generator?

Know:

> A function using `yield` that produces values lazily.

### Q6. Why use generators?

Know:

> To process large or streaming data efficiently without loading the entire result into memory.

### Q7. Iterator vs generator?

Know:

> An iterator implements the iterator protocol; a generator is a convenient way to create an iterator using `yield`.

### Q8. Every generator is an iterator. Is every iterator a generator?

**No.**

### Q9. `yield` vs `return`?

Know:

> `return` terminates the function; `yield` pauses it and produces a value.

### Q10. What is a context manager?

Know:

> It manages resource setup and cleanup.

### Q11. Why use `with`?

Know:

> It ensures resources are cleaned up automatically, even when exceptions occur.

### Q12. What is `json.dumps()`?

> Converts a Python object to a JSON string.

### Q13. What is `json.loads()`?

> Converts a JSON string to a Python object.

### Q14. `dump` vs `dumps`?

> `dump` writes JSON to a file; `dumps` returns JSON as a string.

### Q15. `load` vs `loads`?

> `load` reads JSON from a file; `loads` reads JSON from a string.

### Q16. Why use pathlib?

> For cleaner, object-oriented and platform-independent filesystem operations.

### Q17. Why avoid bare `except`?

> It can hide unexpected errors and make debugging difficult.

### Q18. Does Python enforce type hints at runtime?

> No. Type hints primarily support static analysis and developer tooling.

---

# 18. GenAI Interview Connections

Remember these connections because interviewers often move from Python fundamentals into practical questions.

### Generator

```text
Large documents
      ↓
Generator
      ↓
Process one document
      ↓
Embedding
      ↓
Vector database
```

### TypedDict

```text
User query
    ↓
Agent State
    ↓
LangGraph nodes
    ↓
Updated State
```

### Pydantic

```text
API Request
     ↓
Pydantic validation
     ↓
FastAPI endpoint
     ↓
Business logic
```

### Context Manager

```text
Database / HTTP / File resource
          ↓
     with / async with
          ↓
      automatic cleanup
```

### JSON

```text
Frontend
   ↓
JSON
   ↓
FastAPI
   ↓
Python object
   ↓
LLM / Agent
```

---

# 19. Quick Revision — 5 Minute Version

Before an interview, remember this:

```text
Type hints
→ Documentation + static checking
→ Not runtime validation

dataclass
→ Data-focused Python object

TypedDict
→ Typed dictionary structure

Pydantic
→ Runtime validation + serialization

Enum
→ Fixed set of valid values

Iterator
→ __iter__() + __next__()

Generator
→ Iterator created using yield

yield
→ Pause + produce value

return
→ End function + return value

Context manager
→ Resource lifecycle management

with
→ Automatic cleanup

json.dumps()
→ Python → JSON string

json.loads()
→ JSON string → Python

dump
→ JSON → file

load
→ file → Python

pathlib
→ Clean/platform-independent filesystem paths
```

---

# 20. Must-Remember Interview Answers

### Dataclass vs TypedDict vs Pydantic

> Dataclass represents structured Python objects, TypedDict describes dictionary structures for static typing, and Pydantic provides runtime validation and serialization.

### Iterator vs Generator

> An iterator implements `__iter__` and `__next__`, while a generator is a convenient way to create an iterator using `yield`.

### Yield vs Return

> `return` terminates a function, while `yield` pauses the function and allows values to be produced lazily.

### Why generators in AI systems?

> Generators help process large datasets, documents, or streams incrementally without loading the entire result into memory.

### Why Pydantic in FastAPI?

> Pydantic validates incoming data at runtime and provides structured serialization for API models.

### Why context managers?

> They ensure resources are properly acquired and released, even when exceptions occur.

---

# 21. Day 1 Interview Checklist

Before moving to Day 2, I should be able to explain without notes:

* [ ] Type hints
* [ ] Runtime vs static typing
* [ ] Dataclass
* [ ] TypedDict
* [ ] Pydantic
* [ ] Dataclass vs TypedDict vs Pydantic
* [ ] Enum
* [ ] Iterator
* [ ] Generator
* [ ] `yield`
* [ ] `return`
* [ ] Iterator vs generator
* [ ] Context manager
* [ ] `with`
* [ ] Exception handling
* [ ] `json.dumps`
* [ ] `json.loads`
* [ ] `dump` vs `dumps`
* [ ] `load` vs `loads`
* [ ] pathlib
* [ ] Lazy evaluation
* [ ] Memory-efficient processing

---

# 22. Day 1 Practical Project

Implemented:

```text
Enterprise AI Agent
        ↓
Document ingestion
        ↓
pathlib
        ↓
Read documents
        ↓
Document dataclass
        ↓
Generator / yield
        ↓
Process documents lazily
```

This is the first building block of the larger project.

The project will progressively evolve into:

```text
Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Search
    ↓
Hybrid Search
    ↓
RAG
    ↓
LLM
    ↓
LangGraph
    ↓
MCP Tools
    ↓
Guardrails
    ↓
Observability
    ↓
Docker
    ↓
AWS
```

---

# 23. Interview Strategy

For technical questions, answer using:

**Definition → Why → Example → Real-world use**

Example:

> **What is a generator?**

**Definition:** A generator is a function that uses `yield` to produce values lazily.

**Why:** It avoids loading the entire result into memory.

**Example:** A function that reads documents one at a time.

**Real-world use:** In a RAG ingestion pipeline, generators can process large numbers of documents incrementally before chunking and embedding them.

This structure should be used throughout the remaining preparation.

---

## Day 1 Status

**Python Foundations: COMPLETED ✅**

Next:

**Day 2 — Async Python + Concurrency**

Focus areas:

* `async` / `await`
* Event loop
* Coroutine
* Task
* `asyncio.gather()`
* Concurrent vs parallel execution
* Threading vs asyncio
* Blocking vs non-blocking code
* Async HTTP calls
* Practical FastAPI/GenAI use cases
* Interview questions
