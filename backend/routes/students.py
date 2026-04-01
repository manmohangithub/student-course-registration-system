from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from database import SessionLocal
from models.student import Student
from schemas.student import StudentCreate, StudentUpdate, StudentOut

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=StudentOut)
def create_student(payload: StudentCreate, db: Session = Depends(get_db)):
    obj = Student(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/", response_model=List[StudentOut])
def list_students(
    db: Session = Depends(get_db),
    search: Optional[str] = Query(None),
    skip: int = 0,
    limit: int = 10
):
    q = db.query(Student)
    if search:
        q = q.filter(Student.name.like(f"%{search}%"))
    return q.offset(skip).limit(limit).all()

@router.get("/{student_id}", response_model=StudentOut)
def get_student(student_id: int, db: Session = Depends(get_db)):
    obj = db.query(Student).filter(Student.id == student_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Student not found")
    return obj

@router.put("/{student_id}", response_model=StudentOut)
def update_student(student_id: int, payload: StudentUpdate, db: Session = Depends(get_db)):
    obj = db.query(Student).filter(Student.id == student_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Student not found")
    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return obj

@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    obj = db.query(Student).filter(Student.id == student_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(obj)
    db.commit()
    return {"message": "Deleted"}
