

def test_hello(client):
    response = client.get('/')
    assert response.status_code==200
