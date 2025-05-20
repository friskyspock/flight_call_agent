from crewai.llm import LLM
from dotenv import load_dotenv 

load_dotenv()

llm = LLM(
    model="azure/gpt-35-turbo",
    api_version="2024-08-01-preview"
)