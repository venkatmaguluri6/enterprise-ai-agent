import pytest

from app.services.llm_demo import (
    generate_next_token,
    generate_response,
    token_to_id,
    tokenize,
)


def test_tokenize_words_and_punctuation():
    assert tokenize("What is RAG?") == ["what", "is", "rag", "?"]


def test_token_to_id_uses_toy_vocabulary():
    assert token_to_id(["what", "unknown"]) == [1, 0]


def test_generate_next_token_for_rag_prompt():
    assert generate_next_token(["what", "is", "rag", "?"]) == "retrieval"


def test_generate_response_appends_tokens():
    response = generate_response("What is RAG?", max_tokens=3)
    assert response.startswith("What is RAG?")
    assert "retrieval augmented generation" in response


def test_generate_response_rejects_negative_max_tokens():
    with pytest.raises(ValueError):
        generate_response("Hello", max_tokens=-1)


def test_zero_max_tokens_returns_prompt():
    assert generate_response("Hello", max_tokens=0) == "Hello"
