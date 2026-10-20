import sys
import os

# Menambahkan direktori root ke system path agar app bisa diimpor
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_hello_endpoint():
    client = app.test_client()
    response = client.get('/api/hello')
    assert response.status_code == 200
    assert response.json["message"] == "Hello, DevSecOps Pipeline with Python is working!"