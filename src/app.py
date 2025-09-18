from src.ingestion.loaders import load_documents
from src.ingestion.preprocessors import split_documents
from src.ingestion.embeddings import get_embeddings
from src.vectorstore.chroma_store import get_chroma
from dotenv import load_dotenv
load_dotenv()

def ingest():
    print("📥 Loading docs...")
    docs = load_documents()
    chunks = split_documents(docs)
    chroma = get_chroma()
    chroma.add_documents(chunks)
    print("✅ Ingestion complete.")

if __name__ == "__main__":
    ingest()
