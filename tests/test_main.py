from fastapi.testclient import TestClient
from app.main import app

#from app.main import get_stock_winners

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_get_stock_winners(expected_output):
    response = client.get("/get_stock_winners")
    assert response.status_code == 200
    assert response.json() == expected_output