import axios from "axios";
import React, { useEffect, useState} from "react";
import { Link, useLocation } from "react-router-dom";
import { useNavigate } from "react-router-dom";

const FacultyActiveCoursesPage: React.FC = () => {
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const course_id = queryParams.get("course_id"); // Get course ID from query params
  const [courseId, setCourseId] = useState("");
  const [courseDetails, setCourseDetails] = useState<any>(null);
  const navigate = useNavigate();
  const userId = localStorage.getItem('user_id')

useEffect(() => {
  if (!course_id) {
    setCourseDetails(null)
    return;
  }
  fetchCourseDetails(course_id);
}, [course_id]);

  const fetchCourseDetails = async (courseId: string) => {
    try {
      const currentDate: string = new Date().toISOString().split('T')[0];
      const body = {
        input_course_id: courseId,
        current_date: currentDate,
        user_modifying: userId,
      };
    const permission = await axios.post('http://localhost:8000/check_course_details', 
        body, 
        {headers: {
      'Content-Type': 'application/json',
    }, withCredentials: false});
    const permissions = permission.data
    console.log(permissions.message)
    if (permissions.message === 'Modification allowed'){
      const response = await fetch(`http://localhost:8000/api/v1/active-course?course_id=${course_id}`);
      const data = await response.json();
      if (data?.course) {
        setCourseDetails(data.course);
      } else {
        console.log("Course not found");
        throw new Error("Course not found");
      }
    }
  else{
    window.alert(`You do not have permission to modify this course: ${permissions.message}`)
    throw new Error(`You do not have permission to modify this course: ${permissions.message}`);
  }} catch (error) {
      console.error("Error fetching course data:", error);
      window.alert(error);
      navigate(-1)
    }
  };

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    // Handle form submission logic here
    setCourseId("");
    navigate("/faculty/active-courses?course_id=" + courseId);
  };

  return (
    <div>
      <h1>Go to Active Course</h1>
      {!courseDetails && (
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="courseId">Course ID</label>
            <input
              type="text"
              id="courseId"
              value={courseId}
              onChange={(e) => setCourseId(e.target.value)}
              required
            />
          </div>
          <button type="submit">
            Submit
          </button>
        </form>
      )}

      {courseDetails && <h2>Course: {courseDetails?.course_name}</h2>}
      <ul>
        {courseDetails && (
          <>
            <li>
              <Link
                to={`/faculty/view-worklist?course_id=${courseDetails.course_id}`}
              >
                1. View Worklist
              </Link>
            </li>
            <li>
              <Link
                to={`/faculty/approve-enrollment?course_id=${courseDetails.course_id}`}
              >
                2. Approve Enrollment
              </Link>
            </li>
            <li>
              <Link
                to={`/faculty/view-students?course_id=${courseDetails.course_id}`}
              >
                3. View Students
              </Link>
            </li>
            <li>
              <Link
                to={`/faculty/add-new-chapter?course_id=${courseDetails.course_id}&tb_id=${courseDetails.textbook_id}`}
              >
                4. Add new chapter
              </Link>
            </li>
            <li>
              <Link
                to={`/faculty/modify-chapter?course_id=${courseDetails.course_id}&tb_id=${courseDetails.textbook_id}`}
              >
                5. Modify chapters
              </Link>
            </li>
            <li>
              <Link
                to={`/faculty/add-ta?course_id=${courseDetails.course_id}`}
              >
                6. Add TA
              </Link>
            </li>
            <li>
              <Link
                to={`/faculty/active-courses`}
                onClick={() => {
                  setCourseDetails('');
                  setCourseId('');
                }}
              >
                7. Go Back
              </Link>
            </li>
          </>
        )}

        {!courseDetails && (
          <li>
            <Link to={`/faculty/landing`}>7. Go Back</Link>{" "}
          </li>
        )}
        <li>
          <Link to={`/faculty/landing`}>8. Landing Page</Link>
        </li>
      </ul>
    </div>
  );
};

export default FacultyActiveCoursesPage;
