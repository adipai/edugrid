import axios from "axios";
import React, { useEffect, useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";


const FacultyAddNewChapter: React.FC = () => {
  const [chapterId, setChapterId] = useState("");
  const [chapterTitle, setChapterTitle] = useState("");
  const [tbDetails, setTbDetails] = useState<any>({});

  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const tb_id = queryParams.get("tb_id");
  const createdBy = localStorage.getItem('user_id')
  const navigate = useNavigate();

  useEffect(() => {
    if (!tb_id) {
      return;
    }
    // Fetch textbook data here
    fetch(`http://localhost:8000/api/v1/textbook?tb_id=${tb_id}`)
      .then((response) => response.json())
      .then((data) => {
        // Handle the fetched textbook data here
        setTbDetails(data.textbook);
      })
      .catch((error) => {
        console.error("Error fetching textbook data:", error);
      });
  }, [tb_id]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    // Handle form submission logic here
    try {
      const response = await axios.post(
        "http://localhost:8000/create_chapter",
        {
          tb_id,
          chap_id: chapterId,
          chap_title: chapterTitle,
          created_by: createdBy,
        }
      );
      console.log("Chapter created:", response.data);
      navigate(`/faculty/create-new-section?tb_id=${tb_id}&chap_id=${chapterId}`);
    } catch (error) {
      console.error("Error creating chapter:", error);
    }
  };

  return (
    <div>
      <h1>Add New Chapter</h1>
      <h3>Textbook Name: {tbDetails?.title}</h3>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="chapterId">Unique Chapter ID:</label>
          <input
            type="text"
            id="chapterId"
            value={chapterId}
            onChange={(e) => setChapterId(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="chapterTitle">Chapter Title:</label>
          <input
            type="text"
            id="chapterTitle"
            value={chapterTitle}
            onChange={(e) => setChapterTitle(e.target.value)}
          />
        </div>
        <ul>
          <li>
            <button type="submit">Add Chapter</button>
          </li>
          <li>
          <div onClick={() => navigate(-1)}>Go back</div>
          </li>
          <li>
            <Link to={`/faculty/landing`}>Landing Page</Link>
          </li>
        </ul>
      </form>
    </div>
  );
};

export default FacultyAddNewChapter;
