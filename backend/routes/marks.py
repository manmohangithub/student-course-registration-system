from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy import func

from database import SessionLocal
from models.mark import Mark
from schemas.mark import MarkCreate, MarkOut

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=MarkOut)
def add_mark(payload: MarkCreate, db: Session = Depends(get_db)):
    obj = Mark(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/student/{student_id}", response_model=List[MarkOut])
def get_marks(student_id: int, db: Session = Depends(get_db)):
    return db.query(Mark).filter(Mark.student_id == student_id).all()

@router.get("/average/{student_id}")
def average_marks(student_id: int, db: Session = Depends(get_db)):
    avg = db.query(func.avg(Mark.marks)).filter(Mark.student_id == student_id).scalar()
    return {"student_id": student_id, "average": float(avg) if avg is not None else 0.0}
