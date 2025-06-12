from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

class Settings(BaseSettings):
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "E-Commerce API")
    API_V1_STR: str = os.getenv("API_V1_STR", "/api/v1")
    REDIS_HOST: str = os.getenv("REDIS_HOST", "TEMP_REDIST_HOST")
    REDIS_PORT: str = os.getenv("REDIS_PORT", "TEMP_REDIST_PORT")
    S3_BUCKET_NAME: str = os.getenv("S3_BUCKET_NAME", "TEMP_S3_BUCKET")

    class Config:
        case_sensitive = True

settings = Settings()