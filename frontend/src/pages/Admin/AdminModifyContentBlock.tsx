import React from "react";
import { Link } from "react-router-dom";

const AdminModifyContentBlock = () => {
  const [contentBlockId, setContentBlockId] = React.useState("");

  const handleAddText = () => {
    console.log(`Add text to content block ${contentBlockId}`);
  };

  const handleAddPicture = () => {
    console.log(`Add picture to content block ${contentBlockId}`);
  };

  const handleAddActivity = () => {
    console.log(`Add activity to content block ${contentBlockId}`);
  };

  return (
    <div>
      <h1>Modify Content Block</h1>
      <div>
        <label htmlFor="chapterId">Chapter ID:</label>
        <input
          type="text"
          id="chapterId"
          value={contentBlockId}
          onChange={(e) => setContentBlockId(e.target.value)}
        />
      </div>
      <button onClick={handleAddText}>Add Text</button>
      <button onClick={handleAddPicture}>Add Picture</button>
      <button onClick={handleAddActivity}>Add Activity</button>
      <div>
        <Link to="/admin">Go Back</Link>
        <br />
        <Link to="/admin/landing">Landing Page</Link>
      </div>
    </div>
  );
};

export default AdminModifyContentBlock;
