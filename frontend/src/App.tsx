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
import FacultyCoursesPage from "./pages/Faculty/FacultyCoursesPage";
import AdminCreateTextbook from "./pages/Admin/AdminCreateTextbook";
import AdminAddNewChapter from "./pages/Admin/AdminAddNewChapter";
import AdminModifyTextbook from "./pages/Admin/AdminModifyTextbook";
import AdminAddNewSection from "./pages/Admin/AdminAddNewSection";
import AdminAddNewContentBlock from "./pages/Admin/AdminAddNewContentBlock";
import AdminModifyChapter from "./pages/Admin/AdminModifyChapter";
import AdminContentAddText from "./pages/Admin/AdminContentAddText";
import AdminContentPicText from "./pages/Admin/AdminContentAddPic";
import AdminActivityAddQuestion from "./pages/Admin/AdminActivityAddQuestion";
import AdminModifySection from "./pages/Admin/AdminModifySection";
import AdminModifyContentBlock from "./pages/Admin/AdminModifyContentBlock";
import FacultyActiveCoursesPage from "./pages/Faculty/FacultyActiveCoursesPage";
import FacultyEvaluationCoursesPage from "./pages/Faculty/FacultyEvaluationCoursesPage";
import AdminContentAddActivity from "./pages/Admin/AdminContentAddActivity";
import FacultyViewWorklistPage from "./pages/Faculty/FacultyViewWorklistPage";
import FacultyViewStudentsPage from "./pages/Faculty/FacultyViewStudentsPage";
import FacultyApproveEnrollmentPage from "./pages/Faculty/FacultyApproveEnrollment";
import FacultyAddNewChapter from "./pages/Faculty/FacultyAddNewChapter";
import FacultyAddNewSection from "./pages/Faculty/FacultyAddNewSection";
import FacultyAddNewContentBlock from "./pages/Faculty/FacultyAddNewContentBlock";
import FacultyContentAddActivity from "./pages/Faculty/FacultyContentAddActivity";
import FacultyContentAddPic from "./pages/Faculty/FacultyContentAddPic";
import FacultyContentAddText from "./pages/Faculty/FacultyContentAddText";
import FacultyActivityAddQuestion from "./pages/Faculty/FacultyActivityAddQuestion";
import FacultyModifyChapter from "./pages/Faculty/FacultyModifyChapter";
import FacultyModifySection from "./pages/Faculty/FacultyModifySection";
import FacultyModifyContentBlock from "./pages/Faculty/FacultyModifyContentBlock";
import FacultyCreateTa from "./pages/Faculty/FacultyAddTa";

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
        <Route path="/admin/create-new-section" element={<AdminAddNewSection />} />
        <Route path="/admin/create-new-block" element={<AdminAddNewContentBlock />} />
        <Route path="/admin/content-add-text" element={<AdminContentAddText />} />
        <Route path="/admin/content-add-pic" element={<AdminContentPicText />} />
        <Route path="/admin/content-add-activity" element={<AdminContentAddActivity />} />
        <Route path="/admin/activity-add-question" element={<AdminActivityAddQuestion />} />
        <Route path="/admin/modify-textbook" element={<AdminModifyTextbook />} />
        <Route path="/admin/modify-chapter" element={<AdminModifyChapter />} />
        <Route path="/admin/modify-section" element={<AdminModifySection />} />
        <Route path="/admin/modify-content" element={<AdminModifyContentBlock />} />

        
        {/* Faculty routes */}
        <Route path="/faculty/login" element={<FacultyLoginPage />} />
        <Route path="/faculty/landing" element={<FacultyLandingPage />} />
        <Route path="/faculty/courses" element={<FacultyCoursesPage />} />
        <Route path="/faculty/active-courses" element={<FacultyActiveCoursesPage />} />
        <Route path="/faculty/evaluation-courses" element={<FacultyEvaluationCoursesPage />} />
        <Route path="/faculty/view-worklist" element={<FacultyViewWorklistPage />} />
        <Route path="/faculty/view-students" element={<FacultyViewStudentsPage />} />
        <Route path="/faculty/approve-enrollment" element={<FacultyApproveEnrollmentPage />} />
        <Route path="/faculty/add-new-chapter" element={<FacultyAddNewChapter />} />
        <Route path="/faculty/create-new-section" element={<FacultyAddNewSection />} />
        <Route path="/faculty/create-new-block" element={<FacultyAddNewContentBlock />} />
        <Route path="/faculty/content-add-activity" element={<FacultyContentAddActivity />} />
        <Route path="/faculty/content-add-pic" element={<FacultyContentAddPic />} />
        <Route path="/faculty/content-add-text" element={<FacultyContentAddText />} />
        <Route path="/faculty/activity-add-question" element={<FacultyActivityAddQuestion />} />
        <Route path="/faculty/modify-chapter" element={<FacultyModifyChapter />} />
        <Route path="/faculty/modify-section" element={<FacultyModifySection />} />
        <Route path="/faculty/modify-content" element={<FacultyModifyContentBlock />} />
        <Route path="/faculty/add-ta" element={<FacultyCreateTa />} />

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
