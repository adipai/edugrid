import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const AdminModifySection: React.FC = () => {
    const [tbId, setTbId] = useState('');
    const [chapterId, setChapterId] = useState('');
    const [sectionId, setSectionId] = useState('');

    const handleAddContentBlock = () => {
        // Add content block logic here
        console.log('Add content block', { tbId, chapterId, sectionId });
    };

    const handleModifyContentBlock = () => {
        // Modify content block logic here
        console.log('Modify content block', { tbId, chapterId, sectionId });
    };

    return (
        <div>
            <h1>Admin Modify Section</h1>
            <form>
                <div>
                    <label>Unique TB ID:</label>
                    <input
                        type="text"
                        value={tbId}
                        onChange={(e) => setTbId(e.target.value)}
                    />
                </div>
                <div>
                    <label>Chapter ID:</label>
                    <input
                        type="text"
                        value={chapterId}
                        onChange={(e) => setChapterId(e.target.value)}
                    />
                </div>
                <div>
                    <label>Section ID:</label>
                    <input
                        type="text"
                        value={sectionId}
                        onChange={(e) => setSectionId(e.target.value)}
                    />
                </div>
                <div>
                    <button type="button" onClick={handleAddContentBlock}>
                        Add New Content Block
                    </button>
                    <br />
                    <button type="button" onClick={handleModifyContentBlock}>
                        Modify Content Block
                    </button>
                </div>
            </form>
            <div>
                <Link to="/admin">Go Back</Link>
                <br/>
                <Link to="/">Landing Page</Link>
            </div>
        </div>
    );
};

// const AdminModifySection: React.FC = () => {
//     return <h1>Hello world</h1>
// };

export default AdminModifySection;