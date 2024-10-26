import React, { useState } from "react";
import { Link } from "react-router-dom";

const AdminModifyChapter: React.FC = () => {
  const [chapterId, setChapterId] = useState("");

  const handleAddSection = () => {
    // Logic to add a new section
    console.log("Add new section for Chapter ID:", chapterId);
  };

  return (
    <div>
      <h1>Modify Chapter</h1>
      <div>
        <label htmlFor="chapterId">Chapter ID:</label>
        <input
          type="text"
          id="chapterId"
          value={chapterId}
          onChange={(e) => setChapterId(e.target.value)}
        />
      </div>
      <button onClick={handleAddSection}>Add new section</button>
      <br />
      <Link to="/modify-section">Modify section</Link>
      <br />
      <Link to="/go-back">Go back</Link>
      <br />
      <Link to="/landing-page">Landing page</Link>
    </div>
  );
};

export default AdminModifyChapter;
