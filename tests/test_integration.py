import pytest
from fastapi.testclient import TestClient
from fastapi_flex.integration import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_websocket():
    with client.websocket_connect("/ws") as websocket:
        data = websocket.receive_text()
        assert data == "Hello, WebSocket!"
