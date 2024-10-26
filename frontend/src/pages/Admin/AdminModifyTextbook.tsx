import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const AdminModifyTextbook: React.FC = () => {
  const [searchTbId, setSearchTbId] = useState("");
  const [textbookId, setTextbookId] = useState("");
  const [textbookDetails, setTextbookDetails] = useState<any>(null);

  useEffect(() => {
    // Fetch textbook data here
    if (!searchTbId){
        return;
    }
    console.log(`http://localhost:8000/api/v1/textbook?tb_id=${searchTbId}`);
    fetch(`http://localhost:8000/api/v1/textbook?tb_id=${searchTbId}`)
      .then((response) => response.json())
      .then((data) => {
        // Handle the fetched textbook data here
        console.log(data)
        if (data?.textbook){
            setTextbookDetails(data.textbook);
        }else{
            window.alert("Textbook not found");
        }
      })
      .catch((error) => {
        console.error("Error fetching textbook data:", error);
      });
  }, [searchTbId]);

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    // Handle form submission logic here
    console.log("Submitted e-textbook ID:", textbookId);
  };

  const handleSearch = (event: React.FormEvent) => {
    event.preventDefault();
    setSearchTbId(textbookId);
    setTextbookId("");
  };

  const handleGoBack = (e: React.FormEvent) => {
    setSearchTbId("");
    setTextbookDetails(null);
  };

  return (
    <div>
      <h1>Modify E-Textbook</h1>
      {!textbookDetails && (
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="textbookId">Unique E-Textbook ID:</label>
            <input
              type="text"
              id="textbookId"
              value={textbookId}
              onChange={(e) => setTextbookId(e.target.value)}
              required
            />
          </div>
          <button type="submit" onClick={(e) => handleSearch(e)}>
            Submit
          </button>
        </form>
      )}
      {textbookDetails && (
        <>
          <h2>Textbook: {textbookDetails?.title}</h2>
          <ul>
            <li>
              <Link to={`/admin/create-new-section?tb_id=${textbookDetails.textbook_id}`}>
                1. Add New Chapter
              </Link>
            </li>
            <li>
              <Link to={`/admin/modify-chapter?tb_id=${textbookDetails.textbook_id}`}>
                2. Modify Chapter
              </Link>
            </li>
            <li>
              {/* <Link to={`/admin/landing`}>3. Go Back</Link> */}
              <div onClick={(e) => handleGoBack(e)}>3. Go Back</div>
            </li>
            <li>
              <Link to={`/admin/landing`}>4. Landing Page</Link>
            </li>
          </ul>
        </>
      )}
    </div>
  );
};

export default AdminModifyTextbook;
