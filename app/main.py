from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/items")
def list_items():
    return [{"id": 1, "name": "Item A"}, {"id": 2, "name": "Item B"}]

@app.post("/items")
def create_item(item: dict):
    return {"id": 3, **item}
    
@app.get("/version")
def get_version():
    return {
        "version": os.environ.get("APP_VERSION", "dev"),
        "commit": os.environ.get("GIT_COMMIT", "unknown")
    }
