from datetime import datetime
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

class SignupRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    role: str

@router.post('/signup')
async def signup(signup_request: SignupRequest):
    first_name = signup_request.first_name
    last_name = signup_request.last_name
    email = signup_request.email
    password = signup_request.password
    role = signup_request.role
    
    # Get current date
    current_date = datetime.now()
    
    # Calculate user_id
    user_id = (first_name[:2] + last_name[:2] + current_date.strftime('%m%y')).capitalize()
    
    result = await add_user(first_name, last_name, email, password, current_date, user_id, role)
    
    print(result)
    
    if result == 'user_exists':
        return {'error': 'User already exists'}, 400
    elif result == 'error':
        return {'error': 'Error creating user'}, 500
    return {'message': 'User created successfully'}, 201


class CreateTextbookRequest(BaseModel):
    tb_id: int
    tb_name: str


@router.post('/create_textbook')
async def create_textbook_request(create_textbook_request: CreateTextbookRequest):
    tb_id = create_textbook_request.tb_id
    tb_name = create_textbook_request.tb_name
    
    result = await create_textbook(tb_id, tb_name)
    
    if result == 'textbook_exists':
        return {'error': 'Textbook already exists'}, 400
    elif result == 'error':
        return {'error': 'Error creating textbook'}, 500
    return {'message': 'Textbook created successfully'}, 201