from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# First do posts, then do get
# def test