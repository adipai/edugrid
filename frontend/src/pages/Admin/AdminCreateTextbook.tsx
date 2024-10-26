import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';

const AdminCreateTextbook: React.FC = () => {
    const [textbookId, setTextbookId] = useState('');
    const [textbookName, setTextbookName] = useState('');
    const navigate = useNavigate();


    const handleCreateTextbook = async () => {
        try {
            const response = await axios.post('http://localhost:8000/create_textbook', {
                tb_id: textbookId,
                tb_name: textbookName,
            });
            console.log('Textbook created:', response.data);
            navigate('/admin/create-new-section?tb_id=' + textbookId);
        } catch (error) {
            console.error('Error creating textbook:', error);
        }
    };

    return (
        <div>
            <h1>Create Textbook</h1>
            <div>
                <label>
                    Textbook ID:
                    <input
                        type="text"
                        value={textbookId}
                        onChange={(e) => setTextbookId(e.target.value)}
                    />
                </label>
            </div>
            <div>
                <label>
                    Textbook Name:
                    <input
                        type="text"
                        value={textbookName}
                        onChange={(e) => setTextbookName(e.target.value)}
                    />
                </label>
            </div>
            <button onClick={handleCreateTextbook}>Create Textbook</button>
            <div>
                <Link to="/admin/landing">Go Back</Link>
            </div>
        </div>
    );
};

export default AdminCreateTextbook;