import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_ENV = os.getenv("APP_ENV")
    PORT = int(os.getenv("PORT", 8000))

    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

settings = Settings()
