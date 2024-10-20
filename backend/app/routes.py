from flask import request, jsonify
from app import app, get_db_connection
from app.utils import add_user, check_user

# Signup route
@app.route('/signup', methods=['POST'])
def signup():
    print("Hello world")
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')
    
    print(username, password, role)

    if not username or not password or not role:
        return jsonify({'error': 'Missing fields'}), 400

    connection = get_db_connection()
    
    print(connection)
    result = add_user(connection, username, password, role)
    connection.close()

    if result == 'user_exists':
        return jsonify({'error': 'User already exists'}), 400
    return jsonify({'message': 'User created successfully'}), 201

# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    if not username or not password or not role:
        return jsonify({'error': 'Missing fields'}), 400

    connection = get_db_connection()
    
    
    user = check_user(connection, username, password, role)
    connection.close()

    if user:
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'error': 'Invalid credentials'}), 401
