import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const AdminContentAddActivity: React.FC = () => {
    const [text, setText] = useState('');

    const handleAddClick = () => {
        // Handle the add text logic here
        console.log('Text added:', text);
    };

    return (
        <div>
            <div>
                <label htmlFor="addText">Unique Acitivity ID:</label>
                <input
                    type="text"
                    id="addText"
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                />
            </div>
            <button onClick={handleAddClick}>Add Question</button>
            <div>
                <Link to="/admin">Go Back</Link>
            </div>
            <div>
                <Link to="/">Landing Page</Link>
            </div>
        </div>
    );
};

export default AdminContentAddActivity;