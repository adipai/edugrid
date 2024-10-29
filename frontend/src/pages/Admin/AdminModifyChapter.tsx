import React, { useEffect, useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";

const AdminModifyChapter: React.FC = () => {
  const [chapterId, setChapterId] = useState("");
  const [textbookDetails, setTextbookDetails] = useState<any>(null);
  const [chapDetails, setChapDetails] = useState<any>({});

  const navigate = useNavigate();
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);

  const tb_id = queryParams.get("tb_id");
  const chap_id = queryParams.get("chap_id");

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
      });
  }, [tb_id]);

  useEffect(() => {
    if (!tb_id || !chap_id) {
      setChapDetails(null);
      return;
    }
    fetch(
      `http://localhost:8000/api/v1/chapter?tb_id=${tb_id}&chap_id=${chap_id}`
    )
      .then((response) => response.json())
      .then((data) => {
        // Handle the fetched chapter data here
        if (data?.chapter) {
          setChapDetails(data.chapter);
        } else {
          console.log("Chapter not found");
          throw new Error("Chapter not found");
        }
      })
      .catch((error) => {
        console.error("Error fetching textbook data:", error);
        window.alert("Not Chapter found");
        navigate(-1);
      });
  }, [tb_id, chap_id]);

  const handleChapterId = (e: any) => {
    e.preventDefault();
    // Logic to add a new section
    console.log("Add new section for Chapter ID:", chapterId);
    setChapterId("");
    navigate("/admin/modify-chapter?tb_id=" + tb_id + "&chap_id=" + chapterId);
  };

  return (
    <div>
      <h1>Modify Chapter</h1>
      {textbookDetails && <h2>Textbook: {textbookDetails?.title}</h2>}
      {!chapDetails && (
        <form onSubmit={handleChapterId}>
          <div>
            <label htmlFor="chapterId">Chapter ID:</label>
            <input
              type="text"
              id="chapterId"
              value={chapterId}
              onChange={(e) => setChapterId(e.target.value)}
              required
            />
          </div>
          <button type="submit">Submit</button>
        </form>
      )}
      {chapDetails && (
        <>
          <h3>Chapter: {chapDetails?.title}</h3>
          <div>
            <Link
              to={`/admin/create-new-section?tb_id=${tb_id}&chap_id=${chapDetails?.chapter_id}`}
            >
              1. Add new section
            </Link>
          </div>
          <div>
            <Link
              to={`/admin/modify-section?tb_id=${tb_id}&chap_id=${chapDetails?.chapter_id}`}
            >
              2. Modify section
            </Link>
          </div>
        </>
      )}
      <div>
        <div onClick={() => navigate(-1)}>3. Go back</div>
      </div>
      <div>
        <Link to="/admin/landing">4.Landing page</Link>
      </div>
    </div>
  );
};

export default AdminModifyChapter;
