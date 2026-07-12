import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.schemas import NoteCreate
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

def test_search_notes_by_title():
    client.post("/notes/", json={"title": "Test Note", "content": "This is a test note."})
    response = client.get("/notes/search?q=Test")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "Test Note"

def test_search_notes_by_content():
    client.post("/notes/", json={"title": "Test Note", "content": "This is a test note."})
    response = client.get("/notes/search?q=test")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["content"] == "This is a test note."

def test_search_notes_no_results():
    response = client.get("/notes/search?q=NonExistent")
    assert response.status_code == 200
    assert len(response.json()) == 0
