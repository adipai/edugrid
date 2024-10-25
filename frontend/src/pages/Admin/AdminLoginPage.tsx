import axios from "axios";
import { useState } from "react";

const AdminLoginPage = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const role = "admin";

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
      <h3>Admin Login</h3>
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
    </form>
  );
};

export default AdminLoginPage;
