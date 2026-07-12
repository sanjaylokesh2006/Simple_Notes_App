import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.schemas import UserCreate
from app.database import get_db, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

client = TestClient(app)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(autouse=True)
def clean_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def test_create_user():
    user_data = UserCreate(username="testuser", email="test@example.com", password="password123")
    response = client.post("/users/", json=user_data.dict())
    assert response.status_code == 201
    assert response.json()["username"] == "testuser"
    assert response.json()["email"] == "test@example.com"

def test_login_user():
    user_data = UserCreate(username="testuser", email="test@example.com", password="password123")
    client.post("/users/", json=user_data.dict())
    login_data = {"username": "testuser", "password": "password123"}
    response = client.post("/token", data=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_invalid_login():
    user_data = UserCreate(username="testuser", email="test@example.com", password="password123")
    client.post("/users/", json=user_data.dict())
    login_data = {"username": "testuser", "password": "wrongpassword"}
    response = client.post("/token", data=login_data)
    assert response.status_code == 401
