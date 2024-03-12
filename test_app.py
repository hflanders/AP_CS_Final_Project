import pytest
from app import create_app

@pytest.fixture
def client():
    """creating a client that will create an app"""
    app = create_app()
    client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    yield client
    ctx.pop()

def test_say_hi(client):
    response = client.get('/say')
    assert response.status_code == 200 