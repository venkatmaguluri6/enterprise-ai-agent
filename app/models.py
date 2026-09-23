from dataclasses import dataclass
from enum import Enum
from typing import TypedDict


class ActionStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class AgentState(TypedDict):
    query: str
    answer: str
    documents: list[str]


@dataclass
class Document:
    document_id: str
    content: str
    source: str


@dataclass
class SearchResult:
    document_id: str
    content: str
    score: float
