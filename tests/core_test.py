from fastapi.testclient import TestClient

from core.app import app

client = TestClient(app)


def test_healthcheck() -> None:
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"detail": "OK"}


def test_favicon() -> None:
    response = client.get("/favicon.ico")
    assert response.status_code == 200
