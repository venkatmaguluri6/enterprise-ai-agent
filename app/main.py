from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Enterprise AI Agent",
    description="A production-oriented GenAI application built with Python, FastAPI, RAG, LangGraph, MCP and AWS.",
    version="0.1.0",
)

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5

class SearchResponse(BaseModel):
    query: str
    results: list[str]
    total: int

@app.get("/")
def home() -> dict[str, str]:
    return {"message": "Welcome to the Enterprise AI Agent", "status": "running"}

@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "healthy"}

@app.get("/documents/{document_id}")
def get_document(document_id: str) -> dict[str, str]:
    return {"document_id": document_id, "message": "Document retrieved successfully"}

@app.get("/search")
def search(query: str, top_k: int = 5) -> dict[str, object]:
    return {"query": query, "top_k": top_k, "message": "Search completed successfully"}

@app.post("/search", response_model=SearchResponse)
def search_documents(request: SearchRequest) -> SearchResponse:
    results = [
        "RAG combines retrieval with generation.",
        "Embeddings represent text as vectors.",
    ]
    selected_results = results[:request.top_k]
    return SearchResponse(
        query=request.query,
        results=selected_results,
        total=len(selected_results),
    )


""" Now our API contract is explicit.

        Request
        ↓
        SearchRequest
        ↓
        Service
        ↓
        SearchResponse
        ↓
        Client

"""
# This is the pattern we'll eventually use for our GenAI APIs.

# Async FastAPI endpoint
@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }

@app.get("/async-search")
async def async_search():
    results = await some_async_operation()
    return results

# Now eventually our endpoint can call it:
'''        POST /search
            ↓
        FastAPI
            ↓
        SearchRequest
            ↓
        concurrent_search()
            ↓
        Vector Search
        BM25 Search
        Metadata
            ↓
        Response

'''
