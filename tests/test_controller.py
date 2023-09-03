import pytest
import sys
import os

# Get the current directory (where this test file is located)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to sys.path (the src directory)
parent_dir = os.path.join(current_dir, "..")
sys.path.insert(0, parent_dir)

from src.run import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_portfolio(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Vitus Putra" in response.data


def test_settings(client):
    response = client.get("/settings")
    assert response.status_code == 200
