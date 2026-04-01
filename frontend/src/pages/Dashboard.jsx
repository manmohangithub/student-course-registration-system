import { useEffect, useState } from "react";
import API from "../services/api";

export default function Dashboard(){
  const [stats,setStats]=useState({});
  useEffect(()=>{ API.get("/dashboard/stats").then(r=>setStats(r.data)); },[]);
  return (
    <div className="container">
      <h2>Dashboard</h2>
      <div className="card">Total Students: {stats.total_students}</div>
      <div className="card">Total Courses: {stats.total_courses}</div>
      <div className="card">Attendance %: {stats.attendance_percentage}</div>
      <div className="card">Average Marks: {stats.average_marks}</div>
    </div>
  );
}
