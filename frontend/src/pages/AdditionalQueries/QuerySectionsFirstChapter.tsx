import axios from "axios";
import React, { useEffect, useState } from "react";

type QueryResult = {};

const QuerySectionsFirstChapter: React.FC = () => {
  // /sections_in_first_chapter
  const [queryResult, setQueryResult] = useState<any>(null);
  const [text, setText] = useState("");


  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
        const response = await axios.post("http://localhost:8000/sections_in_first_chapter", {
          textbook_id: text,
        });
        setQueryResult(response.data.number_of_sections);
      } catch (error) {
        console.error("Error creating block:", error);
      }
  };

  return (
    <>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="addText">Textbook ID:</label>
          <input
            type="text"
            id="addText"
            value={text}
            onChange={(e) => setText(e.target.value)}
            required
          />
        </div>
        <button type="submit">Add</button>
      </form>
      {queryResult && <p>The textbook {text} has <span>{JSON.stringify(queryResult)}</span> sections in first chapter</p>}
    </>
  );
};

export default QuerySectionsFirstChapter;
