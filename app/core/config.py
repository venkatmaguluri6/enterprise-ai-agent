import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    llm_model: str = os.getenv("LLM_MODEL", "mock-llm")
    llm_api_key: str | None = os.getenv("LLM_API_KEY")


settings = Settings()
