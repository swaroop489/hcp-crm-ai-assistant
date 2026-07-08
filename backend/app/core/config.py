from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    GROQ_API_KEY: str | None = None
    GEMINI_API_KEY: str | None = None
    GEMINI_MODEL_NAME: str = "gemini-flash-latest"

    class Config:
        env_file = ".env"

settings = Settings()
