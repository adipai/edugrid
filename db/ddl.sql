
-- Table DDLs

CREATE TABLE user (
  user_id varchar(8) NOT NULL,
  first_name varchar(50) NOT NULL,
  last_name varchar(50) NOT NULL,
  email varchar(100) NOT NULL,
  password varchar(255) NOT NULL,
  role varchar(20) NOT NULL,
  PRIMARY KEY (user_id),
  UNIQUE KEY email (email),
  CONSTRAINT CONSTRAINT_1 CHECK (octet_length(user_id) = 8),
  CONSTRAINT CONSTRAINT_2 CHECK (role in ('admin','faculty','student','teaching assistant'))
);

CREATE TABLE notification (
  notification_id int(11) NOT NULL AUTO_INCREMENT,
  user_id varchar(8) DEFAULT NULL,
  notification_message text DEFAULT NULL,
  timestamp timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (notification_id),
  KEY user_id (user_id),
  CONSTRAINT notification_ibfk_1 FOREIGN KEY (user_id) REFERENCES user (user_id)
) ;

CREATE TABLE textbook (
  textbook_id int(11) NOT NULL,
  title varchar(255) NOT NULL,
  created_by varchar(8) DEFAULT NULL,
  PRIMARY KEY (textbook_id),
  KEY fk_textbook_created_by (created_by),
  CONSTRAINT fk_textbook_created_by FOREIGN KEY (created_by) REFERENCES user (user_id)
);

CREATE TABLE course (
  course_id varchar(30) NOT NULL,
  course_name varchar(100) NOT NULL,
  textbook_id int(11) DEFAULT NULL,
  course_type varchar(15) DEFAULT NULL,
  faculty_id varchar(8) DEFAULT NULL,
  start_date date DEFAULT NULL,
  end_date date DEFAULT NULL,
  unique_token varchar(7) DEFAULT NULL,
  capacity int(11) DEFAULT NULL,
  PRIMARY KEY (course_id),
  UNIQUE KEY unique_token (unique_token),
  KEY faculty_id (faculty_id),
  KEY textbook_id (textbook_id),
  CONSTRAINT course_ibfk_2 FOREIGN KEY (faculty_id) REFERENCES user (user_id),
  CONSTRAINT course_ibfk_3 FOREIGN KEY (textbook_id) REFERENCES textbook (textbook_id),
  CONSTRAINT CONSTRAINT_1 CHECK (course_type in ('Active','Evaluation'))
);

CREATE TABLE student (
  student_id varchar(8) NOT NULL,
  full_name varchar(100) NOT NULL,
  password varchar(255) NOT NULL,
  email varchar(100) NOT NULL,
  PRIMARY KEY (student_id),
  CONSTRAINT student_ibfk_1 FOREIGN KEY (student_id) REFERENCES user (user_id) ON DELETE CASCADE
);

CREATE TABLE faculty (
  faculty_id varchar(8) NOT NULL,
  first_name varchar(50) NOT NULL,
  last_name varchar(50) NOT NULL,
  email varchar(100) NOT NULL,
  password varchar(255) NOT NULL,
  PRIMARY KEY (faculty_id),
  CONSTRAINT faculty_ibfk_1 FOREIGN KEY (faculty_id) REFERENCES user (user_id) ON DELETE CASCADE
); 

CREATE TABLE teaching_assistant (
  ta_id varchar(8) NOT NULL,
  first_name varchar(50) NOT NULL,
  last_name varchar(50) NOT NULL,
  email varchar(100) NOT NULL,
  password varchar(255) NOT NULL,
  course_id varchar(30) DEFAULT NULL,
  PRIMARY KEY (ta_id),
  CONSTRAINT teaching_assistant_ibfk_1 FOREIGN KEY (ta_id) REFERENCES user (user_id) ON DELETE CASCADE
);

CREATE TABLE enrollment (
  unique_course_id varchar(30) NOT NULL,
  student_id varchar(8) NOT NULL,
  status enum('Enrolled','Pending') DEFAULT 'Pending',
  PRIMARY KEY (unique_course_id,student_id),
  KEY student_id (student_id),
  CONSTRAINT enrollment_ibfk_1 FOREIGN KEY (unique_course_id) REFERENCES course (course_id),
  CONSTRAINT enrollment_ibfk_2 FOREIGN KEY (student_id) REFERENCES student (student_id)
);


CREATE TABLE chapter (
  textbook_id int(11) NOT NULL,
  chapter_id varchar(20) NOT NULL,
  title varchar(255) NOT NULL,
  hidden_status varchar(3) DEFAULT 'no',
  created_by varchar(8) DEFAULT NULL,
  PRIMARY KEY (textbook_id,chapter_id),
  KEY fk_chapter_created_by (created_by),
  CONSTRAINT chapter_ibfk_1 FOREIGN KEY (textbook_id) REFERENCES textbook (textbook_id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_chapter_created_by FOREIGN KEY (created_by) REFERENCES user (user_id),
  CONSTRAINT chk_hidden CHECK (hidden_status in ('yes','no'))
);

CREATE TABLE section (
  textbook_id int(11) NOT NULL,
  chapter_id varchar(20) NOT NULL,
  section_id varchar(20) NOT NULL,
  title varchar(255) NOT NULL,
  hidden_status varchar(3) DEFAULT 'no',
  created_by varchar(8) DEFAULT NULL,
  PRIMARY KEY (textbook_id,chapter_id,section_id),
  KEY fk_section_created_by (created_by),
  CONSTRAINT fk_section_created_by FOREIGN KEY (created_by) REFERENCES user (user_id),
  CONSTRAINT section_ibfk_1 FOREIGN KEY (textbook_id, chapter_id) REFERENCES chapter (textbook_id, chapter_id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT chk_hidden CHECK (hidden_status in ('yes','no'))
);

CREATE TABLE block (
  textbook_id int(11) NOT NULL,
  chapter_id varchar(20) NOT NULL,
  section_id varchar(20) NOT NULL,
  block_id varchar(20) NOT NULL,
  block_type varchar(255) DEFAULT NULL,
  content text DEFAULT NULL,
  hidden_status varchar(3) DEFAULT 'no',
  created_by varchar(8) DEFAULT NULL,
  sequence_no int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (textbook_id,chapter_id,section_id,block_id),
  UNIQUE KEY sequence_no (sequence_no),
  KEY fk_block_created_by (created_by),
  CONSTRAINT block_ibfk_1 FOREIGN KEY (textbook_id, chapter_id, section_id) REFERENCES section (textbook_id, chapter_id, section_id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_block_created_by FOREIGN KEY (created_by) REFERENCES user (user_id),
  CONSTRAINT chk_hidden CHECK (hidden_status in ('yes','no'))
);

CREATE TABLE activity (
  textbook_id int(11) NOT NULL,
  chapter_id varchar(20) NOT NULL,
  section_id varchar(20) NOT NULL,
  block_id varchar(20) NOT NULL,
  unique_activity_id varchar(20) NOT NULL,
  hidden_status varchar(3) DEFAULT 'no',
  created_by varchar(8) DEFAULT NULL,
  PRIMARY KEY (textbook_id,chapter_id,section_id,block_id,unique_activity_id),
  KEY fk_activity_created_by (created_by),
  CONSTRAINT activity_ibfk_1 FOREIGN KEY (textbook_id, chapter_id, section_id, block_id) REFERENCES block (textbook_id, chapter_id, section_id, block_id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_activity_created_by FOREIGN KEY (created_by) REFERENCES user (user_id),
  CONSTRAINT chk_hidden CHECK (hidden_status in ('yes','no'))
);

CREATE TABLE question (
  textbook_id int(11) NOT NULL,
  chapter_id varchar(20) NOT NULL,
  section_id varchar(20) NOT NULL,
  block_id varchar(20) NOT NULL,
  unique_activity_id varchar(20) NOT NULL,
  question_id varchar(20) NOT NULL,
  question_text text NOT NULL,
  option_1 text NOT NULL,
  opt_1_explanation text NOT NULL,
  option_2 text NOT NULL,
  opt_2_explanation text NOT NULL,
  option_3 text NOT NULL,
  opt_3_explanation text NOT NULL,
  option_4 text NOT NULL,
  opt_4_explanation text NOT NULL,
  answer tinyint(4) NOT NULL,
  created_by varchar(8) DEFAULT NULL,
  PRIMARY KEY (textbook_id,chapter_id,section_id,block_id,unique_activity_id,question_id),
  KEY fk_question_created_by (created_by),
  CONSTRAINT fk_question_created_by FOREIGN KEY (created_by) REFERENCES user (user_id),
  CONSTRAINT question_ibfk_1 FOREIGN KEY (textbook_id, chapter_id, section_id, block_id, unique_activity_id) REFERENCES activity (textbook_id, chapter_id, section_id, block_id, unique_activity_id) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE participation (
  student_id varchar(8) NOT NULL,
  course_id varchar(30) NOT NULL,
  textbook_id int(11) NOT NULL,
  section_id varchar(20) NOT NULL,
  chapter_id varchar(20) NOT NULL,
  block_id varchar(20) NOT NULL,
  unique_activity_id varchar(20) NOT NULL,
  question_id varchar(20) NOT NULL,
  point int(11) DEFAULT NULL,
  attempted_timestamp timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (student_id,course_id,textbook_id,section_id,chapter_id,block_id,unique_activity_id,question_id),
  KEY course_id (course_id),
  KEY textbook_id (textbook_id,chapter_id,section_id,block_id,unique_activity_id,question_id),
  CONSTRAINT participation_ibfk_1 FOREIGN KEY (student_id) REFERENCES student (student_id) ON DELETE CASCADE,
  CONSTRAINT participation_ibfk_2 FOREIGN KEY (course_id) REFERENCES course (course_id) ON DELETE CASCADE,
  CONSTRAINT participation_ibfk_3 FOREIGN KEY (textbook_id) REFERENCES textbook (textbook_id) ON DELETE CASCADE,
  CONSTRAINT participation_ibfk_4 FOREIGN KEY (textbook_id, chapter_id, section_id, block_id, unique_activity_id, question_id) REFERENCES question (textbook_id, chapter_id, section_id, block_id, unique_activity_id, question_id) ON DELETE CASCADE
);


-- TRIGGERS
-- Trigger for UPDATE operation on enrollment table : when faculty enrolls a student from waitlist
DELIMITER //

CREATE TRIGGER after_enrollment_update
AFTER UPDATE ON enrollment
FOR EACH ROW
BEGIN
    DECLARE course_capacity INT;
    DECLARE enrolled_count INT;
    DECLARE notification_msg TEXT;

    -- Condition 1: Check if status is changed to 'Enrolled'
    IF NEW.status = 'Enrolled' AND OLD.status != 'Enrolled' THEN
        SET notification_msg = CONCAT('You have been enrolled into course ', NEW.unique_course_id);
        INSERT INTO notification (user_id, notification_message)
        VALUES (NEW.student_id, notification_msg);
    END IF;

    -- Condition 2: Check course capacity and notify waitlisted students if capacity is reached
    SELECT capacity INTO course_capacity 
    FROM course 
    WHERE course_id = NEW.unique_course_id;

    SELECT COUNT(*) INTO enrolled_count 
    FROM enrollment 
    WHERE unique_course_id = NEW.unique_course_id AND status = 'Enrolled';

    IF enrolled_count >= course_capacity THEN
        SET notification_msg = CONCAT('Course capacity reached for ', NEW.unique_course_id, ', waitlist has been dropped');

        -- Insert notifications for pending students who have not yet been notified
        INSERT INTO notification (user_id, notification_message)
        SELECT e.student_id, notification_msg
        FROM enrollment e
        LEFT JOIN notification n 
        ON e.student_id = n.user_id 
            AND n.notification_message = notification_msg
        WHERE e.unique_course_id = NEW.unique_course_id
            AND e.status = 'Pending'
            AND n.user_id IS NULL;
    END IF;
END //

DELIMITER ;


-- Trigger to add notifaction for a student who tries to enroll into a course that has reached capacity
DELIMITER //

CREATE TRIGGER check_course_capacity_on_insert
AFTER INSERT ON enrollment
FOR EACH ROW
BEGIN
    DECLARE current_enrollment_count INT;
    DECLARE course_capacity INT;

    -- Get the course capacity
    SELECT capacity INTO course_capacity
    FROM course
    WHERE course_id = NEW.unique_course_id;

    -- Count the current number of enrolled students in the course
    SELECT COUNT(*) INTO current_enrollment_count
    FROM enrollment
    WHERE unique_course_id = NEW.unique_course_id
      AND status = 'Enrolled';

    -- Check if course capacity is reached
    IF current_enrollment_count >= course_capacity THEN
        -- Notify only the student just inserted if they have 'Pending' status
        IF NEW.status = 'Pending' THEN
            INSERT INTO notification (user_id, notification_message)
            VALUES (NEW.student_id, CONCAT('Course capacity reached for ', NEW.unique_course_id, ', waitlist has been dropped.'));
        END IF;
    END IF;

END //

DELIMITER ;
