from fastapi.testclient import TestClient
from fastapi_flex.flexibility import app

client = TestClient(app)

def test_middleware():
    response = client.get("/")
    assert response.status_code == 404  # Assuming the root endpoint is not defined
