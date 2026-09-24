from fastapi import FastAPI

app =FastAPI(
    title="Enterprise AI Agent",
    description="A production-oriented GenAI application built with Python, FastAPI, RAG, LangGraph, MCP and AWS.",
    version="0.1.0",
)

@app.get("/")
def home():
    return {
        "message": "Welcome to the Enterprise AI Agent",
        "status": "running"
        }

@app.get("/documents/{document_id}")
def get_document(document_id: str):
    return {
        "document_id": document_id,
        "message": "Document retrieved successfully"
    }


@app.get("/search")
def search(query:str, top_k:int):
    return {
        "query": query,
        "top_k": top_k,
        "message": "Search completed successfully"
        }

#  Post request where Pydantic becomes important.
from pydantic import BaseModel
class SearchRequest(BaseModel):
    query: str
    top_k: int = 5

@app.post("/search")
def search(request: SearchRequest):
    return {
        "query": request.query,
        "top_k": request.top_k
    }

# Pydantic can also define the response structure.
class SearchResponse(BaseModel):
    query: str
    results: list[dict]
    total: int

@app.post("/search", response_model=SearchResponse)
def search_document(request: SearchRequest):
    results = [
        "RAG combine Retrieval and Generation to answer the query.",
        "Embedding represents the text as a vectors."
    ]

    return SearchResponse(
        query=request.query,
        results=results,
        total=len(results)
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
