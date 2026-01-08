from fastapi import APIRouter, HTTPException
from src.api.schemas import QueryRequest, QueryResponse
from src.agents.sql_agent import build_sql_agent
from src.chains.qa_chain import query_rag

router = APIRouter()

# Lazy initialization for SQL agent (only when needed)
_sql_agent = None

def get_sql_agent():
    global _sql_agent
    if _sql_agent is None:
        _sql_agent = build_sql_agent()
    return _sql_agent

# In-memory chat histories per mode
rag_history: list[tuple[str, str]] = []
sql_history: list[tuple[str, str]] = []

@router.post("/chat", response_model=QueryResponse)
async def chat(request: QueryRequest):
    global rag_history, sql_history

    try:
        if request.mode == "rag":
            # Use provided history or server-side history
            history = request.chat_history or rag_history
            answer = query_rag(request.question, history)
            rag_history.append((request.question, answer))
        else:
            # SQL mode
            agent = get_sql_agent()
            answer = agent.invoke({"input": request.question})["output"]
            sql_history.append((request.question, answer))

        return QueryResponse(answer=answer, mode=request.mode)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/history")
async def clear_history():
    global rag_history, sql_history
    rag_history = []
    sql_history = []
    return {"message": "Chat history cleared"}

@router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "langchain-chatbot"}
