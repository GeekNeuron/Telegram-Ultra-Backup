# Build stage
FROM python:3.11-slim AS builder
WORKDIR /app
COPY bot/ bot/
COPY admin-panel/ admin-panel/
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt

# Final stage
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /wheels /wheels
COPY requirements.txt .
RUN pip install --no-cache-dir --no-index -f /wheels -r requirements.txt
COPY bot/ bot/
COPY admin-panel/ admin-panel/
COPY translations/ translations/
COPY docs/ docs/
COPY .env.example .env
ENV FLASK_APP=admin-panel/app.py
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
