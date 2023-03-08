from unittest.mock import patch
import pytest
from src.app import app as flask_app

@pytest.fixture
def app():
    """Return the Flask app fixture"""
    flask_app.config.update({
        'TESTING': True
    })

    yield flask_app

@pytest.fixture
def client(app):
    """Fixture for the client"""
    return app.test_client()

@pytest.fixture
def elastic_manager_mock():
    """Mocks the ElasticManager class"""
    with patch('src.app.ElasticManager') as mock:
        instance = mock.return_value
        instance.retrieve_recipe.return_value = []

        yield mock
