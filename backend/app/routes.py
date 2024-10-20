from flask import request, Blueprint, jsonify
from app import app, get_db_connection
from app.utils import add_user, check_user
from datetime import datetime

routes = Blueprint('routes', __name__)

# Signup route
@routes.route('/signup', methods=['POST'])
def signup():
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    current_date = datetime.now()
    user_id = (first_name[:2] + last_name[:2] + current_date.strftime('%m%y')).capitalize()
    role = data.get('role')
    
    connection = get_db_connection()
    result = add_user(connection, first_name, last_name, email, password, current_date, user_id, role)
    connection.close()

    if result == 'user_exists':
        return jsonify({'error': 'User already exists'}), 400
    return jsonify({'message': 'User created successfully'}), 201

# Login route
@routes.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')
    connection = get_db_connection()
    
    
    user = check_user(connection, username, password, role)
    connection.close()

    if user:
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'error': 'Invalid credentials'}), 401
