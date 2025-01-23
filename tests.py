import pytest
from fastapi.testclient import TestClient
<<<<<<< HEAD
from app import app
=======
from app import app 
>>>>>>> 21c1e3082011a24f027e34cd75f94b932eb53f1f

client = TestClient(app)

def test_home_endpoint():
    """Test the home endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Spam detection API"}

def test_predict_endpoint():
    """Test the predict endpoint with a sample input"""
    sample_data = {"message": "This is a spam message"}
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 200
    assert "prediction" in response.json()
