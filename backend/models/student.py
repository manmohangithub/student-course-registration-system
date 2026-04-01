from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True)
    phone = Column(String(20))
    course_id = Column(Integer, ForeignKey("courses.id", ondelete="SET NULL"))
    year = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    course = relationship("Course", back_populates="students")
    attendances = relationship("Attendance", back_populates="student", cascade="all, delete")
    marks = relationship("Mark", back_populates="student", cascade="all, delete")
