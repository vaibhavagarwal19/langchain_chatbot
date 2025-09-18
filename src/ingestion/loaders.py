from langchain_community.document_loaders import PyPDFLoader, CSVLoader,TextLoader
import os
def load_documents(path="data/raw"):
    docs = []
    for file in os.listdir(path):
        full_path = os.path.join(path, file)

        if file.endswith(".txt"):
            loader = TextLoader(full_path, encoding="utf-8", autodetect_encoding=True)
        elif file.endswith(".pdf"):
            loader = PyPDFLoader(full_path)
        elif file.endswith(".csv"):
            loader = CSVLoader(full_path)
        else:
            continue

        docs.extend(loader.load())
    return docs
