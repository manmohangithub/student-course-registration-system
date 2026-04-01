import { useEffect, useState } from "react";
import API from "../services/api";

export default function Courses(){
  const [list,setList]=useState([]);
  const [name,setName]=useState("");

  const fetch=()=> API.get("/courses").then(r=>setList(r.data));
  useEffect(()=>{fetch();},[]);

  const add=()=> API.post("/courses",{course_name:name}).then(fetch);
  const del=(id)=> API.delete("/courses/"+id).then(fetch);

  return (
    <div className="container">
      <h2>Courses</h2>
      <input className="input" placeholder="Course" onChange={e=>setName(e.target.value)}/>
      <button className="btn" onClick={add}>Add</button>

      <table className="table">
        <thead><tr><th>Course</th><th>Action</th></tr></thead>
        <tbody>
          {list.map(c=>(
            <tr key={c.id}>
              <td>{c.course_name}</td>
              <td><button className="btn" onClick={()=>del(c.id)}>Delete</button></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
