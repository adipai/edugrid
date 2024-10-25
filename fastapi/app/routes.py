from datetime import datetime
from fastapi import APIRouter, HTTPException
from app.utils import *
from pydantic import BaseModel

router = APIRouter()

@router.get("/")
async def hello():
    result = "Hello world"
    return {"message": result}

class LoginRequest(BaseModel):
    email: str
    password: str
    role: str

@router.post("/login", status_code=201)
async def login(login_request: LoginRequest):
    user_id = login_request.email
    password = login_request.password
    role = login_request.role
    
    user = await get_user(user_id, password, role)
    
    if user:
        return {"status": "success", "user": user}
    else:
        raise HTTPException(status_code=404, detail="User not found")

class AddUserRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    role: str

@router.post('/add_user', status_code=201)
async def addUser(add_user_request: AddUserRequest):
    first_name = add_user_request.first_name
    last_name = add_user_request.last_name
    email = add_user_request.email
    password = add_user_request.password
    role = add_user_request.role
    
    # Get current date
    current_date = datetime.now()
    
    # Calculate user_id
    user_id = (first_name[:2] + last_name[:2] + current_date.strftime('%m%y')).capitalize()
    
    result = await add_user(first_name, last_name, email, password, current_date, user_id, role)
    
    print(result)
    
    if result == 'user_exists':
        raise HTTPException(status_code=409, detail="User already exists")
    elif result == 'error':
        raise HTTPException(status_code=500, detail="Error creating user")
    return {'message': 'User created successfully'}

@router.post('/add_faculty',status_code=201)
async def addFaculty(add_user_request: AddUserRequest):
    first_name = add_user_request.first_name
    last_name = add_user_request.last_name
    email = add_user_request.email
    password = add_user_request.password
    role = "faculty"
    
    # Get current date
    current_date = datetime.now()
    
    # Calculate user_id
    user_id = (first_name[:2] + last_name[:2] + current_date.strftime('%m%y')).capitalize()
    
    result = await add_faculty(first_name, last_name, email, password, current_date, user_id, role)
    
    print(result)
    
    if result == 'user_exists':
        raise HTTPException(status_code=409, detail="User already exists")
    elif result == 'error':
        raise HTTPException(status_code=500, detail="Error creating user")
    return {'message': 'User created successfully'}

class AddTaRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    course_id: str

@router.post('/add_ta',status_code=201)
async def addTa(add_ta_request: AddTaRequest):
    first_name = add_ta_request.first_name
    last_name = add_ta_request.last_name
    email = add_ta_request.email
    password = add_ta_request.password
    course_id = add_ta_request.course_id
    role = "teaching assistant"
    
    # Get current date
    current_date = datetime.now()
    
    # Calculate user_id
    user_id = (first_name[:2] + last_name[:2] + current_date.strftime('%m%y')).capitalize()
    
    result = await add_ta(first_name, last_name, email, password, current_date, user_id, role, course_id)
    
    print(result)
    
    if result == 'user_exists':
        raise HTTPException(status_code=409, detail="User already exists")
    elif result == 'error':
        raise HTTPException(status_code=500, detail="Error creating user")
    return {'message': 'User created successfully'}

class AddStudentRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    username: str
    password: str
    
@router.post('/add_student',status_code=201)
async def addTa(add_student_request: AddStudentRequest):
    first_name = add_student_request.first_name
    last_name = add_student_request.last_name
    email = add_student_request.email
    password = add_student_request.password
    username = add_student_request.username
    role = "student"
    
    # Get current date
    current_date = datetime.now()
    
    # Calculate user_id
    user_id = (first_name[:2] + last_name[:2] + current_date.strftime('%m%y')).capitalize()
    
    result = await add_student(first_name, last_name, email, password, current_date, user_id, role, username)
    
    print(result)
    
    if result == 'user_exists':
        raise HTTPException(status_code=409, detail="User already exists")
    elif result == 'error':
        raise HTTPException(status_code=500, detail="Error creating user")
    return {'message': 'User created successfully'}

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

class CreateCourseRequest(BaseModel):
    course_id: str
    course_name: str
    textbook_id: int
    course_type: str
    faculty_id: str
    ta_id: str 
    start_date: datetime
    end_date: datetime
    unique_token: str
    capacity: int


@router.post('/create_course')
async def create_course_request(create_course_request: CreateCourseRequest):
    course_id = create_course_request.course_id
    course_name = create_course_request.course_name
    textbook_id = create_course_request.textbook_id
    course_type = create_course_request.course_type
    faculty_id = create_course_request.faculty_id
    ta_id = create_course_request.ta_id
    start_date = create_course_request.start_date
    end_date = create_course_request.end_date
    unique_token = create_course_request.unique_token
    capacity = create_course_request.capacity

    result = await create_course(course_id, course_name, textbook_id, course_type, faculty_id, ta_id, start_date, end_date, unique_token, capacity)
    
    if result == 'course_exists':
        return {'error': 'Course already exists'}, 400
    elif result == 'error':
        return {'error': 'Error creating course'}, 500
    return {'message': 'Course created successfully'}, 201