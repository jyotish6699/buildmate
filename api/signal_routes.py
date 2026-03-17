from fastapi import APIRouter
from pydantic import BaseModel

from services.signal_parser import signal_parser
from storage.redis_store import redis_store

router = APIRouter()

class SignalRequest(BaseModel):
    user_id: str
    text: str


@router.post("/signal")
def send_signal(request: SignalRequest):
    # 1. Parse signal
    signal_type = signal_parser.parse(request.text)

    #2.  Push to Redis
    redis_store.push_signal(signal_type, request.user_id)

    # 3. Return response
    return {
        "message": "signal received",
        "signal_type": signal_type
    }

