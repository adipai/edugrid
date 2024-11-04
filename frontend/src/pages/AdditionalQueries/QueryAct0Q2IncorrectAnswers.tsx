import axios from "axios";
import React, { useEffect } from "react";

type QueryResult = {
  option_1: string;
  opt_1_explanation: string;
  option_2: string;
  opt_2_explanation: string;
  option_3: string;
  opt_3_explanation: string;
  option_4: string;
  opt_4_explanation: string;
};

type ViewQueryShape = {
  option: string;
  explanation: string;
};

const QueryAct0Q2IncorrectAnswers: React.FC = () => {
  const [queryResult, setQueryResult] = React.useState<QueryResult[]>([]);
  const [display, setDisplay] = React.useState<ViewQueryShape[]>([]);

  const [textbookId, setTextbookId] = React.useState("");
  const [chapterId, setChapterId] = React.useState("");
  const [sectionId, setSectionId] = React.useState("");
  const [blockId, setBlockId] = React.useState("");

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      const response = await axios.post(
        "http://localhost:8000/incorrect_answers",
        {
          textbook_id: textbookId,
          chapter_id: chapterId,
          section_id: sectionId,
          block_id: blockId,
        }
      );
      setQueryResult(response.data.incorrect_answers);
    } catch (error) {
      console.error("Error creating block:", error);
    }
  };

  useEffect(() => {
    const viewQueryResult: ViewQueryShape[] = queryResult
      .map((result) => [
        { option: result.option_1, explanation: result.opt_1_explanation },
        { option: result.option_2, explanation: result.opt_2_explanation },
        { option: result.option_3, explanation: result.opt_3_explanation },
        { option: result.option_4, explanation: result.opt_4_explanation },
      ])
      .flat();
    console.log(viewQueryResult);
    setDisplay(viewQueryResult);
  }, [queryResult]);

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="addtb">Textbook ID:</label>
          <input
            type="text"
            id="addtb"
            value={textbookId}
            onChange={(e) => setTextbookId(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="addchap">Chapter ID:</label>
          <input
            type="text"
            id="addchap"
            value={chapterId}
            onChange={(e) => setChapterId(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="addchap">Section ID:</label>
          <input
            type="text"
            id="addchap"
            value={sectionId}
            onChange={(e) => setSectionId(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="addchap">Block ID:</label>
          <input
            type="text"
            id="addchap"
            value={sectionId}
            onChange={(e) => setBlockId(e.target.value)}
            required
          />
        </div>
        <button type="submit">Submit</button>
      </form>
      {display.length > 0 && (
        <table style={{ borderCollapse: "collapse", width: "100%" }}>
          <thead>
            <tr>
              <th style={{ border: "1px solid black", padding: "8px" }}>
                Option
              </th>
              <th style={{ border: "1px solid black", padding: "8px" }}>
                Explanation
              </th>
            </tr>
          </thead>
          <tbody>
            {display.map((item, index) => (
              <tr key={index}>
                <td style={{ border: "1px solid black", padding: "8px" }}>
                  {item.option}
                </td>
                <td style={{ border: "1px solid black", padding: "8px" }}>
                  {item.explanation}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default QueryAct0Q2IncorrectAnswers;
