import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';

const AdminCreateTextbook: React.FC = () => {
    const [textbookId, setTextbookId] = useState('');
    const [textbookName, setTextbookName] = useState('');
    const navigate = useNavigate();
    const createdBy = localStorage.getItem('user_id')

    const handleCreateTextbook = async (e: any) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/create_textbook', {
                tb_id: textbookId,
                tb_name: textbookName,
                created_by: createdBy
            });
            console.log('Textbook created:', response.data);
            navigate('/admin/create-new-chapter?tb_id=' + textbookId);
        } catch (error) {
            console.error('Error creating textbook:', error);
        }
    };

    return (
        <div>
            <h1>Create Textbook</h1>
            <form onSubmit={(e) => handleCreateTextbook(e)}>
                <div>
                    <label>
                        Textbook ID:
                        <input
                            type="number"
                            value={textbookId}
                            onChange={(e) => setTextbookId(e.target.value)}
                            required
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
                            required
                        />
                    </label>
                </div>
                <button type='submit'>Create Textbook</button>
            </form>
            <div>
                <Link to="/admin/landing">Go Back</Link>
            </div>
        </div>
    );
};

export default AdminCreateTextbook;