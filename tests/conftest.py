import pytest
from app import app as flask_app
from python.elastic_manager import ElasticManager
from unittest.mock import patch

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
    with patch('app.ElasticManager') as mock:
        instance = mock.return_value
        instance.retrieve_recipe.return_value = []

        yield mock