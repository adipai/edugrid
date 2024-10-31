import axios from "axios";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

type CourseData = {
  course_id: string;
  textbook_id: string;
};

const StudentLandingPage = () => {

  const user_id = localStorage.getItem("user_id");
  const [courseData, setCourseData] = useState<CourseData[]>([]);

  const fetchCourcesDetails = async () => {
    try {
      const response = await axios.get(
        `http://localhost:8000/api/v1/student-courses?student_id=${user_id}`
      );
      setCourseData(response.data.courses);
    } catch (error) {
      console.error("Error fetching chapter details:", error);
    }
  };

  useEffect(() => {
    fetchCourcesDetails();
  }, []);

  return (
    <div>
      <h1>Student Dashboard</h1>
      {courseData && courseData.map((course, i) => (
        <div key={i}>{course.course_id} {course.textbook_id}</div>
      ))}
      <ul>
        <li>
          <Link to="/student/view-section">1. View a Section</Link>
        </li>
        <li>
          <Link to="/student/participation">
            2. View Pariticipation Acitivity Point
          </Link>
        </li>
        <li>
          <Link to="/">3. Logout</Link>
        </li>
      </ul>
    </div>
  );
};

export default StudentLandingPage;
