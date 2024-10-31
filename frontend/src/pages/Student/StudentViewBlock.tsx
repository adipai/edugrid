import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import {TextPicBlock ,ActivityBlock } from "./StudentViewSection";

const StudentViewBlock = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);

  const course_id = queryParams.get("course_id");
  const chap_num = queryParams.get("chap_num");
  const sec_num = queryParams.get("sec_num");
  const block_id = queryParams.get("block_id");

  const [courseId, setCourseId] = useState("");
  const [chapterNumber, setChapterNumber] = useState("");
  const [secNumber, setSectionNumber] = useState("");
  const [blockId, setBlockId] = useState("");

  const [courseData, setCourseData] = useState<any>(null);
  const [blockData, setBlockData] = useState<any>(null);

  useEffect(() => {
    if (!course_id || !chap_num || !sec_num) {
      setCourseData(null);
      return;
    }
    setCourseData(JSON.parse(sessionStorage.getItem(course_id) || ""));
  }, [course_id, chap_num, sec_num]);

  useEffect(() => {
    if (!courseData) {
        return;
    }
    setBlockData(courseData[`${course_id}-${chap_num}-${sec_num}-${block_id}`].split('-'));
  }, [courseData]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log(courseId, chapterNumber, secNumber);
    setCourseId("");
    setChapterNumber("");
    setSectionNumber("");
    setBlockId("");
    navigate(
      `/student/view-block?course_id=${courseId}&chap_num=${chapterNumber}&sec_num=${secNumber}&block_id=${blockId}`
    );
  };

  return (
    <div>
      <h1>Student View Block</h1>
      {!courseData && (
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="course_id">Course ID:</label>
            <input
              type="text"
              id="course_id"
              value={courseId}
              onChange={(e) => setCourseId(e.target.value)}
              required
            />
          </div>
          <div>
            <label htmlFor="chapter_num">Chapter Number:</label>
            <input
              type="text"
              id="chapter_num"
              value={chapterNumber}
              onChange={(e) => setChapterNumber(e.target.value)}
              required
            />
          </div>
          <div>
            <label htmlFor="section_num">Section Number:</label>
            <input
              type="text"
              id="section_num"
              value={secNumber}
              onChange={(e) => setSectionNumber(e.target.value)}
              required
            />
          </div>
          <div>
            <label htmlFor="section_num">Block ID:</label>
            <input
              type="text"
              id="section_num"
              value={blockId}
              onChange={(e) => setBlockId(e.target.value)}
              required
            />
          </div>
          <button type="submit">Submit</button>
        </form>
      )}
      {blockData && blockData[5] === 'text' && <TextPicBlock block={{ block_id: blockData[4], block_type: blockData[5] }} tb_id={blockData[1]} chap_id={blockData[2]} sec_id={blockData[3]} />}
      {blockData && blockData[5] === 'activity' && <ActivityBlock block={{ block_id: blockData[4], block_type: blockData[5] }} tb_id={blockData[1]} chap_id={blockData[2]} sec_id={blockData[3]} course_id={course_id || ""}/>}
    </div>
  );
};

export default StudentViewBlock;
