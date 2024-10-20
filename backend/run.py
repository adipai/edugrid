import json
import sys
from app.routes import routes
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

app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(port=5000, debug=True)