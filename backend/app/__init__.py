from flask import Flask
from app.config import Config
import pymysql
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(Config)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

# Initialize database connection
def get_db_connection():
    connection = pymysql.connect(
        host=app.config['DB_HOST'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        database=app.config['DB_NAME']
    )
    return connection

# Import routes to register them with the app
from app import routes
