from fastapi import APIRouter
from src.api.schemas import QueryRequest, QueryResponse
from src.agents.sql_agent import build_sql_agent

router = APIRouter()
sql_agent = build_sql_agent()
chat_history = []   # store history as list of (q, a) tuples

@router.post("/chat", response_model=QueryResponse)
async def chat(request: QueryRequest):
    global chat_history

    # Agent answers the query
    answer = sql_agent.run(request.question)

    # Save in history
    chat_history.append((request.question, answer))

    # Build a contextual response (optional)
    context = "\n".join([f"Q: {q}\nA: {a}" for q, a in chat_history])

    return QueryResponse(answer=answer)
