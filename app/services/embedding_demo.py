"""Educational embedding/vector-search demo.

This is intentionally NOT a real neural embedding model.
It uses a tiny bag-of-words representation so the mechanics of
embedding, cosine similarity and Top-K retrieval are easy to inspect.
"""
from __future__ import annotations

import math
import re

VOCAB = [
    "aws",
    "async",
    "fastapi",
    "python",
    "rag",
    "retrieval",
    "serverless",
    "vector",
    "search",
]

TOKEN_TO_INDEX = {token: index for index, token in enumerate(VOCAB)}


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z]+", text.lower())


def embed(text: str) -> list[float]:
    """Create a simple normalized bag-of-words vector."""
    vector = [0.0] * len(VOCAB)

    for token in tokenize(text):
        index = TOKEN_TO_INDEX.get(token)
        if index is not None:
            vector[index] += 1.0

    magnitude = math.sqrt(sum(value * value for value in vector))
    if magnitude == 0:
        return vector

    return [value / magnitude for value in vector]


def cosine_similarity(a: list[float], b: list[float]) -> float:
    if len(a) != len(b):
        raise ValueError("vectors must have the same dimension")

    norm_a = math.sqrt(sum(value * value for value in a))
    norm_b = math.sqrt(sum(value * value for value in b))

    if norm_a == 0 or norm_b == 0:
        return 0.0

    dot_product = sum(x * y for x, y in zip(a, b))
    return dot_product / (norm_a * norm_b)


def retrieve_top_k(
    query: str,
    documents: list[str],
    top_k: int = 3,
) -> list[tuple[str, float]]:
    if top_k < 1:
        raise ValueError("top_k must be at least 1")

    query_vector = embed(query)

    ranked = [
        (document, cosine_similarity(query_vector, embed(document)))
        for document in documents
    ]

    ranked.sort(key=lambda item: item[1], reverse=True)
    return ranked[:top_k]


def build_context(results: list[tuple[str, float]]) -> str:
    return "\n".join(document for document, _ in results)


if __name__ == "__main__":
    documents = [
        "FastAPI is a Python API framework",
        "RAG retrieves relevant context",
        "AWS Lambda is serverless",
        "Python supports async programming",
        "Vector search compares embeddings",
    ]

    results = retrieve_top_k("How does RAG retrieve information?", documents, top_k=2)

    print("Top results:")
    for document, score in results:
        print(f"{score:.3f} - {document}")

    print("\nContext:")
    print(build_context(results))
