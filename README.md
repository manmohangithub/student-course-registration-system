# 🎓 Student Management System

## 🚀 Overview

A full-stack **Student Management System** built using **React, FastAPI, and MySQL** to manage students, courses, attendance, and academic performance efficiently.

This project demonstrates real-world full-stack development with clean architecture, REST APIs, and interactive UI.

---

## ✨ Features

### 📊 Dashboard

* View total students, courses
* Attendance percentage
* Average marks analytics

### 👨‍🎓 Student Management

* Add, update, delete students
* Search and filter students
* Pagination support

### 📘 Course Management

* Create and manage courses
* Assign students to courses

### 📅 Attendance System

* Mark daily attendance
* View attendance records per student

### 📝 Marks Management

* Add subject-wise marks
* Calculate average marks

---

## 🛠️ Tech Stack

### 🔹 Frontend

* React.js (Vite)
* Axios
* React Router
* CSS (Custom Styling)

### 🔹 Backend

* FastAPI (Python)
* SQLAlchemy (ORM)
* Pydantic (Validation)

### 🔹 Database

* MySQL

---

## 📁 Project Structure

```
student-management-system/
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   └── styles/
├── backend/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── main.py
│   └── database.py
```

---

## ⚙️ Installation & Setup

### 🔹 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/student-management-system.git
cd student-management-system
```

---

### 🔹 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv .venv
.\.venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn main:app --reload
```

👉 Backend runs at:
http://localhost:8000
👉 API Docs:
http://localhost:8000/docs

---

### 🔹 3. Database Setup

Open MySQL and run:

```sql
CREATE DATABASE student_course_db;
```

Then execute:

```sql
schema.sql
```

Update `.env` file:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=student_course_db
```

---

### 🔹 4. Frontend Setup

```bash
cd frontend

npm install
npm run dev
```

👉 Frontend runs at:
http://localhost:5173

---

## 🔗 API Endpoints

### Students

* `GET /students`
* `POST /students`
* `PUT /students/{id}`
* `DELETE /students/{id}`

### Courses

* `GET /courses`
* `POST /courses`

### Attendance

* `POST /attendance`
* `GET /attendance/student/{id}`

### Marks

* `POST /marks`
* `GET /marks/student/{id}`

### Dashboard

* `GET /dashboard/stats`

---

## 💡 Key Highlights

* Full-stack architecture
* REST API design
* Modular backend structure
* Real-world database relationships
* Scalable and maintainable code

---

## 👨‍💻 Author

**Medapati Manmohan Reddy**
📍 Hyderabad, India
🔗 GitHub: https://github.com/manmohangithub
🔗 LinkedIn: https://www.linkedin.com/in/manmohangreddy1111

---

⭐ If you like this project, give it a star!
