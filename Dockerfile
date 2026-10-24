FROM python:3.14-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# dependencies first: this layer stays cached until requirements.txt changes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8080
EXPOSE 8080
USER 1000:1000
CMD ["sh", "-c", "exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]