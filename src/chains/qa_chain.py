from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
from src.vectorstore.chroma_store import get_chroma

def build_chatbot():
    chroma = get_chroma()
    retriever = chroma.as_retriever()
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    return ConversationalRetrievalChain.from_llm(llm, retriever)
