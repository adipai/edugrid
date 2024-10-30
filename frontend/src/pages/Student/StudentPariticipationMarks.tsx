import React, { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";

const StudentParticipationMarks: React.FC = () => {
  const navigate = useNavigate();

  const [marks, setMarks] = useState(0);

  useEffect(() => {
    fetch(`http://localhost:8000/student/activity_summary`)
    .then((response) => response.json())
    .then((data) => {
      // Handle the fetched textbook data here
      console.log(data);
      if (data?.textbook) {
        // setMarks(data.textbook);
      } else {
        console.log("Textbook not found");
        throw new Error("Textbook not found");
      }
    })
    .catch((error) => {
      console.error("Error fetching textbook data:", error);
    });
  }, []);

  return (
    <div>
      <p>Participation Marks: {marks}</p>
      <div onClick={() => navigate(-1)}>Go back</div>
    </div>
  );
};

export default StudentParticipationMarks;
