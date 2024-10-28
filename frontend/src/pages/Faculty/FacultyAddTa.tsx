import axios from 'axios';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const FacultyCreateTa = () => {
    const queryParams = new URLSearchParams(location.search);
    const courseId = queryParams.get("course_id")
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
                role: "teaching assisant",
                course_id: courseId
              };
            const response = await axios.post('http://localhost:8000/add_ta', 
                body, 
                {headers: {
              'Content-Type': 'application/json',
            }, withCredentials: false});
            console.log('Login successful:', response.data);
            
            window.alert("Teaching Assistant added successfully!");
            navigate(`/faculty/active-courses?course_id=${courseId}`);
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
            <h1>Add Teaching Assistant to {courseId}</h1>
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
                    <label>Default Password:</label>
                    <input 
                        type="password" 
                        value={password} 
                        onChange={(e) => setPassword(e.target.value)} 
                        required 
                    />
                </div>
                <button type="submit">Save</button>
            </form>
            <div onClick={() => navigate(-1)}>Cancel</div>
        </div>
    );
};

export default FacultyCreateTa;