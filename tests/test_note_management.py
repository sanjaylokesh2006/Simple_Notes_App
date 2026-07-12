import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.schemas import NoteCreate, NoteUpdate
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

def test_create_note():
    response = client.post("/notes/", json={"title": "Test Note", "content": "This is a test note."})
    assert response.status_code == 201
    assert response.json()["title"] == "Test Note"
    assert response.json()["content"] == "This is a test note."

def test_read_note():
    response = client.post("/notes/", json={"title": "Test Note", "content": "This is a test note."})
    note_id = response.json()["id"]
    response = client.get(f"/notes/{note_id}")
    assert response.status_code == 200
    assert response.json()["id"] == note_id
    assert response.json()["title"] == "Test Note"
    assert response.json()["content"] == "This is a test note."

def test_update_note():
    response = client.post("/notes/", json={"title": "Test Note", "content": "This is a test note."})
    note_id = response.json()["id"]
    update_data = NoteUpdate(title="Updated Title", content="Updated Content")
    response = client.put(f"/notes/{note_id}", json=update_data.dict())
    assert response.status_code == 200
    assert response.json()["id"] == note_id
    assert response.json()["title"] == "Updated Title"
    assert response.json()["content"] == "Updated Content"

def test_delete_note():
    response = client.post("/notes/", json={"title": "Test Note", "content": "This is a test note."})
    note_id = response.json()["id"]
    response = client.delete(f"/notes/{note_id}")
    assert response.status_code == 204

def test_invalid_input_create_note():
    response = client.post("/notes/", json={"title": "", "content": ""})
    assert response.status_code == 422
