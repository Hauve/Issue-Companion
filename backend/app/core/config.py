from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    qdrant_host: str = "localhost"
    qdrant_port: int = 6333
    collection_name: str = "issues"
    openai_api_key: str
    embedding_model: str = "text-embedding-3-small"
    llm_model: str = "grok-4-fast"
    
    class Config:
        env_file = ".env"


settings = Settings()