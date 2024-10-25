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