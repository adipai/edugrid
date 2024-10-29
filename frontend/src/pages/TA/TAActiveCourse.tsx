import React, { useEffect, useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";

const TAActiveCourse: React.FC = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const queryParams = new URLSearchParams(location.search);

  const course_id = queryParams.get("course_id"); // Get course ID from query params
  const [courseId, setCourseId] = useState("");
  const [courseDetails, setCourseDetails] = useState<any>(null);

  useEffect(() => {
    if (!course_id) {
      setCourseDetails(null);
      return;
    }
    fetchCourseDetails(course_id);
  }, [course_id]);

  const fetchCourseDetails = async (courseId: string) => {
    try {
      const response = await fetch(
        `http://localhost:8000/api/v1/active-course?course_id=${courseId}`
      );
      const data = await response.json();
      if (data?.course) {
        setCourseDetails(data.course);
      } else {
        alert("Course not found");
      }
    } catch (error) {
      console.error("Error fetching course data:", error);
    }
  };

  const handleSearch = (event: React.FormEvent) => {
    event.preventDefault();
    setCourseId("");
    navigate(`/ta/active-course?course_id=${courseId}`);
  };

  return (
    <div>
      <h1>Go to Active Course</h1>
      {!courseDetails && (
        <form onSubmit={handleSearch}>
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
          <button type="submit">Submit</button>
        </form>
      )}

      {courseDetails && <h2>Course: {courseDetails?.course_name}</h2>}
      <ul>
        {courseDetails && (
          <>
            <li>
              <Link
                to={`/ta/view-students?course_id=${course_id}`}
              >
                1. View Students
              </Link>
            </li>
            <li>
              <Link
                to={`/faculty/add-new-chapter?course_id=${courseDetails.course_id}&tb_id=${courseDetails.textbook_id}`}
              >
                2. Add new chapter
              </Link>
            </li>
            <li>
              <Link
                to={`/faculty/modify-chapter?course_id=${courseDetails.course_id}&tb_id=${courseDetails.textbook_id}`}
              >
                3. Modify chapters
              </Link>
            </li>
          </>
        )}

        <li>
          <div onClick={() => navigate(-1)}>4. Go Back</div>{" "}
        </li>

        <li>
          <Link to={`/ta/landing`}>5. Landing Page</Link>
        </li>
      </ul>
    </div>
  );
};

export default TAActiveCourse;
