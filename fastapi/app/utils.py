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

async def create_textbook(tb_id, tb_name):
    # Query to check if textbook exists
    check_query = """SELECT * FROM textbook WHERE textbook_id = :tb_id"""
    
    # Query to insert textbook
    insert_query = """
    INSERT INTO textbook (textbook_id, title) VALUES (:tb_id, :tb_name)
    """
    
    # Start a transaction
    transaction = await database.transaction()
    
    try:
        # Check if textbook exists
        existing_textbook = await database.fetch_one(query=check_query, values={"tb_id": tb_id})
        if existing_textbook:
            return "textbook_exists"
        
        # Insert textbook
        await database.execute(query=insert_query, values={"tb_id": tb_id, "tb_name": tb_name})
        
        # Commit the transaction
        await transaction.commit()
        print(f"Textbook '{tb_name}' created with ID '{tb_id}'.")
        
        return {"message": f"Textbook '{tb_name}' created with ID '{tb_id}'."}
    
    except Exception as e:
        # Rollback the transaction
        await transaction.rollback()
        print(f"Error creating textbook: {e}")
        return 'error'

async def create_course(course_id, course_name, textbook_id, course_type, faculty_id, ta_id, start_date, end_date, unique_token, capacity):
    # Query to check if course exists
    check_query = """SELECT * FROM course WHERE course_id = :course_id"""
    
    # Query to insert textbook
    insert_query = """
    INSERT INTO course (course_id, course_name, textbook_id, course_type, faculty_id, ta_id, start_date, end_date, unique_token, capacity) VALUES (:course_id, :course_name, :textbook_id, :course_type, :faculty_id, :ta_id, :start_date, :end_date, :unique_token, :capacity)
    """
    
    # Start a transaction
    transaction = await database.transaction()
    
    try:
        # Check if textbook exists
        existing_course = await database.fetch_one(query=check_query, values={"course_id": course_id})
        if existing_course:
            return "course_exists"
        
        # Insert textbook
        await database.execute(query=insert_query, values={"course_id": course_id, "course_name": course_name, "textbook_id": textbook_id, "course_type": course_type, "faculty_id": faculty_id, "ta_id": ta_id, "start_date": start_date, "end_date": end_date, "unique_token": unique_token, "capacity": capacity})
        
        # Commit the transaction
        await transaction.commit()
        print(f"Course '{course_name}' created with ID '{course_id}'.")
        
        return {"message": f"Course '{course_name}' created with ID '{course_id}'."}
    
    except Exception as e:
        # Rollback the transaction
        await transaction.rollback()
        print(f"Error creating course: {e}")
        return 'error'

async def get_textbook_details(tb_id):
    query = """
        SELECT * 
        FROM textbook 
        WHERE textbook_id = :tb_id
    """
    values = {"tb_id": tb_id}
    return await database.fetch_one(query=query, values=values)