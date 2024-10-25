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
    INSERT INTO user (user_id, first_name, last_name, email, password, role, score)  VALUES (:user_id, :first_name, :last_name, :email, :password, :role, :score)
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
                    "score": 0
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
