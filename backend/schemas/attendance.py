from pydantic import BaseModel
from datetime import date

class AttendanceCreate(BaseModel):
    student_id: int
    date: date
    status: str  # present/absent

class AttendanceOut(AttendanceCreate):
    id: int

    class Config:
        from_attributes = True
