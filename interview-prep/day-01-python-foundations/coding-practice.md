# Day 1 — Python Foundations
# Daily Reading + Interview Preparation + Coding Practice

## 1. Daily Reading

### Type Hints
Type hints describe expected types. They improve readability and static checking but normally do not enforce runtime validation.

```python
def search_documents(query: str, top_k: int = 5) -> list[str]:
    ...
```

**Remember:** Type hints = describe, Pydantic = runtime validation.

### Dataclass
A dataclass is useful for data-focused Python objects.

```python
from dataclasses import dataclass

@dataclass
class Document:
    document_id: str
    content: str
    source: str
```

**Remember:** dataclass → Python object with data.

### TypedDict
TypedDict describes the expected structure of a dictionary.

```python
class AgentState(TypedDict):
    query: str
    answer: str
    documents: list[str]
```

**Remember:** TypedDict → typed dictionary structure.

### Dataclass vs TypedDict vs Pydantic

| Tool | Remember it as |
|---|---|
| dataclass | Python data object |
| TypedDict | typed dictionary |
| Pydantic | runtime validation + serialization |

**GenAI:** dataclass → document/search result; TypedDict → agent state; Pydantic → FastAPI boundary.

### Enum
Enum represents a fixed set of valid values.

```python
class ActionStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
```

**Remember:** Enum → controlled states.

### Iterator and Generator
An iterator follows `__iter__()` and `__next__()`.

A generator is a convenient way to create an iterator using `yield`.

```python
def generate_numbers():
    for i in range(5):
        yield i
```

**Remember:** Generator → next value only when needed.

**Most important interview sentence:** Every generator is an iterator, but not every iterator is a generator.

### yield vs return

```
return → finish function + return value
yield  → produce value + pause + resume later
```

Generators are useful for large files, datasets, document ingestion and streaming.

### Context Manager

```python
with open("file.txt") as file:
    data = file.read()
```

A context manager manages resource setup/cleanup.

**Remember:** with → use safely → cleanup automatically.

### Exception Handling
Prefer specific exceptions.

```python
try:
    data = path.read_text()
except FileNotFoundError:
    ...
```

Avoid silently swallowing errors with bare `except: pass`.

**Remember:** Catch what you know how to handle.

### JSON

```
dump  → Python → JSON file
dumps → Python → JSON string
load  → JSON file → Python
loads → JSON string → Python
```

**Hack:** `s = string`, so `dumps/loads` involve strings.

### pathlib

```python
Path("data") / "documents" / "file.txt"
```

Useful: `exists()`, `is_file()`, `mkdir()`, `read_text()`, `write_text()`.

### Lazy Evaluation

Normal list → create/store values now.

Generator → produce values when needed.

**GenAI connection:** process a huge document collection one document at a time instead of loading everything into memory.

---

## 2. Easy Memory Structure

```
Python data
   ├── dataclass → object
   ├── TypedDict → dictionary
   ├── Enum → fixed states
   └── Pydantic → validated boundary

Large data
   └── generator → lazy processing

Resources
   └── with → cleanup

Files
   └── pathlib → paths

JSON
   ├── dumps → string
   └── dump → file
```

---

## 3. Most Important Interview Questions

### Q1. Dataclass vs TypedDict vs Pydantic?
**Answer:** Dataclass represents structured Python objects, TypedDict describes dictionary structures for static typing, and Pydantic provides runtime parsing/validation and serialization.

### Q2. Iterator vs generator?
**Answer:** An iterator follows the iterator protocol. A generator is a convenient way to create an iterator using `yield`.

### Q3. yield vs return?
**Answer:** return finishes the function; yield produces a value and pauses execution so it can resume later.

### Q4. Why use generators?
**Answer:** They provide lazy evaluation and can process large data without storing the complete result in memory.

### Q5. What is a context manager?
**Answer:** It manages resource setup and cleanup, commonly through `with`.

### Q6. Does Python enforce type hints?
**Answer:** Normally no. Type hints are mainly for readability and static analysis.

### Q7. Is TypedDict runtime validation?
**Answer:** No. It mainly provides static typing information.

### Q8. Why pathlib?
**Answer:** It provides clean, object-oriented and portable filesystem path handling.

---

## 4. Interview Traps

- Type hints are not general runtime validation.
- TypedDict is not Pydantic.
- dataclass annotations do not automatically validate types.
- Every generator is an iterator, but not every iterator is a generator.
- `yield` does not mean the entire function executes immediately.
- A generator can reduce memory usage, but downstream code can still retain large amounts of data.

---

## 5. 30-Second Interview Answer

> I use type hints and structured models to make Python code maintainable. Dataclasses are useful for internal data objects, TypedDict can describe dictionary-based state, and Pydantic is useful at API boundaries for runtime validation. Generators help process large document collections lazily, while context managers safely manage resources and pathlib provides clean filesystem handling.

---

## 6. Quick Revision Cheat Sheet

```
Type hints   → expected types
dataclass    → data object
TypedDict    → typed dictionary
Pydantic     → runtime validation
Enum         → fixed values
Iterator     → __iter__ + __next__
Generator    → iterator using yield
yield        → produce + pause
return       → finish + return
with         → cleanup
dumps        → JSON string
loads        → Python from JSON string
dump         → JSON file
load         → Python from JSON file
pathlib      → filesystem paths
lazy         → process when needed
```

---

## 7. Coding Practice

### Exercise 1 — Document Generator

Read files from `data/documents/` and yield `Document` objects one at a time.

Requirements:
- use pathlib
- use yield
- don't load every document first
- handle FileNotFoundError
- use filename as source

Expected:

```
data/documents
      ↓
pathlib
      ↓
one file
      ↓
Document
      ↓
yield
      ↓
next file
```

### Exercise 2 — Dataclass

Create the `Document` dataclass and explain why it is appropriate.

### Exercise 3 — TypedDict

Create `AgentState` and explain why it represents a dictionary structure.

### Exercise 4 — JSON

Convert a Python dictionary to JSON and back. Explain dump/dumps/load/loads.

### Exercise 5 — pathlib

Build `data/documents/rag.txt` using:

```python
Path("data") / "documents" / "rag.txt"
```

### Exercise 6 — Context Manager

Read a file with `with open(...)` and explain the cleanup behavior.

### Exercise 7 — Interview Challenge

Without looking at notes, explain:

```
pathlib
   ↓
generator
   ↓
dataclass
   ↓
document processing
   ↓
future RAG ingestion
```

### 20-Minute Routine

5 min → read the Daily Reading section.

5 min → answer the 8 high-value questions aloud.

5 min → code one exercise.

5 min → explain the GenAI connection without notes.
