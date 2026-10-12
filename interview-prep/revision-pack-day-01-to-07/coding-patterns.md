# Coding Patterns for AI Engineer Interviews — Days 1–7

Keep this sheet for quick coding revision. Understand each line rather than memorizing blindly.

## 1. Return the Top 2 highest-scoring chunks

```python
def top_2(results: list[dict]) -> list[dict]:
    return sorted(
        results,
        key=lambda item: item["score"],
        reverse=True,
    )[:2]
```

- Time: **O(n log n)** due to sorting.
- Space: typically **O(n)** for the sorted result.
- Returns the full chunk dictionaries, not only the scores.

Example:
```python
results = [
    {"text": "A", "score": 0.72},
    {"text": "B", "score": 0.91},
    {"text": "C", "score": 0.65},
    {"text": "D", "score": 0.85},
]
assert [x["text"] for x in top_2(results)] == ["B", "D"]
```

### Follow-up: top 2 in one pass

```python
def top_2_one_pass(results: list[dict]) -> list[dict]:
    first = second = None

    for item in results:
        if first is None or item["score"] > first["score"]:
            second = first
            first = item
        elif second is None or item["score"] > second["score"]:
            second = item

    return [item for item in (first, second) if item is not None]
```

- Time: **O(n)**; extra space **O(1)** apart from the returned list.
- Handles empty lists and a one-item list.
- When scores tie, this keeps the earlier item at its current rank because comparisons use `>`.

## 2. Filter chunks above a threshold

```python
def filter_relevant(results: list[dict], threshold: float) -> list[dict]:
    return [item for item in results if item["score"] >= threshold]
```

Reminder: a similarity score is not a calibrated probability of correctness. Choose thresholds based on evaluation data.

## 3. Sort and return Top-K

```python
def top_k(results: list[dict], k: int) -> list[dict]:
    if k <= 0:
        return []
    return sorted(results, key=lambda item: item["score"], reverse=True)[:k]
```

For very large lists and small K, consider `heapq.nlargest(k, results, key=...)`, typically O(n log k).

## 4. Count tokens/words as a basic dictionary exercise

This is a word-frequency example, not a real LLM tokenizer:

```python
from collections import Counter
import re

def word_counts(text: str) -> dict[str, int]:
    words = re.findall(r"\b\w+\b", text.lower())
    return dict(Counter(words))
```

A real LLM tokenizer uses its own tokenization rules and vocabulary; splitting on whitespace is not equivalent.

## 5. Deduplicate while preserving order

```python
def unique_in_order(items: list[str]) -> list[str]:
    return list(dict.fromkeys(items))
```

Useful for removing repeated document IDs or labels while keeping the first occurrence.

## 6. Safe async concurrency pattern

```python
import asyncio

async def gather_with_timeout(coroutines, timeout_seconds: float = 10):
    return await asyncio.wait_for(
        asyncio.gather(*coroutines),
        timeout=timeout_seconds,
    )
```

This is a teaching pattern: if one combined timeout expires, the gathered operation is cancelled. Production code should consider per-request timeouts, partial failure handling, cancellation, and bounded concurrency.

## 7. Pydantic request validation pattern

```python
from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    question: str = Field(min_length=1, max_length=4000)
    top_k: int = Field(default=5, ge=1, le=20)
```

Validate inputs at the API boundary. Also validate authorization and any document/tenant filters server-side.

## 8. Build a prompt from retrieved chunks

```python
def build_context(chunks: list[dict]) -> str:
    return "\\n\\n".join(
        f"[Source: {chunk.get('source', 'unknown')}]\\n{chunk['text']}"
        for chunk in chunks
    )
```

Treat retrieved text as untrusted data. Delimit it clearly and instruct the LLM not to follow instructions embedded inside source documents. Prompting is only one layer of defense.

## 9. Common complexity reminders

| Operation | Typical time |
|---|---:|
| Iterate through a list | O(n) |
| Dictionary lookup | O(1) average |
| Sort n items | O(n log n) |
| Find max in a list | O(n) |
| Top-K using a full sort | O(n log n) |
| Top-K using a heap | O(n log k) |

## Practice without looking

1. Return the highest-scoring chunk.
2. Return Top-K chunks and handle k = 0.
3. Filter results by metadata, such as `department == "HR"`.
4. Remove duplicate document IDs while preserving order.
5. Explain the difference between O(n) top-2 scanning and O(n log n) sorting.
6. Explain why `time.sleep()` blocks an event loop.
7. Write a Pydantic model for a chat request.
8. Explain what should happen when RAG retrieval returns no relevant evidence.
