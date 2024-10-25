import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import LoginPage from "./pages/LoginPage";
import SignUpPage from "./pages/SignUpPage";
import LoginHome from "./pages/LoginHome";
import AdminLoginPage from "./pages/Admin/AdminLoginPage";
import FacultyLoginPage from "./pages/Faculty/FacultyLoginPage";
import TALoginPage from "./pages/TA/TALoginPage";
import StudentLoginPage from "./pages/Student/StudentLoginPage";
import AdminLandingPage from "./pages/Admin/AdminLandingPage";
import FacultyLandingPage from "./pages/Faculty/FacultyLandingPage";
import TALandingPage from "./pages/TA/TALandingPage";
import StudentLandingPage from "./pages/Student/StudentLandingPage";
import StudentPreLogin from "./pages/Student/StudentPreLogin";
import AdminCreateFaculty from "./pages/Admin/AdminCreateFaculty";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginHome />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/signup" element={<SignUpPage />} />

        {/* Admin routes */}
        <Route path="/admin/login" element={<AdminLoginPage />} />
        <Route path="/admin/landing" element={<AdminLandingPage />} />
        <Route path="/admin/create-faculty-account" element={<AdminCreateFaculty />} />

        
        {/* Faculty routes */}
        <Route path="/faculty/login" element={<FacultyLoginPage />} />
        <Route path="/faculty/landing" element={<FacultyLandingPage />} />
        
        {/* TA routes */}
        <Route path="/ta/login" element={<TALoginPage />} />
        <Route path="/ta/landing" element={<TALandingPage />} />
        
        {/* Student routes */}
        <Route path="/student/landing" element={<StudentLandingPage />} />
        <Route path="/student/prelogin" element={<StudentPreLogin />} />
        <Route path="/student/login" element={<StudentLoginPage />} />
        
        <Route path="*" element={<div>404 Not Found</div>} />
      </Routes>
    </Router>
  );
}

export default App;
