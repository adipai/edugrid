import axios from "axios";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const StudentEnrollPage: React.FC = () => {
  const navigate = useNavigate();

  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [courseToken, setCourseToken] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    // Handle form submission logic here
    try {
      const response = await axios.post(
        "http://localhost:8000/enroll_student_in_course",
        {
          first_name: firstName,
          last_name: lastName,
          email,
          course_token: courseToken,
          password,
        }
      );
      if (response.status === 200) {
          window.alert(response.data.message);
          navigate(-1);
      }else{
        throw new Error("Error enrolling student in course");
      }
      // Redirect to the appropriate page based on the block type
    } catch (error) {
      console.error("Error enrolling student:", error);
    }
  };

  return (
    <div>
      <h1>Student Enrollment</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>First Name:</label>
          <input
            type="text"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Last Name:</label>
          <input
            type="text"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Course Token:</label>
          <input
            type="text"
            value={courseToken}
            onChange={(e) => setCourseToken(e.target.value)}
            required
          />
        </div>
        <button type="submit">Enroll</button>
      </form>
    </div>
  );
};

export default StudentEnrollPage;
