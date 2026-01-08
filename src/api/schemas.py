from pydantic import BaseModel
from typing import Literal, Optional, List

class QueryRequest(BaseModel):
    question: str
    mode: Literal["rag", "sql"] = "rag"
    chat_history: Optional[List[tuple[str, str]]] = None

class QueryResponse(BaseModel):
    answer: str
    mode: str
