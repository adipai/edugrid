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
import AdminCreateEvaluationCourse from "./pages/Admin/AdminCreateEvaluationCourse";
import AdminCreateActiveCourse from "./pages/Admin/AdminCreateActiveCourse";
import ChangePasswordPage from "./pages/ChangePasswordPage";

import AdminCreateTextbook from "./pages/Admin/AdminCreateTextbook";
import AdminAddNewChapter from "./pages/Admin/AdminAddNewChapter";
import AdminModifyTextbook from "./pages/Admin/AdminModifyTextbook";
import AdminAddNewSection from "./pages/Admin/AdminAddNewSection";

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
        <Route path="/admin/create-evaluation-course" element={<AdminCreateEvaluationCourse />} />
        <Route path="/admin/create-active-course" element={<AdminCreateActiveCourse />} />
        <Route path="/admin/create-textbook" element={<AdminCreateTextbook />} />
        <Route path="/admin/create-new-chapter" element={<AdminAddNewChapter />} />
        <Route path="/admin/modify-textbook" element={<AdminModifyTextbook />} />
        <Route path="/admin/create-new-section" element={<AdminAddNewSection />} />

        
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
        
        <Route path="/change-password-page" element={<ChangePasswordPage />} />
        <Route path="*" element={<div>404 Not Found</div>} />
      </Routes>
    </Router>
  );
}

export default App;
