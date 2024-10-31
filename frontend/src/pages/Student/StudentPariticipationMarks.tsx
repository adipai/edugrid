import axios from "axios";
import React, { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";

const StudentParticipationMarks: React.FC = () => {
  const navigate = useNavigate();

  const [courseData, setCourseData] = useState<any[]>([]);
  const [marksData, setMarksData] = useState<
    Array<{
      course_id: string;
      total_points: number;
      total_activities_attempted: number;
    }>
  >([]);

  const fetchCourcesDetails = async () => {
    const user_id = localStorage.getItem("user_id");

    try {
      const response = await axios.get(
        `http://localhost:8000/api/v1/student-courses?student_id=${user_id}`
      );
      setCourseData(response.data.courses);
    } catch (error) {
      console.error("Error fetching course details:", error);
    }
  };

  const fetchMarksDetails = async () => {
    if (!courseData) return;
    const user_id = localStorage.getItem("user_id");
    try {
      const response = await axios.post(
        `http://localhost:8000/student/activity_summary` , {
          student_id: user_id,
          course_ids: courseData.map((course) => course.course_id),
        }
      );
      setMarksData(response.data);
    } catch (error) {
      console.error("Error fetching marks details:", error);
    }
  };

  useEffect(() => {
    fetchCourcesDetails();
  }, []);

  useEffect(() => {
    if (!courseData) return;
    fetchMarksDetails();
  }, [courseData]);

  return (
    <div>
      <h1>Student Participation Marks</h1>
      {marksData && marksData.length > 0 ? (
        <table
          style={{ border: "1px solid black", borderCollapse: "collapse" }}
        >
          <thead>
            <tr>
              <th style={{ border: "1px solid black", padding: "8px" }}>
                Course ID
              </th>
              <th style={{ border: "1px solid black", padding: "8px" }}>
                Total Points
              </th>
              <th style={{ border: "1px solid black", padding: "8px" }}>
                Total Activities Attempted
              </th>
            </tr>
          </thead>
          <tbody>
            {marksData.map((mark) => (
              <tr key={mark.course_id}>
                <td style={{ border: "1px solid black", padding: "8px" }}>
                  {mark.course_id}
                </td>
                <td style={{ border: "1px solid black", padding: "8px" }}>
                  {mark.total_points}
                </td>
                <td style={{ border: "1px solid black", padding: "8px" }}>
                  {mark.total_activities_attempted}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No marks data available.</p>
      )}
      <div onClick={() => navigate(-1)}>Go back</div>
    </div>
  );
};

export default StudentParticipationMarks;
