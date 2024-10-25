import traceback
from app.database import database

async def get_user(userid: str, password: str, role: str):
    query = """
        SELECT * 
        FROM user 
        WHERE user_id = :userid 
        AND password = :password 
        AND role = :role
    """
    values = {"userid": userid, "password": password, "role": role}
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
