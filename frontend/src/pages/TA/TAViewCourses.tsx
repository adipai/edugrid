import axios from "axios";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const TAViewCourses = () => {
  const userId = localStorage.getItem('user_id');
  const [courses, setCourses] = useState([]);
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/view_courses',
          {
            user_id: userId,
            role: "teaching assistant"
          },
          {
            headers: { 'Content-Type': 'application/json' },
            withCredentials: false
          }
        );
        setCourses(response.data.courses);  // Set retrieved courses in state
      } catch (error: any) {
        if (error.response) {
          console.error('Error fetching courses:', error.response.data.message);
          setErrorMessage(error.response.data.detail || "Failed to fetch courses");
        } else {
          console.error('An error occurred:', error.message);
          setErrorMessage("An unexpected error occurred.");
        }
      }
    };

    fetchCourses();
  }, [userId]);

  return (
    <div>
      <h3>Courses Assigned to You</h3>

      {errorMessage && <p style={{ color: "red" }}>{errorMessage}</p>}

      {courses.length > 0 ? (
        <table style={{ borderCollapse: "collapse", width: "100%" }}>
        <thead>
          <tr>
            <th style={{ border: "1px solid black", padding: "8px" }}>Course unique Token</th>
            <th style={{ border: "1px solid black", padding: "8px" }}>Course Name</th>
          </tr>
        </thead>
        <tbody>
          {courses.map((course: any) => (
            <tr key={course.course_id}>
              <td style={{ border: "1px solid black", padding: "8px" }}>{course.course_id}</td>
              <td style={{ border: "1px solid black", padding: "8px" }}>{course.course_name}</td>
            </tr>
          ))}
        </tbody>
      </table>
      ) : (
        <p>No courses assigned.</p>
      )}

      <Link to="/ta/landing">Go Back</Link>
    </div>
  );
};

export default TAViewCourses;
