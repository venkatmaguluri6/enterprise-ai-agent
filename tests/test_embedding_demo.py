from app.services.embedding_demo import (
    build_context,
    cosine_similarity,
    embed,
    retrieve_top_k,
)


def test_identical_direction_has_high_similarity():
    assert cosine_similarity([1, 0], [1, 0]) == 1.0


def test_orthogonal_vectors_have_zero_similarity():
    assert cosine_similarity([1, 0], [0, 1]) == 0.0


def test_zero_vector_is_safe():
    assert cosine_similarity([0, 0], [1, 0]) == 0.0


def test_embedding_is_normalized():
    vector = embed("rag retrieval")
    magnitude = sum(value * value for value in vector) ** 0.5
    assert magnitude == 1.0


def test_retrieve_top_k_returns_requested_count():
    documents = [
        "RAG retrieves relevant context",
        "AWS Lambda is serverless",
        "Vector search compares embeddings",
    ]

    results = retrieve_top_k("RAG retrieval", documents, top_k=2)

    assert len(results) == 2
    assert results[0][0] == "RAG retrieves relevant context"


def test_build_context_joins_documents():
    results = [("first document", 0.9), ("second document", 0.8)]
    assert build_context(results) == "first document\nsecond document"
