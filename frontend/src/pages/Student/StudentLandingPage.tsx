import { useEffect } from 'react';
import { Link } from 'react-router-dom';


const StudentLandingPage = () => {
    const course_id = "NCSUOganCSC440F24";

    useEffect(() => {
        
    }, [])

    return (
        <div>
            <h1>Student Dashboard</h1>
            <ul>
                <li><Link to="/student/view-section">1. View a Section</Link></li>
                <li><Link to="/student/participation">2. View Pariticipation Acitivity Point</Link></li>
                <li><Link to="/">3. Logout</Link></li>
            </ul>
        </div>
    );
};

export default StudentLandingPage;