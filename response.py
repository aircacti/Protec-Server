from fastapi.responses import JSONResponse
from typing import Literal

def _make_response(
    result: Literal["ok", "problem"],
    message: str,
    status_code: int = 200,
    extra: dict | None = None
) -> JSONResponse:
    """
    Internal helper to generate standardized JSON response.
    Allows adding extra fields via `extra` dictionary.
    """
    content = {
        "result": result,
        "message": message
    }
    if extra:
        content.update(extra)
    return JSONResponse(status_code=status_code, content=content)


def make_ok_response(message: str, extra: dict | None = None) -> JSONResponse:
    """
    Generates a 200 OK response with result="ok".
    Optional extra fields can be added via `extra`.
    """
    return _make_response("ok", message, status_code=200, extra=extra)


def make_problem_response(status_code: int, message: str, extra: dict | None = None) -> JSONResponse:
    """
    Generates a response with result="problem" and the given HTTP status code.
    Optional extra fields can be added via `extra`.
    """
    return _make_response("problem", message, status_code=status_code, extra=extra)
