import json
import sys

from app.utils import add_user, check_user
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    connection = pymysql.connect(
        host= os.getenv('DB_HOST', 'localhost'),
        user= os.getenv('DB_USER', 'root'),
        password= os.getenv('DB_PASSWORD', 'password'),
        database= os.getenv('DB_NAME', 'flaskdb')
    )
    return connection


app = Flask(__name__)
app.secret_key = "secret key"

cors = CORS(app, resources={r"/*": {"origins": "*"}})
connection = get_db_connection()
if not connection:
    raise Exception("Db not connected")

@app.route('/signup', methods=['POST'])
def signup():
    global connection
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    if not username or not password or not role:
        return jsonify({'error': 'Missing fields'}), 400

    result = add_user(connection, username, password, role)
    connection.close()

    if result == 'user_exists':
        return jsonify({'error': 'User already exists'}), 400
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    global connection
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')
    
    if not username or not password or not role:
        return jsonify({'error': 'Missing fields'}), 400

    user = check_user(connection, username, password, role)
    connection.close()

    if user:
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'error': 'Invalid credentials'}), 401

if __name__ == "__main__":
    app.run(port=5000, debug=True)