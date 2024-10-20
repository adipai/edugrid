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

def check_user(connection, username, password, role):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s AND role = %s",
                   (username, password, role))
    user = cursor.fetchone()
    return user
