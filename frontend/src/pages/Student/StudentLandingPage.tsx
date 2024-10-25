import { Link } from 'react-router-dom';


const StudentLandingPage = () => {
    return (
        <div>
            <h1>Student Dashboard</h1>
            <ul>
                <li><Link to="/create-faculty-account">1. View a Section</Link></li>
                <li><Link to="/create-etextbook">2. View Pariticipation Acitivity Point</Link></li>
                <li><Link to="/">3. Logout</Link></li>
            </ul>
        </div>
    );
};

export default StudentLandingPage;