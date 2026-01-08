import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    CHROMA_DB_DIR = "data/processed/chroma_db"
    DATABASE_URI = os.getenv("DATABASE_URI", "mysql+pymysql://root@localhost:3306/realestate")

settings = Settings()
