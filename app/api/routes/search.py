from fastapi import APIRouter

from app.models.schemas import SearchRequest, SearchResponse
from app.services.search_service import SearchService

router = APIRouter(prefix="/search", tags=["Search"])
search_service = SearchService()


@router.get("/")
async def search(query: str, top_k: int = 5) -> dict[str, object]:
    return await search_service.search_preview(query, top_k)


@router.post("/", response_model=SearchResponse)
async def search_documents(request: SearchRequest) -> SearchResponse:
    return await search_service.search(request)
