from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import database
from app.routes import router

# DATABASE_URL = "mysql://drajend2:200537951@classdb2.csc.ncsu.edu:3306/drajend2"
# database = databases.Database(DATABASE_URL)

app = FastAPI()

origins = [
    '*',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect to the database when the app starts
@app.on_event("startup")
async def startup():
    print("Connecting to the database")
    await database.connect()

# # Disconnect from the database when the app shuts down
@app.on_event("shutdown")
async def shutdown():
    print("Disconnecting from the database")
    await database.disconnect() 
    
app.include_router(router)


# @app.get("/")
# async def hello():
#     return "Hello, World!"
 