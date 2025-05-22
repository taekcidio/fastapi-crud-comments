from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/comments", response_model=schemas.CommentOut)
def create_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    return crud.create_comment(db, comment)

@router.get("/comments/{comment_id}", response_model=schemas.CommentOut)
def read_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = crud.get_comment(db, comment_id)
    if not db_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

@router.get("/comments", response_model=list[schemas.CommentOut])
def list_comments(db: Session = Depends(get_db)):
    return crud.get_all_comments(db)

@router.get("/comments/stats")
def comment_stats(db: Session = Depends(get_db)):
    return crud.get_stats(db)
