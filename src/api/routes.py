from fastapi import APIRouter
from src.api.schemas import QueryRequest, QueryResponse
from src.chains.qa_chain import build_chatbot

router = APIRouter()

chatbot = build_chatbot()
chat_history = []   # list of (question, answer)

@router.post("/chat", response_model=QueryResponse)
async def chat(request: QueryRequest):
    global chat_history

    result = chatbot({
        "question": request.question,
        "chat_history": chat_history
    })

    answer = result["answer"]

    # update memory
    chat_history.append((request.question, answer))

    return QueryResponse(answer=answer)
