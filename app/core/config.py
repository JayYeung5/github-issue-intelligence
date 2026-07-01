from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    GITHUB_TOKEN: str
    SECRET_KEY: str = "changeme"

    class Config:
        env_file = ".env"

settings = Settings()