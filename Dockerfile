FROM python:3.10-slim

WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev

CMD ["python", "bot/main.py"]
