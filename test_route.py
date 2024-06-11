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
    # tests that the code is printed correctly
    response = client.get('/welcome')
    assert response.status_code == 200

def test_question_1(client):
    # tests that the code is printed correctly
    response = client.get('/question/1')
    assert response.status_code == 200 

def test_question_2(client):
    # tests that the code is printed correctly
    response = client.get('/question/2')
    assert response.status_code == 200

def test_question_3(client):
    # tests that the code is printed correctly
    response = client.get('/question/3')
    assert response.status_code == 200

def test_question_4(client):
    # tests that the code is printed correctly
    response = client.get('/question/4')
    assert response.status_code == 200

def test_question_5(client):
    # tests that the code is printed correctly
    response = client.get('/question/5')
    assert response.status_code == 200 

def test_question_6(client):
    # tests that the code is printed correctly
    response = client.get('/question/6')
    assert response.status_code == 200 

def test_question_7(client):
    # tests that the code is printed correctly
    response = client.get('/question/7')
    assert response.status_code == 200 

def test_question_8(client):
    # tests that the code is printed correctly
    response = client.get('/question/8')
    assert response.status_code == 200 

def test_question_9(client):
    # tests that the code is printed correctly
    response = client.get('/question/9')
    assert response.status_code == 200 

def test_question_10(client):
    # tests that the code is printed correctly
    response = client.get('/question/10')
    assert response.status_code == 200 

def test_question_11(client):
    # tests that the code is printed correctly
    response = client.get('/question/11')
    assert response.status_code == 200 

def test_results(client):
    # tests that the code is printed correctly
    response = client.get('/results')
    assert response.status_code == 200