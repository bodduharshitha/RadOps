from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy"
    }


def test_create_security_event():
    event = {
        "type": "BOT_ACTIVITY",
        "severity": "HIGH",
        "source": "10.0.0.50",
        "description": "Repeated automated requests detected"
    }

    response = client.post("/api/security-events", json=event)

    assert response.status_code == 200
    assert response.json() == event