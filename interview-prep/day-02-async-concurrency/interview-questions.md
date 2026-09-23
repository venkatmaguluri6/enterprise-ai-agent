# Day 2 — Async Python & Concurrency Interview Questions

## Fundamentals

1. What is asynchronous programming?
2. What does async def do?
3. What is a coroutine function?
4. What is a coroutine object?
5. What does await do?
6. What is an event loop?
7. What is an asyncio Task?
8. What does asyncio.gather() do?
9. What is concurrency?
10. What is parallelism?

## Important Comparisons

11. Concurrency vs parallelism?
12. I/O-bound vs CPU-bound?
13. time.sleep() vs asyncio.sleep()?
14. Asyncio vs threading?
15. Asyncio vs multiprocessing?
16. Blocking vs non-blocking code?
17. Does async automatically make code faster?
18. Does async def automatically make every operation non-blocking?

## Practical / Production

19. What happens if time.sleep() is called inside an async function?
20. What happens when a coroutine is waiting for I/O?
21. Why is async useful in FastAPI?
22. Why is async useful when calling an LLM API?
23. How can asyncio.gather() help a RAG pipeline?
24. How can an AI agent execute independent tools concurrently?
25. What happens when a blocking library is used inside an async FastAPI endpoint?
26. How can a blocking function be handled from async code?
27. When would you choose threading instead of asyncio?
28. When is multiprocessing more suitable?

## High-Value Answers

**Does async make code automatically faster?**  
No. It can improve throughput and responsiveness for I/O-bound workloads by letting other tasks run while one task waits.

**What is the event loop?**  
It schedules and coordinates async tasks. When one coroutine is waiting for async I/O, the loop can run another ready task.

**Coroutine vs Task?**  
A coroutine is an awaitable unit of async execution. A Task schedules a coroutine on the event loop.

**Why use asyncio.gather()?**  
To run multiple independent async operations concurrently and collect their results.

**Why async for GenAI?**  
GenAI systems often wait for LLM APIs, vector databases, metadata services, and tools. Async lets other work progress during those waits.

**What if a blocking function is called inside async code?**  
It can block the event-loop thread and reduce concurrency. Prefer an async-compatible library or move suitable blocking work to a worker thread.

## Follow-ups

- Why would gather() not help a CPU-bound function?
- Can asyncio tasks automatically use multiple CPU cores?
- How would you limit concurrent LLM requests?
- How would you handle API rate limits?
- How would you add timeouts and retries?
