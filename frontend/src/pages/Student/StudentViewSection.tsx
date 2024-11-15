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
  opt_1_explanation: string;
  option_2: string;
  opt_2_explanation: string;
  option_3: string;
  opt_3_explanation: string;
  option_4: string;
  opt_4_explanation: string;
  answer: number;
};

type SelectedAnswer = {
  [key: string]: number; // key is question_id, value is selected option number
};

type Explanation = {
  [key: string]: string; // key is question_id, value is explanation text
};

const TextPicBlock = (props: {
  block: BlockDetails;
  tb_id: string;
  chap_id: string;
  sec_id: string;
}) => {
  const { block, tb_id, chap_id, sec_id } = props;

  const [content, setContent] = useState("");

  // const location = useLocation();
  // const queryParams = new URLSearchParams(location.search);

  // const tb_id = queryParams.get("tb_id");
  // const chap_id = queryParams.get("chap_id");
  // const sec_id = queryParams.get("sec_id");

  const fetchContentBlock = async () => {
    try {
      const response = await axios.get(
        `http://localhost:8000/student/view_content?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}&block_id=${block.block_id}`
      );
      if (response.status === 200) {
        setContent(response.data.content.content);
      }
    } catch (error) {
      console.error("Error fetching section details:", error);
    }
  };

  useEffect(() => {
    // Fetch the block details
    fetchContentBlock();
  }, []);

  return <div key={content}>{content && content}</div>;
};

const ActivityBlock = (props: {
  block: BlockDetails;
  tb_id: string;
  chap_id: string;
  sec_id: string;
  course_id: string;
}) => {
  const { block, tb_id, chap_id, sec_id, course_id } = props;

  const [activity, setActivity] = useState<ActivityDetails[]>([]);
  const [activityId, setActivityId] = useState<string>("");
  const [selectedAnswers, setSelectedAnswers] = useState<SelectedAnswer>({});
  const [explanations, setExplanations] = useState<Explanation>({});
  const [status, setStatus] = useState<{ [key: string]: string }>({});

  // const location = useLocation();
  // const queryParams = new URLSearchParams(location.search);

  // const course_id = queryParams.get("course_id");
  // const tb_id = queryParams.get("tb_id");
  // const chap_id = queryParams.get("chap_id");
  // const sec_id = queryParams.get("sec_id");

  const user_id = localStorage.getItem("user_id");

  const fetchActivityBlock = async () => {
    try {
      const response = await axios.get(
        `http://localhost:8000/student/view_activity_block`,
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
        setActivityId(response.data.activity_id);
        setActivity(response.data.questions);
      }
    } catch (error) {
      console.error("Error fetching section details:", error);
    }
  };

  useEffect(() => {
    fetchActivityBlock();
  }, [tb_id, chap_id, sec_id, block.block_id]);

  const handleOptionChange = (questionId: string, selectedOption: number) => {
    setSelectedAnswers((prev) => ({ ...prev, [questionId]: selectedOption }));
  };

  const handleSubmit = async () => {
    // Loop through each question and submit the answer status
    for (const question of activity) {
      const selectedOption = selectedAnswers[question.question_id];
      const isCorrect = selectedOption === question.answer;
      const feedback = selectedOption
        ? isCorrect
          ? "correct"
          : "incorrect"
        : "unanswered";

      // Determine the explanation text
      let explanation = "";
      if (selectedOption) {
        debugger;
        if (isCorrect) {
          // Correct answer selected, show the correct option's explanation
          const kk = `opt_${selectedOption}_explanation`;
          // @ts-ignore
          const option: any = question[kk];
          explanation = `${option || "Test"}`;
        } else {
          // Incorrect answer selected, show selected option's explanation and correct answer
          explanation = `${
            // @ts-ignore
            question[`opt_${selectedOption}_explanation`] || ""
          }.`;
        }
      } else {
        // No answer selected, show the correct option's explanation
        explanation = `No option selected. The correct answer is Option ${
          question.answer
          // @ts-ignore
        }: ${question[`opt_${question.answer}_explanation`] || ""}`;
      }

      // Update explanations and status
      setExplanations((prev) => ({
        ...prev,
        [question.question_id]: explanation,
      }));
      setStatus((prev) => ({ ...prev, [question.question_id]: feedback }));

      // Call the API
      try {
        const response = await axios.post(
          `http://localhost:8000/api/v1/participation`,
          {
            student_id: user_id,
            course_id,
            textbook_id: tb_id,
            chapter_id: chap_id,
            section_id: sec_id,
            block_id: block.block_id,
            unique_activity_id: activityId,
            question_id: question.question_id,
            correct: feedback,
          }
        );

        if (response.status !== 200) {
          window.alert("An error occurred while submitting your answers.");
        }
      } catch (error) {
        console.error("Error submitting answer:", error);
      }
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
                {/* Display Status */}
                {status[act.question_id] && (
                  <div
                    style={{
                      marginTop: "5px",
                      textTransform: "capitalize",
                      color:
                        status[act.question_id] === "correct"
                          ? "green"
                          : status[act.question_id] === "incorrect"
                          ? "red"
                          : "grey",
                    }}
                  >
                    {status[act.question_id]}
                  </div>
                )}
              </div>
            ))}
            <button onClick={handleSubmit} style={{ marginTop: "20px" }}>
              Submit
            </button>
          </div>
        </div>
      )}
    </>
  );
};

const StudentViewSection = () => {
  const [contentDetails, setContentDetails] = useState<BlockDetails[]>([]);

  const navigate = useNavigate();
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);

  const tb_id = queryParams.get("tb_id");
  const chap_id = queryParams.get("chap_id");
  const sec_id = queryParams.get("sec_id");
  const course_id = queryParams.get("course_id");

  const fetchBlockDetails = async () => {
    try {
      const response = await axios.get(
        `http://localhost:8000/fetch_content?tb_id=${tb_id}&chap_id=${chap_id}&sec_id=${sec_id}`
      );
      setContentDetails(response.data);
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
      <h1>View Section</h1>
      {contentDetails &&
        contentDetails.map((block, i) => {
          switch (block.block_type) {
            case "text":
              return (
                <TextPicBlock
                  key={i}
                  block={block}
                  tb_id={tb_id || ""}
                  sec_id={sec_id || ""}
                  chap_id={chap_id || ""}
                />
              );
            case "picture":
              return (
                <TextPicBlock
                  key={i}
                  block={block}
                  tb_id={tb_id || ""}
                  sec_id={sec_id || ""}
                  chap_id={chap_id || ""}
                />
              );
            case "activity":
              return (
                <ActivityBlock
                  key={i}
                  block={block}
                  tb_id={tb_id || ""}
                  sec_id={sec_id || ""}
                  chap_id={chap_id || ""}
                  course_id={course_id || ""}
                />
              );
            default:
              return <></>;
          }
        })}
    </div>
  );
};

export default StudentViewSection;
export { TextPicBlock, ActivityBlock };
