-- Create e_textbook table
CREATE TABLE e_textbook (
    tb_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL
);

-- Create chapter table
CREATE TABLE chapter (
    tb_id INT,
    chap_no INT,
    title VARCHAR(255) NOT NULL,
    hidden_status BOOLEAN DEFAULT 0,
    created_by VARCHAR(100),
    PRIMARY KEY (tb_id, chap_no),
    FOREIGN KEY (tb_id) REFERENCES e_textbook(tb_id)
);

-- Create section table
CREATE TABLE section (
    sec_no INT,
    title VARCHAR(255) NOT NULL,
    hidden_status BOOLEAN DEFAULT 0,
    created_by VARCHAR(100),
    tb_id INT,
    chap_no INT,
    PRIMARY KEY (tb_id, chap_no, sec_no),
    FOREIGN KEY (tb_id, chap_no) REFERENCES chapter(tb_id, chap_no)
);

-- Create content table
CREATE TABLE content (
    sequence_no INT,
    sec_no INT,
    chap_no INT,
    tb_id INT,
    hidden BOOLEAN NOT NULL,
    content_type VARCHAR(255) NOT NULL,
    PRIMARY KEY (sequence_no, sec_no, chap_no, tb_id),
    FOREIGN KEY (tb_id, chap_no, sec_no) REFERENCES section (tb_id, chap_no, sec_no)
);

-- Create activity table
CREATE TABLE activity (
    activity_id INT,
    sec_no INT,
    chap_no INT,
    tb_id INT,
    hidden BOOLEAN NOT NULL,
    question VARCHAR(255) NOT NULL,
    PRIMARY KEY (activity_id, sec_no, chap_no, tb_id),
    FOREIGN KEY (tb_id, chap_no, sec_no) REFERENCES section(tb_id, chap_no, sec_no)
);

-- Create options table
CREATE TABLE options (
    option_id INT,
    activity_id INT,
    sec_no INT,
    chap_no INT,
    tb_id INT,
    is_correct BOOLEAN NOT NULL,
    text VARCHAR(255) NOT NULL,
    explanation VARCHAR(255) NOT NULL,
    PRIMARY KEY (option_id, activity_id, sec_no, chap_no, tb_id),
    FOREIGN KEY (activity_id, sec_no, chap_no, tb_id) REFERENCES activity (activity_id, sec_no, chap_no, tb_id)
);

-- Create user table
CREATE TABLE user (
    user_id VARCHAR(8) PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,    
    last_name VARCHAR(50) NOT NULL,     
    email VARCHAR(100) NOT NULL UNIQUE,  
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL,
    score INT DEFAULT 0,
    CHECK (LENGTH(user_id) = 8),
    CHECK (role IN ('admin', 'faculty', 'student', 'teaching assistant'))
);

-- Create courses table
CREATE TABLE courses (
    course_id VARCHAR(20) PRIMARY KEY,
    course_title VARCHAR(100) NOT NULL,
    faculty_id VARCHAR(8) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    FOREIGN KEY (faculty_id) REFERENCES user(user_id)
);

-- Create active_courses table
CREATE TABLE active_courses (
    active_course_id VARCHAR(20) PRIMARY KEY,
    course_id VARCHAR(20) NOT NULL,
    unique_token VARCHAR(7) NOT NULL UNIQUE,
    capacity INT NOT NULL,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Create teaching_assistants table
CREATE TABLE teaching_assistants (
    ta_id VARCHAR(8),
    active_course_id VARCHAR(20), 
    PRIMARY KEY (ta_id, active_course_id),
    FOREIGN KEY (active_course_id) REFERENCES active_courses (active_course_id)
);

-- Create participation table
CREATE TABLE participation (
    user_id VARCHAR(8),
    activity_id INT,
    sec_no INT,
    chap_no INT,
    tb_id INT,
    score SMALLINT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, activity_id, sec_no, chap_no, tb_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (activity_id, sec_no, chap_no, tb_id) REFERENCES activity(activity_id, sec_no, chap_no, tb_id)
);

-- Create notification table
CREATE TABLE notification (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(8),
    message VARCHAR(200),
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);

-- Create enrollment table
CREATE TABLE enrollment (
    course_id VARCHAR(8),
    user_id VARCHAR(8),
    title VARCHAR(255),
    PRIMARY KEY (course_id, user_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);
