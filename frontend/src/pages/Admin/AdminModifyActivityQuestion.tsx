import axios from "axios";
import React, { useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";

const AdminModifyActivityQuestion: React.FC = () => {
  const [formData, setFormData] = useState<any>({
    questionId: "",
    questionText: "",
    options: [
      { text: "", explanation: "", label: "incorrect" },
      { text: "", explanation: "", label: "incorrect" },
      { text: "", explanation: "", label: "incorrect" },
      { text: "", explanation: "", label: "incorrect" },
    ],
  });

  const navigate = useNavigate();
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);

  const tb_id = queryParams.get("tb_id");
  const chap_id = queryParams.get("chap_id");
  const sec_id = queryParams.get("sec_id");
  const block_id = queryParams.get("block_id");
  const activity_id = queryParams.get("activity_id");
  const user_id = localStorage.getItem("user_id");

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>,
    index?: number,
    field?: string
  ) => {
    if (index !== undefined && field) {
      const newOptions = [...formData.options];
      newOptions[index][field] = e.target.value;
      setFormData({ ...formData, options: newOptions });
    } else {
      setFormData({ ...formData, [e.target.name]: e.target.value });
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    // Handle form submission logic here
    // console.log(formData);
    let answerCount = 0;
    let answer = 0;

    formData.options.forEach((option: any, index: any) => {
      if (option.label === "correct") {
        answerCount++;
        answer = index + 1;
      }
    });

    if (answerCount !== 1) {
      window.alert("Please select exactly one correct answer");
      return;
    }

    const body = {
      tb_id,
      chap_id,
      sec_id,
      block_id,
      activity_id,
      question_id: formData.questionId,
      question_text: formData.questionText,
      option_1: formData.options[0].text,
      option_1_explanation: formData.options[0].explanation,
      option_2: formData.options[1].text,
      option_2_explanation: formData.options[1].explanation,
      option_3: formData.options[2].text,
      option_3_explanation: formData.options[2].explanation,
      option_4: formData.options[3].text,
      option_4_explanation: formData.options[3].explanation,
      answer: answer,
      user_modifying: user_id,
    };

    try {
      const response = await axios.post(
        "http://localhost:8000/modify_content_add_question",
        body
      );
      console.log("Block created:", response.data);
      // Redirect to the appropriate page based on the block type
      navigate(
        `/admin/content-add-activity?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}&block_id=${block_id}&activity_id=${activity_id}`
      );
    } catch (error) {
      console.error("Error creating block:", error);
    }
  };

  return (
    <div>
      <h1>Add New Question</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Question ID:</label>
          <input
            type="text"
            name="questionId"
            value={formData.questionId}
            onChange={handleChange}
          />
        </div>
        <div>
          <label>Question Text:</label>
          <input
            type="text"
            name="questionText"
            value={formData.questionText}
            onChange={handleChange}
          />
        </div>
        {formData.options.map((option: any, index: any) => (
          <div key={index}>
            <h3>Option {index + 1}</h3>
            <div>
              <label>Text:</label>
              <input
                type="text"
                value={option.text}
                onChange={(e) => handleChange(e, index, "text")}
              />
            </div>
            <div>
              <label>Explanation:</label>
              <input
                type="text"
                value={option.explanation}
                onChange={(e) => handleChange(e, index, "explanation")}
              />
            </div>
            <div>
              <label>Label:</label>
              <select
                value={option.label}
                onChange={(e) => handleChange(e, index, "label")}
              >
                <option value="correct">Correct</option>
                <option value="incorrect">Incorrect</option>
              </select>
            </div>
          </div>
        ))}
        <button type="submit">Save</button>
      </form>
      <div>
        <br />
        <div onClick={() => navigate(-1)}>Cancel</div>
        <br />
        <Link to="/admin/landing">Landing Page</Link>
      </div>
    </div>
  );
};

export default AdminModifyActivityQuestion;
