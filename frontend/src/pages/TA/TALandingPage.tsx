import { Link } from 'react-router-dom';


const TALandingPage = () => {
    return (
        <div>
            <h1>Teaching Assistant Dashboard</h1>
            <ul>
                <li><Link to="/ta/active-courses">1. Go to active Course</Link></li>
                <li><Link to="/ta/courses">2. View Courses</Link></li>
                <li><Link to="/change-password-page">3. Change Password</Link></li>
                <li><Link to="/">4. Logout</Link></li>
            </ul>
        </div>
    );
};

export default TALandingPage;