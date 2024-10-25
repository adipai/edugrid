import { Link } from 'react-router-dom';

const LoginHome = () => {
    localStorage.clear()

    return (
        <div>
            <h1>Login Home</h1>
            <nav>
                <ul>
                    <li><Link to="/admin/login">1. Admin Login</Link></li>
                    <li><Link to="/faculty/login">2. Faculty Login</Link></li>
                    <li><Link to="/ta/login">3. Teaching Assitant Login</Link></li>
                    <li><Link to="/student/login">4. Student Login</Link></li>
                </ul>
            </nav>
        </div>
    );
};

export default LoginHome;