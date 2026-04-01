from pydantic import BaseModel

class MarkCreate(BaseModel):
    student_id: int
    subject: str
    marks: float

class MarkOut(MarkCreate):
    id: int

    class Config:
        from_attributes = True
