import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Dashboard from "./pages/Dashboard";
import Students from "./pages/Students";
import Courses from "./pages/Courses";
import Attendance from "./pages/Attendance";
import Marks from "./pages/Marks";

export default function App(){
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Dashboard/>}/>
        <Route path="/students" element={<Students/>}/>
        <Route path="/courses" element={<Courses/>}/>
        <Route path="/attendance" element={<Attendance/>}/>
        <Route path="/marks" element={<Marks/>}/>
      </Routes>
    </BrowserRouter>
  );
}
