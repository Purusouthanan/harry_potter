from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_harry_route():
    response = client.get('/harry')
    assert response.status_code == 200
    assert response.json() == {
        'name': 'harry potter',
        'house': 'gryffindor',
    }
