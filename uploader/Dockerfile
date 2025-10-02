FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Use environment variables for configs
ENV DB_PATH=/data/uploader.db

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
