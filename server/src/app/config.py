from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database
    DATABASE_URI: str

    # Language model
    LANGUAGE_MODEL_API: str = "http://localhost:8080/v1"
    LANGUAGE_MODEL_NAME: str = "SmolLM3-Q4_K_M.gguf"

    # Security
    ORIGIN: str
    SECRET_KEY : str 
    ACCESS_TOKEN_EXPIRE_MINUTES: int 

    class Config:
        env_file = ".env"

settings = Settings()