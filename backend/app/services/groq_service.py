from langchain_groq import ChatGroq
from app.core.config import settings

def get_llm():
    """
    Returns an instance of the Groq LLM initialized with our settings.
    We use gemma2-9b-it as specified in the project requirements.
    """
    return ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model_name="gemma2-9b-it",
        temperature=0.0
    )
