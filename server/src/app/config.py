from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # Database
    DATABASE_URI: str = Field("sqlite:///database.db", env='DATABASE_URI')  

    # Language model
    LANGUAGE_MODEL_API: str = Field("http://localhost:8080/v1", env='LANGUAGE_MODEL_API') 
    LANGUAGE_MODEL_NAME: str = Field("SmolLM3-Q4_K_M.gguf", env='LANGUAGE_MODEL_NAME')  

    # Security
    ORIGIN: str = Field('http://localhost:5173', env='ORIGIN')
    SECRET_KEY : str = Field('random_string', env='SECRET_KEY')
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 240
    ALGORITHM: str = "HS256"
    USER_LIMIT: int = 10

    class Config:
        env_file = ".env"

settings = Settings()