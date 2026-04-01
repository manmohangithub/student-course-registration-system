from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal
from models.course import Course
from schemas.course import CourseCreate, CourseUpdate, CourseOut

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CourseOut)
def create_course(payload: CourseCreate, db: Session = Depends(get_db)):
    obj = Course(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/", response_model=List[CourseOut])
def list_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()

@router.get("/{course_id}", response_model=CourseOut)
def get_course(course_id: int, db: Session = Depends(get_db)):
    obj = db.query(Course).filter(Course.id == course_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    return obj

@router.put("/{course_id}", response_model=CourseOut)
def update_course(course_id: int, payload: CourseUpdate, db: Session = Depends(get_db)):
    obj = db.query(Course).filter(Course.id == course_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return obj

@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    obj = db.query(Course).filter(Course.id == course_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Course not found")
    db.delete(obj)
    db.commit()
    return {"message": "Deleted"}
