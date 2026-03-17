from fastapi import FastAPI
from core.config import settings

from storage.redis_store import redis_store
from storage.postgres_store import postgres_store

from api.signal_routes import router as signal_route

from realtime.websocket_routes import router as ws_router


app = FastAPI()

# Register routes
app.include_router(signal_route)
app.include_router(ws_router)

@app.get("/")
def root():
    return {
        "message": "BuildMate backend running",
        "env": settings.APP_ENV
    }


@app.get("/test-storage")
def test_storage():
    # Redis test
    redis_store.add_online_user("test_user")

    # Postgres test
    result = postgres_store.execute("SELECT 1 as test", fetch=True)

    return {
        "redis": "ok",
        "postgres": result
    }