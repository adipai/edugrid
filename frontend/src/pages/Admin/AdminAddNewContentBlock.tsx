import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';

const AdminAddNewContentBlock: React.FC = () => {
    const [contentId, setContentId] = useState('');
    const location = useLocation();
    const queryParams = new URLSearchParams(location.search);
    const tb_id = queryParams.get("tb_id");
    const chapter_id = queryParams.get("chapter_id");
    const section_id = queryParams.get("section_id");

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setContentId(e.target.value);
    };

    const handleAddText = () => {
        console.log('Add text clicked');
    };

    const handleAddPicture = () => {
        console.log('Add picture clicked');
    };

    const handleAddActivity = () => {
        console.log('Add activity clicked');
    };

    return (
        <div>
            <form>
                <div>
                    <label htmlFor="contentId">Content Id:</label>
                    <input
                        type="text"
                        id="contentId"
                        value={contentId}
                        onChange={handleInputChange}
                    />
                </div>
            </form>
            <div>
                <button onClick={handleAddText}>Add text</button>
                <button onClick={handleAddPicture}>Add picture</button>
                <button onClick={handleAddActivity}>Add activity</button>
            </div>
            <Link to={`/admin/`}>Go Back</Link>
            <Link to="/admin/landing">Landing Page</Link>
        </div>
    );
};

export default AdminAddNewContentBlock;