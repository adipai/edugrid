-- Adding or modifying 'created_by' column in textbook table with foreign key constraint
ALTER TABLE textbook 
ADD COLUMN IF NOT EXISTS created_by VARCHAR(8) DEFAULT NULL AFTER title,
ADD CONSTRAINT fk_textbook_created_by FOREIGN KEY (created_by) REFERENCES user(user_id);

-- Adding or modifying 'created_by' column in chapter table with foreign key constraint
ALTER TABLE chapter 
MODIFY COLUMN created_by VARCHAR(8) DEFAULT NULL,
ADD CONSTRAINT fk_chapter_created_by FOREIGN KEY (created_by) REFERENCES user(user_id);

-- Adding or modifying 'created_by' column in section table with foreign key constraint
ALTER TABLE section 
MODIFY COLUMN created_by VARCHAR(8) DEFAULT NULL,
ADD CONSTRAINT fk_section_created_by FOREIGN KEY (created_by) REFERENCES user(user_id);

-- Adding or modifying 'created_by' column in block table with foreign key constraint
ALTER TABLE block 
ADD COLUMN IF NOT EXISTS created_by VARCHAR(8) DEFAULT NULL AFTER hidden_status,
ADD CONSTRAINT fk_block_created_by FOREIGN KEY (created_by) REFERENCES user(user_id);

-- Adding or modifying 'created_by' column in question table with foreign key constraint
ALTER TABLE question 
ADD COLUMN IF NOT EXISTS created_by VARCHAR(8) DEFAULT NULL AFTER answer,
ADD CONSTRAINT fk_question_created_by FOREIGN KEY (created_by) REFERENCES user(user_id);

ALTER TABLE activity 
ADD COLUMN IF NOT EXISTS created_by VARCHAR(8) DEFAULT NULL AFTER hidden_status,
ADD CONSTRAINT fk_activity_created_by FOREIGN KEY (created_by) REFERENCES user(user_id);
