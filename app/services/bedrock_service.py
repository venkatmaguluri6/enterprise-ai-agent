"""Small Amazon Bedrock Converse integration.

Real AWS calls are only made when no client is injected. Tests should inject
a fake client so they do not require AWS credentials or call the network.
"""
from __future__ import annotations

from typing import Any


def generate_text(
    prompt: str,
    model_id: str,
    region_name: str,
    max_tokens: int = 300,
    temperature: float = 0.2,
    client: Any | None = None,
) -> str:
    """Generate text using a model that supports Bedrock's Converse API."""
    if not prompt or not prompt.strip():
        raise ValueError("prompt must not be empty")
    if not model_id or not model_id.strip():
        raise ValueError("model_id must not be empty")
    if not region_name or not region_name.strip():
        raise ValueError("region_name must not be empty")
    if max_tokens < 1:
        raise ValueError("max_tokens must be at least 1")
    if not 0.0 <= temperature <= 1.0:
        raise ValueError("temperature must be between 0.0 and 1.0")

    if client is None:
        import boto3

        client = boto3.client("bedrock-runtime", region_name=region_name)

    response = client.converse(
        modelId=model_id,
        messages=[
            {
                "role": "user",
                "content": [{"text": prompt.strip()}],
            }
        ],
        inferenceConfig={
            "maxTokens": max_tokens,
            "temperature": temperature,
        },
    )

    try:
        content_blocks = response["output"]["message"]["content"]
        text_blocks = [
            block["text"] for block in content_blocks if isinstance(block, dict) and "text" in block
        ]
    except (KeyError, TypeError) as exc:
        raise RuntimeError("Bedrock returned an unexpected response shape") from exc

    if not text_blocks:
        raise RuntimeError("Bedrock response did not contain generated text")
    return "\n".join(text_blocks)
