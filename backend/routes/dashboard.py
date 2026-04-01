from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import SessionLocal
from models.student import Student
from models.course import Course
from models.attendance import Attendance
from models.mark import Mark

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/stats")
def stats(db: Session = Depends(get_db)):
    total_students = db.query(func.count(Student.id)).scalar() or 0
    total_courses = db.query(func.count(Course.id)).scalar() or 0
    total_attendance = db.query(func.count(Attendance.id)).scalar() or 0

    present_count = db.query(func.count(Attendance.id)).filter(Attendance.status == 'present').scalar() or 0
    attendance_pct = (present_count / total_attendance * 100) if total_attendance else 0

    avg_marks = db.query(func.avg(Mark.marks)).scalar()
    return {
        "total_students": total_students,
        "total_courses": total_courses,
        "attendance_percentage": round(attendance_pct, 2),
        "average_marks": float(avg_marks) if avg_marks is not None else 0.0
    }
