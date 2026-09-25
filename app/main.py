from fastapi import FastAPI

from app.api.routes.chat import router as chat_router
from app.api.routes.health import router as health_router
from app.api.routes.search import router as search_router

app = FastAPI(
    title="Enterprise AI Agent",
    description=(
        "A production-oriented GenAI application built with Python, FastAPI, "
        "RAG, LangGraph, MCP and AWS."
    ),
    version="0.2.0",
)

app.include_router(health_router)
app.include_router(search_router)
app.include_router(chat_router)


@app.get("/")
async def home() -> dict[str, str]:
    return {
        "message": "Welcome to the Enterprise AI Agent",
        "status": "running",
    }
