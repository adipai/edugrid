import React, { useEffect, useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";

const FacultyModifyContentBlock = () => {
  const [contentBlockId, setContentBlockId] = React.useState("");

  const [textbookDetails, setTextbookDetails] = useState<any>(null);
  const [chapDetails, setChapDetails] = useState<any>({});
  const [secDetails, setSecDetails] = useState<any>({});
  const [blockDetails, setBlockDetails] = useState<any>({});

  const navigate = useNavigate();
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);

  const tb_id = queryParams.get("tb_id");
  const chap_id = queryParams.get("chap_id");
  const sec_id = queryParams.get("sec_id");
  const block_id = queryParams.get("block_id");

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
      });
  }, [tb_id, chap_id, sec_id]);

  useEffect(() => {
    if (!tb_id || !chap_id || !sec_id || !block_id) {
      setBlockDetails(null);
      return;
    }
    fetch(
      `http://localhost:8000/api/v1/block?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}&block_id=${block_id}`
    )
      .then((response) => response.json())
      .then((data) => {
        // Handle the fetched block data here
        if (data?.block) {
          setBlockDetails(data.block);
        } else {
          console.log("Block not found");
          throw new Error("Block not found");
        }
      })
      .catch((error) => {
        console.error("Error fetching block data:", error);
        window.alert("Block not found");
        navigate(-1);
      });
  }, [tb_id, chap_id, sec_id, block_id]);

  const handleAddContent = (type: string) => {
    if (type === 'text') {
      navigate(`/faculty/content-add-text?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}&block_id=${block_id}`)
    }else if (type === 'picture') {
      navigate(`/faculty/content-add-pic?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}&block_id=${block_id}`)
    } else if (type === 'activity') {
      navigate(`/faculty/modify-activity?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}&block_id=${block_id}`)
    }
  };

  const handleBlockId = (e: React.FormEvent) => {
    e.preventDefault();
    setContentBlockId("");
    navigate(
      `/faculty/modify-content?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}&block_id=${contentBlockId}`
    );
  };

  return (
    <div>
      <h1>Modify Content Block</h1>
      {textbookDetails && <h3>Textbook: {textbookDetails?.title}</h3>}
      {chapDetails && <h3>Chapter: {chapDetails?.title}</h3>}
      {secDetails && <h3>Section: {secDetails?.title}</h3>}
      {blockDetails && <h3>Block: {blockDetails?.block_id}</h3>}
      {!blockDetails && (
        <form onSubmit={handleBlockId}>
          <div>
            <label htmlFor="chapterId">Content Block ID:</label>
            <input
              type="text"
              id="chapterId"
              value={contentBlockId}
              onChange={(e) => setContentBlockId(e.target.value)}
            />
          </div>
          <button type="submit">Submit</button>
        </form>
      )}
      {!!blockDetails && (
        <>
        <div>
        <Link
              to={`/save-cancel?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}&block_id=${block_id}&endpoint=hide_block`}
            >
              1. Hide Content Block
            </Link>
        </div>
        <div>
        <Link
              to={`/save-cancel?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}&block_id=${block_id}&endpoint=delete_block`}
            >
              2. Delete Content Block
            </Link>
        </div>
          <button onClick={() => handleAddContent('text')}>Add Text</button>
          <button onClick={() => handleAddContent('picture')}>Add Picture</button>
          <button onClick={() => handleAddContent('activity')}>Add Activity</button>
        </>
      )}
      <div>
        <div onClick={() => navigate(-1)}>Go Back</div>
      </div>
      <div>
        <Link to="/faculty/landing">Landing Page</Link>
      </div>
    </div>
  );
};

export default FacultyModifyContentBlock;
