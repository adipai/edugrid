def add_user(connection, username, password, role):
    try:
        cursor = connection.cursor()
        # Check if user exists
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            return 'user_exists'

        # Insert new user
        cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                       (username, password, role))
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
