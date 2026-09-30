"""Educational mock pipeline illustrating tokenization and autoregressive generation.

This is deliberately NOT a real language model. It uses a tiny toy vocabulary
and deterministic rules so the mechanics are easy to inspect.
"""
from __future__ import annotations

import re

TOY_VOCAB: dict[str, int] = {
    "what": 1,
    "is": 2,
    "rag": 3,
    "retrieval": 4,
    "augmented": 5,
    "generation": 6,
    "combines": 7,
    "with": 8,
    "language": 9,
    "model": 10,
    "?": 11,
    ".": 12,
    ":": 13,
}
UNKNOWN_TOKEN_ID = 0


def tokenize(text: str) -> list[str]:
    """Split text into word-like pieces and punctuation (toy tokenizer)."""
    return re.findall(r"\w+|[^\w\s]", text.lower())


def token_to_id(tokens: list[str]) -> list[int]:
    """Map tokens to toy vocabulary IDs; unknown tokens map to 0."""
    return [TOY_VOCAB.get(token, UNKNOWN_TOKEN_ID) for token in tokens]


def generate_next_token(tokens: list[str]) -> str:
    """Return a rule-based next token to demonstrate the generation loop."""
    normalized = [token.lower() for token in tokens]

    if not normalized:
        return "hello"
    if "rag" in normalized and "retrieval" not in normalized:
        return "retrieval"
    if "retrieval" in normalized and "augmented" not in normalized:
        return "augmented"
    if "augmented" in normalized and "generation" not in normalized:
        return "generation"
    if "generation" in normalized and "." not in normalized:
        return "."
    return "language"


def generate_response(prompt: str, max_tokens: int = 5) -> str:
    """Append toy next tokens to a prompt; this is not real LLM inference."""
    if max_tokens < 0:
        raise ValueError("max_tokens must be non-negative")

    generated_tokens = tokenize(prompt)
    for _ in range(max_tokens):
        next_token = generate_next_token(generated_tokens)
        generated_tokens.append(next_token)
        if next_token == ".":
            break

    # Preserve the user's original prompt in the displayed response.
    suffix_tokens = generated_tokens[len(tokenize(prompt)) :]
    suffix = " ".join(suffix_tokens)
    return f"{prompt.rstrip()} {suffix}".strip() if suffix else prompt
