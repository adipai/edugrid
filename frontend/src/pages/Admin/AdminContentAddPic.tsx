import axios from "axios";
import React, { useEffect, useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";

const AdminContentAddPic: React.FC = () => {
  const [pic, setPic] = useState("");

  const navigate = useNavigate();
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);

  const tb_id = queryParams.get("tb_id");
  const chap_id = queryParams.get("chap_id");
  const sec_id = queryParams.get("sec_id");
  const block_id = queryParams.get("block_id");
  const createdBy = localStorage.getItem("user_id");

  const [chapDetails, setChapDetails] = useState<any>({});
  const [tbDetails, setTbDetails] = useState<any>({});
  const [secDetails, setSecDetails] = useState<any>({});
  const [blockDetails, setBlockDetails] = useState<any>({});

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
        console.error("Error fetching section details:", error);
      }
    };

    fetchChapterDetails();
    fetchTbDetails();
    fetchSectionDetails();
    fetchBlockDetails();
  }, [tb_id, chap_id, sec_id, block_id]);

  const handleAddClick = async () => {
    try {
      const response = await axios.post("http://localhost:8000/add_content", {
        tb_id,
        chap_id,
        sec_id,
        content: pic,
        block_id,
        block_type: "picture",
        created_by: createdBy,
      });
      console.log("Block created:", response.data);
      // Redirect to the appropriate page based on the block type
      navigate(
        `/admin/create-new-block?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}`
      );
    } catch (error) {
      console.error("Error creating block:", error);
    }
  };

  return (
    <div>
      <h1>Add Picture</h1>
      <h3>Textbook Name: {tbDetails?.title}</h3>
      <h3>Chapter Name: {chapDetails?.title}</h3>
      <h3>Section Name: {secDetails?.title}</h3>
      <h3>Block Name: {blockDetails?.block_id}</h3>
      <div>
        <label htmlFor="addPic">Add pic:</label>
        <input
          type="text"
          id="addPic"
          value={pic}
          onChange={(e) => setPic(e.target.value)}
        />
      </div>
      <button onClick={handleAddClick}>Add</button>
      <div>
        <div onClick={() => navigate(-1)}>Go Back</div>
      </div>
      <div>
        <Link to="/admin/landing">Landing Page</Link>
      </div>
    </div>
  );
};

export default AdminContentAddPic;
