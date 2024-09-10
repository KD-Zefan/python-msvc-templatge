from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ENVIRONMENT: str = "local"

    class Config:
        env_file = ".env"


settings = Settings()
