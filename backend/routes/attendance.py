from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal
from models.attendance import Attendance
from schemas.attendance import AttendanceCreate, AttendanceOut

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AttendanceOut)
def mark_attendance(payload: AttendanceCreate, db: Session = Depends(get_db)):
    obj = Attendance(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/student/{student_id}", response_model=List[AttendanceOut])
def get_attendance(student_id: int, db: Session = Depends(get_db)):
    return db.query(Attendance).filter(Attendance.student_id == student_id).all()
