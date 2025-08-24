from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Sistema Lifeflow"
    API_V1_STR: str = "/api/v1"
    
    # Configurações do MongoDB
    MONGODB_URL: str
    MONGODB_DATABASE: str

    class Config:
        env_file = ".env" # Aponta para o arquivo .env na raiz do projeto

settings = Settings()