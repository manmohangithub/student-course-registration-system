import { useState } from "react";
import API from "../services/api";

export default function Attendance(){
  const [studentId,setStudentId]=useState("");
  const [data,setData]=useState([]);

  const fetch=()=> API.get("/attendance/student/"+studentId).then(r=>setData(r.data));
  const mark=()=> API.post("/attendance",{student_id:studentId,date:new Date().toISOString().slice(0,10),status:"present"}).then(fetch);

  return (
    <div className="container">
      <h2>Attendance</h2>
      <input className="input" placeholder="Student ID" onChange={e=>setStudentId(e.target.value)}/>
      <button className="btn" onClick={fetch}>View</button>
      <button className="btn" onClick={mark}>Mark Present</button>

      <ul>
        {data.map(a=><li key={a.id}>{a.date} - {a.status}</li>)}
      </ul>
    </div>
  );
}
