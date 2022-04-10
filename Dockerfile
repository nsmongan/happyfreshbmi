# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt
COPY main.py main.py

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
