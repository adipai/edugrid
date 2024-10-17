# Backend
## API list
### Start page
* credentials_validate - validates the login for each role - SELECT from table, match in code
* update_password
  
### Admin
* create_account_faculty - INSERT 
* create_etextbook - INSERT
* modify_etextbooks - UPDATE
* create_new_active_course - INSERT
* create_new_evaluation_course - INSERT

* **add_new_chapter - INSERT**
* **modify_chapter - UPDATE**
* **add_new_section - INSERT**
* **add_new_content - INSERT**
* **add_content_text - INSERT**
* **add_content_picture - INSERT**
* **add_content_activity - INSERT**

### Faculty
* view_worklist - SELECT
* approve_enrollment - UPDATE
* view_students - SELECT
* **add_new_chapter - INSERT**
* **modify_chapter - UPDATE**
* add_ta  - INSERT

* **hide_chapter - UPDATE**
* **delete_chapter - DELETE FROM**
* **add_new_section - INSERT**
* **modify_section - UPDATE**
* **add_new_content - INSERT**
* **hide_section - INSERT**
* **delete_section - INSERT**
* **add_new_content_block - INSERT**

* **hide_content_block - UPDATE**
* **delete_content_block - DELETE FROM**
* **hide_activity - UPDATE**
* **delete_activity - DELETE FROM**
* **add activity - INSERT**
* **modify_content_block - INSERT**
* **add_content_text - INSERT**
* **add_content_picture - INSERT**
* **add_content_activity - INSERT**
* **add_question - INSERT**


## TA
* view_courses
* view_students
* **add_new_chapter - INSERT**
* **modify_chapter - UPDATE**
* **add_new_section - INSERT**
* **add_content_text - INSERT**
* **add_content_picture - INSERT**
* **add_content_activity - INSERT**
* **add_question - INSERT**
* **hide_content_block - UPDATE**
* **delete_content_block - DELETE FROM**

## Student
* enroll_in_course
* view_section
* view_participation_activity_point
* view_block -- if question take input
