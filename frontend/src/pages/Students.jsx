import { useEffect, useState } from "react";
import API from "../services/api";

export default function Students(){
  const [list,setList]=useState([]);
  const [name,setName]=useState("");
  const [search,setSearch]=useState("");

  const fetch=()=> API.get("/students",{params:{search}}).then(r=>setList(r.data));
  useEffect(()=>{fetch();},[]);

  const add=()=> API.post("/students",{name}).then(fetch);
  const del=(id)=> API.delete("/students/"+id).then(fetch);

  return (
    <div className="container">
      <h2>Students</h2>
      <input className="input" placeholder="Search" onChange={e=>setSearch(e.target.value)}/>
      <button className="btn" onClick={fetch}>Search</button>
      <br/>
      <input className="input" placeholder="Name" onChange={e=>setName(e.target.value)}/>
      <button className="btn" onClick={add}>Add</button>

      <table className="table">
        <thead><tr><th>Name</th><th>Action</th></tr></thead>
        <tbody>
          {list.map(s=>(
            <tr key={s.id}>
              <td>{s.name}</td>
              <td><button className="btn" onClick={()=>del(s.id)}>Delete</button></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
