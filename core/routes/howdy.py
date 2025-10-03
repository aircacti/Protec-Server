from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from core.database import SessionLocal
from core.models.mode import Mode
from core.models.device_report import DeviceReport
from core.auth import require_token
from core.response import make_ok_response, make_problem_response
from core.utils.TimeUtility import TimeUtility

router = APIRouter(prefix="/howdy", tags=["howdy"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", dependencies=[Depends(require_token)])
def howdy(request: Request, db: Session = Depends(get_db)):
    current_mode = db.query(Mode).first()
    mode_value = current_mode.mode if current_mode else "normal"

    device_name = request.headers.get("Device-Name")
    if not device_name:
        return make_problem_response(400, "Missing required header: Device-Name")

    report = db.query(DeviceReport).filter_by(device_name=device_name).first()
    system_timestamp = TimeUtility.current_time_ms()
    ip = request.client.host

    ip_changed = False
    if not report:

        report = DeviceReport(
            device_name=device_name,
            last_seen=system_timestamp,
            last_ip=ip
        )
        db.add(report)
        ip_changed = True
    else:
        report.last_seen = system_timestamp
        if report.last_ip != ip:
            ip_changed = True
            report.last_ip = ip

    db.commit()

    extra = {
        "mode": mode_value,
        "order": "none",
        "timestamp": system_timestamp,
        "ip_changed": ip_changed
    }
    return make_ok_response(f"Great {device_name}", extra)
