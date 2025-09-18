from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.base import create_sql_agent, SQLDatabaseToolkit
from langchain_openai import ChatOpenAI
from src.config.settings import settings

def build_sql_agent():
    # Connect lazily when called
    db = SQLDatabase.from_uri("mysql+pymysql://root@localhost:3306/realestate")

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        api_key=settings.OPENAI_API_KEY
    )

    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True
    )
    return agent_executor
