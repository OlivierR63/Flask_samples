import pytest
from lab.server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello World\n'

def test_no_content_route(client):
    response = client.get('/no_content')
    assert response.status_code == 204

def test_get_data_route(client):
    response = client.get('/data')
    assert response.status_code == 200
    assert b'Data of length' in response.data

def test_name_search_route(client):
    response = client.get('/name_search?q=Tanya')
    assert response.status_code == 200
    assert b'Tanya' in response.data

    response = client.get('/name_search?q=')
    assert response.status_code == 400

def test_count_route(client):
    response = client.get('/count')
    assert response.status_code == 200
    assert b'data count' in response.data

def test_find_by_uuid_route(client):
    response = client.get('/person/3b58aade-8415-49dd-88db-8d7bce14932a')
    assert response.status_code == 200
    assert b'Tanya' in response.data

def test_delete_by_uuid_route(client):
    response = client.delete('/person/3b58aade-8415-49dd-88db-8d7bce14932a')
    assert response.status_code == 200
    assert b'Person with ID' in response.data

def test_add_by_uuid_route(client):
    new_person = {
        "id": "new-id",
        "first_name": "New",
        "last_name": "Person",
        "graduation_year": 2023,
        "address": "123 New Address",
        "city": "New City",
        "zip": "12345",
        "country": "New Country",
        "avatar": "http://dummyimage.com/100x100.png/000/fff"
    }
    response = client.post('/person', json=new_person)
    assert response.status_code == 200
    assert b'New person new-id created successfully' in response.data