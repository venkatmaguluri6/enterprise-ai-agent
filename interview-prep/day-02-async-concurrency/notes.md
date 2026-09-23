# Day 2 — Async Python & Concurrency

## Core Concepts

- **async def** → defines a coroutine function.
- **Coroutine object** → created when an async function is called.
- **await** → suspends the current coroutine while an async operation is pending, allowing the event loop to run other ready tasks.
- **Event loop** → schedules and coordinates asynchronous tasks.
- **Task** → schedules a coroutine to run on the event loop; commonly created with asyncio.create_task().
- **asyncio.gather()** → runs multiple independent awaitables concurrently and collects their results.

## Concurrency vs Parallelism

- Concurrency: multiple tasks make progress during overlapping periods.
- Parallelism: multiple tasks execute simultaneously, often using multiple CPU cores/resources.

## I/O-Bound vs CPU-Bound

I/O-bound work waits for APIs, databases, LLM services, vector stores, or networks. Async is often useful.

CPU-bound work spends most of its time computing. Asyncio does not automatically distribute CPU work across cores; multiprocessing may be more appropriate.

## Blocking vs Non-Blocking

time.sleep() blocks the thread and can block the event loop.

await asyncio.sleep() performs a non-blocking async wait, allowing other async tasks to run.

Important: async def does NOT make every operation inside it non-blocking.

## GenAI Connection

A RAG/agent request may need independent calls:

User Query
  ├── Vector Search
  ├── Keyword/BM25 Search
  └── Metadata Service
             ↓
       Combine Results

These can potentially run concurrently.

For waits of 2s, 1s, and 1s:
- Sequential ≈ 4s
- Concurrent ≈ 2s

Async does not make the individual APIs intrinsically faster. It uses waiting time more efficiently.

## Asyncio vs Threading

Asyncio uses an event loop and is excellent for async-compatible I/O.

Threading uses multiple OS threads and can be useful when integrating blocking/synchronous libraries.

For suitable blocking work from async code, asyncio.to_thread() is one option.

## FastAPI Connection

An async FastAPI endpoint can handle async I/O efficiently, but a blocking call inside it can block the event-loop thread. Prefer async-compatible clients when available.
