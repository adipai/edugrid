import { Link } from 'react-router-dom';


const AdminLandingPage = () => {
    return (
        <div>
            <h1>Admin Dashboard</h1>
            <ul>
                <li><Link to="/admin/create-faculty-account">1. Create a Faculty Account</Link></li>
                <li><Link to="/admin/create-textbook">2. Create E-textbook</Link></li>
                <li><Link to="/admin/modify-textbook">3. Modify E-textbooks</Link></li>
                <li><Link to="/admin/create-active-course">4. Create New Active Course</Link></li>
                <li><Link to="/admin/create-evaluation-course">5. Create New Evaluation Course</Link></li>
                <li><Link to="/queires">6. Additional Queries</Link></li>
                <li><Link to="/">6. Logout</Link></li>
            </ul>
        </div>
    );
};

export default AdminLandingPage;