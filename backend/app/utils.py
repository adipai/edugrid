import random
import string
import traceback
import argparse

from datetime import datetime
from constants import connection


def add_user(connection, first_name, last_name, email, password, current_date, user_id, role):
    try:
        cursor = connection.cursor()
        # Check if user exists
        cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
        if cursor.fetchone():
            return 'user_exists'

        # Insert new user
        cursor.execute("INSERT INTO user (user_id, first_name, last_name, email, password, role)  VALUES (%s, %s, %s, %s, %s, %s)",
                       (user_id, first_name, last_name, email, password, role))
        connection.commit()
        return 'user_created'
    except Exception as e:
        print(f"Error: {e}")
        return 'error'
    finally:
        connection.close()

def check_user(connection, email, password, role):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user WHERE email = %s AND password = %s AND role = %s",
                   (email, password, role))
    user = cursor.fetchone()
    connection.close()
    return user

def generate_user_id(length=8):
    """Generate a random alphanumeric user_id of the specified length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def create_account_faculty(connection, first_name, last_name, email, password):
    """
    Admin creating account of faculty based on inputs 
    (first name, last name, email, password)
    """
    try:
        with connection.cursor() as cursor:
            # Check if the email already exists
            cursor.execute("SELECT * FROM user WHERE email = %s", (email,))
            if cursor.fetchone():
                print("Email already exists in the database")
                return

            # Generate a unique user_id of length 8
            new_user_id = generate_user_id()

            # Ensure the generated user_id is unique (not already in the table)
            cursor.execute("SELECT * FROM user WHERE user_id = %s", (new_user_id,))
            while cursor.fetchone():
                new_user_id = generate_user_id()

            # SQL insert statement including user_id
            insert_query = """
            INSERT INTO user (user_id, first_name, last_name, email, password, role, score)
            VALUES (%s, %s, %s, %s, %s, 'faculty', 0)
            """
            
            # Execute the insert query
            cursor.execute(insert_query, (new_user_id, first_name, last_name, email, password))
        
        # Commit the transaction
        connection.commit()
        return 'Success'

    finally:
        # Close the connection
        connection.close()

def create_evaluation_course(connection, course_id, course_name, e_textbook_id, faculty_id, start_date, end_date):
    """Admin creates a new evaluation course."""

    try:
        with connection.cursor() as cursor:
            # Check if course_id already exists to avoid duplication
            cursor.execute("SELECT * FROM course WHERE course_id = %s", (course_id,))
            if cursor.fetchone():
                raise ValueError(f"Error: id {course_id} already exists in the database.")

            # SQL insert statement
            insert_query = """
            INSERT INTO course (course_id, course_title, faculty_id, start_date, end_date)
            VALUES (%s, %s, %s, %s, %s)
            """

            # Execute the insert query
            cursor.execute(insert_query, (course_id, course_name,faculty_id, start_date, end_date))
        
        # Commit the transaction
        connection.commit()
        print(f"Evaluation Course '{course_name}' with id: {course_id} successfully added.")
        return 'Success'
    finally:
        # Close the connection
        connection.close()


def create_active_course(connection, course_id, course_name, e_textbook_id, faculty_id, start_date, end_date, unique_token, course_capacity):
    """Admin creates a new active course."""

    try:
        with connection.cursor() as cursor:
            # Check if course_id already exists to avoid duplication
            cursor.execute("SELECT * FROM course WHERE course_id = %s", (course_id,))
            if cursor.fetchone():
                raise ValueError(f"Error: course_id {course_id} already exists in the database.")
            # Check if course_id already exists to avoid duplication
            cursor.execute("SELECT * FROM active_courses WHERE course_id = %s", (course_id,))
            if cursor.fetchone():
                raise ValueError(f"Error: course_id {course_id} already exists in the database.")

            # SQL insert statement for courses table
            insert_course_query = """
            INSERT INTO course (course_id, course_title, faculty_id, start_date, end_date)
            VALUES (%s, %s, %s, %s, %s)
            """
            # Execute the insert query for courses
            cursor.execute(insert_course_query, (course_id, course_name, faculty_id, start_date, end_date))

            # SQL insert statement for active_courses table
            insert_active_course_query = """
            INSERT INTO active_courses (course_id, course_id, unique_token, capacity)
            VALUES (%s, %s, %s, %s)
            """
            # Insert into active_courses table using active_course_id as '0'
            cursor.execute(insert_active_course_query, ('0', course_id, unique_token, course_capacity))
        
        # Commit the transaction
        connection.commit()
        print(f"Active course '{course_name}' with course_id: {course_id} successfully added.")
        return 'Success'

    finally:
        # Close the connection
        connection.close()

def create_textbook(connection, tb_id, tb_name, created_by):
    """Create a new textbook in the database."""
    
    try:
        with connection.cursor() as cursor:
            # Check if tb_id exists in textbook table
            cursor.execute("SELECT * FROM textbook WHERE textbook_id = %s", (tb_id,))  # Add comma to make it a tuple
            if cursor.fetchone():
                raise ValueError("Textbook ID already exists")

            # If all checks pass, insert into textbook
            cursor.execute("""
                INSERT INTO textbook (textbook_id, title, created_by)
                VALUES (%s, %s, %s)
            """, (tb_id, tb_name, created_by))  # Use tb_name here

            # Commit the changes
            connection.commit()
            print(f"Textbook '{tb_name}' created with ID '{tb_id}'.")

    except Exception as e:
        print(f"Error creating textbook: {e}")
        connection.rollback()  # Rollback in case of error



def create_chapter(connection, tb_id, chap_id, chap_title, created_by):
    """Create a new chapter in the specified textbook."""
    
    try:
        with connection.cursor() as cursor:
            # Check if tb_id and chap_id exist in the chapter table
            cursor.execute("SELECT * FROM chapter WHERE textbook_id = %s AND chapter_id = %s", (tb_id, chap_id))
            if cursor.fetchone():
                raise ValueError("Chapter already exists in the textbook.")

            # If all checks pass, insert into chapter
            cursor.execute("""
                INSERT INTO chapter (textbook_id, chapter_id, title, hidden_status, created_by)
                VALUES (%s, %s, %s, %s, %s)
            """, (tb_id, chap_id, chap_title, "no", created_by))

            # Commit the changes
            connection.commit()
            print(f"Chapter '{chap_title}' created in textbook ID '{tb_id}' with chapter ID '{chap_id}'.")

    except Exception as e:
        print(f"Error creating chapter: {e}")
        connection.rollback()  # Rollback in case of error


def create_section(connection, tb_id, chap_id, sec_id, sec_name, created_by):
    """Create a new section in the specified chapter of a textbook."""
    
    try:
        with connection.cursor() as cursor:
            # Check if tb_id, chap_id, and sec_id exist in the section table
            cursor.execute("SELECT * FROM section WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s", 
                           (tb_id, chap_id, sec_id))
            if cursor.fetchone():
                raise ValueError("Section already exists in the chapter.")

            # If all checks pass, insert into section
            cursor.execute("""
                INSERT INTO section (textbook_id, chapter_id, section_id, title, hidden_status, created_by)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (tb_id, chap_id, sec_id, sec_name, "no", created_by)) 

            # Commit the changes
            connection.commit()
            return f"Section '{sec_name}' created in chapter ID '{chap_id}' of textbook ID '{tb_id}'."

    except Exception as e:
        print(f"Error creating section: {e}")
        connection.rollback()  # Rollback in case of error


def create_block(connection, tb_id, chap_id, sec_id, block_id, created_by):
    """Create a new content block in the specified section of a textbook."""

    try:
        with connection.cursor() as cursor:
            # Check if tb_id, chap_id, sec_id, and block_id already exist in the content table
            cursor.execute("SELECT * FROM block WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s", 
                           (tb_id, chap_id, sec_id, block_id))
            if cursor.fetchone():
                raise ValueError("Content block already exists in the section.")

            # If all checks pass, insert into block
            cursor.execute("""
                INSERT INTO block (textbook_id, chapter_id, section_id, block_id, block_type, content, hidden_status, created_by)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (tb_id, chap_id, sec_id, block_id, None, None, "no", created_by)) 

            # Commit the changes
            connection.commit()
            return f"Content block '{block_id}' created in section ID '{sec_id}' of chapter ID '{chap_id}' in textbook ID '{tb_id}'."

    except Exception as e:
        print(f"Error creating block: {e}")
        connection.rollback()  # Rollback in case of error
        print(traceback.format_exc())

def create_activity(connection, tb_id, chap_id, sec_id, block_id, activity_id, created_by):
    try:
        with connection.cursor() as cursor:
            # Check if tb_id, chap_id, sec_id, block_id and activity_id already exist in the activity table
            cursor.execute("SELECT * FROM activity WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s AND unique_activity_id = %s", 
                           (tb_id, chap_id, sec_id, block_id, activity_id))
            if cursor.fetchone():
                return "Activity block already exists in the section."

            # If all checks pass, insert into activity
            cursor.execute("""
                INSERT INTO activity (textbook_id, chapter_id, section_id, block_id, unique_activity_id, created_by)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (tb_id, chap_id, sec_id, block_id, activity_id, created_by)) 

            # Commit the changes
            connection.commit()
            print(f"Activity block '{block_id}' created in section ID '{sec_id}' of chapter ID '{chap_id}' in textbook ID '{tb_id}'.")

    except Exception as e:
        print(f"Error creating block: {e}")
        connection.rollback()  # Rollback in case of error

    try:
        with connection.cursor() as cursor:
            # SQL query to update the content and block type in the block table
            update_query = """
                UPDATE block
                SET content = %s, block_type = %s
                WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s
            """
            
            # Execute the update query with the provided parameters
            cursor.execute(update_query, (activity_id, "activity", tb_id, chap_id, sec_id, block_id))

            # Commit the changes to the database
            connection.commit()

    except Exception as e:
        connection.rollback()  # Rollback in case of an error
        print(f"Error: {e}")
        print(traceback.format_exc())



def modify_textbook(connection, tb_id, user_modifying):
    """Check if the textbook exists for modification."""

    try:
        with connection.cursor() as cursor:
            # Check if tb_id exists in the textbook table
            cursor.execute("SELECT COUNT(*) FROM textbook WHERE textbook_id = %s", (tb_id,))
            count = cursor.fetchone()[0]
            
            # If tb_id does not exist, raise an error
            if count == 0:
                return "Textbook doesn't exist, so can't modify."

            # Fetch the role of the user modifying
            cursor.execute("SELECT role FROM user WHERE user_id = %s", (user_modifying,))
            modifying_user_role = cursor.fetchone()[0]


            # checking if the user has access to modify the textbook or not (shouldn't be another course's faculty/TA)
            if(modifying_user_role == "faculty"):
                cursor.execute("SELECT textbook_id FROM course WHERE faculty_id = %s", (user_modifying))

                associated_tb_id = cursor.fetchone()[0]
                if(associated_tb_id != tb_id):
                    return "You are not associated with this course, so can't modify"
            
            elif(modifying_user_role == "teaching assistant"):
                cursor.execute("""
                    SELECT c.textbook_id
                    FROM teaching_assistant t
                    JOIN course c ON t.course_id = c.course_id
                    WHERE t.ta_id = %s
                """, (user_modifying,))

                # Fetch the result
                associated_tb_id = cursor.fetchone()[0]

                if(associated_tb_id != tb_id):
                    return "You are not associated with this course, so can't modify"

            return "Textbook under modification"

    except Exception as e:
        print(f"Error modifying textbook: {e}")
        connection.rollback()



def modify_chapter(connection, tb_id, chap_id):
    """Check if the chapter exists for modification."""

    try:
        with connection.cursor() as cursor:
            # Check if chap_id exists in the chapter table
            cursor.execute("SELECT COUNT(*) FROM chapter WHERE textbook_id = %s AND chapter_id = %s", (tb_id, chap_id))
            count = cursor.fetchone()[0]
            
            # If chap_id does not exist, raise an error
            if count == 0:
                return "Chapter doesn't exist, so can't modify."
            
            return "Chapter under modification"

    except Exception as e:
        print(f"Error modifying chapter: {e}")
        connection.rollback()



def modify_section(connection, tb_id, chap_id, sec_id):
    """Check if the section exists for modification."""

    try:
        with connection.cursor() as cursor:
            # Check if sec_id exists in the section table
            cursor.execute("SELECT COUNT(*) FROM section WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s", (tb_id, chap_id, sec_id))
            count = cursor.fetchone()[0]

            # If sec_id does not exist, raise an error
            if count == 0:
                return "Section doesn't exist, so can't modify."
            
            return "Section under modification"

    except Exception as e:
        print(f"Error modifying section: {e}")
        connection.rollback()



def modify_block(connection, tb_id, chap_id, sec_id, block_id, user_modifying):
    """Check if the block exists for modification."""

    try:
        with connection.cursor() as cursor:
            # Check if block_id exists in the block table
            cursor.execute(
                "SELECT COUNT(*), created_by FROM block WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s",
                (tb_id, chap_id, sec_id, block_id)
            )
            count, created_by = cursor.fetchone()

            # If block_id does not exist, raise an error
            if count == 0:
                return "Block doesn't exist, so can't modify."

            # Fetch the role of the user modifying
            cursor.execute("SELECT role FROM user WHERE user_id = %s", (user_modifying,))
            modifying_user_role = cursor.fetchone()[0]

            # Fetch the role of the block creator
            cursor.execute("SELECT role FROM user WHERE user_id = %s", (created_by,))
            creator_user_role = cursor.fetchone()[0]
            
            # if(creator_user_role == None): 
            #     return "Block under modification"
            
            if(creator_user_role == "admin" and modifying_user_role != "admin"):
                return "Don't have permission to modify this block added by admin"
            
            elif(creator_user_role == "faculty" and modifying_user_role == "teaching assistant"):
                return "Don't have permission to modify this block added by faculty"
            
            elif(user_modifying != created_by and creator_user_role == "teaching assistant" and modifying_user_role == "teaching assistant"):
                return "Don't have permission to modify this block added by another TA"
        
            return "Block under modification"

    except Exception as e:
        print(f"Error modifying block: {e}")
        connection.rollback()



# def check_modify_activity(connection, tb_id, chap_id, sec_id, block_id, activity_id):
#     """Check if the activity exists for modification."""

#     try:
#         with connection.cursor() as cursor:
#             # Check if activity_id exists in the activity table
#             cursor.execute("SELECT COUNT(*) FROM activity WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s AND unique_activity_id = %s", (tb_id, chap_id, sec_id, block_id, activity_id))
#             count, created_by = cursor.fetchone()

#             # If activity_id does not exist, raise an error
#             if count > 0:
#                 return "New Activity ID already exists, so can't add"
            
#             return "New Activity ID doesn't exist - good to go!"

#     except Exception as e:
#         print(f"Error modifying activity: {e}")
#         connection.rollback()
    
def modify_activity_add_question(connection, tb_id, chap_id, sec_id, block_id, activity_id, question_id, question_text, \
                option_1, option_1_explanation, option_2, option_2_explanation, \
                option_3, option_3_explanation, option_4, option_4_explanation, answer, user_modifying):
        
    """ Add question and other corresponding things to the question table and delete previous activity"""

    try:
        with connection.cursor() as cursor:
            # Retrieve content from the block table based on tb_id, chap_id, sec_id, and block_id
            cursor.execute(
                "SELECT content, block_type FROM block WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s",
                (tb_id, chap_id, sec_id, block_id)
            )
            content, content_type = cursor.fetchone()

            if(content_type == "activity"):

                # Store the retrieved content as prev_activity_id
                prev_activity_id = content

                # Check if activity_id exists in the activity table
                cursor.execute(
                    "SELECT COUNT(*) FROM activity WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s AND unique_activity_id = %s",
                    (tb_id, chap_id, sec_id, block_id, prev_activity_id)
                )
                count, = cursor.fetchone()

                if count > 0:
                    cursor.execute(
                        "DELETE FROM activity WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s AND unique_activity_id = %s",
                        (tb_id, chap_id, sec_id, block_id, prev_activity_id)
                    )
                    print(f"Previous Activity {[prev_activity_id]} deleted.")
                else:
                    return "Previous Activity does not exist."

                # Update the content of the block table with the new activity_id
                cursor.execute(
                    "UPDATE block SET content = %s WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s",
                    (activity_id, tb_id, chap_id, sec_id, block_id)
                )
                # If all checks pass, insert into activity
                cursor.execute("""
                    INSERT INTO activity (textbook_id, chapter_id, section_id, block_id, unique_activity_id, created_by)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (tb_id, chap_id, sec_id, block_id, activity_id, user_modifying)) 

                add_question(connection, tb_id, chap_id, sec_id, block_id, activity_id, question_id, question_text, \
                    option_1, option_1_explanation, option_2, option_2_explanation, \
                    option_3, option_3_explanation, option_4, option_4_explanation, answer)
                # Commit the changes
                connection.commit()
            
            elif(content_type == "text" or content_type == "picture"):
                # Update the content and contenty type of the block table with the new activity_id
                cursor.execute(
                    "UPDATE block SET content = %s, block_type = %s WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s",
                    (activity_id, "activity", tb_id, chap_id, sec_id, block_id)
                )
                # If all checks pass, insert into activity
                cursor.execute("""
                    INSERT INTO activity (textbook_id, chapter_id, section_id, block_id, unique_activity_id, created_by)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (tb_id, chap_id, sec_id, block_id, activity_id, user_modifying)) 

                add_question(connection, tb_id, chap_id, sec_id, block_id, activity_id, question_id, question_text, \
                    option_1, option_1_explanation, option_2, option_2_explanation, \
                    option_3, option_3_explanation, option_4, option_4_explanation, answer)
                # Commit the changes
                connection.commit()
            
            else:
                return "Invalid existing content type"

            return "Modified Activity"

    except Exception as e:
        print(f"Error creating question: {e}")
        connection.rollback()  # Rollback in case of error
        print(traceback.format_exc())

def add_content(connection, tb_id, chap_id, sec_id, content, block_id, block_type="text"):

    """ Add text/picture content to the block """

    try:
        with connection.cursor() as cursor:

            # Query to find the current block_type
            cursor.execute("""
                SELECT content, block_type
                FROM block
                WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s
            """, (tb_id, chap_id, sec_id, block_id))
            
            # Fetch the current block_type
            current_content, current_block_type = cursor.fetchone()

            if(current_block_type == "activity"):
                delete_query = """
                    DELETE FROM activity
                    WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s AND unique_activity_id = %s
                """
                cursor.execute(delete_query, (tb_id, chap_id, sec_id, block_id, current_content))
                connection.commit()  # Commit the deletion


            # SQL query to update the content and block type in the block table
            update_query = """
                UPDATE block
                SET content = %s, block_type = %s
                WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s
            """
            
            # Execute the update query with the provided parameters
            cursor.execute(update_query, (content, block_type, tb_id, chap_id, sec_id, block_id))

            # Commit the changes to the database
            connection.commit()



    except Exception as e:
        connection.rollback()  # Rollback in case of an error
        print(f"Error: {e}")
        print(traceback.format_exc())


def add_question(connection, tb_id, chap_id, sec_id, block_id, activity_id, question_id, question_text, \
                option_1, option_1_explanation, option_2, option_2_explanation, \
                option_3, option_3_explanation, option_4, option_4_explanation, answer):

    """ Add question and other corresponding things to the question table """

    try:
        with connection.cursor() as cursor:
            # Check if tb_id, chap_id, sec_id, and block_id already exist in the content table
            cursor.execute("SELECT * FROM question WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s AND unique_activity_id= %s AND question_id =%s", 
                           (tb_id, chap_id, sec_id, block_id, activity_id, question_id))
            if cursor.fetchone():
                return "Question ID already exists for the activity"
            
            # If all checks pass, insert into block
            cursor.execute("""
                INSERT INTO question (textbook_id, chapter_id, section_id, block_id, unique_activity_id, question_id, 
                question_text, option_1, opt_1_explanation, option_2, opt_2_explanation, 
                option_3, opt_3_explanation, option_4, opt_4_explanation, answer)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (tb_id, chap_id, sec_id, block_id, activity_id, question_id, question_text, 
                option_1, option_1_explanation, option_2, option_2_explanation, 
                option_3, option_3_explanation, option_4, option_4_explanation, answer)) 

            # Commit the changes
            connection.commit()
            print(f"Question id '{question_id}' created for Activity id {activity_id}.")

    except Exception as e:
        print(f"Error creating question: {e}")
        connection.rollback()  # Rollback in case of error



def delete_chapter(connection, tb_id, chap_id, user_modifying):

    """ Deleting chapter """
    try:
        with connection.cursor() as cursor:
            # Check if chap_id exists in the chapter table
            cursor.execute("SELECT COUNT(*), created_by FROM chapter WHERE textbook_id = %s AND chapter_id = %s", (tb_id, chap_id))
            count, created_by = cursor.fetchone()
            
            # If chap_id does not exist, raise an error
            if count == 0:
                return "Chapter doesn't exist, so can't delete"
            
            # Fetch the role of the user modifying
            cursor.execute("SELECT role FROM user WHERE user_id = %s", (user_modifying,))
            modifying_user_role = cursor.fetchone()[0]

            # Fetch the role of the block creator
            cursor.execute("SELECT role FROM user WHERE user_id = %s", (created_by,))
            creator_user_role = cursor.fetchone()[0]

            if(creator_user_role == "admin" and modifying_user_role != "admin"):
                return "Don't have permission to delete"
            
            elif(creator_user_role == "faculty" and modifying_user_role == "teaching assistant"):
                return "Don't have permission to delete"
            
            cursor.execute("DELETE FROM chapter WHERE textbook_id = %s AND chapter_id = %s", (tb_id, chap_id))
            connection.commit()  # Commit the transaction
            return "Chapter deleted successfully"

    except Exception as e:
        print(f"Error deleting chapter: {e}")
        connection.rollback()
        print(traceback.format_exc())

def delete_section(connection, tb_id, chap_id, sec_id, user_modifying):

    """ Deleting section """
    try:
        with connection.cursor() as cursor:
            # Check if chap_id exists in the chapter table
            cursor.execute("SELECT COUNT(*), created_by FROM section WHERE textbook_id = %s AND chapter_id = %s AND section_id =  %s", (tb_id, chap_id, sec_id))
            count, created_by = cursor.fetchone()
            
            # If chap_id does not exist, raise an error
            if count == 0:
                return "Section doesn't exist, so can't delete"
            
            # Fetch the role of the user modifying
            cursor.execute("SELECT role FROM user WHERE user_id = %s", (user_modifying,))
            modifying_user_role = cursor.fetchone()[0]

            # Fetch the role of the block creator
            cursor.execute("SELECT role FROM user WHERE user_id = %s", (created_by,))
            creator_user_role = cursor.fetchone()[0]

            if(creator_user_role == "admin" and modifying_user_role != "admin"):
                return "Don't have permission to delete"
            
            elif(creator_user_role == "faculty" and modifying_user_role == "teaching assistant"):
                return "Don't have permission to delete"
            
            cursor.execute("DELETE FROM section WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s", (tb_id, chap_id, sec_id))
            connection.commit()  # Commit the transaction
            return "Section deleted successfully"

    except Exception as e:
        print(f"Error deleting section: {e}")
        connection.rollback()
        print(traceback.format_exc())

def delete_block(connection, tb_id, chap_id, sec_id, block_id, user_modifying):

    """ Deleting chapter """
    try:
        with connection.cursor() as cursor:
            # Check if chap_id exists in the chapter table
            cursor.execute("SELECT COUNT(*), created_by FROM block WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s", (tb_id, chap_id, sec_id, block_id))
            count, created_by = cursor.fetchone()
            
            # If chap_id does not exist, raise an error
            if count == 0:
                return "Block doesn't exist, so can't delete"
            
            # Fetch the role of the user modifying
            cursor.execute("SELECT role FROM user WHERE user_id = %s", (user_modifying,))
            modifying_user_role = cursor.fetchone()[0]

            # Fetch the role of the block creator
            cursor.execute("SELECT role FROM user WHERE user_id = %s", (created_by,))
            creator_user_role = cursor.fetchone()[0]

            if(creator_user_role == "admin" and modifying_user_role != "admin"):
                return "Don't have permission to delete"
            
            elif(creator_user_role == "faculty" and modifying_user_role == "teaching assistant"):
                return "Don't have permission to delete"
            
            cursor.execute("DELETE FROM block WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s", (tb_id, chap_id, sec_id, block_id))
            connection.commit()  # Commit the transaction
            return "Block deleted successfully"

    except Exception as e:
        print(f"Error deleting block: {e}")
        connection.rollback()
        print(traceback.format_exc())

        
def check_course_details(connection, input_course_id, current_date, user_modifying):

    """ Checking if user can modify the course content - user should be associated with course and date should be within end date. """

    try:
        with connection.cursor() as cursor:
            # Step 1: Retrieve the role of the user from the user table
            cursor.execute("SELECT role FROM user WHERE user_id = %s", (user_modifying,))
            role = cursor.fetchone()[0]
            end_date = None
            # Step 2: Check end date based on role
            if role == 'faculty':
                # Fetch the end date of the course for the faculty member
                cursor.execute(
                    "SELECT course_id, end_date FROM course WHERE faculty_id = %s",
                    (user_modifying,)
                )
            elif role == 'teaching assistant':
                # Join teaching assistant and course tables to fetch the end date
                cursor.execute(
                    """
                    SELECT c.course_id, c.end_date
                    FROM course c
                    JOIN teaching_assistant ta ON c.course_id = ta.course_id
                    WHERE ta.ta_id = %s
                    """,
                    (user_modifying,)
                )
            original_course_id, original_end_date = cursor.fetchone()

            if(input_course_id != original_course_id):
                return "You are not associated with this course"
            
            else:
                end_date = original_end_date
            

            # Allow modification if current_date is within or before the end date
            if(datetime.strptime(current_date, "%Y-%m-%d").date() <= end_date):
                return "Modification allowed"
            else:
                return "Beyond the end date - can't change the course!"

    except Exception as e:
        print("An error occurred:", e)
        print(traceback.format_exc())
        return "Error"



def hide_chapter(connection, tb_id, chap_id):
    """Set hidden_status of a chapter and all following entities to 'yes'."""
    try:
        with connection.cursor() as cursor:
            # Step 1: Set the chapter row to hidden
            cursor.execute(
                "UPDATE chapter SET hidden_status = 'yes' WHERE textbook_id = %s AND chapter_id = %s",
                (tb_id, chap_id)
            )

            # Step 2: Set related sections to hidden
            cursor.execute(
                "UPDATE section SET hidden_status = 'yes' WHERE textbook_id = %s AND chapter_id = %s",
                (tb_id, chap_id)
            )


            # Step 3: Set related blocks to hidden
            cursor.execute(
                "UPDATE block SET hidden_status = 'yes' WHERE textbook_id = %s AND chapter_id = %s",
                (tb_id, chap_id)
            )

            # Step 4: Set related activities to hidden
            cursor.execute(
                "UPDATE activity SET hidden_status = 'yes' WHERE textbook_id = %s AND chapter_id = %s",
                (tb_id, chap_id)
            )

            # Commit the transaction to save changes
            connection.commit()
            return "Chapter and related entities successfully hidden."

    except Exception as e:
        # Rollback if an error occurs
        connection.rollback()
        print("An error occurred:", e)
        print(traceback.format_exc())
        return "Error"

def hide_section(connection, tb_id, chap_id, sec_id):

    """Set hidden_status of a section and all following entities to 'yes'."""
    try:
        with connection.cursor() as cursor:

            # Step 1: Set related sections to hidden
            cursor.execute(
                "UPDATE section SET hidden_status = 'yes' WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s",
                (tb_id, chap_id, sec_id)
            )

            # Step 2: Set related blocks to hidden
            cursor.execute(
                "UPDATE block SET hidden_status = 'yes' WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s",
                (tb_id, chap_id, sec_id)
            )

            # Step 3: Set related activities to hidden
            cursor.execute(
                "UPDATE activity SET hidden_status = 'yes' WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s",
                (tb_id, chap_id, sec_id)
            )

            # Commit the transaction to save changes
            connection.commit()
            return "Section and related entities successfully hidden."

    except Exception as e:
        # Rollback if an error occurs
        connection.rollback()
        print("An error occurred:", e)
        print(traceback.format_exc())
        return "Error"


def hide_block(connection, tb_id, chap_id, sec_id, block_id):
    """Set hidden_status of a block and all following entities to 'yes'."""
    try:
        with connection.cursor() as cursor:

            # Step 1: Set related blocks to hidden
            cursor.execute(
                "UPDATE block SET hidden_status = 'yes' WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s",
                (tb_id, chap_id, sec_id, block_id)
            )

            # Step 2: Set related activities to hidden
            cursor.execute(
                "UPDATE activity SET hidden_status = 'yes' WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s",
                (tb_id, chap_id, sec_id, block_id)
            )

            # Commit the transaction to save changes
            connection.commit()
            return "Block and related entities successfully hidden."

    except Exception as e:
        # Rollback if an error occurs
        connection.rollback()
        print("An error occurred:", e)
        print(traceback.format_exc())
        return "Error"


def check_hide_block_func(connection):

    print(hide_block(connection, 1, "1", "1", "1"))
    print(hide_block(connection, 1, "1", "1", "4"))

    print(hide_section(connection, 1, "1", "1"))
    print(hide_chapter(connection, 1, "1"))


def check_course_details_func(connection):

    print(check_course_details(connection, "1234", "2025-10-24", "32456789"))  # FAIL - faculty not associated with course
    print(check_course_details(connection, "1234", "2025-10-24", "21348900")) # FAIL - TA not associated with course

    print(check_course_details(connection, "1234", "2025-10-23", "12345678")) # PASS - can modify as within end date
    print(check_course_details(connection, "1234", "2025-10-24", "12345678")) # FAIL - cant as beyond end date
# Testing textbook creation
def textbook_creation_flow(connection):
    try:
        # Step 1: Create Textbook
        tb_id = int(input("Enter textbook ID: "))
        textbook_title = input("Enter textbook name: ")
        create_textbook(connection, tb_id, textbook_title, "12378900")

        while True:
            # Prompt for next action after textbook creation
            action = input("Choose an action: (1) Create Chapter, (2) Back to Main Menu: ")
            
            if action == "1":
                # Step 2: Create Chapter
                chap_no = input("Enter chapter ID: ")
                chap_title = input("Enter chapter name: ")
                create_chapter(connection, tb_id, chap_no, chap_title, "12378900")

                # Step 3: Create Section
                sec_no = input("Enter section ID: ")
                section_title = input("Enter section name: ")
                create_section(connection, tb_id, chap_no, sec_no, section_title, "12378900")

                # Step 4: Create Content Block
                block_no = input("Enter block ID: ")
                create_block(connection, tb_id, chap_no, sec_no, block_no, "12378900")

                # Step 5: Add text
                content = input("Enter content text: ")
                add_content(connection, tb_id, chap_no, sec_no, content, block_no)

                print("Text Content successfully added.")
                break  # Go back to main menu after successful operation

            elif action == "2":
                break  # Return to main menu

            else:
                print("Invalid choice, please try again.")
                continue

    except ValueError as e:
        print(e)
        textbook_creation_flow(connection)  # Restart if error occurs

def modify_textbook_func(connection):
    # Placeholder for modifying textbook functionality

    # should be fine
    print(modify_textbook(connection, 1, "12345678")) # --faculty for tb id 1
    print(modify_textbook(connection, 1, "21115678")) # --teaching assistant for tb id 1

    print(modify_textbook(connection, 2, "32456789")) # --faculty for tb id 2
    print(modify_textbook(connection, 2, "21348900")) # --teaching assistant for tb id 2

    # should give error
    print(modify_textbook(connection, 1, "32456789")) # --faculty for tb id 2
    print(modify_textbook(connection, 1, "21348900")) # --teaching assistant for tb id 2

    print(modify_textbook(connection, 2, "12345678")) # --faculty for tb id 1
    print(modify_textbook(connection, 2, "21115678")) # --teaching assistant for tb id 1

    print(modify_textbook(connection, 3, "12359000")) # -- textbook doesn't exists

def modify_chapter_func(connection):
    # Placeholder for modifying chapter functionality

    # should be fine 
    print(modify_chapter(connection, 1, "1"))

    # errors
    print(modify_chapter(connection, 1 ,"2"))
    print(modify_chapter(connection, 2, "1"))


def modify_section_func(connection):
    # Placeholder for modifying section functionality
    
    # should be fine
    print(modify_section(connection, 1, "1", "1"))

    # errors
    print(modify_section(connection, 1, "1", "2"))

def modify_block_func(connection):
    # Placeholder for modifying block functionality

    ## Modifying block ("1") by admin for tb_id = 1 -- SHOULD PASS
    modify_textbook(connection, 1, "12378900")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    print(modify_block(connection, 1, "1", "1", "1", "12378900"))
    add_content(connection, 1, "1", "1", "OS hello", "1", block_type="text")

    ## Modifying block ("1") by faculty/ta for tb_id = 1 --- SHOULD FAIL
    modify_textbook(connection, 1, "12345678")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    print(modify_block(connection, 1, "1", "1", "1", "12345678"))

    modify_textbook(connection, 1, "21115678")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    print(modify_block(connection, 1, "1", "1", "1", "21115678"))

    ## Modifying block ("2") by admin/faculty for tb_id = 1 -- SHOULD PASS
    modify_textbook(connection, 1, "12378900")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    print(modify_block(connection, 1, "1", "1", "2", "12378900"))
    add_content(connection, 1, "1", "1", "OS Bye", "2", block_type="text")

    modify_textbook(connection, 1, "12345678")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    print(modify_block(connection, 1, "1", "1", "2", "12345678"))
    add_content(connection, 1, "1", "1", "OS Bye", "2", block_type="text")

    ## Modifying block ("2") by TA for tb_id = 1 -- SHOULD FAIL

    modify_textbook(connection, 1, "21115678")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    print(modify_block(connection, 1, "1", "1", "2", "21115678"))

    ## Modifying block ("3") by admin/faculty/same TA for tb_id = 1 -- SHOULD PASS
    modify_textbook(connection, 1, "12378900")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    print(modify_block(connection, 1, "1", "1", "3", "12378900"))
    add_content(connection, 1, "1", "1", "OS Kya", "3", block_type="text")

    modify_textbook(connection, 1, "12345678")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    print(modify_block(connection, 1, "1", "1", "3", "12345678"))
    add_content(connection, 1, "1", "1", "OS Kya", "3", block_type="text")

    modify_textbook(connection, 1, "21115678")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    print(modify_block(connection, 1, "1", "1", "3", "21115678"))
    add_content(connection, 1, "1", "1", "sample.png", "3", block_type="picture")


    ## Modifying block ("3") by another TA for tb_id = 1 -- SHOULD FAIL

    modify_textbook(connection, 1, "23890001")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    print(modify_block(connection, 1, "1", "1", "3", "23890001"))



def add_block_func(connection):
    # Placeholder for adding block functionality

    ## add block ("2") by modifying till section - by faculty (Rishi), tb_id = 1 -- SHOULD PASS
    modify_textbook(connection, 1, "12345678")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    create_block(connection, 1, "1", "1", "2", "12345678")
    add_content(connection, 1, "1", "1", "sample.png", "2", block_type="picture")
 
    ## add block ("3") by modifying till section - by TA (Aditya), tb_id = 1 -- SHOULD PASS
    modify_textbook(connection, 1, "21115678")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    create_block(connection, 1, "1", "1", "3", "21115678")
    add_content(connection, 1, "1", "1", "OS is shit", "3", block_type="text")


def create_activity_func(connection):

    modify_textbook(connection, 1, "12345678")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    create_block(connection, 1, "1", "1", "4", "12345678")
    create_activity(connection, 1, "1", "1", "4", "ACT0", "12345678")
    add_question(connection, 1, "1", "1", "4", "ACT0", "1", "Who is Rishi", "A", "1", "B", "2", "C", "3", "D", "4", 2)

def modify_activity_func(connection):

    modify_textbook(connection, 1, "12345678")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    print(modify_activity_add_question(connection, 1, "1", "1", "4", "ACT0", "1", "Who is Aditya", "P", "6", "Q", "7", "R", "8", "S", "9", 3, "12345678"))

    print(modify_activity_add_question(connection, 1, "1", "1", "4", "ACT1", "1", "Who is Aditya", "P", "6", "Q", "7", "R", "8", "S", "9", 3, "12345678"))

    print(modify_activity_add_question(connection, 1, "1", "1", "4", "ACT0", "2", "Who is Aditya", "P", "6", "Q", "7", "R", "8", "S", "9", 3, "12345678"))

    print(modify_activity_add_question(connection, 1, "1", "1", "4", "ACT0", "1", "Who is Rishi", "A", "1", "B", "2", "C", "3", "D", "4", 2, "12345678"))




def add_block_func_edgecases(connection):
    # Placeholder for adding block edgecases functionality
    ## add block ("2") by modifying till section - by faculty (Rishi), tb_id = 1 -- SHOULD PASS
    modify_textbook(connection, 1, "12345678")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    create_block(connection, 1, "1", "1", "5", "12345678")
    add_content(connection, 1, "1", "1", "Virtualizatio  High", "5", block_type="text")

    ## add block ("2") by modifying till section - by faculty (Rishi), tb_id = 1 -- SHOULD PASS
    modify_textbook(connection, 1, "12345678")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    create_block(connection, 1, "1", "1", "6", "12345678")
    add_content(connection, 1, "1", "1", "sample2.png", "6", block_type="picture")

    ## add block ("2") by modifying till section - by faculty (Rishi), tb_id = 1 -- SHOULD PASS
    modify_textbook(connection, 1, "12345678")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    create_block(connection, 1, "1", "1", "7", "12345678")
    create_activity(connection, 1, "1", "1", "7", "ACT2", "12345678")
    add_question(connection, 1, "1", "1", "7", "ACT2", "1", "Who is Deepak", "L", "1", "M", "2", "N", "3", "O", "4", 3)


def modify_block_func_edgecases(connection):
    # Placeholder for modifying block edgecases functionality

    # Text to Picture/Activity
    modify_textbook(connection, 1, "12378900")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    print(modify_block(connection, 1, "1", "1", "5", "12378900"))
    add_content(connection, 1, "1", "1", "sample3.png", "5", block_type="picture")

    modify_textbook(connection, 1, "12378900")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    print(modify_activity_add_question(connection, 1, "1", "1", "5", "ACT2", "1", "Who is Shashank", "P", "6", "Q", "7", "R", "8", "S", "9", 3, "12378900"))


    # Picture to Text/Activity
    modify_textbook(connection, 1, "12378900")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    print(modify_block(connection, 1, "1", "1", "6", "12378900"))
    add_content(connection, 1, "1", "1", "OS huyaaa", "6", block_type="text")

    modify_textbook(connection, 1, "12378900")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    print(modify_activity_add_question(connection, 1, "1", "1", "6", "ACT2", "1", "Who is Shashank", "P", "6", "Q", "7", "R", "8", "S", "9", 3, "12378900"))


    # Activity to Text/Picture
    modify_textbook(connection, 1, "12378900")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    print(modify_block(connection, 1, "1", "1", "7", "12378900"))
    add_content(connection, 1, "1", "1", "OS is boring", "7", block_type="text")


    modify_textbook(connection, 1, "12378900")
    modify_chapter(connection, 1, "1")
    modify_section(connection, 1, "1", "1")
    print(modify_block(connection, 1, "1", "1", "7", "12378900"))
    add_content(connection, 1, "1", "1", "sample4.png", "7", block_type="picture")


def delete_func(connection):

    # Placeholder for deleting things functionalities

    # first add chapter to tb_id = 1 and then I will start deleting one-by-one
    modify_textbook(connection, 1, "12345678")
    create_chapter(connection, 1, "2", "Abstraction", "12345678")
    create_section(connection, 1, "2", "1", "Def", "12345678")
    create_block(connection, 1, "2", "1", "1", "12345678")
    add_content(connection, 1, "2", "1", "Abstr BOO", "1", block_type = "text")

    # ## --- PASS CASES
    # delete-block
    delete_block(connection, 1, "2", "1", "1", "12345678")
    
    # delete-section
    delete_section(connection, 1, "2", "1", "12345678")

    # delete-chapter
    delete_chapter(connection, 1, "2", "12345678")

    ## --- FAIL CASES
    # delete-block
    print(delete_block(connection, 1, "2", "1", "1", "21115678"))
    
    # delete-section
    print(delete_section(connection, 1, "2", "1", "21115678"))

    # delete-chapter
    print(delete_chapter(connection, 1, "2", "21115678"))


    

def main():
    parser = argparse.ArgumentParser(description="Textbook CLI Tool")
    parser.add_argument("--action", choices=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"], help="1: Create Textbook, \
                                    2: Modify Textbook, 3: Modify Chapter, 4: Modify Section, \
                                    5: Modify Block, 6: Add block, 7: Create Activity, 8: Modify Activity, 9: Edge cases, 10: Delete operations, \
                                    11: check course details, 12: Hiding textbook entities")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Handle the actions
    if args.action == "1":
        textbook_creation_flow(connection)
    elif args.action == "2":
        modify_textbook_func(connection)
    
    elif args.action == "3":
        modify_chapter_func(connection)
    
    elif(args.action == "4"):
        modify_section_func(connection)
    
    elif(args.action == "5"):
        modify_block_func(connection)
    
    elif(args.action == "6"):
        add_block_func(connection)
    
    elif(args.action == "7"):
        create_activity_func(connection)
    
    elif(args.action == "8"):
        modify_activity_func(connection)
    
    elif(args.action == "9"):
        # add_block_func_edgecases(connection)
        modify_block_func_edgecases(connection)
    
    elif(args.action == "10"):
        delete_func(connection)
    
    elif(args.action == "11"):
        check_course_details_func(connection)
    
    elif(args.action == "12"):
        check_hide_block_func(connection)

if __name__ == "__main__":
    main()
