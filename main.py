import os
import sys

import uvicorn
from fastapi import FastAPI, Request
from config import load_config
from starlette.exceptions import HTTPException as StarletteHTTPException
from database import Base, engine
from routes import mode, status, howdy
from response import make_problem_response  # your response helpers
from auth import is_token_valid

config = load_config()

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Protec - Security API")
app.include_router(mode.router)
app.include_router(status.router)
app.include_router(howdy.router)

# Global exception handlers for standardized responses
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):

    # Handle 401 Unauthorized
    if exc.status_code == 401:
        return make_problem_response(401, "Unauthorized", extra={"path": request.url.path})

    # Handle unauthorized 404 and 405
    if exc.status_code in (404, 405) and not is_token_valid(request):
        return make_problem_response(401, "Unauthorized", extra={"path": str(request.url)})

    # Handle authorized 404 Not Found
    if exc.status_code == 404:
        return make_problem_response(404, "Not found", extra={"path": str(request.url)})

    # Handle authorized 405 Method Not Allowed
    if exc.status_code == 405:
        return make_problem_response(405, "Method not allowed", extra={"method": request.method, "path": str(request.url)})


    # Any other HTTP exception
    return make_problem_response(exc.status_code, "Other exception", extra={"details": exc.detail, "path": request.url.path})

if __name__ == "__main__":
    if config["auth"]["token"] == "supersecrettoken123":
        print("Change default token in config.yaml!")

    ssl_config = config.get("server", {}).get("ssl", {})
    ssl_enabled = ssl_config.get("enabled", False)

    if ssl_enabled:
        certfile = ssl_config.get("certfile")
        keyfile = ssl_config.get("keyfile")


        if not (certfile and keyfile):
            print("SSL enabled but certfile or keyfile is not specified in config.yaml!")
            sys.exit(1)
        if not os.path.exists(certfile):
            print(f"SSL certificate file not found: {certfile}")
            sys.exit(1)
        if not os.path.exists(keyfile):
            print(f"SSL key file not found: {keyfile}")
            sys.exit(1)

    uvicorn.run(
        "main:app",
        host=config["server"]["host"],
        port=int(config["server"]["port"]),
        reload=False,
        ssl_certfile=certfile if ssl_enabled else None,
        ssl_keyfile=keyfile if ssl_enabled else None,
    )