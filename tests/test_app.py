from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    r = client.get("/")
    assert r.status_code == 200 and r.json()["message"]


def test_root_default_greeting():
    assert client.get("/").json()["message"] == "Hello, DevOps"


def test_healthz():
    assert client.get("/healthz").json() == {"status": "ok"}


def test_notes():
    assert len(client.get("/notes").json()) == 2

def test_time():
    assert "utc" in client.get("/time").json()