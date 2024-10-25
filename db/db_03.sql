
ALTER TABLE course DROP CONSTRAINT course_ibfk_1;
ALTER TABLE course DROP COLUMN ta_id;

CREATE TABLE IF NOT EXISTS enrollment (
    unique_course_id VARCHAR(30),
    student_id VARCHAR(8),
    status ENUM('Enrolled', 'Pending') DEFAULT 'Pending',
    PRIMARY KEY (unique_course_id, student_id),
    FOREIGN KEY (unique_course_id) REFERENCES course(course_id),
    FOREIGN KEY (student_id) REFERENCES student(student_id)
);

CREATE TABLE participation (
    student_id VARCHAR(8),
    course_id VARCHAR(30),
    textbook_id INT(11),
    section_id VARCHAR(20),
    chapter_id VARCHAR(20),
    block_id VARCHAR(20),
    unique_activity_id VARCHAR(20),
    question_id VARCHAR(20),
    point INT,
    attempted_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (student_id, course_id, textbook_id, section_id, chapter_id, block_id, unique_activity_id, question_id),
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE,
    FOREIGN KEY (textbook_id) REFERENCES textbook(textbook_id) ON DELETE CASCADE,
    FOREIGN KEY (textbook_id, chapter_id, section_id, block_id, unique_activity_id, question_id) 
        REFERENCES question(textbook_id, chapter_id, section_id, block_id, unique_activity_id, question_id) ON DELETE CASCADE
);

CREATE TABLE notification (
    notification_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(8),
    notification_message TEXT,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);
