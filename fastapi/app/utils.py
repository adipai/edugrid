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
        WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id AND block_id = :block_id AND created_by = :created_by
    """
    
    async with database.transaction() as transaction:
        try:
            # Fetch the current content and block type
            current_data = await database.fetch_one(
                query=check_query, 
                values={"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id, "block_id": block_id}
            )

            if current_data:
                current_content, current_block_type = current_data
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
                    "block_id": block_id,
                    "created_by": created_by
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
                       option_4: str, option_4_explanation: str, answer: str):

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
    option_4_explanation: str, answer: str, user_modifying: str
):
    """Modify activity content, add a question, and delete the previous activity if it exists."""
    
    async with database.transaction() as transaction:
        try:
            # Retrieve content and type from block
            content_result = await database.fetch_one(
                query="SELECT content, block_type FROM block WHERE textbook_id = :tb_id AND chapter_id = :chap_id AND section_id = :sec_id AND block_id = :block_id",
                values={"tb_id": tb_id, "chap_id": chap_id, "sec_id": sec_id, "block_id": block_id}
            )
            
            
            content, content_type = content_result

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
    option_4_explanation: str, answer: str, user_modifying: str
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