import { Link } from 'react-router-dom';


const TALandingPage = () => {
    return (
        <div>
            <h1>Teaching Assistant Dashboard</h1>
            <ul>
                <li><Link to="/create-faculty-account">1. Go to active Course</Link></li>
                <li><Link to="/create-etextbook">2. View Courses</Link></li>
                <li><Link to="/modify-etextbooks">3. Change Password</Link></li>
                <li><Link to="/">4. Logout</Link></li>
            </ul>
        </div>
    );
};

export default TALandingPage;