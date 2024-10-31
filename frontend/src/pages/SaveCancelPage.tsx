import axios from "axios";
import { useLocation, useNavigate } from "react-router-dom";

const SaveCancelPage: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);

  const tb_id = queryParams.get("tb_id");
  const chap_id = queryParams.get("chap_id");
  const sec_id = queryParams.get("sec_id");
  const block_id = queryParams.get("block_id")
  const endpoint = queryParams.get("endpoint")
  const user_id = localStorage.getItem("user_id")


  const saveSection = async () => {
    try {
      const body = {
        tb_id: tb_id,
        chap_id: chap_id,
        sec_id: sec_id,
        block_id: block_id,
        user_modifying: user_id
      };

      const response = await axios.post(`http://localhost:8000/${endpoint}`, body, {
        headers: {
          "Content-Type": "application/json",
        },
        withCredentials: false,
      });

      console.log(response.data);
      window.alert(response.data.message);
      
      if (endpoint?.includes("delete")) {
        navigate(-2); // Navigate back twice if endpoint contains "delete"
      } else {
        navigate(-1); // Otherwise, navigate back once
      }
    } catch (error: any) {
      if (error.response) {
        console.error("Failed:", error.response.data.detail || error.response.data.message);
        window.alert(`Error: ${error.response.data.detail || error.response.data.message}`);
      } else {
        console.error("An error occurred:", error.message);
        window.alert(`An error occurred: ${error.message}`);
      }
    }
  };

  // Cancel button function
  const cancel = () => {
    navigate(-1);  // Navigate back
  };

  return (
    <div>
      {/* Save and Cancel buttons */}
      <div>
        <button onClick={saveSection}>Save</button>
        <button onClick={cancel}>Cancel</button>
      </div>
    </div>
  );
};

export default SaveCancelPage;
