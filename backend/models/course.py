from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String(100), nullable=False)
    duration = Column(String(50))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    students = relationship("Student", back_populates="course")
