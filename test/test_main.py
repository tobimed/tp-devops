from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_list_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_item():
    response = client.post("/items", json={"name": "Item C"})
    assert response.status_code == 200
    assert response.json()["name"] == "Item C"
