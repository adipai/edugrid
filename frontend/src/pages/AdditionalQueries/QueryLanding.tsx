import React from "react";
import { Link } from "react-router-dom";

const QueryLanding: React.FC = () => {
  return (
    <div>
      <h1>Additional Queries</h1>

      <div>
          <Link to="/queries/sections-of-first-chapter">
            1. Write a query that prints the number of sections of the first chapter of a textbook.
          </Link>
      </div>

      <div>
          <Link to="/queries/faculty-and-tas">
            2. Print the names of faculty and TAs of all courses. For each person print their role next to their
            names.
          </Link>
      </div>

      <div>
          <Link to="/queries/active-courses">
            3. For each active course, print the course id, faculty member and total number of students
          </Link>
      </div>

      <div>
          <Link to="/queries/largest-waiting-list">
            4. Find the course which the largest waiting list, print the course id and the total number of
            people on the list
          </Link>
      </div>

      <div>
          <Link to="/queries/chapter-02-contents">
            5. Print the contents of Chapter 02 of textbook 101 in proper sequence.
          </Link>
      </div>

      <div>
          <Link to="/queries/activity0-q2-incorrect-answers">
            6. For Q2 of Activity0, print the incorrect answers for that question and their corresponding
            explanations.
          </Link>
      </div>

      <div>
          <Link to="/queries/book-status">
            7. Find any book that is in active status by one instructor but evaluation status by a different
            instructor.
          </Link>
      </div>
    </div>
  );
};

export default QueryLanding;
