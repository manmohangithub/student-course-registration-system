from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base

# Import models to register tables
from models import student, course, attendance, mark  # noqa

from routes import students, courses, attendance, marks, dashboard

app = FastAPI(title="Student Management API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables (optional if you run schema.sql manually)
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(students.router, prefix="/students", tags=["Students"])
app.include_router(courses.router, prefix="/courses", tags=["Courses"])
app.include_router(attendance.router, prefix="/attendance", tags=["Attendance"])
app.include_router(marks.router, prefix="/marks", tags=["Marks"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])

@app.get("/")
def root():
    return {"message": "Student Management API Running"}
