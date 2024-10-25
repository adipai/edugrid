import { Link } from 'react-router-dom';

const StudentPreLogin = () => {
    return (
        <div>
            <h1>Welcome, Student!</h1>
            <ul>
                <li><Link to="/student/enroll">Enroll in course</Link></li>
                <li><Link to="/student/login">Sign in</Link></li>
                <li><Link to="/">Go Back</Link></li>
            </ul>
        </div>
    );
};

export default StudentPreLogin;