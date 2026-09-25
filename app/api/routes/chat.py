from fastapi import APIRouter, Depends

from app.models.schemas import ChatRequest, ChatResponse
from app.services.chat_service import ChatService
from app.services.llm_service import LLMService, get_llm_service

router = APIRouter(prefix="/chat", tags=["Chat"])


def get_chat_service(
    llm_service: LLMService = Depends(get_llm_service),
) -> ChatService:
    return ChatService(llm_service=llm_service)


@router.post("/", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    chat_service: ChatService = Depends(get_chat_service),
) -> ChatResponse:
    return await chat_service.chat(request)
