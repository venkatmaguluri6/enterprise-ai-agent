from app.models.schemas import ChatRequest, ChatResponse
from app.services.llm_service import LLMService


class ChatService:
    def __init__(self, llm_service: LLMService) -> None:
        self.llm_service = llm_service

    async def chat(self, request: ChatRequest) -> ChatResponse:
        answer = await self.llm_service.generate(request.message)
        return ChatResponse(message=request.message, answer=answer)
