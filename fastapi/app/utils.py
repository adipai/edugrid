import traceback
from app.database import database

async def get_user(email: str, password: str, role: str):
    query = """
        SELECT * 
        FROM user 
        WHERE email = :email 
        AND password = :password 
        AND role = :role
    """
    values = {"email": email, "password": password, "role": role}
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
            return existing_user

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
            return existing_user

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