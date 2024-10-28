-- Add sequence number to block, increasing order
ALTER TABLE block ADD COLUMN sequence_no INT NOT NULL AUTO_INCREMENT UNIQUE;

-- Drop username column from student, not needed 
ALTER TABLE student DROP COLUMN username;