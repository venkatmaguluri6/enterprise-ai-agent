from dataclasses import  dataclass
from typing import TypedDict
from enum import Enum

class ActionStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

class AgeentState(TypedDict):
    query: str
    answer: str
    documents: list[str]

@dataclass
class Document():
    document_id: str
    content: str
    source: str

@dataclass
class searchResult():
    document_id: str
    content: str
    score: float