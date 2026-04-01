import { Link } from "react-router-dom";

export default function Navbar(){
  return (
    <div className="nav">
      <Link className="link" to="/">Dashboard</Link>
      <Link className="link" to="/students">Students</Link>
      <Link className="link" to="/courses">Courses</Link>
      <Link className="link" to="/attendance">Attendance</Link>
      <Link className="link" to="/marks">Marks</Link>
    </div>
  );
}
