# Day 1 — Python Foundations Interview Questions

## Level 1 — Fundamentals

### 1. What are type hints?
**Answer:** Type hints describe expected types for variables, parameters, and return values. They improve readability and static analysis but normally do not enforce runtime types.

### 2. Does Python enforce type hints at runtime?
**Answer:** No. Type hints are mainly used by developers, IDEs, and static type checkers. Runtime validation requires tools such as Pydantic.

### 3. What is a dataclass?
**Answer:** A dataclass is a convenient way to create data-focused classes with generated methods such as `__init__`, `__repr__`, and `__eq__`.

### 4. Dataclass vs normal class?
**Answer:** Dataclasses reduce boilerplate for classes that mainly store data. A normal class gives more manual control over initialization and behavior.

### 5. What is TypedDict?
**Answer:** TypedDict describes the expected keys and value types of a dictionary. It is mainly useful for static type checking and does not perform runtime validation.

### 6. What is an Enum?
**Answer:** Enum represents a fixed set of named values, useful for controlled application states.

---

## Level 2 — Comparison Questions

### 7. Dataclass vs TypedDict?
**Answer:** Dataclass represents a Python object accessed with attributes; TypedDict describes a dictionary accessed with keys.

### 8. TypedDict vs Pydantic?
**Answer:** TypedDict mainly provides static typing information for dictionaries. Pydantic validates and serializes data at runtime.

### 9. Dataclass vs Pydantic?
**Answer:** Dataclass is lightweight and mainly focused on structured Python objects. Pydantic adds runtime validation, parsing, and serialization.

### 10. Iterator vs generator?
**Answer:** An iterator implements the iterator protocol. A generator is a convenient way to create an iterator using `yield`.

### 11. yield vs return?
**Answer:** `return` ends the function and returns a value. `yield` produces a value and pauses the function so it can resume later.

### 12. dump vs dumps?
**Answer:** `json.dump()` writes JSON to a file; `json.dumps()` returns JSON as a string.

### 13. load vs loads?
**Answer:** `json.load()` reads JSON from a file; `json.loads()` reads JSON from a string.

---

## Level 3 — Practical Python Questions

### 14. Why use generators?
**Answer:** They provide lazy evaluation and can process large datasets or files without loading everything into memory.

### 15. Why are generators useful in RAG?
**Answer:** A document ingestion pipeline may process thousands or millions of documents. A generator can yield documents one at a time before chunking and embedding them.

### 16. What is a context manager?
**Answer:** A context manager manages resource setup and cleanup, commonly through `__enter__` and `__exit__`.

### 17. Why use the with statement?
**Answer:** It makes resource management safer and ensures cleanup even when an exception occurs.

### 18. Why avoid bare except?
**Answer:** A bare `except` can hide unexpected errors. Specific exceptions make failures easier to understand and handle correctly.

### 19. Why use pathlib?
**Answer:** pathlib provides clean, object-oriented, and platform-independent filesystem path handling.

### 20. What is lazy evaluation?
**Answer:** Lazy evaluation means producing or processing a value only when it is needed.

---

## Level 4 — GenAI / Backend Follow-ups

### 21. How would you represent a document internally?
**Answer:** A dataclass is a simple option for an internal structured document object.

### 22. How would you represent LangGraph-like state?
**Answer:** TypedDict can clearly describe the expected dictionary state structure.

### 23. Where would Pydantic fit in our project?
**Answer:** At API boundaries, especially with FastAPI, for validating and serializing incoming requests and outgoing responses.

### 24. Why should a document ingestion pipeline avoid loading everything into memory?
**Answer:** Large document collections can consume significant memory. Streaming or lazy processing allows the pipeline to process documents incrementally.

### 25. Give a practical example combining today's concepts.
**Answer:** Use pathlib to find document files, a generator to yield files one at a time, a dataclass to represent each document, and Pydantic later at the API boundary.

---

## High-Value Interview Traps

### Trap 1
**Question:** Does `yield` always use less memory?

**Answer:** Not automatically. A generator is lazy, so it can avoid storing the entire generated result, but the memory usage still depends on what the generator and downstream processing retain.

### Trap 2
**Question:** Is TypedDict runtime validation?

**Answer:** No. TypedDict is mainly for static type checking.

### Trap 3
**Question:** Does a dataclass validate types at runtime?

**Answer:** No. Declaring `age: int` in a dataclass does not by itself enforce that the value is an integer.

### Trap 4
**Question:** Is a generator different from an iterator?

**Answer:** Yes. A generator is one way to create an iterator. Every generator is an iterator, but not every iterator is a generator.

### Trap 5
**Question:** What does the "s" mean in dumps and loads?

**Answer:** String.

```text
dumps → JSON string
loads → Python object from JSON string
```

---

## 5 Questions to Memorize First

1. Dataclass vs TypedDict vs Pydantic?
2. Iterator vs generator?
3. yield vs return?
4. Why use generators for large data?
5. Why use context managers?

If these five are strong, move to the remaining questions.
