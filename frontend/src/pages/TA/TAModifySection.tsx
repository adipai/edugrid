import React, { useEffect, useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";

const TAModifySection: React.FC = () => {
  const [sectionId, setSectionId] = useState("");

  const [textbookDetails, setTextbookDetails] = useState<any>(null);
  const [chapDetails, setChapDetails] = useState<any>({});
  const [secDetails, setSecDetails] = useState<any>({});

  const navigate = useNavigate();
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);

  const tb_id = queryParams.get("tb_id");
  const chap_id = queryParams.get("chap_id");
  const sec_id = queryParams.get("sec_id");

  const handleSectionId = (event: React.FormEvent) => {
    event.preventDefault();
    setSecDetails("");
    navigate(
      `/ta/modify-section?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sectionId}`
    );
  };

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
        console.error("Error fetching chapter data:", error);
      });
  }, [tb_id, chap_id]);

  useEffect(() => {
    if (!tb_id || !chap_id || !sec_id) {
      setSecDetails(null);
      return;
    }
    fetch(
      `http://localhost:8000/api/v1/section?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}`
    )
      .then((response) => response.json())
      .then((data) => {
        // Handle the fetched section data here
        if (data?.section) {
          setSecDetails(data.section);
        } else {
          console.log("Section not found");
          throw new Error("Section not found");
        }
      })
      .catch((error) => {
        console.error("Error fetching section data:", error);
        window.alert("Section not found");
        navigate(-1);
      });
  }, [tb_id, chap_id, sec_id]);

  return (
    <div>
      <h1>Teaching Assistant Modify Section</h1>
      {textbookDetails && <h3>Textbook: {textbookDetails?.title}</h3>}
      {chapDetails && <h3>Chapter: {chapDetails?.title}</h3>}
      {secDetails && <h3>Section: {secDetails?.title}</h3>}
      {!secDetails && (
        <form onSubmit={handleSectionId}>
          <div>
            <label>Section ID:</label>
            <input
              type="text"
              value={sectionId}
              onChange={(e) => setSectionId(e.target.value)}
            />
          </div>
          <div>
            <button type="submit">Submit</button>
          </div>
        </form>
      )}
      {secDetails && (
        <>
        <div>
        <Link
              to={`/save-cancel?tb_id=${tb_id}&chap_id=${chap_id}&endpoint=hide_section`}
            >
              1. Hide Section
            </Link>
        </div>
        <div>
        <Link
              to={`/save-cancel?tb_id=${tb_id}&chap_id=${chap_id}&endpoint=delete_section`}
            >
              2. Delete Section
            </Link>
        </div>
          <div>
            <Link
              to={`/ta/create-new-block?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}`}
            >
              3. Add New Content Block
            </Link>
          </div>
          <div>
            <Link
              to={`/ta/modify-content?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}`}
            >
              4. Modify Content Block
            </Link>
          </div>
        </>
      )}
      <div>
        <div onClick={() => navigate(-1)}>Go Back</div>
      </div>
      <div>
        <Link to="/">Landing Page</Link>
      </div>
    </div>
  );
};

// const taModifySection: React.FC = () => {
//     return <h1>Hello world</h1>
// };

export default TAModifySection;
