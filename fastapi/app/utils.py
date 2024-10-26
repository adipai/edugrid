import traceback
from app.database import database

async def get_user(user_id: str, password: str, role: str):
    query = """
        SELECT * 
        FROM user 
        WHERE user_id = :user_id 
        AND password = :password 
        AND role = :role
    """
    values = {"user_id": user_id, "password": password, "role": role}
    return await database.fetch_one(query=query, values=values)

async def add_user(first_name, last_name, email, password, current_date, user_id, role):
    # query to check if user exists
    check_query = "SELECT * FROM user WHERE user_id = :user_id"
    
    # query to insert user
    query = """
    INSERT INTO user (user_id, first_name, last_name, email, password, role)  VALUES (:user_id, :first_name, :last_name, :email, :password, :role)
    """
    
    # Start a transaction
    transaction = await database.transaction()
    
    try:
        check_values = {"user_id": user_id}
        
        values  = {
                    "user_id": user_id,
                    "first_name": first_name, 
                    "last_name": last_name, 
                    "email": email, 
                    "password": password,
                    "role": role,
                   }
        
        # Check if user exists
        existing_user = await database.fetch_one(query=check_query, values=check_values)
        if existing_user:
            return 'user_exists'

        # Insert user
        user = await database.execute(query=query, values=values)
        
        # Commit the transaction
        await transaction.commit()
        return user 
    except Exception as e:
        # Rollback the transaction
        await transaction.rollback()
        print(f"Error: {e}")
        
        traceback.print_exc()
        # Return error
        return 'error'

async def change_password(user_id, old_password, new_password):  
    # query to update password
    query = """
    UPDATE user 
    SET password = :new_password
    WHERE user_id = :user_id AND password = :old_password        
    """
    
    # Start a transaction
    transaction = await database.transaction()
    
    try:
        values  = {
                    "user_id": user_id,
                    "new_password": new_password, 
                    "old_password": old_password
                   }
        
        # Update password
        user = await database.execute(query=query, values=values)
        
        # Commit the transaction
        await transaction.commit()
        return user 
    except Exception as e:
        # Rollback the transaction
        await transaction.rollback()
        print(f"Error: {e}")
        
        traceback.print_exc()
        # Return error
        return 'error'

async def add_faculty(first_name, last_name, email, password, current_date, user_id, role):
    # query to check if user exists
    check_query = "SELECT * FROM user WHERE user_id = :user_id"
    
    # query to insert user
    insert_user_query = """
    INSERT INTO user (user_id, first_name, last_name, email, password, role)  VALUES (:user_id, :first_name, :last_name, :email, :password, :role)
    """
    insert_faculty_query = """
    INSERT INTO faculty (faculty_id, first_name, last_name, email, password)  VALUES (:user_id, :first_name, :last_name, :email, :password)
    """
    # Start a transaction
    transaction = await database.transaction()
    
    try:
        check_values = {"user_id": user_id}
        
        user_values  = {
                    "user_id": user_id,
                    "first_name": first_name, 
                    "last_name": last_name, 
                    "email": email, 
                    "password": password,
                    "role": role,
                   }
        
        faculty_values  = {
                    "user_id": user_id,
                    "first_name": first_name, 
                    "last_name": last_name, 
                    "email": email, 
                    "password": password,
                   }
        
        # Check if user exists
        existing_user = await database.fetch_one(query=check_query, values=check_values)
        if existing_user:
            return 'user_exists'

        # Insert user
        user = await database.execute(query=insert_user_query, values=user_values)
        # Insert faculty
        faculty = await database.execute(query=insert_faculty_query, values=faculty_values)
        
        # Commit the transaction
        await transaction.commit()
        return faculty 
    except Exception as e:
        # Rollback the transaction
        await transaction.rollback()
        print(f"Error: {e}")
        
        traceback.print_exc()
        # Return error
        return 'error'

async def add_ta(first_name, last_name, email, password, current_date, user_id, role, course_id):
    # query to check if user exists
    check_query = "SELECT * FROM user WHERE user_id = :user_id"
    
    # query to insert user
    insert_user_query = """
    INSERT INTO user (user_id, first_name, last_name, email, password, role)  VALUES (:user_id, :first_name, :last_name, :email, :password, :role)
    """
    insert_ta_query = """
    INSERT INTO teaching_assistant (ta_id, first_name, last_name, email, password, course_id)  VALUES (:user_id, :first_name, :last_name, :email, :password, :course_id)
    """
    # Start a transaction
    transaction = await database.transaction()
    
    try:
        check_values = {"user_id": user_id}
        
        user_values  = {
                    "user_id": user_id,
                    "first_name": first_name, 
                    "last_name": last_name, 
                    "email": email, 
                    "password": password,
                    "role": role,
                   }
        
        ta_values  = {
                    "user_id": user_id,
                    "first_name": first_name, 
                    "last_name": last_name, 
                    "email": email, 
                    "password": password,
                    "course_id": course_id,
                   }
        
        # Check if user exists
        existing_user = await database.fetch_one(query=check_query, values=check_values)
        if existing_user:
            return 'user_exists'

        # Insert user
        user = await database.execute(query=insert_user_query, values=user_values)
        # Insert faculty
        faculty = await database.execute(query=insert_ta_query, values=ta_values)
        
        # Commit the transaction
        await transaction.commit()
        return faculty 
    except Exception as e:
        # Rollback the transaction
        await transaction.rollback()
        print(f"Error: {e}")
        
        traceback.print_exc()
        # Return error
        return 'error'

async def add_student(first_name, last_name, email, password, current_date, user_id, role, username):
    # query to check if user exists
    check_query = "SELECT * FROM user WHERE user_id = :user_id"
    
    # query to insert user
    insert_user_query = """
    INSERT INTO user (user_id, first_name, last_name, email, password, role)  VALUES (:user_id, :first_name, :last_name, :email, :password, :role)
    """
    insert_student_query = """
    INSERT INTO student (student_id, full_name, email, password, username)  VALUES (:user_id, :full_name, :email, :password, :username)
    """
    # Start a transaction
    transaction = await database.transaction()
    
    try:
        check_values = {"user_id": user_id}
        
        user_values  = {
                    "user_id": user_id,
                    "first_name": first_name, 
                    "last_name": last_name, 
                    "email": email, 
                    "password": password,
                    "role": role,
                   }
        
        student_values  = {
                    "user_id": user_id,
                    "full_name": first_name+last_name, 
                    "email": email, 
                    "password": password,
                    "username": username,
                   }
        
        # Check if user exists
        existing_user = await database.fetch_one(query=check_query, values=check_values)
        if existing_user:
            return 'user_exists'

        # Insert user
        user = await database.execute(query=insert_user_query, values=user_values)
        # Insert faculty
        faculty = await database.execute(query=insert_student_query, values=student_values)
        
        # Commit the transaction
        await transaction.commit()
        return faculty 
    except Exception as e:
        # Rollback the transaction
        await transaction.rollback()
        print(f"Error: {e}")
        
        traceback.print_exc()
        # Return error
        return 'error'

async def create_course(course_id, course_name, textbook_id, course_type, faculty_id, start_date, end_date, unique_token, capacity):
    # Query to check if course exists
    check_query = """SELECT * FROM course WHERE course_id = :course_id"""
    
    # Query to insert course
    insert_query = """
    INSERT INTO course (course_id, course_name, textbook_id, course_type, faculty_id, start_date, end_date, unique_token, capacity) VALUES (:course_id, :course_name, :textbook_id, :course_type, :faculty_id, :start_date, :end_date, :unique_token, :capacity)
    """
    
    # Start a transaction
    transaction = await database.transaction()
    
    try:
        # Check if textbook exists
        existing_course = await database.fetch_one(query=check_query, values={"course_id": course_id})
        if existing_course:
            return "course_exists"
        
        # Insert textbook
        await database.execute(query=insert_query, values={"course_id": course_id, "course_name": course_name, "textbook_id": textbook_id, "course_type": course_type, "faculty_id": faculty_id, "start_date": start_date, "end_date": end_date, "unique_token": unique_token, "capacity": capacity})
        
        # Commit the transaction
        await transaction.commit()
        print(f"Course '{course_name}' created with ID '{course_id}'.")
        
        return {"message": f"Course '{course_name}' created with ID '{course_id}'."}
    
    except Exception as e:
        # Rollback the transaction
        await transaction.rollback()
        print(f"Error creating course: {e}")
        return 'error'

async def view_courses_faculty(faculty_id):
    # Query to view courses exists
    courses_query = """SELECT * FROM course WHERE faculty_id = :faculty_id"""
    # Start a transaction
    transaction = await database.transaction()
    
    try:
        courses = await database.fetch_all(query=courses_query, values={"faculty_id": faculty_id})
        await transaction.commit()

        if not courses:
            return "no_courses_found"
        
        course_list = [dict(course) for course in courses]
        print(f"Retrieved {len(course_list)} courses for faculty ID '{faculty_id}'.")
        return course_list
    
    except Exception as e:
        # Rollback the transaction
        await transaction.rollback()
        print(f"Error retrieving courses for faculty ID '{faculty_id}': {e}")
        return 'error'
    
async def view_courses_ta(ta_id):
    # Query to view courses exists
    courses_query = """SELECT c.course_id, c.course_name FROM course c
      JOIN teaching_assistant ta ON c.course_id = ta.course_id
      WHERE ta.ta_id = :ta_id"""
    # Start a transaction
    transaction = await database.transaction()
    
    try:
        courses = await database.fetch_all(query=courses_query, values={"ta_id": ta_id})
        await transaction.commit()

        if not courses:
            return "no_courses_found"
        
        course_list = [dict(course) for course in courses]
        print(f"Retrieved {len(course_list)} courses for teaching assistant ID '{ta_id}'.")
        return course_list
    
    except Exception as e:
        # Rollback the transaction
        await transaction.rollback()
        print(f"Error retrieving courses for teaching assistant ID '{ta_id}': {e}")
        return 'error'

async def get_textbook_details(tb_id):
    query = """
        SELECT * 
        FROM textbook 
        WHERE textbook_id = :tb_id
    """
    values = {"tb_id": tb_id}
    return await database.fetch_one(query=query, values=values)

"""
TEXTBOOK MODULE
"""
async def create_textbook(tb_id: int, tb_name: str, created_by: str):
    # Query to check if textbook exists
    check_query = "SELECT * FROM textbook WHERE textbook_id = :tb_id"
    
    # Query to insert textbook
    insert_query = """
    INSERT INTO textbook (textbook_id, title, created_by)
    VALUES (:tb_id, :tb_name, :created_by)
    """
    
    # Start a transaction
    transaction = await database.transaction()
    
    try:
        # Check if textbook exists
        existing_textbook = await database.fetch_one(query=check_query, values={"tb_id": tb_id})
        if existing_textbook:
            return "textbook_exists"
        
        # Insert textbook
        await database.execute(
            query=insert_query, 
            values={"tb_id": tb_id, "tb_name": tb_name, "created_by": created_by}
        )
        
        # Commit the transaction
        await transaction.commit()
        
        return "success"
    
    except Exception as e:
        # Rollback the transaction in case of error
        await transaction.rollback()
        print(f"Error creating textbook: {e}")
        return 'error'


async def create_chapter(tb_id: int, chap_id: str, chap_title: str, created_by: str):
    # Query to check if the chapter already exists in the textbook
    check_query = """
    SELECT * FROM chapter WHERE textbook_id = :tb_id AND chapter_id = :chap_id
    """
    
    # Query to insert a new chapter
    insert_query = """
    INSERT INTO chapter (textbook_id, chapter_id, title, hidden_status, created_by)
    VALUES (:tb_id, :chap_id, :chap_title, :hidden_status, :created_by)
    """
    
    # Start a transaction
    transaction = await database.transaction()
    
    try:
        # Check if the chapter already exists
        existing_chapter = await database.fetch_one(
            query=check_query,
            values={"tb_id": tb_id, "chap_id": chap_id}
        )
        if existing_chapter:
            return "chapter_exists"
        
        # Insert the new chapter with a default hidden status of "no"
        await database.execute(
            query=insert_query,
            values={"tb_id": tb_id, "chap_id": chap_id, "chap_title": chap_title, "hidden_status": "no", "created_by": created_by}
        )
        
        # Commit the transaction
        await transaction.commit()
        
        return "success"
    
    except Exception as e:
        # Rollback the transaction in case of error
        await transaction.rollback()
        print(f"Error creating chapter: {e}")
        return 'error'

async def create_section(tb_id: int, chap_id: str, sec_id: str, sec_name: str, created_by: str):
    # Query to check if the section already exists in the chapter
    check_query = """
    SELECT * FROM section WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id
    """
    
    # Query to insert a new section
    insert_query = """
    INSERT INTO section (textbook_id, chapter_id, section_id, title, hidden_status, created_by)
    VALUES (:tb_id, :chap_id, :sec_id, :sec_name, :hidden_status, :created_by)
    """
    
    # Start a transaction
    transaction = await database.transaction()
    
    try:
        # Check if the section already exists
        existing_section = await database.fetch_one(
            query=check_query,
            values={"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id}
        )
        if existing_section:
            return "section_exists"
        
        # Insert the new section with a default hidden status of "no"
        await database.execute(
            query=insert_query,
            values={
                "tb_id": tb_id,
                "chap_id": chap_id,
                "sec_id": sec_id,
                "sec_name": sec_name,
                "hidden_status": "no",
                "created_by": created_by
            }
        )
        
        # Commit the transaction
        await transaction.commit()
        
        return "success"
    
    except Exception as e:
        # Rollback the transaction in case of error
        await transaction.rollback()
        print(f"Error creating section: {e}")
        return 'error'
    
async def create_block(tb_id: int, chap_id: str, sec_id: str, block_id: str, created_by: str):
    # Query to check if the content block already exists in the section
    check_query = """
    SELECT * FROM block WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id AND block_id = :block_id
    """
    
    # Query to insert a new content block
    insert_query = """
    INSERT INTO block (textbook_id, chapter_id, section_id, block_id, block_type, content, hidden_status, created_by)
    VALUES (:tb_id, :chap_id, :sec_id, :block_id, :block_type, :content, :hidden_status, :created_by)
    """
    
    # Start a transaction
    transaction = await database.transaction()
    
    try:
        # Check if the content block already exists
        existing_block = await database.fetch_one(
            query=check_query,
            values={"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id, "block_id": block_id}
        )
        if existing_block:
            return "block_exists"
        
        # Insert the new content block with default values for block_type and content, and a hidden status of "no"
        await database.execute(
            query=insert_query,
            values={
                "tb_id": tb_id,
                "chap_id": chap_id,
                "sec_id": sec_id,
                "block_id": block_id,
                "block_type": None,
                "content": None,
                "hidden_status": "no",
                "created_by": created_by
            }
        )
        
        # Commit the transaction
        await transaction.commit()
        
        return "success"
    
    except Exception as e:
        # Rollback the transaction in case of error
        await transaction.rollback()
        print(f"Error creating block: {e}")
        return 'error'


async def create_activity(tb_id: int, chap_id: str, sec_id: str, block_id: str, activity_id: str, created_by: str):
    # Query to check if the activity block already exists in the section
    check_query = """
    SELECT * FROM activity WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id AND block_id = :block_id AND unique_activity_id = :activity_id
    """
    
    # Query to insert a new activity block
    insert_query = """
    INSERT INTO activity (textbook_id, chapter_id, section_id, block_id, unique_activity_id, created_by)
    VALUES (:tb_id, :chap_id, :sec_id, :block_id, :activity_id, :created_by)
    """
    
    # Query to update the content and block type in the block table
    update_query = """
    UPDATE block
    SET content = :activity_id, block_type = 'activity'
    WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id AND block_id = :block_id
    """
    
    # Start a transaction
    transaction = await database.transaction()
    
    try:
        # Check if the activity block already exists
        existing_activity = await database.fetch_one(
            query=check_query,
            values={"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id, "block_id": block_id, "activity_id": activity_id}
        )
        if existing_activity:
            return "activity_exists"
    
        # Update the content and block type in the block table
        await database.execute(
            query=update_query,
            values={
                "activity_id": activity_id,
                "tb_id": tb_id,
                "chap_id": chap_id,
                "sec_id": sec_id,
                "block_id": block_id
            }
        )
        
        # Insert the new activity block
        await database.execute(
            query=insert_query,
            values={
                "tb_id": tb_id,
                "chap_id": chap_id,
                "sec_id": sec_id,
                "block_id": block_id,
                "activity_id": activity_id,
                "created_by": created_by
            }
        )
        
        # Commit the transaction
        await transaction.commit()
        
        return "success"
    
    except Exception as e:
        # Rollback the transaction in case of error
        await transaction.rollback()
        print(f"Error creating activity block: {e}")
        return 'error'
