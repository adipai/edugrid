import axios from 'axios';
import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

const AdminCreateEvaluationCourse = () => {
    const [courseID, setCourseId] = useState('');
    const [courseName, setCourseName] = useState('');
    const [textbookId, setTextbookId] = useState('');
    const [facultyId, setFacultyId] = useState('');
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');
    
    const navigate = useNavigate();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            const body = {
                course_id: courseID,
                course_name: courseName,
                textbook_id: textbookId,
                faculty_id: facultyId,
                course_type: "evaluation",
                start_date: startDate,
                end_date: endDate
              };
            const response = await axios.post('http://localhost:8000/create_course', 
                body, 
                {headers: {
              'Content-Type': 'application/json',
            }, withCredentials: false});
            console.log('Login successful:', response.data);
            
            window.alert("Evaluation course created successfully!");
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
            <h1>Create an Evaluation Course</h1>
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
                <button type="submit">Create Evaluation Course</button>
            </form>
            <Link to="/admin/landing">Go Back</Link>
        </div>
    );
};

export default AdminCreateEvaluationCourse;