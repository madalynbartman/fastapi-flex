from fastapi.testclient import TestClient
from fastapi_flex.performance_optimization import app

client = TestClient(app)

def test_optimized_endpoint():
    response = client.get("/optimized-endpoint")
    assert response.status_code == 200
    assert response.json() == {"message": "This endpoint is optimized for performance!"}
