import pytest
from fastapi.testclient import TestClient
from app import app  # Replace 'main' with your actual filename if it's different

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
