import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home page listing"""
    rv = client.get('/')
    assert b"Laptop" in rv.data

def test_add_item(client):
    """Test adding a new item"""
    rv = client.post('/add', data={'item': 'Monitor'}, follow_redirects=True)
    assert b"Monitor" in rv.data
    assert rv.status_code == 200

def test_remove_item(client):
    """Test removing an item"""
    # Add a UNIQUE item that isn't in the default list
    client.post('/add', data={'item': 'Webcam'}, follow_redirects=True)
    
    # Remove that unique item
    rv = client.get('/remove/Webcam', follow_redirects=True)
    
    # Verify 'Webcam' is no longer in the HTML
    assert b"Webcam" not in rv.data
    assert rv.status_code == 200