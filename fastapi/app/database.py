import databases
import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL', 'localhost')
print(DATABASE_URL)
database = databases.Database(DATABASE_URL)
