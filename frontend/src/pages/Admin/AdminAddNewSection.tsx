import React, { useState } from "react";
import { Link } from "react-router-dom";

const AdminAddNewSection: React.FC = () => {
  const [sectionNumber, setSectionNumber] = useState("");
  const [sectionTitle, setSectionTitle] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Handle form submission logic here
    console.log("Section Number:", sectionNumber);
    console.log("Section Title:", sectionTitle);
  };

  return (
    <div>
      <h1>Add New Section</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="sectionNumber">Section Number:</label>
          <input
            type="text"
            id="sectionNumber"
            value={sectionNumber}
            onChange={(e) => setSectionNumber(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="sectionTitle">Section Title:</label>
          <input
            type="text"
            id="sectionTitle"
            value={sectionTitle}
            onChange={(e) => setSectionTitle(e.target.value)}
          />
        </div>
        <button type="submit" onClick={(e) => handleSubmit(e)}>
          Add new content block
        </button>
      </form>
      {/* <div>
        <Link to="/add-content-block">Add new content block</Link>
      </div> */}
      <div>
        <Link to="/admin/landing">Go back</Link>
      </div>
      <div>
        <Link to="/admin/landing">Landing Page</Link>
      </div>
    </div>
  );
};

export default AdminAddNewSection;
