import axios from 'axios';
import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

const AdminCreateActiveCourse = () => {
    const [courseID, setCourseId] = useState('');
    const [courseName, setCourseName] = useState('');
    const [textbookId, setTextbookId] = useState('');
    const [facultyId, setFacultyId] = useState('');
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');
    const [courseCapacity, setCourseCapacity] = useState(0);
    const [uniqueToken, setUniqueToken] = useState('');


    
    const navigate = useNavigate();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            const body = {
                course_id: courseID,
                course_name: courseName,
                textbook_id: textbookId,
                faculty_id: facultyId,
                course_type: "active",
                start_date: startDate,
                end_date: endDate,
                unique_token: uniqueToken,
                capacity: courseCapacity
              };
            const response = await axios.post('http://localhost:8000/create_course', 
                body, 
                {headers: {
              'Content-Type': 'application/json',
            }, withCredentials: false});
            console.log('Login successful:', response.data);
            
            window.alert("Active course created successfully!");
            navigate('/admin/landing');
            // Handle success
          } catch (error: any) {
            if (error.response) {
              console.error('Login failed:', JSON.stringify(error.response.data.detail));
              window.alert(error.response.data.detail);
            } else {
              console.error('An error occurred:', error.message);
              window.alert(error.message);

            }
          }
    };

    return (
        <div>
            <h1>Create an Active Course</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Course ID:</label>
                    <input 
                        type="text" 
                        value={courseID} 
                        onChange={(e) => setCourseId(e.target.value)} 
                        required 
                    />
                </div>
                <div>
                    <label>Unique Token:</label>
                    <input 
                        type="text" 
                        value={uniqueToken} 
                        onChange={(e) => setUniqueToken(e.target.value)} 
                        required 
                    />
                </div>
                <div>
                    <label>Course Name:</label>
                    <input 
                        type="text" 
                        value={courseName} 
                        onChange={(e) => setCourseName(e.target.value)} 
                        required 
                    />
                </div>
                <div>
                    <label>Textbook ID:</label>
                    <input 
                        type="text" 
                        value={textbookId} 
                        onChange={(e) => setTextbookId(e.target.value)} 
                        required 
                    />
                </div>
                <div>
                    <label>Faculty ID:</label>
                    <input 
                        type="text" 
                        value={facultyId} 
                        onChange={(e) => setFacultyId(e.target.value)} 
                        required 
                    />
                </div>
                <div>
                    <label>Course capacity:</label>
                    <input 
                        type="number" 
                        value={courseCapacity} 
                        onChange={(e) => setCourseCapacity(parseInt(e.target.value) || 0)} 
                        required 
                    />
                </div>
                <div>
                    <label>Start Date:</label>
                    <input 
                        type="date" 
                        value={startDate} 
                        onChange={(e) => setStartDate(e.target.value)} 
                        required 
                    />
                </div>
                <div>
                    <label>End Date:</label>
                    <input 
                        type="date" 
                        value={endDate} 
                        onChange={(e) => setEndDate(e.target.value)} 
                        required 
                    />
                </div>
                <button type="submit">Create Active Course</button>
            </form>
            <Link to="/admin/landing">Go Back</Link>
        </div>
    );
};

export default AdminCreateActiveCourse;