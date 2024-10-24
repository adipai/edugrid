
ALTER TABLE active_courses CHANGE active_course_id id varchar(20);

ALTER TABLE user CHANGE user_id id varchar(8);

ALTER TABLE courses CHANGE course_id id varchar(20);

ALTER TABLE courses ADD COLUMN tb_id int(11);

RENAME TABLE courses TO course;

ALTER TABLE e_textbook CHANGE tb_id id int(11);

ALTER TABLE options CHANGE option_id id int(11);

RENAME TABLE options TO option;

ALTER TABLE teaching_assistants CHANGE ta_id id varchar(8);

RENAME TABLE teaching_assistants TO teaching_assistant;

ALTER TABLE user DROP score;

ALTER TABLE user MODIFY COLUMN password VARCHAR(255) DEFAULT 'abc123';

CREATE TABLE student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    user_id VARCHAR(8),
    FOREIGN KEY (user_id) REFERENCES user(id)
);

ALTER TABLE activity DROP question;

CREATE TABLE question (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text VARCHAR(255),
    activity_id INT(11),
    FOREIGN KEY(activity_id) REFERENCES activity(activity_id)
);

DROP TABLE option;

CREATE TABLE option (
  id INT AUTO_INCREMENT PRIMARY KEY,
  question_id INT DEFAULT NULL,
  is_correct tinyint(1) NOT NULL,
  text varchar(255) NOT NULL,
  explanation varchar(255) NOT NULL,
  FOREIGN KEY (question_id) REFERENCES question(id)
  );
