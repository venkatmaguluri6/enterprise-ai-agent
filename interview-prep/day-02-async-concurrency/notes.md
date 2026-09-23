# Day 2 — Async Python & Concurrency

## 1. The Simple Mental Model

Think of async programming like a restaurant.

- The **event loop** is the waiter.
- Each **async task** is a table/order.
- When one table is waiting for food, the waiter can serve another table.
- The waiter does not need to stand at one table doing nothing.

In software:

```text
Task A → waiting for API
              ↓
         Event Loop
          ↙       ↘
     Task B       Task C
       ↓
   Task A resumes when I/O is ready
```

The important point: **async is mainly about not wasting time while waiting for I/O.**

---

## 2. async def

`async def` defines a **coroutine function**.

Example:

```python
async def fetch_user():
    return {"name": "Venkat"}
```

Calling it does not immediately execute it like a normal function:

```python
result = fetch_user()
```

Here:

- `fetch_user` → coroutine function
- `result` → coroutine object

Usually we execute it with:

```python
result = await fetch_user()
```

or schedule it as a task.

### Remember

**async def → coroutine function**

**calling async function → coroutine object**

---

## 3. await

`await` means:

> "I need to wait for this asynchronous operation, but while I am waiting, let the event loop do other useful work."

Example:

```python
async def get_data():
    response = await call_api()
    return response
```

If `call_api()` is waiting for the network, another async task can run.

### Easy memory trick

```text
await = WAIT for this operation
        BUT don't block the event loop
```

---

## 4. Event Loop

The event loop is responsible for scheduling and coordinating async tasks.

Example:

```text
             Event Loop
                 |
       +---------+---------+
       |         |         |
     Task A    Task B    Task C
       |
    waiting
       |
       +----> Event loop runs B/C
       |
       +----> A resumes when ready
```

### Interview answer

> The event loop schedules asynchronous tasks and allows other ready tasks to run when the current task is waiting for asynchronous I/O.

---

## 5. Task

A Task schedules a coroutine to run on the event loop.

Example:

```python
task = asyncio.create_task(fetch_data())
```

Think:

```text
coroutine
   ↓
create_task()
   ↓
Task
   ↓
Event Loop
```

### Coroutine vs Task

**Coroutine:** describes asynchronous work.

**Task:** schedules that coroutine for execution.

---

## 6. asyncio.gather()

Use `asyncio.gather()` when you have multiple independent async operations.

Example:

```python
results = await asyncio.gather(
    fetch_vector_search(query),
    fetch_keyword_search(query),
    fetch_metadata(query),
)
```

Instead of:

```text
Vector Search → 2 sec
      ↓
Keyword Search → 1 sec
      ↓
Metadata → 1 sec

Total ≈ 4 sec
```

we can have:

```text
Vector Search ────────── 2 sec
Keyword Search ─── 1 sec
Metadata ───────── 1 sec

Total ≈ 2 sec
```

The operations themselves did not become faster.

**Their waiting time overlapped.**

---

## 7. Concurrency vs Parallelism

### Concurrency

Multiple tasks make progress during overlapping periods.

```text
Task A → waiting
Task B → running
Task C → running
Task A → resumes
```

### Parallelism

Multiple tasks actually execute at the same time, commonly using multiple CPU cores.

```text
CPU 1 → Task A
CPU 2 → Task B
CPU 3 → Task C
```

### Remember

**Concurrency = dealing with multiple tasks**

**Parallelism = executing multiple tasks at the same time**

---

## 8. I/O-Bound vs CPU-Bound

### I/O-bound

The program spends time waiting for something outside the CPU.

Examples:

- LLM API
- REST API
- Database
- Vector database
- File/network operation

Example:

```text
Python
  ↓
API request
  ↓
WAIT...
  ↓
Response
```

Async is often very useful here.

### CPU-bound

The program spends most of its time calculating.

Examples:

- Heavy mathematical computation
- CPU-intensive transformations
- Large calculations

Asyncio does not automatically make CPU-bound work parallel.

Depending on the problem, multiprocessing or other CPU-oriented approaches may be better.

---

## 9. Does async make code faster?

**Not automatically.**

This is an important interview question.

Bad answer:

> Async always makes Python faster.

Better answer:

> Async can improve throughput and responsiveness for I/O-bound workloads because other tasks can run while one task is waiting.

For example, if an LLM API takes 3 seconds to respond, async does not necessarily make that API respond in 1 second.

It prevents your application from sitting idle during those 3 seconds.

---

## 10. time.sleep() vs asyncio.sleep()

### Blocking

```python
async def process():
    time.sleep(5)
```

`time.sleep()` blocks the thread.

If that thread is running the event loop, other async tasks cannot make progress.

### Non-blocking async wait

```python
async def process():
    await asyncio.sleep(5)
```

The coroutine waits, but the event loop can run other tasks.

### Remember

```text
time.sleep()
     ↓
BLOCKS thread ❌

await asyncio.sleep()
     ↓
NON-BLOCKING async wait ✅
```

---

## 11. Very Important: async def Does NOT Make Everything Async

This is a common interview trap.

This function is async:

```python
async def endpoint():
    result = requests.get(url)
    return result.json()
```

But `requests.get()` is still a blocking synchronous operation.

So:

```text
async def
   ↓
blocking requests.get()
   ↓
event loop can be blocked
```

Using `async def` alone does not magically convert synchronous code into asynchronous code.

---

## 12. Asyncio vs Threading

### Asyncio

- Event-loop based
- Usually works very well for async I/O
- Often uses a single thread
- Good for many concurrent network operations

### Threading

- Uses multiple OS threads
- Useful for blocking/synchronous libraries
- Can be useful when an async version of a library is unavailable

Example:

```python
result = await asyncio.to_thread(blocking_function)
```

This can move suitable blocking work away from the event-loop thread.

---

## 13. Asyncio vs Multiprocessing

Use multiprocessing when the problem is CPU-heavy and you need actual parallel CPU execution.

Simple rule:

```text
I/O-bound
   ↓
asyncio / threading

CPU-bound
   ↓
multiprocessing / process-based execution
```

This is a simplified rule; the correct choice depends on the workload and library behavior.

---

## 14. Why This Matters for Our GenAI Project

Our future RAG pipeline can have:

```text
                   User Query
                       |
        +--------------+--------------+
        |              |              |
        ↓              ↓              ↓
   Vector Search   BM25 Search   Metadata Search
        |              |              |
        +--------------+--------------+
                       |
                 Hybrid Ranking
                       |
                    LLM
                       |
                    Answer
```

Vector search, BM25 search, and metadata retrieval may be independent.

Therefore, we can potentially execute them concurrently:

```python
results = await asyncio.gather(
    vector_search(query),
    bm25_search(query),
    metadata_search(query),
)
```

This is the reason we are learning asyncio **before building the real RAG pipeline**.

---

## 15. Our Day 2 Project Example

File:

`app/async_demo.py`

We simulate:

- Vector search → 2 seconds
- Keyword search → 1 second
- Metadata → 1 second

Sequential:

```text
2 + 1 + 1 = approximately 4 seconds
```

Concurrent:

```text
max(2, 1, 1) = approximately 2 seconds
```

Run:

```bash
python -m app.async_demo
```

Test:

```bash
pytest
```

---

## 16. Interview Cheat Sheet

| Concept | Easy Meaning |
|---|---|
| `async def` | Defines coroutine function |
| Coroutine | Async unit of work |
| `await` | Wait without blocking event loop |
| Event loop | Schedules async work |
| Task | Scheduled coroutine |
| `gather()` | Run independent async operations concurrently |
| Concurrency | Multiple tasks make progress |
| Parallelism | Multiple tasks execute simultaneously |
| I/O-bound | Mostly waiting |
| CPU-bound | Mostly calculating |
| `time.sleep()` | Blocking |
| `asyncio.sleep()` | Non-blocking async wait |
| Asyncio | Event-loop based concurrency |
| Threading | Multiple OS threads |
| Multiprocessing | Process-based CPU parallelism |

---

## 17. 30-Second Interview Answer

If the interviewer asks:

> "Explain asyncio in Python."

Say:

> Asyncio is Python's framework for asynchronous programming. It uses an event loop to schedule coroutines. When a coroutine reaches an awaitable I/O operation, it can suspend and allow other tasks to run. This is especially useful for I/O-bound workloads such as API calls, database operations and LLM requests. For independent operations, asyncio.gather() can execute them concurrently and improve overall throughput. It does not automatically make CPU-bound code faster.

That is the answer I want you to remember for interviews.
