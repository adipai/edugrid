import { useEffect, useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import { TextPicBlock, ActivityBlock } from "./StudentViewSection";

const StudentViewBlock = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);

  const course_id = queryParams.get("course_id");
  const chap_num = queryParams.get("chap_num");
  const sec_num = queryParams.get("sec_num");
  const block_num: number | null = parseInt(queryParams.get("block_num") as string) || null;

  const [courseId, setCourseId] = useState("");
  const [chapterNumber, setChapterNumber] = useState("");
  const [secNumber, setSectionNumber] = useState("");
  const [blockNum, setBlockNum] = useState("");

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
    if (!courseData || !block_num) {
      return;
    }
    console.log(courseData)
    if (`${course_id}-${chap_num}-${sec_num}-${block_num}` in courseData) {
    setBlockData(
      courseData[`${course_id}-${chap_num}-${sec_num}-${block_num}`]?.split("-")
    );
  }
  else{
    console.error("Should navigate");
    navigate('/student/landing')
  }
  }, [courseData, block_num]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log(courseId, chapterNumber, secNumber);
    setCourseId("");
    setChapterNumber("");
    setSectionNumber("");
    setBlockNum("");
    navigate(
      `/student/view-block?course_id=${courseId}&chap_num=${chapterNumber}&sec_num=${secNumber}&block_num=${blockNum}`
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
              value={blockNum}
              onChange={(e) => setBlockNum(e.target.value)}
              required
            />
          </div>
          <button type="submit">Submit</button>
        </form>
      )}
      {blockData && blockData[5] === "text" && (
        <TextPicBlock
          block={{ block_id: blockData[4], block_type: blockData[5] }}
          tb_id={blockData[1]}
          chap_id={blockData[2]}
          sec_id={blockData[3]}
        />
      )}
      {blockData && blockData[5] === "picture" && (
        <TextPicBlock
          block={{ block_id: blockData[4], block_type: blockData[5] }}
          tb_id={blockData[1]}
          chap_id={blockData[2]}
          sec_id={blockData[3]}
        />
      )}
      {blockData && blockData[5] === "activity" && (
        <ActivityBlock
          block={{ block_id: blockData[4], block_type: blockData[5] }}
          tb_id={blockData[1]}
          chap_id={blockData[2]}
          sec_id={blockData[3]}
          course_id={course_id || ""}
        />
      )}

      <div>
        <Link to={`/student/view-block?course_id=${course_id}&chap_num=${chap_num}&sec_num=${sec_num}&block_num=${(block_num || 0)+ 1}`}>Next</Link>
      </div>
      <div>
        <div style={{"margin":"4px"}} onClick={() => navigate(-1)}>Go Back</div>
      </div>
    </div>
  );
};

export default StudentViewBlock;
