import { useState } from "react";
import API from "../services/api";

export default function Marks(){
  const [studentId,setStudentId]=useState("");
  const [marks,setMarks]=useState([]);

  const fetch=()=> API.get("/marks/student/"+studentId).then(r=>setMarks(r.data));
  const add=()=> API.post("/marks",{student_id:studentId,subject:"Math",marks:90}).then(fetch);

  return (
    <div className="container">
      <h2>Marks</h2>
      <input className="input" placeholder="Student ID" onChange={e=>setStudentId(e.target.value)}/>
      <button className="btn" onClick={fetch}>View</button>
      <button className="btn" onClick={add}>Add Sample</button>

      <ul>
        {marks.map(m=><li key={m.id}>{m.subject} - {m.marks}</li>)}
      </ul>
    </div>
  );
}
