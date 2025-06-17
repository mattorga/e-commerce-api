from fastapi import FastAPI
from app.core.config import settings
from app.api.routers import products

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# print(f"Redist Host: {settings.REDIS_HOST}")
# print(f"Redist Port: {settings.REDIS_PORT}")
# print(f"S3 Bucket Name: {settings.S3_BUCKET_NAME}")
