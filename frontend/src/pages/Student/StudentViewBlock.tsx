import axios from "axios";
import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";

type BlockDetails = {
  block_id: string;
  block_type: string;
};

type ActivityDetails = {
  question_id: string;
  question_text: string;
  option_1: string;
  opt_1_explaination: string;
  option_2: string;
  opt_2_explaination: string;
  option_3: string;
  opt_3_explaination: string;
  option_4: string;
  opt_4_explaination: string;
  answer: number;
};

type SelectedAnswer = {
    [key: string]: number; // key is question_id, value is selected option number
  };
  
  type Explanation = {
    [key: string]: string; // key is question_id, value is explanation text
  };

const TextPicBlock = ({ block }: { block: BlockDetails }) => {
  const [content, setContent] = useState("");

  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);

  const tb_id = queryParams.get("tb_id");
  const chap_id = queryParams.get("chap_id");
  const sec_id = queryParams.get("sec_id");

  const fetchContentBlock = async () => {
    try {
      const response = await axios.get(
        `http://localhost:8000/student/view_content?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}&block_id=${block.block_id}`
      );
      if (response.status === 200) {
        setContent(response.data.content);
      }
    } catch (error) {
      console.error("Error fetching section details:", error);
    }
  };

  useEffect(() => {
    // Fetch the block details
    fetchContentBlock();
  }, []);

  return <>{content && content}</>;
};

const ActivityBlock = ({ block }: { block: BlockDetails }) => {
  const [activity, setActivity] = useState<ActivityDetails[]>([]);
  const [selectedAnswers, setSelectedAnswers] = useState<SelectedAnswer>({});
  const [explanations, setExplanations] = useState<Explanation>({});
  const [disabledQuestions, setDisabledQuestions] = useState<{
    [key: string]: boolean;
  }>({});

  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);

  const tb_id = queryParams.get("tb_id");
  const chap_id = queryParams.get("chap_id");
  const sec_id = queryParams.get("sec_id");

  const fetchActivityBlock = async () => {
    try {
      const response = await axios.get(
        `http://localhost:8000/student/view_content`,
        {
          params: {
            tb_id,
            chap_id,
            sec_id,
            block_id: block.block_id,
          },
        }
      );
      if (response.status === 200) {
        setActivity(response.data.content);
      }
    } catch (error) {
      console.error("Error fetching section details:", error);
    }
  };

  useEffect(() => {
    fetchActivityBlock();
  }, [tb_id, chap_id, sec_id, block.block_id]);

  const handleOptionChange = async (
    questionId: string,
    selectedOption: number
  ) => {
    // Prevent multiple selections
    if (disabledQuestions[questionId]) return;

    // Update selected answers
    setSelectedAnswers((prev) => ({ ...prev, [questionId]: selectedOption }));

    // Disable the question to prevent changes
    setDisabledQuestions((prev) => ({ ...prev, [questionId]: true }));

    try {
      const response = await axios.post(
        `http://localhost:8000/student/submit_answer`,
        {
          tb_id,
          chap_id,
          sec_id,
          block_id: block.block_id,
          question_id: questionId,
          selected_option: selectedOption,
        }
      );

      if (response.status === 200) {
        const data = response.data;

        // Assuming the API returns whether the answer was correct and the explanation
        if (data.correct) {
          // Handle correct answer case
          console.log("Correct answer selected.");
        } else {
          console.log("Incorrect answer selected.");
        }

        // Set the explanation based on the selected option
        const question = activity.find((q) => q.question_id === questionId);
        if (question) {
          let explanation = "";
          switch (selectedOption) {
            case 1:
              explanation = question.opt_1_explaination;
              break;
            case 2:
              explanation = question.opt_2_explaination;
              break;
            case 3:
              explanation = question.opt_3_explaination;
              break;
            case 4:
              explanation = question.opt_4_explaination;
              break;
            default:
              explanation = "";
          }
          setExplanations((prev) => ({ ...prev, [questionId]: explanation }));
        }
      }
    } catch (error) {
      console.error("Error submitting answer:", error);
      // Optionally, re-enable the question if there's an error
      setDisabledQuestions((prev) => ({ ...prev, [questionId]: false }));
    }
  };

  return (
    <>
      {activity && activity.length > 0 && (
        <div>
          <h1>Activity</h1>
          <div>
            {activity.map((act) => (
              <div key={act.question_id} style={{ marginBottom: "20px" }}>
                <h2>{act.question_text}</h2>
                <div>
                  <input
                    type="radio"
                    value="1"
                    name={act.question_id}
                    disabled={disabledQuestions[act.question_id]}
                    checked={selectedAnswers[act.question_id] === 1}
                    onChange={() => handleOptionChange(act.question_id, 1)}
                  />
                  <label>{act.option_1}</label>
                </div>
                <div>
                  <input
                    type="radio"
                    value="2"
                    name={act.question_id}
                    disabled={disabledQuestions[act.question_id]}
                    checked={selectedAnswers[act.question_id] === 2}
                    onChange={() => handleOptionChange(act.question_id, 2)}
                  />
                  <label>{act.option_2}</label>
                </div>
                <div>
                  <input
                    type="radio"
                    value="3"
                    name={act.question_id}
                    disabled={disabledQuestions[act.question_id]}
                    checked={selectedAnswers[act.question_id] === 3}
                    onChange={() => handleOptionChange(act.question_id, 3)}
                  />
                  <label>{act.option_3}</label>
                </div>
                <div>
                  <input
                    type="radio"
                    value="4"
                    name={act.question_id}
                    disabled={disabledQuestions[act.question_id]}
                    checked={selectedAnswers[act.question_id] === 4}
                    onChange={() => handleOptionChange(act.question_id, 4)}
                  />
                  <label>{act.option_4}</label>
                </div>
                {/* Display Explanation */}
                {explanations[act.question_id] && (
                  <div
                    style={{
                      marginTop: "10px",
                      padding: "10px",
                      backgroundColor: "#f0f0f0",
                    }}
                  >
                    <strong>Explanation:</strong>{" "}
                    {explanations[act.question_id]}
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      )}
    </>
  );
};

const StudentViewBlock = () => {
  const [contentDetails, setContentDetails] = useState<BlockDetails[]>([]);

  const navigate = useNavigate();
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);

  const tb_id = queryParams.get("tb_id");
  const chap_id = queryParams.get("chap_id");
  const sec_id = queryParams.get("sec_id");

  const fetchBlockDetails = async () => {
    try {
      const response = await axios.get(
        `http://localhost:8000/fetch_content?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}`
      );
      setContentDetails(response.data.block);
    } catch (error) {
      console.error("Error fetching section details:", error);
    }
  };

  useEffect(() => {
    if (!tb_id || !chap_id || !sec_id) {
      return;
    }
    fetchBlockDetails();
  }, [tb_id, chap_id, sec_id]);

  return (
    <div>
      <h1>Details</h1>
      {contentDetails.map((block) => {
        switch (block.block_type) {
          case "text":
            return <TextPicBlock key={block.block_id} block={block} />;
          case "picture":
            return <TextPicBlock key={block.block_id} block={block} />;
          case "activity":
            return <ActivityBlock key={block.block_id} block={block} />;
          default:
            return null;
        }
      })}
    </div>
  );
};

export default StudentViewBlock;
