from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)

# generate once, reuse across tests
TEST_USERNAME = f"testuser_{uuid.uuid4().hex[:6]}"
TEST_EMAIL = f"{TEST_USERNAME}@email.com"
TEST_PASSWORD = "testpass"

def test_register():
    response = client.post("/users/register", json={
        "username": TEST_USERNAME,
        "email": TEST_EMAIL,
        "password": TEST_PASSWORD
    })
    assert response.status_code == 200

def test_login():
    response = client.post("/users/login", data={
        "username": TEST_USERNAME,
        "password": TEST_PASSWORD
    })
    assert "access_token" in response.json()


def test_get_jobs():
    response = client.get("/jobs/") 
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_save_favorite():
    login = client.post("/users/login", data={
    "username": TEST_USERNAME,
    "password": TEST_PASSWORD
     })
    token = login.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}

    response = client.post("/favorites", json={"job_id": "123", "job_title": "Backend Dev",
                                               "company": "Test_corp"}, headers=headers)
    assert response.status_code == 200
