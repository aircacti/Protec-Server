from fastapi import APIRouter
from response import make_ok_response
from datetime import datetime, timezone

router = APIRouter(prefix="/status", tags=["status"])

@router.get("/")
def status():
    timestamp_ms = int(datetime.now(timezone.utc).timestamp() * 1000) # timestamp in ms since Unix epoch, e.g. 1759327447499
    return make_ok_response(
        "Protec API is running",
        extra={"timestamp": timestamp_ms}
    )