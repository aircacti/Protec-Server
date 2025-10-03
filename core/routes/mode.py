from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import SessionLocal
from core.models.mode import Mode
from core.auth import verify_token
from core.response import make_ok_response, make_problem_response

router = APIRouter(prefix="/mode", tags=["mode"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/set/{mode}", dependencies=[Depends(verify_token)])
def set_mode(mode: str, db: Session = Depends(get_db)):
    if mode not in ["normal", "lockdown", "shutdown"]:
        return make_problem_response(400, "Invalid mode. Allowed: normal, lockdown, shutdown.")

    current = db.query(Mode).first()
    old_mode = current.mode if current else None

    if not current:
        current = Mode(mode=mode)
        db.add(current)
    else:
        current.mode = mode

    db.commit()

    msg = f"Changed {old_mode} to {mode}" if old_mode else f"Mode set to: {mode}"
    extra = {"old_mode": old_mode, "new_mode": mode}

    return make_ok_response(msg, extra)

@router.get("/current", dependencies=[Depends(verify_token)])
def get_mode(db: Session = Depends(get_db)):
    current = db.query(Mode).first()
    mode_val = current.mode if current else "normal"

    msg = f"Current mode: {mode_val}"
    extra = {"mode": mode_val}
    return make_ok_response(msg, extra)
