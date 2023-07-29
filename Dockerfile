# Dockerfile
FROM python:3

COPY requirements.txt .

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt && \
    apt-get update && apt-get upgrade -y && \
    apt-get install -y libgl1-mesa-dev

WORKDIR /python
COPY /app.py /