import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_get(client):
    """Test GET request to index"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'שלום' in response.data


def test_index_post(client):
    """Test POST request with form data"""
    response = client.post('/', data={'name': 'TestUser'})
    assert response.status_code == 200
    assert b'TestUser' in response.data


def test_ai_endpoint(client):
    """Test AI endpoint returns JSON"""
    response = client.get('/AI')
    assert response.status_code == 200
    assert response.json == {"message": "Activate AI for next buy"}


def test_ai_endpoint_content_type(client):
    """Test AI endpoint returns JSON content type"""
    response = client.get('/AI')
    assert response.content_type == 'application/json'
