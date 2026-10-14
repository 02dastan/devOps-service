# devOps-service

## What it does
This is a small HTTP service I built with FastAPI for my INF 345 DevOps course. It has four endpoints: `GET /` returns a greeting, `GET /healthz` returns `{"status": "ok"}` and is the health check I will use later for Docker and Kubernetes, `GET /notes` returns a hard-coded list of notes, and `GET /time` returns the current UTC time. It has no database. I keep it small on purpose, because the course is about the path from my laptop to production, not about the app itself.

## How to run
I start the service with one command:

```bash
./scripts/run.sh
```

The script creates a virtual environment in `.venv`, installs the packages from `requirements.txt`, and starts uvicorn. Then I open `http://localhost:8080/`.

## How to test
I run the tests with:

```bash
./scripts/test.sh
```

It installs the dependencies, runs pytest (4 tests that call the real app), and prints `TESTS: n/n`. It exits with code 0 if everything passes and a non-zero code if something fails.

## Port
The service reads the port from the `PORT` environment variable and uses 8080 if it is not set. For example, `PORT=9000 ./scripts/run.sh` starts it on port 9000.