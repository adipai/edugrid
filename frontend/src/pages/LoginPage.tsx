import axios from "axios";
import { useState } from "react";

const LoginPage = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("user");

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/login', {
        email,
        password,
        role,
      }, {headers: {
        'Content-Type': 'application/json',
      }, withCredentials: false});
      console.log('Login successful:', response.data);
      window.alert('Login successful');
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

      <div>
        <label htmlFor="role">Role:</label>
        <select
          id="role"
          value={role}
          onChange={(e) => setRole(e.target.value)}
        >
          <option value="admin">Admin</option>
          <option value="faculty">Faculty</option>
          <option value="teaching assistant">Teaching Assistant</option>
          <option value="user">User</option>
        </select>
      </div>

      <button type="submit">Login</button>
    </form>
  );
};

export default LoginPage;
