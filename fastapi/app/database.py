import databases

DATABASE_URL = "mysql://drajend2:200537951@classdb2.csc.ncsu.edu:3306/drajend2"
# DATABASE_URL = "mysql://user:user_password@localhost:3306/mydb"

database = databases.Database(DATABASE_URL)
