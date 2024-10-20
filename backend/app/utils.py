import pymysql
import random
import string
from datetime import datetime

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