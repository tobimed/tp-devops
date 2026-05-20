# Etapa 1: instalar dependencias
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 2: imagen final
FROM python:3.12-slim
WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin/uvicorn /usr/local/bin/uvicorn
COPY --from=builder /usr/local/bin/newrelic-admin /usr/local/bin/newrelic-admin

COPY app/ ./app/

EXPOSE 8000

ENV NEW_RELIC_APP_NAME="TP DevOps API"
ENV NEW_RELIC_LOG=stdout

CMD ["newrelic-admin", "run-program", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
