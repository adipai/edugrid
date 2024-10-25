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
        cursor.execute("SELECT * FROM user WHERE id = %s", (user_id,))
        if cursor.fetchone():
            return 'user_exists'

        # Insert new user
        cursor.execute("INSERT INTO user (id, first_name, last_name, email, password, role)  VALUES (%s, %s, %s, %s, %s, %s)",
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
            cursor.execute("SELECT * FROM course WHERE id = %s", (course_id,))
            if cursor.fetchone():
                raise ValueError(f"Error: id {course_id} already exists in the database.")

            # SQL insert statement
            insert_query = """
            INSERT INTO course (id, course_title, faculty_id, start_date, end_date)
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
            cursor.execute("SELECT * FROM course WHERE id = %s", (course_id,))
            if cursor.fetchone():
                raise ValueError(f"Error: course_id {course_id} already exists in the database.")
            # Check if course_id already exists to avoid duplication
            cursor.execute("SELECT * FROM active_courses WHERE id = %s", (course_id,))
            if cursor.fetchone():
                raise ValueError(f"Error: course_id {course_id} already exists in the database.")

            # SQL insert statement for courses table
            insert_course_query = """
            INSERT INTO course (id, course_title, faculty_id, start_date, end_date)
            VALUES (%s, %s, %s, %s, %s)
            """
            # Execute the insert query for courses
            cursor.execute(insert_course_query, (course_id, course_name, faculty_id, start_date, end_date))

            # SQL insert statement for active_courses table
            insert_active_course_query = """
            INSERT INTO active_courses (id, course_id, unique_token, capacity)
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
            print(f"Section '{sec_name}' created in chapter ID '{chap_id}' of textbook ID '{tb_id}'.")

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
                INSERT INTO block (textbook_id, chapter_id, section_id, block_id, block_type, content, hidden_status, content, created_by)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (tb_id, chap_id, sec_id, block_id, None, None, "no", created_by)) 

            # Commit the changes
            connection.commit()
            print(f"Content block '{block_id}' created in section ID '{sec_id}' of chapter ID '{chap_id}' in textbook ID '{tb_id}'.")

    except Exception as e:
        print(f"Error creating block: {e}")
        connection.rollback()  # Rollback in case of error

def create_activity(connection, tb_id, chap_id, sec_id, block_id, activity_id):
    try:
        with connection.cursor() as cursor:
            # Check if tb_id, chap_id, sec_id, block_id and activity_id already exist in the activity table
            cursor.execute("SELECT * FROM activity WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s AND unique_activity_id = %s", 
                           (tb_id, chap_id, sec_id, block_id, activity_id))
            if cursor.fetchone():
                raise ValueError("Activity block already exists in the section.")

            # If all checks pass, insert into block
            cursor.execute("""
                INSERT INTO activity (textbook_id, chapter_id, section_id, block_id, unique_activity_id)
                VALUES (%s, %s, %s, %s, %s)
            """, (tb_id, chap_id, sec_id, block_id, activity_id)) 

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



def modify_textbook(connection, tb_id):
    """Check if the textbook exists for modification."""

    try:
        with connection.cursor() as cursor:
            # Check if tb_id exists in the textbook table
            cursor.execute("SELECT COUNT(*) FROM textbook WHERE textbook_id = %s", (tb_id,))
            count = cursor.fetchone()[0]
            
            # If tb_id does not exist, raise an error
            if count == 0:
                raise ValueError("Textbook doesn't exist, so can't modify.")

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
                raise ValueError("Chapter doesn't exist, so can't modify.")

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
                raise ValueError("Section doesn't exist, so can't modify.")

    except Exception as e:
        print(f"Error modifying section: {e}")
        connection.rollback()



def modify_block(connection, tb_id, chap_id, sec_id, block_id):
    """Check if the block exists for modification."""

    try:
        with connection.cursor() as cursor:
            # Check if block_id exists in the block table
            cursor.execute("SELECT COUNT(*) FROM block WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s", (tb_id, chap_id, sec_id, block_id))
            count = cursor.fetchone()[0]

            # If block_id does not exist, raise an error
            if count == 0:
                raise ValueError("Block doesn't exist, so can't modify.")

    except Exception as e:
        print(f"Error modifying block: {e}")
        connection.rollback()



def modify_activity(connection, tb_id, chap_id, sec_id, block_id, activity_id):
    """Check if the activity exists for modification."""

    try:
        with connection.cursor() as cursor:
            # Check if activity_id exists in the activity table
            cursor.execute("SELECT COUNT(*) FROM activity WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s AND unique_activity_id = %s", (tb_id, chap_id, sec_id, block_id, activity_id))
            count = cursor.fetchone()[0]

            # If activity_id does not exist, raise an error
            if count == 0:
                raise ValueError("Activity doesn't exist, so can't modify.")

    except Exception as e:
        print(f"Error modifying activity: {e}")
        connection.rollback()



def add_content(connection, tb_id, chap_id, sec_id, content, block_id, block_type="text"):

    """ Add text/picture content to the block """

    try:
        with connection.cursor() as cursor:
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
                raise ValueError("Question ID already exists for the activity")

            # If all checks pass, insert into block
            cursor.execute("""
                INSERT INTO question (textbook_id, chapter_id, section_id, block_id, unique_activity_id, question_id, \
                question_text, option_1, option_1_explanation, option_2, option_2_explanation, \
                option_3, option_3_explanation, option_4, option_4_explanation, answer)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (tb_id, chap_id, sec_id, block_id, activity_id, question_id, question_text, \
                option_1, option_1_explanation, option_2, option_2_explanation, \
                option_3, option_3_explanation, option_4, option_4_explanation, answer)) 

            # Commit the changes
            connection.commit()
            print(f"Question id '{question_id}' created for Activity id {activity_id}.")

    except Exception as e:
        print(f"Error creating question: {e}")
        connection.rollback()  # Rollback in case of error



# Testing textbook creation
def textbook_creation_flow(connection):
    try:
        # Step 1: Create Textbook
        tb_id = input("Enter textbook ID: ")
        textbook_title = input("Enter textbook name: ")
        create_textbook(connection, tb_id, textbook_title)

        while True:
            # Prompt for next action after textbook creation
            action = input("Choose an action: (1) Create Chapter, (2) Back to Main Menu: ")
            
            if action == "1":
                # Step 2: Create Chapter
                chap_no = int(input("Enter chapter ID: "))
                chap_title = input("Enter chapter name: ")
                create_chapter(connection, tb_id, chap_no, chap_title)

                # Step 3: Create Section
                sec_no = int(input("Enter section ID: "))
                section_title = input("Enter section name: ")
                create_section(connection, tb_id, chap_no, sec_no, section_title)

                # Step 4: Create Content Block
                block_no = int(input("Enter block ID: "))
                create_block(connection, tb_id, chap_no, sec_no, block_no)

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

def modify_textbook():
    # Placeholder for modifying textbook functionality
    print("Modify textbook functionality not yet implemented.")

def main():
    parser = argparse.ArgumentParser(description="Textbook CLI Tool")
    parser.add_argument("--action", choices=["1", "2"], help="1: Create Textbook, 2: Modify Textbook")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Handle the actions
    if args.action == "1":
        textbook_creation_flow(connection)
    elif args.action == "2":
        modify_textbook()

if __name__ == "__main__":
    main()
