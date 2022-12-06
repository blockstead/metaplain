from fastapi.testclient import TestClient

from http import HTTPStatus
from src.main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == "OK"


def test_get():
    response = client.get("/get")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == "OK"


def test_put():
    response = client.get("/put")
    assert response.status_code == HTTPStatus.NOT_IMPLEMENTED
    assert response.json() == "ERROR"


def test_patch():
    response = client.get("/patch")
    assert response.status_code == HTTPStatus.NOT_IMPLEMENTED
    assert response.json() == "ERROR"


def test_delete():
    response = client.get("/delete")
    assert response.status_code == HTTPStatus.NOT_IMPLEMENTED
    assert response.json() == "ERROR"
