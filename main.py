from fastapi import FastAPI
from core.config import settings

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "BuildMate backend running",
        "env": settings.APP_ENV
    }
