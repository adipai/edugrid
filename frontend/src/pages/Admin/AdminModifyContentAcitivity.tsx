import axios from "axios";
import React, { useEffect, useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";

const AdminModifyContentActivity: React.FC = () => {
  const [text, setText] = useState("");

  const navigate = useNavigate();
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);

  const tb_id = queryParams.get("tb_id");
  const chap_id = queryParams.get("chap_id");
  const sec_id = queryParams.get("sec_id");
  const block_id = queryParams.get("block_id");
  // const user_id = localStorage.getItem("user_id");
  const activity_id = queryParams.get("activity_id");

  const [chapDetails, setChapDetails] = useState<any>({});
  const [tbDetails, setTbDetails] = useState<any>({});
  const [secDetails, setSecDetails] = useState<any>({});
  const [blockDetails, setBlockDetails] = useState<any>({});
  //   const [activityDetails, setActivityDetails] = useState<any>({});

  useEffect(() => {
    if (!tb_id || !chap_id || !sec_id || !block_id) {
      return;
    }

    const fetchChapterDetails = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/api/v1/chapter?tb_id=${tb_id}&chap_id=${chap_id}`
        );
        setChapDetails(response.data.chapter);
      } catch (error) {
        console.error("Error fetching chapter details:", error);
      }
    };

    const fetchTbDetails = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/api/v1/textbook?tb_id=${tb_id}`
        );
        setTbDetails(response.data.textbook);
      } catch (error) {
        console.error("Error fetching textbook details:", error);
      }
    };

    const fetchSectionDetails = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/api/v1/section?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}`
        );
        setSecDetails(response.data.section);
      } catch (error) {
        console.error("Error fetching section details:", error);
      }
    };
    const fetchBlockDetails = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/api/v1/block?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}&block_id=${block_id}`
        );
        setBlockDetails(response.data.block);
      } catch (error) {
        console.error("Error fetching block details:", error);
      }
    };
    
    fetchChapterDetails();
    fetchTbDetails();
    fetchSectionDetails();
    fetchBlockDetails();
  }, [tb_id, chap_id, sec_id, block_id]);

  const handleAddClick = async (e: any) => {
    e.preventDefault();
    if (activity_id) {
      navigate(
        `/admin/activity-add-question?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}&block_id=${block_id}&activity_id=${activity_id}`
      );
    } else {
      navigate(
        `/admin/modify-add-question?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}&block_id=${block_id}&activity_id=${text}`
      );
    }
  };

  return (
    <div>
      <h1>Modify Activity</h1>
      <h3>Textbook Name: {tbDetails?.title}</h3>
      <h3>Chapter Name: {chapDetails?.title}</h3>
      <h3>Section Name: {secDetails?.title}</h3>
      <h3>Block Name: {blockDetails?.block_id}</h3>
      <form onSubmit={handleAddClick}>
        <div>
          <label htmlFor="addText">Unique Acitivity ID:</label>
          {activity_id && (
            <input type="text" id="addText" value={activity_id} disabled={true} />
          )}
          {!activity_id && (
            <input
              type="text"
              id="addText"
              value={text}
              onChange={(e) => setText(e.target.value)}
            />
          )}
        </div>
        <button type="submit">Add Question</button>
      </form>
      <div>
        <div onClick={() => navigate(-1)}>Go Back</div>
      </div>
      <div>
        <Link to="/admin/landing">Landing Page</Link>
      </div>
    </div>
  );
};

export default AdminModifyContentActivity;
