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

def test_welcome_image(client):
    response = client.get('/welcome')
    assert response.status_code == 200

def test_question_1(client):
    response = client.get('/question/1')
    assert response.status_code == 200 

def test_question_2(client):
    response = client.get('/question/2')
    assert response.status_code == 200

def test_question_3(client):
    response = client.get('/question/3')
    assert response.status_code == 200

def test_question_4(client):
    response = client.get('/question/4')
    assert response.status_code == 200