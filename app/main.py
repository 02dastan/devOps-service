from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI()

NOTES = [{"id": 1, "text": "first"}, {"id": 2, "text": "second"}]


@app.get("/")
async def root():
    return {"message": "Hello, DevOps"}


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}


@app.get("/notes")
async def notes():
    return NOTES

@app.get("/time")
async def server_time():
    return {"utc": datetime.now(timezone.utc).isoformat()}