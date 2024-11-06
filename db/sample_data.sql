
-- Delete all existing data
DELETE FROM participation;
DELETE FROM question;
DELETE FROM activity;
DELETE FROM block;
DELETE FROM section;
DELETE FROM chapter;
DELETE FROM enrollment;
DELETE FROM teaching_assistant;
DELETE FROM faculty;
DELETE FROM student;
DELETE FROM course;
DELETE FROM textbook;
DELETE FROM notification;
DELETE FROM user;


-- Start populating tables in order (parent tables first)

-- Insert users (includes all types of users)
INSERT INTO user (user_id, first_name, last_name, email, password, role) VALUES
('admin000', 'Admin', 'Boss', 'bossman@gmail.com', 'test', 'admin'),
('ErPe1024', 'Eric', 'Perrig', 'ez356@example.mail', 'qwdmq', 'student'),
('AlAr1024', 'Alice', 'Artho', 'aa23@edu.mail', 'omdsws', 'student'),
('BoTe1024', 'Bob', 'Temple', 'bt163@template.mail', 'sak+=', 'student'),
('LiGa1024', 'Lily', 'Gaddy', 'li123@example.edu', 'cnaos', 'student'),
('ArMo1024', 'Aria', 'Morrow', 'am213@example.edu', 'jwocals', 'student'),
('KeRh1014', 'Kellan', 'Rhodes', 'kr21@example.edu', 'camome', 'student'),
('SiHa1024', 'Sienna', 'Hayes', 'sh13@example.edu', 'asdqm', 'student'),
('FiWi1024', 'Finn', 'Wilder', 'fw23@example.edu', 'f13mas', 'student'),
('LeMe1024', 'Leona', 'Mercer', 'lm56@example.edu', 'ca32', 'student'),
('KeOg1024', 'Kemafor', 'Ogan', 'kogan@ncsu.edu', 'Ko2024!rpc', 'faculty'),
('JoDo1024', 'John', 'Doe', 'john.doe@example.com', 'Jd2024!abc', 'faculty'),
('SaMi1024', 'Sarah', 'Miller', 'sarah.miller@domain.com', 'Sm#Secure2024', 'faculty'),
('DaBr1024', 'David', 'Brown', 'david.b@webmail.com', 'DbPass123!', 'faculty'),
('EmDa1024', 'Emily', 'Davis', 'emily.davis@email.com', 'Emily#2024!', 'faculty'),
('MiWi1024', 'Michael', 'Wilson', 'michael.w@service.com', 'Mw987secure', 'faculty'),
('JaWi1024', 'James', 'Williams', 'jwilliams@ncsu.edu', 'jwilliams@1234', 'teaching assistant'),
('LiAl0924', 'Lisa', 'Alberti', 'lalberti@ncsu.edu', 'lalberti&5678@', 'teaching assistant'),
('DaJo1024', 'David', 'Johnson', 'djohnson@ncsu.edu', 'djohnson%@1122', 'teaching assistant'),
('ElCl1024', 'Ellie', 'Clark', 'eclark@ncsu.edu', 'eclark^#3654', 'teaching assistant'),
('JeGi0924', 'Jeff', 'Gibson', 'jgibson@ncsu.edu', 'jgibson$#9877', 'teaching assistant');

-- Insert students
INSERT INTO student (student_id, full_name, password, email) VALUES
('ErPe1024', 'Eric Perrig', 'qwdmq', 'ez356@example.mail'),
('AlAr1024', 'Alice Artho', 'omdsws', 'aa23@edu.mail'),
('BoTe1024', 'Bob Temple', 'sak+=', 'bt163@template.mail'),
('LiGa1024', 'Lily Gaddy', 'cnaos', 'li123@example.edu'),
('ArMo1024', 'Aria Morrow', 'jwocals', 'am213@example.edu'),
('KeRh1014', 'Kellan Rhodes', 'camome', 'kr21@example.edu'),
('SiHa1024', 'Sienna Hayes', 'asdqm', 'sh13@example.edu'),
('FiWi1024', 'Finn Wilder', 'f13mas', 'fw23@example.edu'),
('LeMe1024', 'Leona Mercer', 'ca32', 'lm56@example.edu');

-- Insert faculty
INSERT INTO faculty (faculty_id, first_name, last_name, email, password) VALUES
('KeOg1024', 'Kemafor', 'Ogan', 'kogan@ncsu.edu', 'Ko2024!rpc'),
('JoDo1024', 'John', 'Doe', 'john.doe@example.com', 'Jd2024!abc'),
('SaMi1024', 'Sarah', 'Miller', 'sarah.miller@domain.com', 'Sm#Secure2024'),
('DaBr1024', 'David', 'Brown', 'david.b@webmail.com', 'DbPass123!'),
('EmDa1024', 'Emily', 'Davis', 'emily.davis@email.com', 'Emily#2024!'),
('MiWi1024', 'Michael', 'Wilson', 'michael.w@service.com', 'Mw987secure');

-- Insert teaching assistants
INSERT INTO teaching_assistant (ta_id, first_name, last_name, email, password, course_id) VALUES
('JaWi1024', 'James', 'Williams', 'jwilliams@ncsu.edu', 'jwilliams@1234', 'NCSUOganCSC440F24'),
('LiAl0924', 'Lisa', 'Alberti', 'lalberti@ncsu.edu', 'lalberti&5678@', 'NCSUOganCSC540F24'),
('DaJo1024', 'David', 'Johnson', 'djohnson@ncsu.edu', 'djohnson%@1122', 'NCSUSaraCSC326F24'),
('ElCl1024', 'Ellie', 'Clark', 'eclark@ncsu.edu', 'eclark^#3654', NULL),
('JeGi0924', 'Jeff', 'Gibson', 'jgibson@ncsu.edu', 'jgibson$#9877', NULL);

-- Insert textbooks
INSERT INTO textbook (textbook_id, title, created_by) VALUES
(101, 'Database Management Systems', 'admin000'),
(102, 'Fundamentals of Software Engineering', 'admin000'),
(103, 'Fundamentals of Machine Learning', 'admin000');

-- Insert courses
INSERT INTO course (course_id, course_name, textbook_id, course_type, faculty_id, start_date, end_date, unique_token, capacity) VALUES
('NCSUOganCSC440F24', 'CSC440 Database Systems', 101, 'Active', 'KeOg1024', '2024-08-15', '2024-12-15', 'XYJKLM', 60),
('NCSUOganCSC540F24', 'CSC540 Database Systems', 101, 'Active', 'KeOg1024', '2024-08-17', '2024-12-15', 'STUKZT', 50),
('NCSUSaraCSC326F24', 'CSC326 Software Engineering', 102, 'Active', 'SaMi1024', '2024-08-23', '2024-10-23', 'LRUFND', 100),
('NCSUDoeCSC522F24', 'CSC522 Fundamentals of Machine Learning', 103, 'Evaluation', 'JoDo1024', '2025-08-25', '2025-12-18', NULL, NULL),
('NCSUSaraCSC326F25', 'CSC326 Software Engineering', 102, 'Evaluation', 'SaMi1024', '2025-08-27', '2025-12-19', NULL, NULL);

-- Insert chapters
INSERT INTO chapter (textbook_id, chapter_id, title, hidden_status, created_by) VALUES
(101, 'chap01', 'introduction to Database', 'no', 'admin000'),
(101, 'chap02', 'The Relational Model', 'no', 'admin000'),
(102, 'chap01', 'introduction to Software Engineering', 'no', 'admin000'),
(102, 'chap02', 'introduction to Software Development Life Cycle (SDLC)', 'no', 'admin000'),
(103, 'chap01', 'Introduction to Machine Learning', 'no', 'admin000');

-- Insert sections
INSERT INTO section (textbook_id, chapter_id, section_id, title, hidden_status, created_by) VALUES
(101, 'chap01', 'Sec01', 'Database Management Systems (DBMS) Overview', 'no', 'admin000'),
(101, 'chap01', 'Sec02', 'Data Models and Schemas', 'no', 'admin000'),
(101, 'chap02', 'Sec01', 'Entities, Attributes, and Relationships', 'no', 'admin000'),
(101, 'chap02', 'Sec02', 'Normalization and Integrity Constraints', 'no', 'admin000'),
(102, 'chap01', 'Sec01', 'History and Evolution of Software Engineering', 'no', 'admin000'),
(102, 'chap01', 'Sec02', 'Key Principles of Software Engineering', 'no', 'admin000'),
(102, 'chap02', 'Sec01', 'Phases of the SDLC', 'yes', 'admin000'),
(102, 'chap02', 'Sec02', 'Agile vs. Waterfall Models', 'no', 'admin000'),
(103, 'chap01', 'Sec01', 'Overview of Machine Learning', 'yes', 'admin000'),
(103, 'chap01', 'Sec02', 'Supervised vs Unsupervised Learning', 'no', 'admin000');

-- Insert blocks
INSERT INTO block (textbook_id, chapter_id, section_id, block_id, block_type, content, hidden_status, created_by) VALUES
(101, 'chap01', 'Sec01', 'Block01', 'text', 'A Database Management System (DBMS) is software that enables users to efficiently create, manage, and manipulate databases. It serves as an interface between the database and end users, ensuring data is stored securely, retrieved accurately, and maintained consistently. Key features of a DBMS include data organization, transaction management, and support for multiple users accessing data concurrently.', 'no', 'admin000'),
(101, 'chap01', 'Sec02', 'Block01', 'activity', 'ACT0', 'no', 'admin000'),
(101, 'chap02', 'Sec01', 'Block01', 'text', 'DBMS systems provide structured storage and ensure that data is accessible through queries using languages like SQL. They handle critical tasks such as maintaining data integrity, enforcing security protocols, and optimizing data retrieval, making them essential for both small-scale and enterprise-level applications. Examples of popular DBMS include MySQL, Oracle, and PostgreSQL.', 'no', 'admin000'),
(101, 'chap02', 'Sec02', 'Block01', 'picture', 'sample.png', 'no', 'admin000'),
(102, 'chap01', 'Sec01', 'Block01', 'text', 'The history of software engineering dates back to the 1960s, when the "software crisis" highlighted the need for structured approaches to software development due to rising complexity and project failures. Over time, methodologies such as Waterfall, Agile, and DevOps evolved, transforming software engineering into a disciplined, iterative process that emphasizes efficiency, collaboration, and adaptability.', 'no', 'admin000'),
(102, 'chap01', 'Sec02', 'Block01', 'activity', 'ACT0', 'no', 'admin000'),
(102, 'chap02', 'Sec01', 'Block01', 'text', 'The Software Development Life Cycle (SDLC) consists of key phases including requirements gathering, design, development, testing, deployment, and maintenance. Each phase plays a crucial role in ensuring that software is built systematically, with feedback and revisions incorporated at each step to deliver a high-quality product.', 'no', 'admin000'),
(102, 'chap02', 'Sec02', 'Block01', 'picture', 'sample2.png', 'no', 'admin000'),
(103, 'chap01', 'Sec01', 'Block01', 'text', 'Machine learning is a subset of artificial intelligence that enables systems to learn from data, identify patterns, and make decisions with minimal human intervention. By training algorithms on vast datasets, machine learning models can improve their accuracy over time, driving advancements in fields like healthcare, finance, and autonomous systems.', 'no', 'admin000'),
(103, 'chap01', 'Sec02', 'Block01', 'activity', 'ACT0', 'no', 'admin000');

-- Insert activities
INSERT INTO activity (textbook_id, chapter_id, section_id, block_id, unique_activity_id, hidden_status, created_by) VALUES
(101, 'chap01', 'Sec02', 'Block01', 'ACT0', 'no', 'admin000'),
(102, 'chap01', 'Sec02', 'Block01', 'ACT0', 'no', 'admin000'),
(103, 'chap01', 'Sec02', 'Block01', 'ACT0', 'no', 'admin000');

-- Notifications
INSERT INTO notification (user_id, notification_message) VALUES
('ErPe1024', 'Welcome to CSC440 Database Systems!'),
('AlAr1024', 'You have been enrolled in CSC440'),
('BoTe1024', 'New activity available in Database Systems chapter 1'),
('LiGa1024', 'Welcome to CSC440 and CSC540'),
('FiWi1024', 'Your enrollment request for CSC440 is pending');


-- Questions (based on the provided question data)
INSERT INTO question (textbook_id, chapter_id, section_id, block_id, unique_activity_id, question_id, question_text, option_1, opt_1_explanation, option_2, opt_2_explanation, option_3, opt_3_explanation, option_4, opt_4_explanation, answer) VALUES
(101, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q1', 'What does a DBMS provide?', 'Data storage only', 'Incorrect: DBMS provides more than just storage', 'Data storage and retrieval', 'Correct: DBMS manages both storing and retrieving data', 'Only security features', 'Incorrect: DBMS also handles other functions', 'Network management', 'Incorrect: DBMS does not manage network infrastructure', 2),
(101, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q2', 'Which of these is an example of a DBMS?', 'Microsoft Excel', 'Incorrect: Excel is a spreadsheet application', 'MySQL', 'Correct: MySQL is a popular DBMS', 'Google Chrome', 'Incorrect: Chrome is a web browser', 'Windows 10', 'Incorrect: Windows is an operating system', 2),
(101, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q3', 'What type of data does a DBMS manage?', 'Structured data', 'Correct: DBMS primarily manages structured data', 'Unstructured multimedia', 'Incorrect: While some DBMS systems can handle it, it''s not core', 'Network traffic data', 'Incorrect: DBMS doesn''t manage network data', 'Hardware usage statistics', 'Incorrect: DBMS does not handle hardware usage data', 1),
(102, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q1', 'What was the "software crisis"?', 'A hardware shortage', 'Incorrect: The crisis was related to software development issues', 'Difficulty in software creation', 'Correct: The crisis was due to the complexity and unreliability of software', 'A network issue', 'Incorrect: It was not related to networking', 'Lack of storage devices', 'Incorrect: The crisis was not about physical storage limitations', 2),
(102, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q2', 'Which methodology was first introduced in software engineering?', 'Waterfall model', 'Correct: Waterfall was the first formal software development model', 'Agile methodology', 'Incorrect: Agile was introduced much later', 'DevOps', 'Incorrect: DevOps is a more recent development approach', 'Scrum', 'Incorrect: Scrum is a part of Agile, not the first methodology', 1),
(102, 'chap01', 'Sec02', 'Block01', 'ACT0', 'Q3', 'What challenge did early software engineering face?', 'Lack of programming languages', 'Incorrect: Programming languages existed but were difficult to manage', 'Increasing complexity of software', 'Correct: Early engineers struggled with managing large, complex systems', 'Poor hardware development', 'Incorrect: The issue was primarily with software, not hardware', 'Internet connectivity issues', 'Incorrect: Internet connectivity wasn''t a challenge in early software', 2);


-- Enrollments (based on the waitlists data)
INSERT INTO enrollment (unique_course_id, student_id, status) VALUES
('NCSUOganCSC440F24', 'ErPe1024', 'Enrolled'),
('NCSUOganCSC540F24', 'ErPe1024', 'Enrolled'),
('NCSUOganCSC440F24', 'AlAr1024', 'Enrolled'),
('NCSUOganCSC440F24', 'BoTe1024', 'Enrolled'),
('NCSUOganCSC440F24', 'LiGa1024', 'Enrolled'),
('NCSUOganCSC540F24', 'LiGa1024', 'Enrolled'),
('NCSUOganCSC540F24', 'ArMo1024', 'Enrolled'),
('NCSUOganCSC440F24', 'ArMo1024', 'Enrolled'),
('NCSUOganCSC440F24', 'SiHa1024', 'Enrolled'),
('NCSUSaraCSC326F24', 'FiWi1024', 'Enrolled'),
('NCSUOganCSC440F24', 'LeMe1024', 'Enrolled'),
('NCSUOganCSC440F24', 'FiWi1024', 'Pending'),
('NCSUOganCSC540F24', 'LeMe1024', 'Pending'),
('NCSUOganCSC540F24', 'AlAr1024', 'Pending'),
('NCSUOganCSC540F24', 'SiHa1024', 'Pending'),
('NCSUOganCSC540F24', 'FiWi1024', 'Pending');

-- Participations (based on the provided student participation data)
INSERT INTO participation (student_id, course_id, textbook_id, section_id, chapter_id, block_id, unique_activity_id, question_id, point, attempted_timestamp) VALUES
('ErPe1024', 'NCSUOganCSC440F24', 101, 'Sec02', 'chap01', 'Block01', 'ACT0', 'Q1', 3, '2024-08-01 11:10:00'),
('ErPe1024', 'NCSUOganCSC440F24', 101, 'Sec02', 'chap01', 'Block01', 'ACT0', 'Q2', 1, '2024-08-01 14:18:00'),
('ErPe1024', 'NCSUOganCSC540F24', 101, 'Sec02', 'chap01', 'Block01', 'ACT0', 'Q1', 1, '2024-08-02 19:06:00'),
('AlAr1024', 'NCSUOganCSC440F24', 101, 'Sec02', 'chap01', 'Block01', 'ACT0', 'Q1', 3, '2024-08-01 13:24:00'),
('BoTe1024', 'NCSUOganCSC440F24', 101, 'Sec02', 'chap01', 'Block01', 'ACT0', 'Q1', 0, '2024-08-01 09:24:00'),
('LiGa1024', 'NCSUOganCSC440F24', 101, 'Sec02', 'chap01', 'Block01', 'ACT0', 'Q1', 3, '2024-08-01 07:45:00'),
('LiGa1024', 'NCSUOganCSC440F24', 101, 'Sec02', 'chap01', 'Block01', 'ACT0', 'Q2', 3, '2024-08-01 12:30:00'),
('LiGa1024', 'NCSUOganCSC540F24', 101, 'Sec02', 'chap01', 'Block01', 'ACT0', 'Q1', 3, '2024-08-03 16:52:00'),
('ArMo1024', 'NCSUOganCSC440F24', 101, 'Sec02', 'chap01', 'Block01', 'ACT0', 'Q1', 1, '2024-08-01 21:18:00'),
('ArMo1024', 'NCSUOganCSC440F24', 101, 'Sec02', 'chap01', 'Block01', 'ACT0', 'Q2', 3, '2024-08-01 05:03:00'),
('FiWi1024', 'NCSUSaraCSC326F24', 102, 'Sec02', 'chap01', 'Block01', 'ACT0', 'Q1', 1, '2024-08-29 22:41:00');
