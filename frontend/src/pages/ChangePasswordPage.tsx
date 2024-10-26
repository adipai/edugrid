import axios from "axios";
import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

const ChangePasswordPage = () => {
  const [oldPassword, setOldPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const navigate = useNavigate();
  const userId =  localStorage.getItem('user_id');
  const handleSubmit = async (e: any) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/change_password', {
        user_id: userId,
        old_password: oldPassword,
        new_password: newPassword
      }, {headers: {
        'Content-Type': 'application/json',
      }, withCredentials: false});
      console.log('Login successful:', response.data);
      // Handle success
      window.alert("Password changed successfully!");
      navigate(-1);
    } catch (error: any) {
      if (error.response) {
        console.error('Login failed:', error.response.data.message);
      } else {
        console.error('An error occurred:', error.message);
      }
      window.alert("Attempt unsuccessful, please make sure you enter your correct password. New password must not be the same as old password");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
        <h3>Change Password</h3>
      <div>
        <label htmlFor="oldPassword">Old Password:</label>
        <input
          type="password"
          id="oldPassword"
          value={oldPassword}
          onChange={(e) => setOldPassword(e.target.value)}
          required
        />
      </div>

      <div>
        <label htmlFor="newPassword">Password:</label>
        <input
          type="password"
          id="newPassword"
          value={newPassword}
          onChange={(e) => setNewPassword(e.target.value)}
          required
        />
      </div>

      <button type="submit">Change Password</button>
      <br />
      <Link to="/">Go Back</Link>
    </form>
  );
};

export default ChangePasswordPage;
