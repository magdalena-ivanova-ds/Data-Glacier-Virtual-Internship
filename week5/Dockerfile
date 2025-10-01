# Python runtime
FROM python:3.11-slim

# Prevents Python from writing .pyc files & buffering stdout/err
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# System deps (optional but handy)
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

# Copy and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt && pip install --no-cache-dir gunicorn

# Copy the rest of the app
COPY . /app

# Cloud providers expect the app to listen on $PORT
ENV PORT=8080

EXPOSE 8080

# Use gunicorn for prod servers
CMD ["gunicorn", "-w", "2", "-k", "gthread", "-b", "0.0.0.0:8080", "app:app"]
