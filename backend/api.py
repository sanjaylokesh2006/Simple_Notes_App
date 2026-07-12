from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import (relationship, Session, declarative_base, sessionmaker)
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .schemas import NoteCreate, NoteUpdate, NoteResponse
from .crud import create_note, get_note, update_note, delete_note
from .dependencies import get_db, get_current_user

router = APIRouter()

@router.post("/notes/", response_model=NoteResponse)
async def create_new_note(note: NoteCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_note(db=db, note=note)

@router.get("/notes/{note_id}", response_model=NoteResponse)
async def read_note(note_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    note = get_note(db=db, note_id=note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.put("/notes/{note_id}", response_model=NoteResponse)
async def update_note(note_id: int, note: NoteUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    updated_note = update_note(db=db, note_id=note_id, note=note)
    if updated_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated_note

@router.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(note_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    deleted_note = delete_note(db=db, note_id=note_id)
    if deleted_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"detail": "Note deleted"}
