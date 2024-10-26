import axios from "axios";
import React, { useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";

const AdminAddNewContentBlock: React.FC = () => {
  const [blockId, setBlockId] = useState("");

  const navigate = useNavigate();
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);

  const tb_id = queryParams.get("tb_id");
  const chap_id = queryParams.get("chap_id");
  const sec_id = queryParams.get("sec_id");

  const created_by = localStorage.getItem("user_id");

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setBlockId(e.target.value);
  };

  const handleCreateBlock = async (action: string) => {
    try {
      const response = await axios.post("http://localhost:8000/create_block", {
        tb_id,
        chap_id,
        sec_id,
        block_id: blockId,
        created_by,
      });
      console.log("Block created:", response.data);
      // Redirect to the appropriate page based on the block type
      if (action === "text") {
        navigate(
          `/admin/content-add-text?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}&block_id=${blockId}`
        );
      } else if (action === "pic") {
        navigate(
          `/admin/content-add-pic?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}&block_id=${blockId}`
        );
      } else if (action === "activity") {
        navigate(
          `/admin/activity-add-question?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}&block_id=${blockId}`
        );
      }

      // navigate(`/admin/create-new-section?tb_id=${tb_id}&chap_id=${chapterId}`);
    } catch (error) {
      console.error("Error creating block:", error);
    }
  };

  return (
    <div>
      <form>
        <div>
          <label htmlFor="contentId">Content Id:</label>
          <input
            type="text"
            id="contentId"
            value={blockId}
            onChange={handleInputChange}
          />
        </div>
      </form>
      <div>
        <button onClick={() => handleCreateBlock("text")}>Add text</button>
        <button onClick={() => handleCreateBlock("pic")}>Add picture</button>
        <button onClick={() => handleCreateBlock("activity")}>
          Add activity
        </button>
      </div>
      {/* <Link to={`/admin/`}>Go Back</Link> */}
      <div onClick={() => navigate(-1)}>Go Back</div>
      <Link to="/admin/landing">Landing Page</Link>
    </div>
  );
};

export default AdminAddNewContentBlock;
