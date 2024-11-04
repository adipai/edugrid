import axios from "axios";
import React from "react";

const QueryChap2Contents: React.FC = () => {
  const [textbookId, setTextbookId] = React.useState("");
  const [chapterId, setChapterId] = React.useState("");

  const [queryResult, setQueryResult] = React.useState<string[]>([]);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      const response = await axios.post(
        "http://localhost:8000/chapter_contents",
        {
          textbook_id: textbookId,
          chapter_id: chapterId,
        }
      );
      setQueryResult(response.data.chapter_contents);
    } catch (error) {
      console.error("Error creating block:", error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="addtb">Textbook ID:</label>
          <input
            type="text"
            id="addText"
            value={textbookId}
            onChange={(e) => setTextbookId(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="addchapter">Chapter ID:</label>
          <input
            type="text"
            id="addText"
            value={chapterId}
            onChange={(e) => setChapterId(e.target.value)}
            required
          />
        </div>
        <button type="submit">Submit</button>
      </form>
    {queryResult.length > 0 && (
        <table style={{ borderCollapse: "collapse", width: "100%", marginTop: "20px" }}>
            <thead>
                <tr>
                    <th style={{ border: "1px solid black", padding: "8px" }}>Content</th>
                </tr>
            </thead>
            <tbody>
                {queryResult.map((content, index) => (
                    <tr key={index}>
                        <td style={{ border: "1px solid black", padding: "8px" }}>{content}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    )}

    </div>
  );
};

export default QueryChap2Contents;
