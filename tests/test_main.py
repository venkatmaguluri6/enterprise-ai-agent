from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_search_query_params():
    response = client.get(
        "/search/",
        params={"query": "What is RAG?", "top_k": 3},
    )
    assert response.status_code == 200
    assert response.json()["query"] == "What is RAG?"
    assert response.json()["top_k"] == 3


def test_search_request_body():
    response = client.post(
        "/search/",
        json={"query": "What is RAG?", "top_k": 2},
    )
    assert response.status_code == 200
    assert response.json()["total"] == 2
    assert len(response.json()["results"]) == 2


def test_search_invalid_body():
    response = client.post("/search/", json={"top_k": 5})
    assert response.status_code == 422


def test_search_invalid_top_k():
    response = client.post(
        "/search/",
        json={"query": "What is RAG?", "top_k": 0},
    )
    assert response.status_code == 422


def test_chat():
    response = client.post(
        "/chat/",
        json={"message": "Explain RAG"},
    )
    assert response.status_code == 200
    assert "Mock answer" in response.json()["answer"]


def test_chat_invalid_body():
    response = client.post("/chat/", json={})
    assert response.status_code == 422
