import traceback
import logging
from app.database import database
from datetime import datetime
 
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
            print("no_courses_found")
            return []
        
        course_list = [dict(course) for course in courses]
        print(f"Retrieved {len(course_list)} courses for faculty ID '{faculty_id}'.")
        return course_list
    
    except Exception as e:
        # Rollback the transaction
        await transaction.rollback()
        print(f"Error retrieving courses for faculty ID '{faculty_id}': {e}")
        return []
    
async def view_courses_ta(ta_id):
    # Query to view courses exists
    courses_query = """SELECT * FROM course c
      JOIN teaching_assistant ta ON c.course_id = ta.course_id
      WHERE ta.ta_id = :ta_id"""
    # Start a transaction
    transaction = await database.transaction()
    
    try:
        courses = await database.fetch_all(query=courses_query, values={"ta_id": ta_id})
        await transaction.commit()

        if not courses:
            print("no_courses_found")
            return []
        
        course_list = [dict(course) for course in courses]
        print(f"Retrieved {len(course_list)} courses for teaching assistant ID '{ta_id}'.")
        return course_list
    
    except Exception as e:
        # Rollback the transaction
        await transaction.rollback()
        print(f"Error retrieving courses for teaching assistant ID '{ta_id}': {e}")
        return []

async def get_textbook_details(tb_id):
    query = """
        SELECT * 
        FROM textbook 
        WHERE textbook_id = :tb_id
    """
    values = {"tb_id": tb_id}
    return await database.fetch_one(query=query, values=values)

async def get_chapter_details(tb_id, chap_id):
    query = """
        SELECT * 
        FROM chapter 
        WHERE textbook_id = :tb_id AND chapter_id = :chap_id
    """
    values = {"tb_id": tb_id, "chap_id": chap_id}
    return await database.fetch_one(query=query, values=values)

async def get_section_details(tb_id, chap_id, sec_id):
    query = """
        SELECT * 
        FROM section 
        WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id
    """
    values = {"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id}
    return await database.fetch_one(query=query, values=values)

async def get_block_details(tb_id, chap_id, sec_id, block_id):
    query = """
        SELECT * 
        FROM block 
        WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id AND block_id = :block_id
    """
    values = {"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id, "block_id": block_id}
    return await database.fetch_one(query=query, values=values)

async def get_activity_details(tb_id, chap_id, sec_id, block_id, activity_id):
    query = """
        SELECT * 
        FROM activity 
        WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id AND block_id = :block_id AND unique_activity_id = :activity_id
    """
    values = {"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id, "block_id": block_id, "activity_id": activity_id}
    return await database.fetch_one(query=query, values=values)

async def get_active_course_details(course_id):
    query = """
        SELECT * 
        FROM course 
        WHERE course_id = :course_id AND course_type = "active"
    """
    values = {"course_id": course_id}
    return await database.fetch_one(query=query, values=values)

async def get_eval_course_details(course_id):
    query = """
        SELECT * 
        FROM course 
        WHERE course_id = :course_id AND course_type = 'evaluation'
    """
    values = {"course_id": course_id}
    return await database.fetch_one(query=query, values=values)

async def get_worklist(course_id):
    query = """
        SELECT * 
        FROM enrollment
        WHERE unique_course_id = :course_id AND status = "pending"
    """
    values = {"course_id": course_id}
    try:
        worklist = await database.fetch_all(query=query, values=values)
        if not worklist:
            print("no_students_found")
            return []
            
        work_list = [dict(student) for student in worklist]
        print(f"Retrieved {len(work_list)} waitlisted students for course ID '{course_id}'.")
        return work_list

    except Exception as e:
        # Rollback the transaction
        print(f"Error retrieving worklist for course ID '{course_id}': {e}")
        return []

async def get_enrolled_list(course_id):
    query = """
        SELECT * 
        FROM enrollment
        WHERE unique_course_id = :course_id AND status = "enrolled"
    """
    values = {"course_id": course_id}
    try:
        worklist = await database.fetch_all(query=query, values=values)
        if not worklist:
            print("no_students_found")
            return []
            
        work_list = [dict(student) for student in worklist]
        print(f"Retrieved {len(work_list)} enrolled students for course ID '{course_id}'.")
        return work_list

    except Exception as e:
        # Rollback the transaction
        print(f"Error retrieving enrolled for course ID '{course_id}': {e}")
        return []
    
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


async def add_content(tb_id: int, chap_id: str, sec_id: str, content: str, block_id: str, block_type: str, created_by: str):
    check_query = """
        SELECT content, block_type FROM block 
        WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id AND block_id = :block_id
    """
    delete_activity_query = """
        DELETE FROM activity WHERE textbook_id = :tb_id AND chapter_id = :chap_id 
        AND section_id = :sec_id AND block_id = :block_id AND unique_activity_id = :activity_id
    """
    update_query = """
        UPDATE block SET content = :content, block_type = :block_type 
        WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id AND block_id = :block_id
    """
    
    async with database.transaction() as transaction:
        try:
            # Fetch the current content and block type
            current_data = await database.fetch_one(
                query=check_query, 
                values={"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id, "block_id": block_id}
            )

            if current_data:
                current_content, current_block_type = current_data['content'], current_data['block_type']
                if current_block_type == "activity":
                    await database.execute(
                        query=delete_activity_query, 
                        values={"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id, "block_id": block_id, "activity_id": current_content }
                    )

            # Update the content and block type in the block table
            await database.execute(
                query=update_query, 
                values={
                    "content": content, 
                    "block_type": block_type, 
                    "tb_id": tb_id, 
                    "chap_id": chap_id, 
                    "sec_id": sec_id, 
                    "block_id": block_id
                }
            )

            return "success"

        except Exception as e:
            await transaction.rollback()
            print(f"Error adding {block_type}: {e}")
            print(traceback.format_exc())
            return "error"


async def add_question(tb_id: int, chap_id: str, sec_id: str, block_id: str, 
                       activity_id: str, question_id: str, question_text: str, 
                       option_1: str, option_1_explanation: str, option_2: str, 
                       option_2_explanation: str, option_3: str, option_3_explanation: str, 
                       option_4: str, option_4_explanation: str, answer: int):

    check_query = """
        SELECT question_id FROM question 
        WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id 
        AND block_id = :block_id AND unique_activity_id = :activity_id 
        AND question_id = :question_id
    """
    insert_query = """
        INSERT INTO question (textbook_id, chapter_id, section_id, block_id, unique_activity_id, 
                              question_id, question_text, option_1, opt_1_explanation, 
                              option_2, opt_2_explanation, option_3, opt_3_explanation, 
                              option_4, opt_4_explanation, answer) 
        VALUES (:tb_id, :chap_id, :sec_id, :block_id, :activity_id, :question_id, 
                :question_text, :option_1, :option_1_explanation, 
                :option_2, :option_2_explanation, :option_3, 
                :option_3_explanation, :option_4, :option_4_explanation, :answer)
    """

    async with database.transaction() as transaction:
        try:
            # Check if the question ID already exists for the activity
            existing_question = await database.fetch_one(
                query=check_query, 
                values={
                    "tb_id": tb_id, 
                    "chap_id": chap_id, 
                    "sec_id": sec_id, 
                    "block_id": block_id, 
                    "activity_id": activity_id, 
                    "question_id": question_id
                }
            )

            if existing_question:
                return "Question ID already exists for the activity"

            # Insert the new question into the question table
            await database.execute(
                query=insert_query, 
                values={
                    "tb_id": tb_id,
                    "chap_id": chap_id,
                    "sec_id": sec_id,
                    "block_id": block_id,
                    "activity_id": activity_id,
                    "question_id": question_id,
                    "question_text": question_text,
                    "option_1": option_1,
                    "option_1_explanation": option_1_explanation,
                    "option_2": option_2,
                    "option_2_explanation": option_2_explanation,
                    "option_3": option_3,
                    "option_3_explanation": option_3_explanation,
                    "option_4": option_4,
                    "option_4_explanation": option_4_explanation,
                    "answer": answer
                }
            )

            return "success"

        except Exception as e:
            await transaction.rollback()
            print(f"Error adding question: {e}")
            print(traceback.format_exc())
            return "error"


async def modify_textbook(tb_id: int, user_modifying: str):
    """Check if the textbook exists for modification and validate user access."""

    # Queries to check textbook existence and user access
    check_textbook_query = """
        SELECT COUNT(*) FROM textbook WHERE textbook_id = :tb_id
    """
    check_user_role_query = """
        SELECT role FROM user WHERE user_id = :user_modifying
    """
    check_faculty_access_query = """
        SELECT textbook_id FROM course WHERE faculty_id = :user_modifying
    """
    check_ta_access_query = """
        SELECT c.textbook_id
        FROM teaching_assistant t
        JOIN course c ON t.course_id = c.course_id
        WHERE t.ta_id = :user_modifying
    """

    async with database.transaction() as transaction:
        try:
            # Check if textbook exists
            count = await database.fetch_val(
                query=check_textbook_query, 
                values={"tb_id": tb_id}
            )
            if count == 0:
                return "Textbook doesn't exist, so can't modify."

            # Fetch the role of the user modifying
            modifying_user_role = await database.fetch_val(
                query=check_user_role_query, 
                values={"user_modifying": user_modifying}
            )

            # Check access based on user role
            if modifying_user_role == "faculty":
                associated_tb_id = await database.fetch_val(
                    query=check_faculty_access_query, 
                    values={"user_modifying": user_modifying}
                )
                if associated_tb_id != tb_id:
                    return "You are not associated with this course, so can't modify."

            elif modifying_user_role == "teaching assistant":
                associated_tb_id = await database.fetch_val(
                    query=check_ta_access_query, 
                    values={"user_modifying": user_modifying}
                )
                if associated_tb_id != tb_id:
                    return "You are not associated with this course, so can't modify."

            return "Textbook under modification"

        except Exception as e:
            await transaction.rollback()
            print(f"Error modifying textbook: {e}")
            print(traceback.format_exc())
            return "error"

async def modify_chapter(tb_id: int, chap_id: str):
    """Check if the chapter exists for modification."""
    check_query = """
        SELECT COUNT(*) FROM chapter WHERE textbook_id = :tb_id AND chapter_id = :chap_id
    """
    async with database.transaction() as transaction:
        try:
            count = await database.fetch_val(query=check_query, values={"tb_id": tb_id, "chap_id": chap_id})
            if count == 0:
                return "Chapter doesn't exist, so can't modify."
            return "Chapter under modification"

        except Exception as e:
            await transaction.rollback()
            print(f"Error modifying chapter: {e}")
            print(traceback.format_exc())
            return "error"


async def modify_section(tb_id: int, chap_id: str, sec_id: str):
    """Check if the section exists for modification."""
    check_query = """
        SELECT COUNT(*) FROM section WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id
    """
    async with database.transaction() as transaction:
        try:
            count = await database.fetch_val(query=check_query, values={"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id})
            if count == 0:
                return "Section doesn't exist, so can't modify."
            return "Section under modification"

        except Exception as e:
            await transaction.rollback()
            print(f"Error modifying section: {e}")
            print(traceback.format_exc())
            return "error"


async def modify_block(tb_id: int, chap_id: str, sec_id: str, block_id: str, user_modifying: str):
    """Check if the block exists for modification and verify user permissions."""
    
    check_query = """
        SELECT COUNT(*), created_by FROM block 
        WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id AND block_id = :block_id
    """
    role_query = "SELECT role FROM user WHERE user_id = :user_id"
    
    async with database.transaction() as transaction:
        try:
            # Check if block exists and get the creator
            result = await database.fetch_one(
                query=check_query,
                values={"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id, "block_id": block_id}
            )
            count, created_by = result if result else (0, None)
            
            if count == 0:
                return "Block doesn't exist, so can't modify."

            # Fetch the roles of both the user modifying and the block creator
            modifying_user_role = await database.fetch_val(query=role_query, values={"user_id": user_modifying})
            creator_user_role = await database.fetch_val(query=role_query, values={"user_id": created_by})

            # Check permissions based on roles
            if creator_user_role == "admin" and modifying_user_role != "admin":
                return "Don't have permission to modify this block added by admin"
            elif creator_user_role == "faculty" and modifying_user_role == "teaching assistant":
                return "Don't have permission to modify this block added by faculty"
            elif user_modifying != created_by and creator_user_role == "teaching assistant" and modifying_user_role == "teaching assistant":
                return "Don't have permission to modify this block added by another TA"

            return "Block under modification"

        except Exception as e:
            await transaction.rollback()
            print(f"Error modifying block: {e}")
            print(traceback.format_exc())
            return "error"



async def modify_content_add_question(
    tb_id: int, chap_id: str, sec_id: str, block_id: str, activity_id: str, question_id: str,
    question_text: str, option_1: str, option_1_explanation: str, option_2: str,
    option_2_explanation: str, option_3: str, option_3_explanation: str, option_4: str,
    option_4_explanation: str, answer: int, user_modifying: str
):
    """Modify activity content, add a question, and delete the previous activity if it exists."""
    
    async with database.transaction() as transaction:
        try:
            # Retrieve content and type from block
            content_result = await database.fetch_one(
                query="SELECT content, block_type FROM block WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id AND block_id = :block_id",
                values={"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id, "block_id": block_id}
            )
            
            
            content, content_type = content_result['content'], content_result['block_type']
            print(content_type)

            # If the content type is activity, remove previous activity if it exists
            if content_type == "activity":
                prev_activity_id = content


                # Check if activity exists in the activity table
                count = await database.fetch_val(
                    query="SELECT COUNT(*) FROM activity WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id AND block_id = :block_id AND unique_activity_id = :prev_activity_id",
                    values={"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id, "block_id": block_id, "prev_activity_id": prev_activity_id}
                )
                
                # If activity exists, delete it
                if count > 0:
                    await database.execute(
                        query="DELETE FROM activity WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id AND block_id = :block_id AND unique_activity_id = :prev_activity_id",
                        values={"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id, "block_id": block_id, "prev_activity_id": prev_activity_id}
                    )
                    print(f"Previous Activity [{prev_activity_id}] deleted.")
                    await database.execute(
                        query="UPDATE block SET content = :activity_id, block_type = 'activity' WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id AND block_id = :block_id",
                        values={"activity_id": activity_id, "tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id, "block_id": block_id}
                    )
                else:
                    return "Previous Activity does not exist."

            # If the content type is text or picture, update block content and type to 'activity'
            if content_type in ["text", "picture"]:
                await database.execute(
                    query="UPDATE block SET content = :activity_id, block_type = 'activity' WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id AND block_id = :block_id",
                    values={"activity_id": activity_id, "tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id, "block_id": block_id}
                )

            # Insert new activity
            await database.execute(
                query="INSERT INTO activity (textbook_id, chapter_id, section_id, block_id, unique_activity_id, created_by) VALUES (:tb_id, :chap_id, :sec_id, :block_id, :activity_id, :user_modifying)",
                values={"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id, "block_id": block_id, "activity_id": activity_id, "user_modifying": user_modifying}
            )

            # Insert question details
            await add_question(
                tb_id, chap_id, sec_id, block_id, activity_id, question_id, question_text,
                option_1, option_1_explanation, option_2, option_2_explanation,
                option_3, option_3_explanation, option_4, option_4_explanation, answer
            )

            
            return "Modified Activity"

        except Exception as e:
            await transaction.rollback()
            print(f"Error creating question: {e}")
            return "Error"


async def modify_activity_add_question(
    tb_id: int, chap_id: str, sec_id: str, block_id: str, activity_id: str, question_id: str,
    question_text: str, option_1: str, option_1_explanation: str, option_2: str,
    option_2_explanation: str, option_3: str, option_3_explanation: str, option_4: str,
    option_4_explanation: str, answer: int, user_modifying: str
):
    """Modify activity content by adding a new question."""
    
    async with database.transaction() as transaction:
        try:

            # Insert question details
            await add_question(
                tb_id, chap_id, sec_id, block_id, activity_id, question_id, question_text,
                option_1, option_1_explanation, option_2, option_2_explanation,
                option_3, option_3_explanation, option_4, option_4_explanation, answer
            )
            
            return "Added new Question to this activity"

        except Exception as e:
            await transaction.rollback()
            print(f"Error creating question: {e}")
            return "Error"


async def delete_chapter_async(connection, tb_id, chap_id, user_modifying):
    """ Deleting chapter asynchronously. """
    try:
        async with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*), created_by FROM chapter WHERE textbook_id = %s AND chapter_id = %s", (tb_id, chap_id))
            count, created_by = await cursor.fetchone()
            
            if count == 0:
                return "Chapter doesn't exist, so can't delete"
            
            cursor.execute("SELECT role FROM user WHERE user_id = %s", (user_modifying,))
            modifying_user_role = await cursor.fetchone()[0]

            cursor.execute("SELECT role FROM user WHERE user_id = %s", (created_by,))
            creator_user_role = await cursor.fetchone()[0]

            if creator_user_role == "admin" and modifying_user_role != "admin":
                return "Don't have permission to delete"
            elif creator_user_role == "faculty" and modifying_user_role == "teaching assistant":
                return "Don't have permission to delete"
            
            await cursor.execute("DELETE FROM chapter WHERE textbook_id = %s AND chapter_id = %s", (tb_id, chap_id))
            await connection.commit()
            return "Chapter deleted successfully"

    except Exception as e:
        print(f"Error deleting chapter: {e}")
        await connection.rollback()
        print(traceback.format_exc())
        return "An error occurred while deleting the chapter."

async def delete_section_async(connection, tb_id, chap_id, sec_id, user_modifying):
    """ Deleting section asynchronously. """
    try:
        async with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*), created_by FROM section WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s", (tb_id, chap_id, sec_id))
            count, created_by = await cursor.fetchone()
            
            if count == 0:
                return "Section doesn't exist, so can't delete"
            
            cursor.execute("SELECT role FROM user WHERE user_id = %s", (user_modifying,))
            modifying_user_role = await cursor.fetchone()[0]

            cursor.execute("SELECT role FROM user WHERE user_id = %s", (created_by,))
            creator_user_role = await cursor.fetchone()[0]

            if creator_user_role == "admin" and modifying_user_role != "admin":
                return "Don't have permission to delete"
            elif creator_user_role == "faculty" and modifying_user_role == "teaching assistant":
                return "Don't have permission to delete"
            
            await cursor.execute("DELETE FROM section WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s", (tb_id, chap_id, sec_id))
            await connection.commit()
            return "Section deleted successfully"

    except Exception as e:
        print(f"Error deleting section: {e}")
        await connection.rollback()
        print(traceback.format_exc())
        return "An error occurred while deleting the section."

async def delete_block_async(connection, tb_id, chap_id, sec_id, block_id, user_modifying):
    """ Deleting block asynchronously. """
    try:
        async with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*), created_by FROM block WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s", (tb_id, chap_id, sec_id, block_id))
            count, created_by = await cursor.fetchone()
            
            if count == 0:
                return "Block doesn't exist, so can't delete"
            
            cursor.execute("SELECT role FROM user WHERE user_id = %s", (user_modifying,))
            modifying_user_role = await cursor.fetchone()[0]

            cursor.execute("SELECT role FROM user WHERE user_id = %s", (created_by,))
            creator_user_role = await cursor.fetchone()[0]

            if creator_user_role == "admin" and modifying_user_role != "admin":
                return "Don't have permission to delete"
            elif creator_user_role == "faculty" and modifying_user_role == "teaching assistant":
                return "Don't have permission to delete"
            
            await cursor.execute("DELETE FROM block WHERE textbook_id = %s AND chapter_id = %s AND section_id = %s AND block_id = %s", (tb_id, chap_id, sec_id, block_id))
            await connection.commit()
            return "Block deleted successfully"

    except Exception as e:
        print(f"Error deleting block: {e}")
        await connection.rollback()
        print(traceback.format_exc())
        return "An error occurred while deleting the block."


async def fetch_pending_enrollments(unique_course_id: str):
    
    enrollment_query = """
    SELECT student_id, status
    FROM enrollment
    WHERE unique_course_id = :unique_course_id AND status = 'Pending'
    """
    try:
        
        enrollments = await database.fetch_all(query=enrollment_query, values={"unique_course_id": unique_course_id})
        return enrollments
    except Exception as e:
        print(f"Error fetching pending enrollments for course ID '{unique_course_id}': {e}")
        return None
    
    
async def fetch_approved_enrollments(unique_course_id: str):
    
    enrollment_query = """
    SELECT student_id, status
    FROM enrollment
    WHERE unique_course_id = :unique_course_id AND status = 'Enrolled'
    """
    try:
        enrollments = await database.fetch_all(query=enrollment_query, values={"unique_course_id": unique_course_id})
        return enrollments
    except Exception as e:
        print(f"Error fetching enrolled students for course ID '{unique_course_id}': {e}")
        return None


async def check_course_details(input_course_id: str, current_date: str, user_modifying: str):
    """Check if user can modify the course content - user should be associated with course and within end date."""
    async with database.transaction():
        try:
            # Step 1: Retrieve the role of the user from the user table
            query_role = "SELECT role FROM user WHERE user_id = :user_id"
            role_result = await database.fetch_one(query=query_role, values={"user_id": user_modifying})
            
            role = role_result["role"]

            # Step 2: Check course association and end date based on role
            if role == 'faculty':
                query_course = "SELECT * FROM course WHERE faculty_id = :faculty_id AND course_id = :course_id"
                course_data = await database.fetch_one(query=query_course, values={"faculty_id": user_modifying, "course_id": input_course_id})
                
            elif role == 'teaching assistant':
                query_course = """
                    SELECT *
                    FROM course c
                    JOIN teaching_assistant ta ON c.course_id = ta.course_id
                    WHERE ta.ta_id = :ta_id AND ta.course_id = :course_id
                """
                course_data = await database.fetch_one(query=query_course, values={"ta_id": user_modifying, "course_id": input_course_id})

            original_course_id, end_date = course_data["course_id"], course_data["end_date"]

            # Step 3: Validate course association and modification permission
            if input_course_id != original_course_id:
                return {"message": "You are not associated with this course"}

            # Convert current_date to date object and check against end_date
            current_date_obj = datetime.strptime(current_date, "%Y-%m-%d").date()
            if current_date_obj <= end_date:
                return {"message": "Modification allowed"}
            else:
                return {"message": "Beyond the end date - can't change the course!"}

        except Exception as e:
            print("An error occurred:", e)
            print(traceback.format_exc())
            return "Error"

    
async def hide_chapter(tb_id: int, chap_id: str):
    """Set hidden_status of a chapter and all following entities to 'yes'."""
    async with database.transaction():
        try:
            # Step 1: Set the chapter row to hidden
            await database.execute(
                "UPDATE chapter SET hidden_status = 'yes' WHERE textbook_id = :tb_id AND chapter_id = :chap_id",
                {"tb_id": tb_id, "chap_id": chap_id}
            )

            # Step 2: Set related sections to hidden
            await database.execute(
                "UPDATE section SET hidden_status = 'yes' WHERE textbook_id = :tb_id AND chapter_id = :chap_id",
                {"tb_id": tb_id, "chap_id": chap_id}
            )

            # Step 3: Set related blocks to hidden
            await database.execute(
                "UPDATE block SET hidden_status = 'yes' WHERE textbook_id = :tb_id AND chapter_id = :chap_id",
                {"tb_id": tb_id, "chap_id": chap_id}
            )

            # Step 4: Set related activities to hidden
            await database.execute(
                "UPDATE activity SET hidden_status = 'yes' WHERE textbook_id = :tb_id AND chapter_id = :chap_id",
                {"tb_id": tb_id, "chap_id": chap_id}
            )

            return "Chapter and related entities successfully hidden."

        except Exception as e:
            print("An error occurred:", e)
            print(traceback.format_exc())
            return "Error"


async def hide_section(tb_id: int, chap_id: str, sec_id: str):
    """Set hidden_status of a section and all following entities to 'yes'."""
    async with database.transaction():
        try:
            # Step 1: Set related sections to hidden
            await database.execute(
                "UPDATE section SET hidden_status = 'yes' WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id",
                {"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id}
            )

            # Step 2: Set related blocks to hidden
            await database.execute(
                "UPDATE block SET hidden_status = 'yes' WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id",
                {"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id}
            )

            # Step 3: Set related activities to hidden
            await database.execute(
                "UPDATE activity SET hidden_status = 'yes' WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id",
                {"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id}
            )

            return "Section and related entities successfully hidden."

        except Exception as e:
            print("An error occurred:", e)
            print(traceback.format_exc())
            return "Error"



async def hide_block(tb_id: int, chap_id: str, sec_id: str, block_id: str):
    """Set hidden_status of a block and all following entities to 'yes'."""
    async with database.transaction():
        try:
            # Step 1: Set related blocks to hidden
            await database.execute(
                "UPDATE block SET hidden_status = 'yes' WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id AND block_id = :block_id",
                {"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id, "block_id": block_id}
            )

            # Step 2: Set related activities to hidden
            await database.execute(
                "UPDATE activity SET hidden_status = 'yes' WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id AND block_id = :block_id",
                {"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id, "block_id": block_id}
            )

            return "Block and related entities successfully hidden."

        except Exception as e:
            print("An error occurred:", e)
            print(traceback.format_exc())
            return "Error"
        

async def enroll_student(course_id: str, student_id: str):
    # Query to check if the student is already enrolled
    check_enrollment_query = """
    SELECT status
    FROM enrollment
    WHERE unique_course_id = :course_id AND student_id = :student_id;
    """
    
    # Query to check course capacity
    check_capacity_query = """
    SELECT c.capacity, COUNT(e.student_id) AS enrolled_count
    FROM course AS c
    LEFT JOIN enrollment AS e ON c.course_id = e.unique_course_id AND e.status = 'Enrolled'
    WHERE c.course_id = :course_id
    GROUP BY c.capacity
    HAVING enrolled_count < c.capacity;
    """
    
    # Query to update enrollment status
    update_status_query = """
    UPDATE enrollment
    SET status = 'Enrolled'
    WHERE unique_course_id = :course_id AND student_id = :student_id AND status = 'Pending';
    """
    
    async with database.transaction() as transaction:
        try:
            # Step 1: Check if the student is already enrolled
            enrollment_status = await database.fetch_one(
                query=check_enrollment_query,
                values={"course_id": course_id, "student_id": student_id}
            )

            if enrollment_status:
                if enrollment_status["status"] == 'Enrolled':
                    return "already_enrolled"

            # Step 2: Check if the course has capacity
            capacity_available = await database.fetch_one(
                query=check_capacity_query,
                values={"course_id": course_id}
            )

            if not capacity_available:
                return "at_capacity"

            # Step 3: Update the status to 'Enrolled'
            await database.execute(
                query=update_status_query,
                values={"course_id": course_id, "student_id": student_id}
            )

            # Commit the transaction
            return "enrolled"

        except Exception as e:
            # Rollback the transaction in case of error
            await transaction.rollback()
            print(f"Error enrolling student: {e}")
            return "error"
        
# Function for student joining a waitlist        
async def process_enrollment(first_name: str, last_name: str, email: str, course_token: str, password: str):
    try:
        # Step 1: Check if the student exists in the 'user' table
        check_student_query = "SELECT user_id FROM user WHERE email = :email;"
        user = await database.fetch_one(query=check_student_query, values={"email": email})
        
        if user:
            # Student exists, use existing user_id
            user_id = user["user_id"]
        else:
            # Generate new user_id based on the template
            current_date = datetime.now()
            user_id = (first_name[:2] + last_name[:2] + current_date.strftime('%m%y')).capitalize()

            # Insert into 'user' and 'student' tables
            insert_user_query = """
            INSERT INTO user (user_id, first_name, last_name, email, password, role)
            VALUES (:user_id, :first_name, :last_name, :email, :password, 'student');
            """
            await database.execute(query=insert_user_query, values={
                "user_id": user_id,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "password": password
            })

            insert_student_query = """
            INSERT INTO student (student_id, full_name, password, email)
            VALUES (:student_id, :full_name, :password, :email);
            """
            full_name = f"{first_name} {last_name}"
            await database.execute(query=insert_student_query, values={
                "student_id": user_id,
                "full_name": full_name,
                "password": password,
                "email": email
            })

        # Step 2: Get course_id using the course_token
        get_course_query = "SELECT course_id FROM course WHERE unique_token = :course_token;"
        course = await database.fetch_one(query=get_course_query, values={"course_token": course_token})

        if not course:
            return {"status": "course_not_found"}

        course_id = course["course_id"]

        # Step 3: Check if student is already enrolled in the course
        check_enrollment_query = """
        SELECT 1 FROM enrollment WHERE unique_course_id = :course_id AND student_id = :student_id;
        """
        enrollment = await database.fetch_one(query=check_enrollment_query, values={
            "course_id": course_id,
            "student_id": user_id
        })

        if enrollment:
            return {"status": "already_enrolled"}

        # Step 4: Enroll student in the course
        enroll_student_query = """
        INSERT INTO enrollment (unique_course_id, student_id, status)
        VALUES (:course_id, :student_id, 'Pending');
        """
        await database.execute(query=enroll_student_query, values={
            "course_id": course_id,
            "student_id": user_id
        })

        return {"status": "enrollment_success", "user_id": user_id, "course_id": course_id}

    except Exception as e:
        return {"status": "error", "detail": str(e)}
    
    
async def fetch_student_activity_summary(student_id: str, course_id: str):
    """Retrieve total points and total activities attempted for a student in a course."""
    try:
        # SQL query to get activity summary
        activity_summary_query = """
        SELECT 
            course_id,
            SUM(point) AS total_points,
            COUNT(DISTINCT unique_activity_id) AS total_activities_attempted
        FROM 
            participation
        WHERE 
            student_id = :student_id AND course_id = :course_id
        GROUP BY 
            student_id, 
            course_id;
        """

        # Execute query with provided student_id and course_id
        result = await database.fetch_one(query=activity_summary_query, values={"student_id": student_id, "course_id": course_id})

        # If result exists, return it as a dictionary
        if result:
            return {
                "course_id": result["course_id"],
                "total_points": result["total_points"],
                "total_activities_attempted": result["total_activities_attempted"]
            }
        else:
            return "no_records"  # No records found

    except Exception as e:
        print(f"Error retrieving activity summary: {e}")
        return "error"  



async def fetch_text_picture_block(tb_id: int, chap_id: str, sec_id: str, block_id: str):
    """Fetch content for text or picture block types based on the provided IDs."""
    try:
        content_result = await database.fetch_one(
            """
            SELECT content 
            FROM block 
            WHERE textbook_id = :tb_id 
              AND chapter_id = :chap_id 
              AND section_id = :sec_id 
              AND block_id = :block_id
            """,
            {"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id, "block_id": block_id}
        )

        if content_result:
            return content_result

        return "No content found for the specified block."

    except Exception as e:
        print("An error occurred:", e)
        return "Error retrieving content"


async def fetch_activity_block(tb_id: int, chap_id: str, sec_id: str, block_id: str):
    """Fetch questions for activity block types based on the provided IDs."""
    try:
        # Step 1: Fetch unique activity identifier (block_content)
        block_content = await database.fetch_one(
            """
            SELECT content
            FROM block 
            WHERE textbook_id = :tb_id 
              AND chapter_id = :chap_id 
              AND section_id = :sec_id 
              AND block_id = :block_id
            """,
            {"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id, "block_id": block_id}
        )

        if not block_content:
            return "Block content not found."
        
        activity_id = block_content[0]

        # Step 2: Fetch questions related to the unique activity ID
        questions = await database.fetch_all(
            """
            SELECT question_id, question_text, option_1, opt_1_explanation, 
                   option_2, opt_2_explanation, option_3, opt_3_explanation, 
                   option_4, opt_4_explanation, answer 
            FROM question 
            WHERE textbook_id = :tb_id 
              AND chapter_id = :chap_id 
              AND section_id = :sec_id 
              AND block_id = :block_id 
              AND unique_activity_id = :unique_activity_id
            ORDER BY question_id
            """,
            {
                "tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id, 
                "block_id": block_id, "unique_activity_id": activity_id
            }
        )
        if questions:
            return {"activity_id": activity_id, "questions":questions}
        return "No questions found for the specified block."

    except Exception as e:
        print("An error occurred:", e)
        return "Error retrieving questions"

async def fetch_content(tb_id: int, chap_id: str, sec_id: str):
    """Fetch block_id and block_type from block table with hidden_status as 'no' and ordered by sequence_no."""
    try:
        # Step 1: Check if the chapter exists and is not hidden
        chapter_result = await database.fetch_one(
            """
            SELECT hidden_status 
            FROM chapter 
            WHERE textbook_id = :tb_id AND chapter_id = :chap_id
            """,
            {"tb_id": tb_id, "chap_id": chap_id}
        )
        if not chapter_result:
            return "Chapter does not exist."
        if chapter_result["hidden_status"] == 'yes':
            return "Chapter is hidden."

        # Step 2: Check if the section exists and is not hidden
        section_result = await database.fetch_one(
            """
            SELECT hidden_status 
            FROM section 
            WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id
            """,
            {"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id}
        )
        if not section_result:
            return "Section does not exist."
        if section_result["hidden_status"] == 'yes':
            return "Section is hidden."

        # Step 3: Fetch block_id and block_type with hidden_status as 'no' ordered by sequence_no
        blocks = await database.fetch_all(
            """
            SELECT block_id, block_type 
            FROM block 
            WHERE textbook_id = :tb_id 
              AND chapter_id = :chap_id 
              AND section_id = :sec_id 
              AND hidden_status = 'no' 
            ORDER BY sequence_no
            """,
            {"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id}
        )

        return blocks if blocks else "No visible blocks found in the specified section."

    except Exception as e:
        print("An error occurred:", e)
        return "Error retrieving content."
    

async def get_student_courses_and_textbooks(student_id: str):
    
    """Fetch a list of course IDs and associated textbook IDs for a given student."""

    query = """
    SELECT 
        enrollment.unique_course_id AS course_id,
        course.textbook_id
    FROM 
        enrollment
    JOIN 
        course ON enrollment.unique_course_id = course.course_id
    WHERE 
        enrollment.student_id = :student_id 
        AND enrollment.status = 'Enrolled';
    """

    values = {"student_id": student_id}
    results = await database.fetch_all(query=query, values=values)

    # Format results as a list of dictionaries
    if results:
        return [{"course_id": result["course_id"], "textbook_id": result["textbook_id"]} for result in results]
    else:
        return None


async def insert_participation_record(entry):
    """Insert a participation record into the database."""
    
    point = 3 if entry.correct else 1

    query = """
    INSERT INTO participation (
        student_id, course_id, textbook_id, section_id, chapter_id, 
        block_id, unique_activity_id, question_id, point, attempted_timestamp
    )
    VALUES (
        :student_id, :course_id, :textbook_id, :section_id, :chapter_id, 
        :block_id, :unique_activity_id, :question_id, :point, :timestamp
    )
    """

    values = {
        "student_id": entry.student_id,
        "course_id": entry.course_id,
        "textbook_id": entry.textbook_id,
        "section_id": entry.section_id,
        "chapter_id": entry.chapter_id,
        "block_id": entry.block_id,
        "unique_activity_id": entry.unique_activity_id,
        "question_id": entry.question_id,
        "point": point,
        "timestamp": datetime.now()
    }

    try:
        await database.execute(query=query, values=values)
        return True
    except Exception as e:
        print(f"Error inserting participation record: {e}")
        return False
    
class NotificationResponse(BaseModel):
    notification_message: str
    timestamp: datetime

# Utility function to fetch notifications
async def fetch_notifications(user_id: str):
    query = """
        SELECT notification_message, timestamp
        FROM notification
        WHERE user_id = :user_id
        ORDER BY timestamp DESC
    """
    values = {"user_id": user_id}

    # Start a transaction
    transaction = await database.transaction()

    try:
        notifications = await database.fetch_all(query=query, values=values)
        await transaction.commit()

        if notifications:
            return [
                NotificationResponse(
                    notification_message=notification["notification_message"],
                    timestamp=notification["timestamp"]
                )
                for notification in notifications
            ]
        else:
            print(f"No notifications found for user ID '{user_id}'.")
            return []

    except Exception as e:
        # Rollback transaction in case of error
        await transaction.rollback()
        print(f"Error retrieving notifications for user ID '{user_id}': {e}")
        return []