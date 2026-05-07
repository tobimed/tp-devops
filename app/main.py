from fastapi import FastAPI

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
