from app.core.config import settings


class LLMService:
    def __init__(self, model: str | None = None) -> None:
        self.model = model or settings.llm_model

    async def generate(self, prompt: str) -> str:
        # Mock provider for Day 4. A real async LLM client will be added later.
        return f"Mock answer from {self.model}: {prompt}"


def get_llm_service() -> LLMService:
    return LLMService()
