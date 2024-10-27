import React, { useEffect, useState} from "react";
import { Link } from "react-router-dom";
// import { useNavigate } from "react-router-dom";

const FacultyActiveCoursesPage: React.FC = () => {
  const [searchCourseId, setSearchCourseId] = useState("");
  const [courseId, setCourseId] = useState("");
  const [courseDetails, setCourseDetails] = useState<any>(null);
//   const navigate = useNavigate();

  useEffect(() => {
    // Fetch textbook data here
    if (!searchCourseId) {
      return;
    }
    console.log(`http://localhost:8000/api/v1/active-course?course_id=${searchCourseId}`);
    fetch(`http://localhost:8000/api/v1/active-course?course_id=${searchCourseId}`)
      .then((response) => response.json())
      .then((data) => {
        // Handle the fetched textbook data here
        console.log(data);
        if (data?.course) {
          setCourseDetails(data.course);
        } else {
          window.alert("Course not found");
        }
      })
      .catch((error) => {
        console.error("Error fetching course data:", error);
      });
  }, [searchCourseId]);

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    // Handle form submission logic here
    console.log("Submitted course ID:", courseId);
  };

  const handleSearch = (event: React.FormEvent) => {
    event.preventDefault();
    setSearchCourseId(courseId);
    setCourseId("");
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
          <button type="submit" onClick={(e) => handleSearch(e)}>
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
                to={`/faculty/modify-chapters?course_id=${courseDetails.course_id}&tb_id=${courseDetails.textbook_id}`}
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
                  setSearchCourseId('');
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
