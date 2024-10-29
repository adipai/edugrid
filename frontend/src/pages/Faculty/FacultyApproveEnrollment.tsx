import axios from "axios";
import React, { useState} from "react";
import { useLocation } from "react-router-dom";
import { useNavigate } from "react-router-dom";

const FacultyApproveEnrollmentPage: React.FC = () => {
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const courseId = queryParams.get("course_id") 
  const [studentId, setStudentId] = useState("")
  const navigate = useNavigate();
    const enrollStudent = async () => {
      try {
        await axios.post(
          `http://localhost:8000/enroll_student`,
          {
            course_id: courseId,
            student_id: studentId
          },
          {
            headers: { 'Content-Type': 'application/json' },
            withCredentials: false
          }
        );
        window.alert("Student successfully enrolled")
        navigate(`/faculty/active-courses?course_id=${courseId}`);
      } catch (error: any) {
        if (error.response) {
          console.error('Error enrolling student:', error.response.data.message);
        } else {
          console.error('An error occurred:', error.message);
        }
      }
    };

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    // Handle form submission logic here
    enrollStudent();

  };

  return (
    <div>
      <h1>Approve Enrollment</h1>
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="studentId">Student ID</label>
            <input
              type="text"
              id="studentId"
              value={studentId}
              onChange={(e) => setStudentId(e.target.value)}
              required
            />
          </div>
          <button type="submit">
            Save
          </button>
        </form>
      <ul>
        <li>
        <div onClick={() => navigate(-1)}>Cancel</div>
        </li>
      </ul>
    </div>
  );
};

export default FacultyApproveEnrollmentPage;
