from fastapi import APIRouter
from response import make_ok_response
from utils.TimeUtility import TimeUtility

router = APIRouter(prefix="/status", tags=["status"])

@router.get("/")
def status():
    timestamp_ms = TimeUtility.current_time_ms()
    return make_ok_response(
        "Protec API is running",
        extra={"timestamp": timestamp_ms}
    )