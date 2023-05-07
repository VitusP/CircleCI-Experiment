import pytest
from flask import template_rendered
from controller import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_portfolio(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Vitus Putra" in response.data

def test_settings(client):
    response = client.get('/settings')
    assert response.status_code == 200
