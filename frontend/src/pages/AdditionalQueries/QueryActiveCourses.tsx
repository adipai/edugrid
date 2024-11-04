import axios from "axios";
import React, { useEffect, useState } from "react";

type QueryResult = {
  course_id: string;
  faculty_name: string;
  total_students: number;
};

const QueryActiveCourses: React.FC = () => {
  const [queryResult, setQueryResult] = useState<QueryResult[]>([]);

  const fetchData = async () => {
    try {
      const response = await axios.get(
        `http://localhost:8000/active_courses_with_students`
      );
      setQueryResult(response.data.active_courses);
    } catch (error) {
      console.error("Error fetching chapter details:", error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div>
      <table style={{ borderCollapse: "collapse", width: "100%" }}>
        <thead>
          <tr>
            <th style={{ border: "1px solid black", padding: "8px" }}>
              Course ID
            </th>
            <th style={{ border: "1px solid black", padding: "8px" }}>
              Faculty Name
            </th>
            <th style={{ border: "1px solid black", padding: "8px" }}>
              Total Students
            </th>
          </tr>
        </thead>
        <tbody>
          {queryResult.map((result) => (
            <tr key={result.course_id}>
              <td style={{ border: "1px solid black", padding: "8px" }}>
                {result.course_id}
              </td>
              <td style={{ border: "1px solid black", padding: "8px" }}>
                {result.faculty_name}
              </td>
              <td style={{ border: "1px solid black", padding: "8px" }}>
                {result.total_students}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default QueryActiveCourses;
