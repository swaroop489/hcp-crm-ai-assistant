from langchain_groq import ChatGroq
from app.core.config import settings

def get_llm():
    """
    Returns an instance of the LLM initialized with our settings.
    Prefers Groq (llama-3.1-8b-instant), but falls back to Google Gemini if Groq is empty.
    """
    if settings.GROQ_API_KEY and settings.GROQ_API_KEY.strip():
        return ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model_name="llama-3.1-8b-instant",
            temperature=0.0,
            max_retries=0,
            timeout=15
        )
    elif settings.GEMINI_API_KEY and settings.GEMINI_API_KEY.strip():
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(
            model=settings.GEMINI_MODEL_NAME,
            google_api_key=settings.GEMINI_API_KEY,
            temperature=0.0,
            max_retries=0
        )
    else:
        raise ValueError("No API key provided for Groq or Gemini.")
