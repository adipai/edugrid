import pymysql
import random
import string
from datetime import datetime
import traceback
import argparse

textbook_operations = ""

def get_connection():
    """Returns a new connection to the database."""
    return pymysql.connect(
        host='classdb2.csc.ncsu.edu',
        user='rsingha4',
        password='200533346',
        database='rsingha4'
    )

def add_user(connection, first_name, last_name, email, password, current_date, user_id, role):
    try:
        cursor = connection.cursor()
        # Check if user exists
        cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
        if cursor.fetchone():
            return 'user_exists'

        # Insert new user
        cursor.execute("INSERT INTO user (user_id, first_name, last_name, email, password, role, score)  VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (user_id, first_name, last_name, email, password, role, 0))
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

def create_etextbook(connection, tb_id, title):
    """Admin creates the e-textbook for the course."""

    try:
        with connection.cursor() as cursor:
            # Check if tb_id already exists to avoid duplication
            cursor.execute("SELECT * FROM e_textbook WHERE tb_id = %s", (tb_id,))
            if cursor.fetchone():
                raise ValueError(f"Error: tb_id {tb_id} already exists in the database.")
            
            # SQL insert statement
            insert_query = """
            INSERT INTO e_textbook (tb_id, title)
            VALUES (%s, %s)
            """
            
            # Execute the insert query
            cursor.execute(insert_query, (tb_id, title))
        
        # Commit the transaction
        connection.commit()
        print(f"Textbook with tb_id: {tb_id} and title: '{title}' successfully added.")
        return 'Success'

    finally:
        # Close the connection
        connection.close()

def create_evaluation_course(connection, course_id, course_name, e_textbook_id, faculty_id, start_date, end_date):
    """Admin creates a new evaluation course."""

    try:
        with connection.cursor() as cursor:
            # Check if course_id already exists to avoid duplication
            cursor.execute("SELECT * FROM courses WHERE course_id = %s", (course_id,))
            if cursor.fetchone():
                raise ValueError(f"Error: course_id {course_id} already exists in the database.")

            # SQL insert statement
            insert_query = """
            INSERT INTO courses (course_id, course_title, faculty_id, start_date, end_date)
            VALUES (%s, %s, %s, %s, %s)
            """

            # Execute the insert query
            cursor.execute(insert_query, (course_id, course_name,faculty_id, start_date, end_date))
        
        # Commit the transaction
        connection.commit()
        print(f"Evaluation Course '{course_name}' with course_id: {course_id} successfully added.")
        return 'Success'
    finally:
        # Close the connection
        connection.close()


def create_active_course(connection, course_id, course_name, e_textbook_id, faculty_id, start_date, end_date, unique_token, course_capacity):
    """Admin creates a new active course."""

    try:
        with connection.cursor() as cursor:
            # Check if course_id already exists to avoid duplication
            cursor.execute("SELECT * FROM courses WHERE course_id = %s", (course_id,))
            if cursor.fetchone():
                raise ValueError(f"Error: course_id {course_id} already exists in the database.")
            # Check if course_id already exists to avoid duplication
            cursor.execute("SELECT * FROM active_courses WHERE course_id = %s", (course_id,))
            if cursor.fetchone():
                raise ValueError(f"Error: course_id {course_id} already exists in the database.")

            # SQL insert statement for courses table
            insert_course_query = """
            INSERT INTO courses (course_id, course_title, faculty_id, start_date, end_date)
            VALUES (%s, %s, %s, %s, %s)
            """
            # Execute the insert query for courses
            cursor.execute(insert_course_query, (course_id, course_name, faculty_id, start_date, end_date))

            # SQL insert statement for active_courses table
            insert_active_course_query = """
            INSERT INTO active_courses (active_course_id, course_id, unique_token, capacity)
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

def create_textbook(connection, tb_id, tb_name):
    global textbook_operations
    textbook_operations += "C"

def create_chapter(connection, tb_id, chap_id, chap_title):
    global textbook_operations
    textbook_operations += "C"

def create_section(connection, tb_id, chap_id, sec_id, sec_name):
    global textbook_operations
    textbook_operations += "C"

def create_block(connection, block_id):
    global textbook_operations
    textbook_operations += "C"


def modify_textbook(connection, tb_id):
    global textbook_operations
    textbook_operations += "M"

def modify_chapter(connection, chap_id):
    global textbook_operations
    textbook_operations += "M"

def modify_section(connection, sec_id):
    global textbook_operations
    textbook_operations += "M"

def modify_block(connection, block_id):
    global textbook_operations
    textbook_operations += "M"



def create_text_content(connection, tb_id, chap_no, sec_no, content, textbook_title, chap_title, section_title, block_no, block_type="text"):

    """ Add text content to the section """

    global textbook_operations
    try:
        with connection.cursor() as cursor:
            
            if(textbook_operations == "CCCC"):

                # Check if tb_id exists in e_textbook table
                cursor.execute("SELECT * FROM textbook WHERE textbook_id = %s", (tb_id))
                if cursor.fetchone():
                    raise ValueError("Textbook ID already exists")

                # If all checks pass, insert into textbook, chapter, section, content tables one-by-one in order
                cursor.execute("""
                    INSERT INTO textbook (textbook_id, title)
                    VALUES (%s, %s)
                """, (tb_id, textbook_title))

                cursor.execute("""
                    INSERT INTO chapter (textbook_id, chapter_id, title, hidden_status, created_by)
                    VALUES (%s, %s, %s, %s, %s)
                """, (tb_id, chap_no, chap_title, "no", "admin"))

                cursor.execute("""
                    INSERT INTO section (textbook_id, chapter_id, section_id, title, hidden_status, created_by)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (tb_id, chap_no, sec_no, section_title, "no", "admin"))

                cursor.execute("""
                    INSERT INTO block (textbook_id, chapter_id, section_id, block_id, block_type, hidden_status, content)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (tb_id, chap_no, sec_no, block_no, block_type, "no", content))

                # Commit the transaction
                connection.commit()
            
            elif(textbook_operations == "MCCC"):
                # Check if tb_id exists in the textbook table
                cursor.execute("SELECT COUNT(*) FROM textbook WHERE textbook_id = %s", (tb_id,))
                count = cursor.fetchone()[0]
                
                # If tb_id does not exist, raise an error
                if count == 0:
                    raise ValueError("Textbook doesn't exist so can't modify")
                
                # Check if tb_id and chap_no exist in chapter table
                cursor.execute("SELECT * FROM chapter WHERE textbook_id = %s AND chapter_id = %s", (tb_id, chap_no))
                if cursor.fetchone():
                    raise ValueError("Chapter already exists in the textbook.")

                # Check if tb_id, chap_no, and sec_no exist in section table
                cursor.execute("SELECT * FROM section WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s", 
                            (tb_id, chap_no, sec_no))
                if cursor.fetchone():
                    raise ValueError("Section already exists in the chapter.")

                # Check if tb_id, chap_no, sec_no, and sequence_no already exist in content table
                cursor.execute("SELECT * FROM content WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s", 
                            (tb_id, chap_no, sec_no, block_id))
                if cursor.fetchone():
                    raise ValueError("Block already exists in the section.")

                # If all checks pass, insert into chapter, section, content tables one-by-one in order

                cursor.execute("""
                    INSERT INTO chapter (textbook_id, chapter_id, title, hidden_status, created_by)
                    VALUES (%s, %s, %s, %s, %s)
                """, (tb_id, chap_no, chap_title, "no", "admin"))

                cursor.execute("""
                    INSERT INTO section (textbook_id, chapter_id, section_id, title, hidden_status, created_by)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (tb_id, chap_no, sec_no, section_title, "no", "admin"))

                cursor.execute("""
                    INSERT INTO block (textbook_id, chapter_id, section_id, block_id, block_type, hidden_status, content)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (tb_id, chap_no, sec_no, block_no, block_type, "no", content))
                # Commit the transaction
                connection.commit()
            
            elif(textbook_operations == "MMCC"):

                # Check if tb_id exists in the textbook table
                cursor.execute("SELECT COUNT(*) FROM textbook WHERE textbook_id = %s", (tb_id,))
                count = cursor.fetchone()[0]
                
                # If tb_id does not exist, raise an error
                if count == 0:
                    raise ValueError("Textbook doesn't exist so can't modify")

                # Check if tb_id exists in the textbook table
                cursor.execute("SELECT COUNT(*) FROM chapter WHERE textbook_id = %s AND chapter_id = %s" , (tb_id,chap_no,))
                count = cursor.fetchone()[0]
                
                # If tb_id does not exist, raise an error
                if count == 0:
                    raise ValueError("Chapter doesn't exist so can't modify")

                # Check if tb_id, chap_no, and sec_no exist in section table
                cursor.execute("SELECT * FROM section WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s", 
                            (tb_id, chap_no, sec_no))
                if cursor.fetchone():
                    raise ValueError("Section already exists in the chapter.")

                # Check if tb_id, chap_no, sec_no, and sequence_no already exist in content table
                cursor.execute("SELECT * FROM content WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s", 
                            (tb_id, chap_no, sec_no, block_id))
                if cursor.fetchone():
                    raise ValueError("Block already exists in the section.")

                # If all checks pass, insert into section, content tables one-by-one in order
                cursor.execute("""
                    INSERT INTO section (textbook_id, chapter_id, section_id, title, hidden_status, created_by)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (tb_id, chap_no, sec_no, section_title, "no", "admin"))

                cursor.execute("""
                    INSERT INTO block (textbook_id, chapter_id, section_id, block_id, block_type, hidden_status, content)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (tb_id, chap_no, sec_no, block_no, block_type, "no", content))

                # Commit the transaction
                connection.commit()
            
            elif(textbook_operations == "MMMC" or textbook_operations == "MMMM"):


                # Check if tb_id exists in the textbook table
                cursor.execute("SELECT COUNT(*) FROM textbook WHERE textbook_id = %s", (tb_id,))
                count = cursor.fetchone()[0]
                
                # If tb_id does not exist, raise an error
                if count == 0:
                    raise ValueError("Textbook doesn't exist so can't modify")

                # Check if tb_id exists in the textbook table
                cursor.execute("SELECT COUNT(*) FROM chapter WHERE textbook_id = %s AND chapter_id = %s" , (tb_id,chap_no,))
                count = cursor.fetchone()[0]
                
                # If tb_id does not exist, raise an error
                if count == 0:
                    raise ValueError("Chapter doesn't exist so can't modify")

                # Check if tb_id exists in the textbook table
                cursor.execute("SELECT COUNT(*) FROM section WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s" , (tb_id,chap_no,sec_no,))
                count = cursor.fetchone()[0]
                
                # If tb_id does not exist, raise an error
                if count == 0:
                    raise ValueError("section doesn't exist so can't modify")

                # Check if tb_id, chap_no, sec_no, and sequence_no already exist in content table
                cursor.execute("SELECT * FROM content WHERE tb_id = %s AND chap_no = %s AND sec_no = %s AND sequence_no = %s", 
                            (tb_id, chap_no, sec_no, sequence_no))
                if cursor.fetchone():
                    raise ValueError("content block already exists in the section.")

                # If all checks pass, content tables one-by-one in order

                cursor.execute("""
                    INSERT INTO block (textbook_id, chapter_id, section_id, block_id, block_type, hidden_status, content)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (tb_id, chap_no, sec_no, block_no, block_type, "no", content))

                # Commit the transaction
                connection.commit()

            # elif(textbook_operations == "MMMM"):


            #     # Check if tb_id exists in the textbook table
            #     cursor.execute("SELECT COUNT(*) FROM textbook WHERE textbook_id = %s", (tb_id,))
            #     count = cursor.fetchone()[0]
                
            #     # If tb_id does not exist, raise an error
            #     if count == 0:
            #         raise ValueError("Textbook doesn't exist so can't modify")

            #     # Check if tb_id exists in the textbook table
            #     cursor.execute("SELECT COUNT(*) FROM chapter WHERE textbook_id = %s AND chapter_id = %s" , (tb_id,chap_no,))
            #     count = cursor.fetchone()[0]
                
            #     # If tb_id does not exist, raise an error
            #     if count == 0:
            #         raise ValueError("Chapter doesn't exist so can't modify")

            #     # Check if tb_id exists in the textbook table
            #     cursor.execute("SELECT COUNT(*) FROM section WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s" , (tb_id,chap_no,sec_no,))
            #     count = cursor.fetchone()[0]
                
            #     # If tb_id does not exist, raise an error
            #     if count == 0:
            #         raise ValueError("section doesn't exist so can't modify")

            #     # Check if tb_id, chap_no, sec_no, and sequence_no already exist in content table
            #     cursor.execute("SELECT * FROM content WHERE tb_id = %s AND chap_no = %s AND sec_no = %s AND sequence_no = %s", 
            #                 (tb_id, chap_no, sec_no, sequence_no))
            #     if cursor.fetchone():
            #         raise ValueError("content block already exists in the section.")

            #     # If all checks pass, content tables one-by-one in order

            #     cursor.execute("""
            #         INSERT INTO block (textbook_id, chapter_id, section_id, block_id, block_type, hidden, content)
            #         VALUES (%s, %s, %s, %s, %s, %s)
            #     """, (tb_id, chap_no, sec_no, block_no, block_type, "no", content))

            #     # Commit the transaction
            #     connection.commit()
            
            print(textbook_operations)

            textbook_operations = ""

    except Exception as e:
        connection.rollback()  # Rollback in case of an error
        print(f"Error: {e}")
        print(traceback.format_exc())
        

## create-text content test case
# create_text_content(get_connection(), 1, 1, 1, 1, "DBMS is important", "DBMS Book", "Normalization", "1NF")
# create_text_content(get_connection(), 2, 1, 1, 1, "OS is important", "OS Book", "OS Basics", "Virtualization")
# create_text_content(get_connection(), 3, 1, 1, 2, "OOPS is important", "OOPS Book", "OOPS Basics", "Abstraction")
# create_text_content(get_connection(), 3, 0, 0, 1, "OOPS is important", "OOPS Book", "OOPS Basics", "Abstraction")


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
                create_chapter(connection, chap_no, chap_title)

                # Step 3: Create Section
                sec_no = int(input("Enter section ID: "))
                section_title = input("Enter section name: ")
                create_section(connection, sec_no, section_title)

                # Step 4: Create Content Block
                block_no = int(input("Enter block ID: "))
                content = input("Enter content text: ")
                create_block(connection, block_no)
                create_text_content(connection, tb_id, chap_no, sec_no, content, textbook_title, chap_title, section_title, block_no)

                print("Content successfully added.")
                print(textbook_operations)
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
        textbook_creation_flow(get_connection())
    elif args.action == "2":
        modify_textbook()

if __name__ == "__main__":
    main()