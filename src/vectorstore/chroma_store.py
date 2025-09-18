from langchain_chroma import Chroma
from src.ingestion.embeddings import get_embeddings
from src.config.settings import settings
import os

def get_chroma(persist=True):
    embeddings = get_embeddings()
    db_path = settings.CHROMA_DB_DIR

    os.makedirs(db_path, exist_ok=True)
    return Chroma(persist_directory=db_path, embedding_function=embeddings)
