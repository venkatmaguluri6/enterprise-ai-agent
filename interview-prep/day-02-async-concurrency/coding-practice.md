# Day 2 — Async Python & Concurrency Coding Practice

## Exercise 1 — Sequential Retrieval

Simulate:
- Vector search → 2 seconds
- Keyword/BM25 search → 1 second
- Metadata lookup → 1 second

Expected: approximately 4 seconds.

## Exercise 2 — Concurrent Retrieval

Run the same operations using asyncio.gather().

Expected: approximately 2 seconds.

## Exercise 3 — Explain

Sequential = 2 + 1 + 1 ≈ 4 seconds

Concurrent = max(2, 1, 1) ≈ 2 seconds

The waits overlap because the operations are independent.

## Exercise 4 — Blocking Code

Why is this problematic?

    async def process():
        time.sleep(5)

Compare with:

    async def process():
        await asyncio.sleep(5)

## Exercise 5 — Production Follow-up

If an async FastAPI endpoint uses a synchronous blocking SDK:
1. Prefer an async-compatible SDK if available.
2. Otherwise move suitable blocking work off the event-loop thread, e.g. asyncio.to_thread().
3. Consider timeouts, retries, rate limits, and concurrency limits.

## Project

Implementation: app/async_demo.py

Run:
python -m app.async_demo

Tests:
pytest
