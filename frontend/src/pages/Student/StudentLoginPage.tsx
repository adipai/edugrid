import axios from "axios";
import { useState } from "react";
import { Link } from "react-router-dom";

const StudentLoginPage = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const role = "student";

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/login', {
        email,
        password,
        role,
      }, {headers: {
        'Content-Type': 'application/json',
      }, withCredentials: false});
      console.log('Login successful:', response.data);

      const user = response.data.user;
      localStorage.setItem('user_email', user.email);
      localStorage.setItem('user_first_name', user.first_name);
      localStorage.setItem('user_last_name', user.last_name);
      localStorage.setItem('user_role', user.role);
      localStorage.setItem('user_id', user.user_id);
      // Handle success
    } catch (error: any) {
      if (error.response) {
        console.error('Login failed:', error.response.data.message);
      } else {
        console.error('An error occurred:', error.message);
      }
    }
  };

  return (
    <form onSubmit={handleSubmit}>
        <h3>Student Login</h3>
      <div>
        <label htmlFor="email">Email:</label>
        <input
          type="text"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
      </div>

      <div>
        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
      </div>

      <button type="submit">Login</button>
      
      <br />
      <Link to="/">Go Back</Link>
    </form>
  );
};

export default StudentLoginPage;
