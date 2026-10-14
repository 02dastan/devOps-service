from fastapi import FastAPI

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