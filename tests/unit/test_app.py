def test_ping(client):
    """Test the ping method"""
    response = client.get('/ping')

    assert response.status_code == 200
    assert response.data == b'pong'

def test_home(client):
    """Test that home page loads"""
    response = client.get('/')

    assert response.status_code == 200

def test_generate_recipes(client, elastic_manager_mock):  # pylint: disable=unused-argument
    """Test that generate recipes endpoint loads"""
    response = client.post('/generate_recipes', data={
        'ingredients': '',
        'dietary_restrictions': '',
        'liked_foods': '',
        'time_to_cook': 60,
    })

    assert response.status_code == 200
