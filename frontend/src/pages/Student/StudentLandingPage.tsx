import axios from "axios";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

type CourseData = {
  course_id: string;
  textbook_id: number;
};

type HierarcyTextbook = {
  tb_id: number;
  textbook_name: string;
  chapters: HierarcyChapter[];
};

type HierarcyChapter = {
  chapter_id: string;
  chapter_name: string;
  sections: HierarcySection[];
};

type HierarcySection = {
  section_id: string;
  section_name: string;
  blocks: HierarcyBlock[];
};

type HierarcyBlock = {
  block_id: string;
  block_name: string;
};

const CourseHierarchyView = (props: any) => {
  const { tb_id, course_id } = props;

  const [courseHierarchy, setCourseHierarchy] = useState<HierarcyTextbook[]>(
    []
  );

  const fetchCourseHierarchy = async (textbook_id: number) => {
    try {
      const response = await axios.get(
        `http://localhost:8000/display_textbook?tb_id=${textbook_id}`
      );
      setCourseHierarchy(response.data);
    } catch (error) {
      console.error("Error fetching chapter details:", error);
    }
  };

  useEffect(() => {
    fetchCourseHierarchy(tb_id);
  }, [tb_id]);

  return (
    <div>
      {courseHierarchy &&
        courseHierarchy.map((textbook, i) => (
          <div key={`${textbook.tb_id}-${i}`} style={{ paddingLeft: "8px" }}>
            <h2 className="zero-spaces" style={{ padding: "2px" }}>
              {textbook.textbook_name}
            </h2>
            {textbook.chapters.map((chapter, i) => (
              <div
                key={`${chapter.chapter_id}-${i}`}
                style={{ paddingLeft: "8px" }}
              >
                <h3 className="zero-spaces" style={{ padding: "2px" }}>
                  {i + 1}. {chapter.chapter_name}
                </h3>
                {chapter.sections.map((section, j) => (
                  <div
                    key={`${section.section_id}-${j}`}
                    style={{ paddingLeft: "8px" }}
                  >
                    <h4 className="zero-spaces" style={{ padding: "2px" }}>
                      {`${i + 1}.${j + 1}`} {section.section_name}
                    </h4>
                    {section.blocks.map((block, k) => (
                      <div
                        key={`${block.block_id}-${k}`}
                        style={{ paddingLeft: "8px" }}
                      >
                        <Link
                          className="zero-spaces"
                          style={{ padding: "2px" }}
                          to={`/student/view-section?course_id=${course_id}&tb_id=${textbook.tb_id}&chap_id=${chapter.chapter_id}&sec_id=${section.section_id}`}
                        >
                          {block.block_id}
                        </Link>
                      </div>
                    ))}
                  </div>
                ))}
              </div>
            ))}
          </div>
        ))}
    </div>
  );
};

const StudentLandingPage = () => {
  const user_id = localStorage.getItem("user_id");
  const [courseData, setCourseData] = useState<CourseData[]>([]);

  const fetchCourcesDetails = async () => {
    try {
      const response = await axios.get(
        `http://localhost:8000/api/v1/student-courses?student_id=${user_id}`
      );
      setCourseData(response.data.courses);
    } catch (error) {
      console.error("Error fetching chapter details:", error);
    }
  };

  useEffect(() => {
    fetchCourcesDetails();
  }, []);

  // useEffect(() => {}, [courseData]);

  return (
    <div>
      <h1>Student Dashboard</h1>
      {courseData &&
        courseData.map((course, i) => (
          <div key={`${course.course_id}-${course.textbook_id}-${i}`}>
            <CourseHierarchyView tb_id={course.textbook_id} />
          </div>
        ))}
      <ul>
        <li>
          <Link to="/student/view-section">1. View a Section</Link>
        </li>
        <li>
          <Link to="/student/participation">
            2. View Pariticipation Acitivity Point
          </Link>
        </li>
        <li>
          <Link to="/">3. Logout</Link>
        </li>
      </ul>
    </div>
  );
};

export default StudentLandingPage;
