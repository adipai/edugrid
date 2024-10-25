from flask import request, Blueprint, jsonify
from app import app, get_db_connection
from app.utils import *
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

    if result == 'user_exists':
        return jsonify({'error': 'User already exists'}), 400
    return jsonify({'message': 'User created successfully'}), 201

# Login route
@routes.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')
    
    connection = get_db_connection()
    user = check_user(connection, email, password, role)

    if user:
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'error': 'Invalid credentials'}), 401


@routes.route('/add_evaluation_course', methods=['POST'])
def add_evaluation_course():
    data = request.json
    # course_id, course_name, e_textbook_id, faculty_id, start_date, end_date are the input fields
    course_id = data.get('course_id')
    course_name = data.get('course_name')
    e_textbook_id = data.get('e_textbook_id')
    faculty_id = data.get('faculty_id')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    
    connection = get_db_connection()
    result = create_evaluation_course(connection, course_id, course_name, e_textbook_id, faculty_id, start_date, end_date)

    if result:
        return jsonify({'message': 'Evaluation course added successfully'}), 201
    return jsonify({'error': 'Evaluation course already exists'}), 400

@routes.route('/add_active_course', methods=['POST'])
def add_active_course():
    data = request.json
    # course_id, course_name, e_textbook_id, faculty_id, start_date, end_date are the input fields
    course_id = data.get('course_id')
    course_name = data.get('course_name')
    e_textbook_id = data.get('e_textbook_id')
    faculty_id = data.get('faculty_id')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    unique_token = data.get('unique_token')
    course_capacity = data.get('course_capacity')
    
    connection = get_db_connection()
    result = create_active_course(connection, course_id, course_name, e_textbook_id, faculty_id, start_date, end_date, unique_token, course_capacity)
    connection.close()

    if result:
        return jsonify({'message': 'Evaluation course added successfully'}), 201
    return jsonify({'error': 'Evaluation course already exists'}), 400

@routes.route('/content/create_text_context', methods=['POST'])
def create_text_context():
    data = request.json

    # Extract data, clean data

    # Connect to db
    connection = get_db_connection()
    
    # Run action function

    connection.close()
