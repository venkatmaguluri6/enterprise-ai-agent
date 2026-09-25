from app.models.schemas import SearchRequest, SearchResponse


class SearchService:
    async def search(self, request: SearchRequest) -> SearchResponse:
        results = [
            "RAG combines retrieval with generation.",
            "Embeddings represent text as vectors.",
            "Hybrid search can combine keyword and vector search.",
        ]
        selected_results = results[: request.top_k]
        return SearchResponse(
            query=request.query,
            results=selected_results,
            total=len(selected_results),
        )

    async def search_preview(self, query: str, top_k: int = 5) -> dict[str, object]:
        return {
            "query": query,
            "top_k": top_k,
            "message": "Search service executed successfully",
        }
