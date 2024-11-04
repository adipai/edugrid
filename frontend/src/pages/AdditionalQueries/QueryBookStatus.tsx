import axios from "axios";
import React, { useEffect, useState } from "react";

type QueryResult = {
  textbook_id: string;
  active_faculty: string;
  evaluation_faculty: string;
};

const QueryBookStatus: React.FC = () => {
  const [queryResult, setQueryResult] = useState<QueryResult[]>([]);

  const fetchData = async () => {
    try {
      const response = await axios.get(
        `http://localhost:8000/books_with_different_status_instructors`
      );
      setQueryResult(response.data.books_with_different_status_instructors);
    } catch (error) {
      console.error("Error fetching chapter details:", error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div>
    {queryResult.length > 0 && <table style={{ border: "1px solid black", borderCollapse: "collapse", width: "100%" }}>
        <thead>
            <tr>
                <th style={{ border: "1px solid black", padding: "8px" }}>Textbook ID</th>
                <th style={{ border: "1px solid black", padding: "8px" }}>Active Faculty</th>
                <th style={{ border: "1px solid black", padding: "8px" }}>Evaluation Faculty</th>
            </tr>
        </thead>
        <tbody>
            {queryResult.map((result, index) => (
                <tr key={index}>
                    <td style={{ border: "1px solid black", padding: "8px" }}>{result.textbook_id}</td>
                    <td style={{ border: "1px solid black", padding: "8px" }}>{result.active_faculty}</td>
                    <td style={{ border: "1px solid black", padding: "8px" }}>{result.evaluation_faculty}</td>
                </tr>
            ))}
        </tbody>
    </table>}
    {queryResult.length == 0 && <p>No data found</p>}
    </div>
  );
};

export default QueryBookStatus;
