from fastapi.testclient import TestClient

from ..app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Bigger Applications!"}


def test_read_item():
    response = client.get("/items/foo", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

    response = client.get("/items/plumbus", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}

    response = client.get("/items/plumbus", headers={"X-Token": "fake-super-secret-token"})
    assert response.status_code == 200
    assert response.json() == {
        "item_id": "plumbus",
        "name": "Plumbus",
    }
