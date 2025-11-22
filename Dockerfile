FROM python:3.12-slim

LABEL maintainer="YT-HourGen"
LABEL description="Generate 1-hour looped videos from YouTube"

RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/assets

ENTRYPOINT ["python", "main.py"]

CMD ["--help"]
