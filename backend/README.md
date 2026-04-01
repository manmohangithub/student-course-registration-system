# Student Management System (FastAPI + MySQL)

## Overview
Advanced backend for managing Students, Courses, Attendance, and Marks with dashboard analytics.
No authentication (JWT) included.

## Tech Stack
- FastAPI
- SQLAlchemy (ORM)
- MySQL (PyMySQL)
- Pydantic

## Features
- Full CRUD for Students and Courses
- Attendance marking and retrieval
- Marks management and average calculation
- Dashboard statistics (totals, averages)
- Search, filter, pagination (students)

## Setup
1. Create DB:
   CREATE DATABASE student_course_db;

2. Create .env from .env.example and update password.

3. Install deps:
   pip install -r requirements.txt

4. Run:
   uvicorn main:app --reload

## Docs
- Swagger: http://localhost:8000/docs

## Project Structure
backend/
├── main.py
├── database.py
├── config.py
├── models/
├── schemas/
├── routes/
├── schema.sql
├── requirements.txt
├── .env.example
