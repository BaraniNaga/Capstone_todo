# Dockerfile
# 1) Base image
FROM python:3.12-slim

# 2) Environment
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# 3) Workdir
WORKDIR /app

# 4) Install build deps only if needed (comment out if not)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# 5) Install Python deps
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements

# 6) Copy project
COPY . /app

# 7) Cloud Run defaults to $PORT=8080; use it
ENV PORT=8080

# 8) Start FastAPI
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
