from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import database
from app.routes import router

app = FastAPI()

origins = ['*']

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