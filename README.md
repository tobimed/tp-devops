# TP DevOps

API REST desarrollada con FastAPI.

## Endpoints

- GET / - Health check
- GET /items - Lista items
- POST /items - Crea un item

## Correr localmente

```bash
uvicorn app.main:app --reload
```

## Correr con Docker

```bash
docker-compose up --build
```

## Tests

```bash
pytest
```
