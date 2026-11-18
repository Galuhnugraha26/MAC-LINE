
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements-serving.txt .

RUN python -m pip install --no-cache-dir \
    -r requirements-serving.txt

COPY app.py .
COPY model/model.joblib model/model.joblib

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app:app", \
     "--host", "0.0.0.0", "--port", "8000"]
