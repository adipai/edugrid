

CREATE TABLE IF NOT EXISTS textbook (
  textbook_id int(11) NOT NULL,
  title varchar(255) NOT NULL,
  PRIMARY KEY (textbook_id)
);

CREATE TABLE IF NOT EXISTS chapter (
  textbook_id int(11) NOT NULL,
  chapter_id varchar(20) NOT NULL,
  title varchar(255) NOT NULL,
  hidden_status varchar(3) DEFAULT 'no',
  created_by varchar(100) DEFAULT NULL,
  PRIMARY KEY (textbook_id, chapter_id),
  FOREIGN KEY (textbook_id) REFERENCES textbook(textbook_id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT chk_hidden CHECK (hidden_status IN ('yes', 'no'))
);

CREATE TABLE IF NOT EXISTS section (
    textbook_id int(11) NOT NULL,
    chapter_id varchar(20) NOT NULL,
    section_id varchar(20) NOT NULL,
    title varchar(255) NOT NULL,
    hidden_status varchar(3) DEFAULT 'no',
    created_by varchar(100) DEFAULT NULL,
    PRIMARY KEY (textbook_id, chapter_id, section_id),
    FOREIGN KEY (textbook_id, chapter_id) REFERENCES chapter (textbook_id, chapter_id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT chk_hidden CHECK (hidden_status IN ('yes', 'no'))
);

CREATE TABLE IF NOT EXISTS block (
  textbook_id int(11) NOT NULL,
  chapter_id varchar(20) NOT NULL,
  section_id varchar(20) NOT NULL,
  block_id varchar(20) NOT NULL,
  block_type varchar(255),
  content TEXT,
  hidden_status varchar(3) DEFAULT 'no',
  PRIMARY KEY (textbook_id, chapter_id, section_id, block_id),
  FOREIGN KEY (textbook_id, chapter_id, section_id) REFERENCES section (textbook_id, chapter_id, section_id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT chk_hidden CHECK (hidden_status IN ('yes', 'no'))
);

CREATE TABLE IF NOT EXISTS activity (
  textbook_id int(11) NOT NULL,
  chapter_id varchar(20) NOT NULL,
  section_id varchar(20) NOT NULL,
  block_id varchar(20) NOT NULL,
  unique_activity_id varchar(20) NOT NULL,
  hidden_status varchar(3) DEFAULT 'no',
  PRIMARY KEY (textbook_id, chapter_id, section_id, block_id, unique_activity_id),
  FOREIGN KEY (textbook_id, chapter_id, section_id, block_id) REFERENCES block (textbook_id, chapter_id, section_id, block_id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT chk_hidden CHECK (hidden_status IN ('yes', 'no'))
);

CREATE TABLE IF NOT EXISTS question (
    textbook_id int(11) NOT NULL,
    chapter_id varchar(20) NOT NULL,
    section_id varchar(20) NOT NULL,
    block_id varchar(20) NOT NULL,
    unique_activity_id varchar(20) NOT NULL,
    question_id varchar(20) NOT NULL,
    question_text TEXT NOT NULL,
    option_1 TEXT NOT NULL,
    opt_1_explanation TEXT NOT NULL,
    option_2 TEXT NOT NULL,
    opt_2_explanation TEXT NOT NULL,
    option_3 TEXT NOT NULL,
    opt_3_explanation TEXT NOT NULL,
    option_4 TEXT NOT NULL,
    opt_4_explanation TEXT NOT NULL,
    answer TINYINT NOT NULL,
    PRIMARY KEY (textbook_id, chapter_id, section_id, block_id, unique_activity_id, question_id),
    FOREIGN KEY (textbook_id, chapter_id, section_id, block_id, unique_activity_id) REFERENCES activity (textbook_id, chapter_id, section_id, block_id, unique_activity_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS user (
    user_id VARCHAR(8) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,    
    last_name VARCHAR(50) NOT NULL,     
    email VARCHAR(100) NOT NULL UNIQUE,  
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL,
    CHECK (LENGTH(user_id) = 8),
    CHECK (role IN ('admin', 'faculty', 'student', 'teaching assistant'))
);

CREATE TABLE IF NOT EXISTS student (
    student_id VARCHAR(8) PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL,
    FOREIGN KEY (student_id) REFERENCES user(user_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS faculty (
    faculty_id VARCHAR(8) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    FOREIGN KEY (faculty_id) REFERENCES user(user_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS teaching_assistant (
    ta_id VARCHAR(8) PRIMARY KEY,  
    first_name VARCHAR(50) NOT NULL,  
    last_name VARCHAR(50) NOT NULL,  
    email VARCHAR(100) NOT NULL, 
    password VARCHAR(255) NOT NULL, 
    course_id VARCHAR(10), 
    FOREIGN KEY (ta_id) REFERENCES user(user_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS course (
    course_id VARCHAR(30) PRIMARY KEY, 
    course_name VARCHAR(100) NOT NULL, 
    textbook_id INT(11) NOT NULL, 
    course_type VARCHAR(15) NOT NULL, 
    faculty_id VARCHAR(8) NOT NULL, 
    ta_id VARCHAR(8) NOT NULL,
    start_date DATE NOT NULL, 
    end_date DATE NOT NULL, 
    unique_token VARCHAR(7) NOT NULL UNIQUE, 
    FOREIGN KEY (ta_id) REFERENCES user(user_id),
    FOREIGN KEY (faculty_id) REFERENCES user(user_id),
    FOREIGN KEY (textbook_id) REFERENCES textbook(textbook_id),
    CHECK (course_type IN ('Active', 'Evaluation'))
);
