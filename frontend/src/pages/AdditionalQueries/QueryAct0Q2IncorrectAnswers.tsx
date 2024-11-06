import axios from "axios";
import React, { useEffect } from "react";

type QueryResult = {
  Incorrect_Answer: string;
  Explanation: string;
};

type ViewQueryShape = {
  option: string;
  explanation: string;
};

const QueryAct0Q2IncorrectAnswers: React.FC = () => {
  const [queryResult, setQueryResult] = React.useState<QueryResult[]>([]);

  const fetchQuery = async () => {
    try {
      const response = await axios.post(
        "http://localhost:8000/incorrect_answers"
      );
      setQueryResult(response.data.incorrect_answers);
    } catch (error) {
      console.error("Error creating block:", error);
    }
  };

  useEffect(() => {
    fetchQuery();
  }, []);

  return (
    <div>
      {queryResult.length > 0 ? (
        <table style={{ borderCollapse: "collapse", width: "100%" }}>
          <thead>
            <tr>
              <th style={{ border: "1px solid black", padding: "8px" }}>
                Incorrect Answer
              </th>
              <th style={{ border: "1px solid black", padding: "8px" }}>
                Explanation
              </th>
            </tr>
          </thead>
          <tbody>
            {queryResult.map((result, index) => (
              <tr key={index}>
                <td style={{ border: "1px solid black", padding: "8px" }}>
                  {result.Incorrect_Answer}
                </td>
                <td style={{ border: "1px solid black", padding: "8px" }}>
                  {result.Explanation}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No results found.</p>
      )}
    </div>
  );
};

export default QueryAct0Q2IncorrectAnswers;
