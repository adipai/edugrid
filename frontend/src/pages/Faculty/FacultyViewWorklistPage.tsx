import axios from "axios";
import { useEffect, useState } from "react";
import { Link, useLocation } from "react-router-dom";

const FacultyViewWorklistPage = () => {
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const courseId =  queryParams.get("course_id");
  const [students, setStudents] = useState([]);
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
    const fetchWorklist = async () => {
      try {
        const response = await axios.post(
          `http://localhost:8000/view_worklist`,
          {
            course_id: courseId
          },
          {
            headers: { 'Content-Type': 'application/json' },
            withCredentials: false
          }
        );
        setStudents(response.data.students);  // Set retrieved courses in state
      } catch (error: any) {
        if (error.response) {
          console.error('Error fetching worklist:', error.response.data.message);
          setErrorMessage(error.response.data.detail || "Failed to fetch worklist");
        } else {
          console.error('An error occurred:', error.message);
          setErrorMessage("An unexpected error occurred.");
        }
      }
    };

    fetchWorklist();
  }, []);

  return (
    <div>
      <h3>Worklist for {courseId} </h3>

      {errorMessage && <p style={{ color: "red" }}>{errorMessage}</p>}

      {students.length > 0 ? (
        <table style={{ borderCollapse: "collapse", width: "100%" }}>
        <thead>
          <tr>
            <th style={{ border: "1px solid black", padding: "8px" }}>Course ID</th>
            <th style={{ border: "1px solid black", padding: "8px" }}>Student ID</th>
            <th style={{ border: "1px solid black", padding: "8px" }}>Status</th>
          </tr>
        </thead>
        <tbody>
          {students.map((student: any) => (
            <tr key={student.course_id}>
              <td style={{ border: "1px solid black", padding: "8px" }}>{student.unique_course_id}</td>
              <td style={{ border: "1px solid black", padding: "8px" }}>{student.student_id}</td>
              <td style={{ border: "1px solid black", padding: "8px" }}>{student.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
      ) : (
        <p>No students in course Waitlist</p>
      )}
      <Link to={`/faculty/active-courses?course_id=${courseId}`}>Go Back</Link>
    </div>
  );
};

export default FacultyViewWorklistPage;
