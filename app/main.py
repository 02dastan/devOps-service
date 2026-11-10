import os
from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI()

# the greeting comes from the environment so I can change it without rebuilding the image
GREETING = os.environ.get("GREETING", "Hello, DevOps")

NOTES = [{"id": 1, "text": "first"}, {"id": 2, "text": "second"}]


@app.get("/")
async def root():
    return {"message": GREETING}


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}


@app.get("/notes")
async def notes():
    return NOTES

@app.get("/time")
async def server_time():
    return {"utc": datetime.now(timezone.utc).isoformat()}