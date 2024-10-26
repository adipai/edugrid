import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const AdminActivityAddQuestion: React.FC = () => {
    const [formData, setFormData] = useState<any>({
        questionId: '',
        questionText: '',
        options: [
            { text: '', explanation: '', label: 'incorrect' },
            { text: '', explanation: '', label: 'incorrect' },
            { text: '', explanation: '', label: 'incorrect' },
            { text: '', explanation: '', label: 'incorrect' },
        ],
    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>, index?: number, field?: string) => {
        if (index !== undefined && field) {
            const newOptions = [...formData.options];
            newOptions[index][field] = e.target.value;
            setFormData({ ...formData, options: newOptions });
        } else {
            setFormData({ ...formData, [e.target.name]: e.target.value });
        }
    };

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        // Handle form submission logic here
        console.log(formData);
    };

    return (
        <div>
            <h1>Add New Question</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Question ID:</label>
                    <input
                        type="text"
                        name="questionId"
                        value={formData.questionId}
                        onChange={handleChange}
                    />
                </div>
                <div>
                    <label>Question Text:</label>
                    <input
                        type="text"
                        name="questionText"
                        value={formData.questionText}
                        onChange={handleChange}
                    />
                </div>
                {formData.options.map((option: any, index: any) => (
                    <div key={index}>
                        <h3>Option {index + 1}</h3>
                        <div>
                            <label>Text:</label>
                            <input
                                type="text"
                                value={option.text}
                                onChange={(e) => handleChange(e, index, 'text')}
                            />
                        </div>
                        <div>
                            <label>Explanation:</label>
                            <input
                                type="text"
                                value={option.explanation}
                                onChange={(e) => handleChange(e, index, 'explanation')}
                            />
                        </div>
                        <div>
                            <label>Label:</label>
                            <select
                                value={option.label}
                                onChange={(e) => handleChange(e, index, 'label')}
                            >
                                <option value="correct">Correct</option>
                                <option value="incorrect">Incorrect</option>
                            </select>
                        </div>
                    </div>
                ))}
                <button type="submit">Save</button>
            </form>
            <div>
                <br />
                <Link to="/admin">Cancel</Link>
                <br />
                <Link to="/admin/landing">Landing Page</Link>
            </div>
        </div>
    );
};

export default AdminActivityAddQuestion;