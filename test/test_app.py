from app import app

def test_hello_endpoint():
    client = app.test_client()
    response = client.get('/api/hello')
    assert response.status_code == 200
    assert response.json["message"] == "Hello, DevSecOps Pipeline with Python is working!"