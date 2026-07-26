import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_cpi_data(client):
    response = client.get('/cpi-data')
    assert response.status_code == 200
    data = response.get_json()
    assert data['2022'][0] == 281.148
