

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
  block_type varchar(255) NOT NULL,
  content TEXT NOT NULL,
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
