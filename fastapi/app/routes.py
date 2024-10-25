from http.client import HTTPException
from fastapi import APIRouter
from app.utils import *
from pydantic import BaseModel

router = APIRouter()

@router.get("/")
async def hello():
    result = "Hello world"
    return {"message": result}

class LoginRequest(BaseModel):
    user_id: str
    password: str
    role: str

@router.post("/login")
async def login(login_request: LoginRequest):
    user_id = login_request.user_id
    password = login_request.password
    role = login_request.role
    
    print(user_id, password, role)
    user = await get_user(user_id, password, role)
    print(user)
    
    if user:
        return {"status": "success", "user": user}
    else:
        raise HTTPException(status_code=404, detail="User not found")
