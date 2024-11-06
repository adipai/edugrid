
-- Add timestamp column to notification table
ALTER TABLE notification
ADD COLUMN timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

-- Change course_id size to match cpourse table
ALTER TABLE teaching_assistant MODIFY COLUMN course_id VARCHAR(30);

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



