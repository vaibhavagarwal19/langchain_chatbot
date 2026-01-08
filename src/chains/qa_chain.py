from langchain.chains import ConversationalRetrievalChain
from langchain_google_genai import ChatGoogleGenerativeAI
from src.vectorstore.chroma_store import get_chroma
from src.config.settings import settings

_qa_chain = None

def get_qa_chain():
    """Lazy initialization of the QA chain (singleton)."""
    global _qa_chain
    if _qa_chain is None:
        chroma = get_chroma()
        retriever = chroma.as_retriever(search_kwargs={"k": 4})
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0,
            google_api_key=settings.GOOGLE_API_KEY
        )
        _qa_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=retriever,
            return_source_documents=True,
            verbose=True
        )
    return _qa_chain

def query_rag(question: str, chat_history: list[tuple[str, str]] = None) -> str:
    """Query the RAG chain with optional chat history."""
    chain = get_qa_chain()
    history = chat_history or []
    result = chain.invoke({"question": question, "chat_history": history})
    return result["answer"]
