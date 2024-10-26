import axios from 'axios';
import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

const AdminCreateFaculty = () => {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const navigate = useNavigate();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            const body = {
                first_name: firstName,
                last_name: lastName,
                email: email,
                password: password,
                role: "faculty"
              };
            const response = await axios.post('http://localhost:8000/add_faculty', 
                body, 
                {headers: {
              'Content-Type': 'application/json',
            }, withCredentials: false});
            console.log('Login successful:', response.data);
            
            window.alert("Faculty account created successfully!");
            navigate('/admin/landing');
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
        <div>
            <h1>Create a Faculty Account</h1>
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
                <button type="submit">Create Account</button>
            </form>
            <Link to="/admin/landing">Go Back</Link>
        </div>
    );
};

export default AdminCreateFaculty;