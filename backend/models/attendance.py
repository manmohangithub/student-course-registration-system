from sqlalchemy import Column, Integer, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    date = Column(Date, nullable=False)
    status = Column(Enum('present','absent'), nullable=False)

    student = relationship("Student", back_populates="attendances")
