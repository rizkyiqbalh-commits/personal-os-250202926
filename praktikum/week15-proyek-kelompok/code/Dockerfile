FROM python:3.12-slim

WORKDIR /app

COPY main.py .
COPY cpu_scheduling.py .
COPY page_replacement.py .
COPY deadlock_detection.py .

COPY data/ ./data/

ENV PYTHONUNBUFFERED=1


CMD ["python", "main.py"]