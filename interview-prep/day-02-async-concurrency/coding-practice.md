# Day 2 — Async Python & Concurrency
# Daily Reading + Interview Preparation + Coding Practice

## 1. Daily Reading

### Simple Mental Model

Think of async like a restaurant:

- event loop = waiter
- async task = table/order
- waiting for food = waiting for I/O
- waiter serves another table instead of standing idle

```
Task A → waiting for API
              ↓
         Event Loop
          ↙       ↘
     Task B       Task C
       ↓
   Task A resumes
```

**Core idea:** async is mainly about using waiting time efficiently for I/O.

### async def

`async def` defines a coroutine function.

```python
async def fetch_user():
    return {"name": "Venkat"}
```

Calling it creates a coroutine object.

**Remember:** async def → coroutine function; calling it → coroutine object.

### await

`await` suspends the current coroutine while the awaited async operation is pending, allowing the event loop to run other ready work.

**Hack:** await = “wait for this, but don't block the event loop.”

### Event Loop

The event loop schedules and coordinates async tasks.

### Task

```python
task = asyncio.create_task(fetch_data())
```

A Task schedules a coroutine for execution on the event loop.

**Coroutine = async work. Task = scheduled async work.**

### asyncio.gather()

Use it for independent async operations.

```python
results = await asyncio.gather(
    vector_search(query),
    bm25_search(query),
    metadata_search(query),
)
```

It waits for all and returns their results.

**Remember:** gather = run independent async work together.

### Concurrency vs Parallelism

**Concurrency:** multiple tasks make progress during overlapping periods.

**Parallelism:** multiple tasks actually execute simultaneously, often using multiple CPU cores.

**Hack:** concurrency = dealing with many; parallelism = doing many at the same time.

### I/O-bound vs CPU-bound

I/O-bound = mostly waiting: APIs, DB, network, LLM calls, vector DB.

CPU-bound = mostly computation: image processing, heavy calculations, large transformations.

Asyncio is especially useful for I/O-bound workloads.

### time.sleep vs asyncio.sleep

```python
time.sleep(5)
```

blocks the thread.

```python
await asyncio.sleep(5)
```

performs a non-blocking async wait.

**Important:** async def does not make blocking operations magically non-blocking.

### Asyncio vs Threading

Asyncio uses an event loop and cooperative async tasks.

Threading uses multiple OS threads.

Use asyncio when libraries support async I/O. Threading can be useful for blocking/synchronous libraries.

### Asyncio vs Multiprocessing

Multiprocessing uses separate processes and is more suitable for CPU-bound parallel work.

### Does async automatically make code faster?

No.

Async improves throughput/responsiveness when tasks spend significant time waiting for I/O. It does not automatically speed up CPU calculations.

---

## 2. GenAI Connection

RAG often has independent retrieval operations:

```
User query
   ↓
 ┌───────────────┬───────────────┬───────────────┐
 ↓               ↓               ↓
Vector search   BM25 search    Metadata
 ↓               ↓               ↓
 └───────────────┴───────────────┘
                 ↓
          combine/rank
                 ↓
                LLM
```

If each operation waits on I/O, they can often be performed concurrently.

Agent example:

```
Agent
 ├── Search tool
 ├── Customer tool
 └── Knowledge tool
        ↓
independent calls
        ↓
async concurrency
```

---

## 3. Day 2 Project Example

Our project simulates:

- Vector search → 2 seconds
- Keyword search → 1 second
- Metadata → 1 second

Sequential:

```
2 + 1 + 1 ≈ 4 seconds
```

Concurrent:

```
max(2, 1, 1) ≈ 2 seconds
```

Run:

```bash
python -m app.async_demo
pytest
```

---

## 4. Most Important Interview Questions

### Q1. What is async programming?
**Answer:** Async programming allows an I/O-bound task to suspend while waiting, so other tasks can make progress.

### Q2. What does async def do?
**Answer:** It defines a coroutine function.

### Q3. What does await do?
**Answer:** It suspends the current coroutine while an async operation is pending and lets the event loop run other ready tasks.

### Q4. What is an event loop?
**Answer:** It schedules and coordinates asynchronous tasks.

### Q5. Coroutine vs Task?
**Answer:** A coroutine represents async work; a Task schedules that coroutine on the event loop.

### Q6. What does gather do?
**Answer:** It concurrently waits for multiple independent awaitables and collects their results.

### Q7. Concurrency vs parallelism?
**Answer:** Concurrency is overlapping progress; parallelism is simultaneous execution.

### Q8. I/O-bound vs CPU-bound?
**Answer:** I/O-bound workloads spend time waiting; CPU-bound workloads spend time computing.

### Q9. Does async automatically make code faster?
**Answer:** No. It improves overlap of I/O waits and can improve throughput.

### Q10. What happens with time.sleep in async code?
**Answer:** It blocks the thread and can block the event loop.

### Q11. Why async for LLM APIs?
**Answer:** LLM calls are network I/O. While one request waits, other tasks can make progress.

### Q12. Why async for RAG?
**Answer:** Independent vector, keyword and metadata searches can often overlap their I/O waits.

### Q13. What if a blocking SDK is used in an async endpoint?
**Answer:** It can block the event loop. Prefer an async SDK or move suitable blocking work to a worker thread.

---

## 5. Interview Traps

- Don't say “async always makes code faster.”
- Don't confuse concurrency with parallelism.
- Don't say async automatically uses multiple CPU cores.
- Don't put blocking calls inside async code without considering event-loop impact.
- `asyncio.gather()` is not a magic solution for CPU-bound work.

---

## 6. Memory Structure

```
async def
   ↓
coroutine
   ↓
await
   ↓
event loop
   ↓
Task
   ↓
gather()
   ↓
concurrent I/O
```

Workload decision:

```
I/O-bound + async library → asyncio
I/O-bound + blocking library → thread / compatible async library
CPU-bound → multiprocessing / process-based approach
```

---

## 7. 30-Second Interview Answer

> Asyncio is Python's framework for asynchronous programming. It uses an event loop to schedule coroutines. When a coroutine reaches an awaitable I/O operation, it can suspend and allow other tasks to run. This is useful for I/O-bound workloads such as API calls, database operations and LLM requests. For independent operations, asyncio.gather() can execute them concurrently and improve throughput. It does not automatically make CPU-bound code faster.

---

## 8. Coding Practice

### Exercise 1 — Sequential Retrieval

Simulate:
- Vector search → 2 seconds
- Keyword search → 1 second
- Metadata → 1 second

Expected ≈ 4 seconds.

### Exercise 2 — Concurrent Retrieval

Use `asyncio.gather()`.

Expected ≈ 2 seconds.

### Exercise 3 — Blocking Code

Explain why this is problematic:

```python
async def process():
    time.sleep(5)
```

Compare with:

```python
async def process():
    await asyncio.sleep(5)
```

### Exercise 4 — Production Follow-up

If an async FastAPI endpoint uses a synchronous SDK:
1. Prefer an async-compatible SDK.
2. Otherwise move suitable blocking work off the event-loop thread, e.g. `asyncio.to_thread()`.
3. Consider timeouts, retries, rate limits and concurrency limits.

### Exercise 5 — Interview Coding

Write a function that concurrently calls three independent async tools and returns a combined dictionary.

### 20-Minute Routine

5 min → read the Daily Reading.

5 min → answer the 13 high-value questions aloud.

5 min → run `app.async_demo.py` and `pytest`.

5 min → explain the RAG concurrency architecture without notes.
