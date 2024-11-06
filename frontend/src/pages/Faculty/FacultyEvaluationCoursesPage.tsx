import axios from "axios";
import React, { useEffect, useState } from "react";
import { Link, useLocation } from "react-router-dom";
import { useNavigate } from "react-router-dom";

const FacultyEvaluationCoursesPage: React.FC = () => {
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const course_id = queryParams.get("course_id"); // Get course ID from query params
  const [courseId, setCourseId] = useState("");
  const [courseDetails, setCourseDetails] = useState<any>(null);
  const navigate = useNavigate();
  const userId = localStorage.getItem("user_id");

  useEffect(() => {
    if (!course_id) {
      setCourseDetails(null);
      return;
    }
    fetchCourseDetails(course_id);
  }, [course_id]);

// modify_block

  const fetchCourseDetails = async (courseId: string) => {
    try {
      const currentDate: string = new Date().toISOString().split("T")[0];
      const body = {
        input_course_id: courseId,
        current_date: currentDate,
        user_modifying: userId,
      };
      const permission = await axios.post(
        "http://localhost:8000/check_course_details",
        body,
        {
          headers: {
            "Content-Type": "application/json",
          },
          withCredentials: false,
        }
      );
      const response = await fetch(
        `http://localhost:8000/api/v1/evaluation-course?course_id=${course_id}`
      );
      const data = await response.json();
      if (data?.course) {
        setCourseDetails(data.course);
      } else {
        console.log("Course not found");
        throw new Error("Course not found");
      }
    } catch (error: any) {
      if (error?.response?.status === 403) {
        window.alert(
          `You do not have permission to modify this course: ${error.response.data.detail}`
        );
      } else if (error?.response?.status === 500) {
        window.alert(error.response.data.detail);
      }
      console.error("Error fetching course data:", error);
      // window.alert("Error fetching course data");
      navigate(-1);
    }
  };

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    // Handle form submission logic here
    setCourseId("");
    navigate("/faculty/evaluation-courses?course_id=" + courseId);
  };

  return (
    <div>
      <h1>Go to Evaluation Course</h1>
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
          <button type="submit">Submit</button>
        </form>
      )}

      {courseDetails && <h2>Course: {courseDetails?.course_name}</h2>}
      <ul>
        {courseDetails && (
          <>
            <li>
              <Link
                to={`/faculty/add-new-chapter?course_id=${courseDetails.course_id}&tb_id=${courseDetails.textbook_id}`}
              >
                1. Add new chapter
              </Link>
            </li>
            <li>
              <Link
                to={`/faculty/modify-chapter?course_id=${courseDetails.course_id}&tb_id=${courseDetails.textbook_id}`}
              >
                2. Modify chapters
              </Link>
            </li>
            <li>
              <Link
                to={`/faculty/evaluation-courses`}
                onClick={() => {
                  setCourseDetails("");
                  setCourseId("");
                }}
              >
                3. Go Back
              </Link>
            </li>
          </>
        )}

        {!courseDetails && (
          <li>
            <Link to={`/faculty/landing`}>3. Go Back</Link>{" "}
          </li>
        )}
        <li>
          <Link to={`/faculty/landing`}>4. Landing Page</Link>
        </li>
      </ul>
    </div>
  );
};

export default FacultyEvaluationCoursesPage;
