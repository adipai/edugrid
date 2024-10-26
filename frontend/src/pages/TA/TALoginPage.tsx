import axios from "axios";
import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

const TALoginPage = () => {
  const [userId, setUserId] = useState("");
  const [password, setPassword] = useState("");
  const role = "teaching assistant";
  const navigate = useNavigate();

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/login', {
        user_id: userId,
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
      navigate('/ta/landing');
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
        <h3>Teaching Assitant Login</h3>
      <div>
        <label htmlFor="userId">User ID:</label>
        <input
          type="text"
          id="userId"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
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

export default TALoginPage;
