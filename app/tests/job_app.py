from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)

def test_root_returns_message():
    response = client.get("/")