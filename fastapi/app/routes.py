from datetime import datetime
from typing import Optional
from fastapi import APIRouter, HTTPException
from app.utils import *
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

@router.get("/")
async def hello():
    result = "Hello world"
    return {"message": result}

class LoginRequest(BaseModel):
    user_id: str
    password: str
    role: str

@router.post("/login", status_code=200)
async def login(login_request: LoginRequest):
    user_id = login_request.user_id
    password = login_request.password
    role = login_request.role
    
    user = await get_user(user_id, password, role)
    
    if user:
        return {"status": "success", "user": user}
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
class ChangePasswordRequest(BaseModel):
    user_id: str
    old_password: str
    new_password: str

@router.post("/change_password", status_code=200)    
async def changePassword(change_password_request: ChangePasswordRequest):
    user_id = change_password_request.user_id
    old_password = change_password_request.old_password
    new_password = change_password_request.new_password
    
    user = await change_password(user_id, old_password, new_password)
    
    if user:
        return {"status": "success", "user": user}
    else:
        raise HTTPException(status_code=400, detail="Incorrect details")
    
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

"""
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
"""

class CreateCourseRequest(BaseModel):
    course_id: str
    course_name: str
    textbook_id: int
    course_type: str
    faculty_id: str
    start_date: datetime
    end_date: datetime
    unique_token: Optional[str] = None
    capacity: Optional[int] = None


@router.post('/create_course')
async def create_course_request(create_course_request: CreateCourseRequest):
    course_id = create_course_request.course_id
    course_name = create_course_request.course_name
    textbook_id = create_course_request.textbook_id
    course_type = create_course_request.course_type
    faculty_id = create_course_request.faculty_id
    start_date = create_course_request.start_date
    end_date = create_course_request.end_date
    unique_token = create_course_request.unique_token
    capacity = create_course_request.capacity

    result = await create_course(course_id, course_name, textbook_id, course_type, faculty_id, start_date, end_date, unique_token, capacity)
    
    if result == 'course_exists':
        return {'error': 'Course already exists'}, 400
    elif result == 'error':
        return {'error': 'Error creating course'}, 500
    return {'message': 'Course created successfully'}

class ViewCoursesRequest(BaseModel):
    user_id: str
    role: str

@router.post("/view_courses", status_code=200)    
async def view_courses_request(view_courses_request: ViewCoursesRequest):
    user_id = view_courses_request.user_id
    role = view_courses_request.role
    if role == "faculty":
        courses = await view_courses_faculty(user_id)
    else:
        courses = await view_courses_ta(user_id)
    
    if courses:
        return {"status": "success", "courses": courses}
    else:
        raise HTTPException(status_code=404, detail="Not found")
class GetTextBookRequest(BaseModel):
    tb_id: int

@router.get('/api/v1/textbook')
async def _get_textbook(tb_id: Optional[int] = None):
    
    result = await get_textbook_details(tb_id)
    
    print(result)
    if not result:
        raise HTTPException(status_code=404, detail="Textbook not found")
    return {'textbook': result}

class CreateTextbookRequest(BaseModel):
    tb_id: int
    tb_name: str
    created_by: str

@router.post('/create_textbook')
async def create_textbook_request(create_textbook_request: CreateTextbookRequest):
    tb_id = create_textbook_request.tb_id
    tb_name = create_textbook_request.tb_name
    created_by = create_textbook_request.created_by
    
    # Call the create_textbook function to handle the logic
    result = await create_textbook(tb_id, tb_name, created_by)
    
    if result == 'textbook_exists':
        raise HTTPException(status_code=400, detail="Textbook ID already exists")
    elif result == 'error':
        raise HTTPException(status_code=500, detail="Error creating textbook")
    
    return {"message": "Textbook created successfully"}

class CreateChapterRequest(BaseModel):
    tb_id: int
    chap_id: str
    chap_title: str
    created_by: str

@router.post('/create_chapter')
async def create_chapter_request(create_chapter_request: CreateChapterRequest):
    tb_id = create_chapter_request.tb_id
    chap_id = create_chapter_request.chap_id
    chap_title = create_chapter_request.chap_title
    created_by = create_chapter_request.created_by
    
    # Call the create_chapter function to handle the logic
    result = await create_chapter(tb_id, chap_id, chap_title, created_by)
    
    if result == 'chapter_exists':
        raise HTTPException(status_code=400, detail="Chapter already exists in the textbook.")
    elif result == 'error':
        raise HTTPException(status_code=500, detail="Error creating chapter")
    
    return {"message": "Chapter created successfully"}

class CreateSectionRequest(BaseModel):
    tb_id: int
    chap_id: str
    sec_id: str
    sec_name: str
    created_by: str

@router.post('/create_section')
async def create_section_request(create_section_request: CreateSectionRequest):
    tb_id = create_section_request.tb_id
    chap_id = create_section_request.chap_id
    sec_id = create_section_request.sec_id
    sec_name = create_section_request.sec_name
    created_by = create_section_request.created_by
    
    # Call the create_section function to handle the logic
    result = await create_section(tb_id, chap_id, sec_id, sec_name, created_by)
    
    if result == 'section_exists':
        raise HTTPException(status_code=400, detail="Section already exists in the chapter.")
    elif result == 'error':
        raise HTTPException(status_code=500, detail="Error creating section")
    
    return {"message": "Section created successfully"}

class CreateBlockRequest(BaseModel):
    tb_id: int
    chap_id: int
    sec_id: int
    block_id: int
    created_by: str

@router.post('/create_block')
async def create_block_request(create_block_request: CreateBlockRequest):
    tb_id = create_block_request.tb_id
    chap_id = create_block_request.chap_id
    sec_id = create_block_request.sec_id
    block_id = create_block_request.block_id
    created_by = create_block_request.created_by
    
    # Call the create_block function to handle the logic
    result = await create_block(tb_id, chap_id, sec_id, block_id, created_by)
    
    if result == 'block_exists':
        raise HTTPException(status_code=400, detail="Content block already exists in the section.")
    elif result == 'error':
        raise HTTPException(status_code=500, detail="Error creating content block")
    
    return {"message": "Content block created successfully"}

class CreateActivityRequest(BaseModel):
    tb_id: int
    chap_id: int
    sec_id: int
    block_id: int
    activity_id: int
    created_by: str

@router.post('/create_activity')
async def create_activity_request(create_activity_request: CreateActivityRequest):
    tb_id = create_activity_request.tb_id
    chap_id = create_activity_request.chap_id
    sec_id = create_activity_request.sec_id
    block_id = create_activity_request.block_id
    activity_id = create_activity_request.activity_id
    created_by = create_activity_request.created_by
    
    # Call the create_activity function to handle the logic
    result = await create_activity(tb_id, chap_id, sec_id, block_id, activity_id, created_by)
    
    if result == 'activity_exists':
        raise HTTPException(status_code=400, detail="Activity block already exists in the section.")
    elif result == 'error':
        raise HTTPException(status_code=500, detail="Error creating activity block")
    
    return {"message": "Activity block created and updated successfully"}
