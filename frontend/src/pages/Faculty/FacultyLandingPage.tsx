import { Link } from 'react-router-dom';


const FacultyLandingPage = () => {
    return (
        <div>
            <h1>Faculty Dashboard</h1>
            <ul>
                <li><Link to="/create-faculty-account">1. Go to Active Course</Link></li>
                <li><Link to="/create-etextbook">2. Go to Evaluation Course</Link></li>
                <li><Link to="/faculty/courses">3. View Courses</Link></li>
                <li><Link to="/change-password-page">4. Change Password</Link></li>
                <li><Link to="/">5. Logout</Link></li>
            </ul>
        </div>
    );
};

export default FacultyLandingPage;