import React, { useEffect, useState } from "react";
import { Link, useLocation } from "react-router-dom";
import { useNavigate } from "react-router-dom";

const AdminModifyTextbook: React.FC = () => {
  const [textbookId, setTextbookId] = useState("");
  const [textbookDetails, setTextbookDetails] = useState<any>(null);

  const navigate = useNavigate();
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);

  const tb_id = queryParams.get("tb_id");

  useEffect(() => {
    if (!tb_id) {
      setTextbookDetails(null);
      return;
    }
    fetch(`http://localhost:8000/api/v1/textbook?tb_id=${tb_id}`)
      .then((response) => response.json())
      .then((data) => {
        // Handle the fetched textbook data here
        console.log(data);
        if (data?.textbook) {
          setTextbookDetails(data.textbook);
        } else {
          console.log("Textbook not found");
          throw new Error("Textbook not found");
        }
      })
      .catch((error) => {
        console.error("Error fetching textbook data:", error);
        window.alert("Error fetching textbook data");
        navigate(-1)
      });
  }, [tb_id]);

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    // Handle form submission logic here
    setTextbookId("");
    navigate("/admin/modify-textbook?tb_id=" + textbookId);
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
          <button type="submit">Submit</button>
        </form>
      )}

      {textbookDetails && <h2>Textbook: {textbookDetails?.title}</h2>}
      <ul>
        {textbookDetails && (
          <>
            <li>
              <Link
                to={`/admin/create-new-chapter?tb_id=${textbookDetails.textbook_id}`}
              >
                1. Add New Chapter
              </Link>
            </li>
            <li>
              <Link
                to={`/admin/modify-chapter?tb_id=${textbookDetails.textbook_id}`}
              >
                2. Modify Chapter
              </Link>
            </li>
          </>
        )}
        <li>
          <div onClick={() => navigate(-1)}>3. Go Back</div>
        </li>
        <li>
          <Link to={`/admin/landing`}>4. Landing Page</Link>
        </li>
      </ul>
    </div>
  );
};

export default AdminModifyTextbook;
