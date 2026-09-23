import pytest

from app.async_demo import (
    concurrent_search,
    fetch_keyword_search,
    fetch_metadata,
    fetch_vector_search,
)


@pytest.mark.asyncio
async def test_vector_search():
    assert len(await fetch_vector_search("What is RAG?")) == 2


@pytest.mark.asyncio
async def test_keyword_search():
    assert len(await fetch_keyword_search("What is RAG?")) == 2


@pytest.mark.asyncio
async def test_metadata_search():
    result = await fetch_metadata("What is RAG?")
    assert result["query"] == "What is RAG?"


@pytest.mark.asyncio
async def test_concurrent_search():
    result = await concurrent_search("What is RAG?")
    assert len(result["vector_results"]) == 2
    assert len(result["keyword_results"]) == 2
    assert result["metadata"]["query"] == "What is RAG?"
