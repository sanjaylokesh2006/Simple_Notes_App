from sqlalchemy.orm import (relationship, Session, declarative_base, sessionmaker)
from fastapi import Depends
from sqlalchemy.orm import Session
from .database import get_db

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
