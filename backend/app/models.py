def create_users_table(connection):
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        username VARCHAR(50) UNIQUE,
                        password VARCHAR(100),
                        role VARCHAR(50)
                      )''')
    connection.commit()
