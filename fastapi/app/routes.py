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
    elif result == 'faculty_not_found':
        return {'error': 'Facult not found'}, 400
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
async def _get_textbook(tb_id: int):
    
    result = await get_textbook_details(tb_id)
    
    print(result)
    if not result:
        raise HTTPException(status_code=404, detail="Textbook not found")
    return {'textbook': result}

@router.get('/api/v1/chapter')
async def _get_chapter(tb_id: int, chap_id: str):
    
    result = await get_chapter_details(tb_id,chap_id)
    
    print(result)
    if not result:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return {'chapter': result}


@router.get('/api/v1/section')
async def _get_section(tb_id:int, chap_id: str, sec_id: str):
    
    result = await get_section_details(tb_id,chap_id, sec_id)
    
    print(result)
    if not result:
        raise HTTPException(status_code=404, detail="Section not found")
    return {'section': result}

@router.get('/api/v1/block')
async def _get_block(tb_id:int, chap_id: str, sec_id: str, block_id: str):
    
    result = await get_block_details(tb_id,chap_id, sec_id, block_id)
    
    print(result)
    if not result:
        raise HTTPException(status_code=404, detail="Block not found")
    return {'block': result}

@router.get('/api/v1/activity')
async def _get_activity(tb_id:int, chap_id: str, sec_id: str, block_id: str, activity_id: str):
    # print(tb_id,chap_id, sec_id, block_id, activity_id)
    result = await get_activity_details(tb_id,chap_id, sec_id, block_id, activity_id)
    
    print(result)
    if not result:
        raise HTTPException(status_code=404, detail="Block not found")
    return {'activity': result}

@router.get('/api/v1/active-course')
async def _get_active_course(course_id: str):
    
    result = await get_active_course_details(course_id)
    
    print(result)
    if not result:
        raise HTTPException(status_code=404, detail="Course not found")
    return {'course': result}

@router.get('/api/v1/evaluation-course')
async def _get_eval_course(course_id: int):
    
    result = await get_eval_course_details(course_id)
    
    print(result)
    if not result:
        raise HTTPException(status_code=404, detail="Course not found")
    return {'course': result}

class ViewWorklistRequest(BaseModel):
    course_id: str

@router.post('/view_worklist')
async def _view_worklist(view_worklist_request: ViewWorklistRequest):
    course_id = view_worklist_request.course_id
    result = await get_worklist(course_id)
    
    print(result)
    if not result:
        raise HTTPException(status_code=404, detail="Waitlist empty")
    return {'students': result}

@router.post('/view_enrolled_students')
async def _view_worklist(view_worklist_request: ViewWorklistRequest):
    course_id = view_worklist_request.course_id
    result = await get_enrolled_list(course_id)
    
    print(result)
    if not result:
        raise HTTPException(status_code=404, detail="Enrolled list empty")
    return {'students': result}

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
    chap_id: str
    sec_id: str
    block_id: str
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
    chap_id: str
    sec_id: str
    block_id: str
    activity_id: str
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
    
    return {"message": "Activity created successfully"}



class AddContentRequest(BaseModel):
    tb_id: int
    chap_id: str
    sec_id: str
    content: str
    block_id: str
    block_type: str
    created_by: str


## need to send block type from front-end (here block type is either "text" or "picture" depending on what is clicked)
@router.post("/add_content")
async def add_content_request(add_content_request: AddContentRequest):

    tb_id = add_content_request.tb_id
    chap_id = add_content_request.chap_id
    sec_id = add_content_request.sec_id
    content = add_content_request.content
    block_id = add_content_request.block_id
    block_type = add_content_request.block_type
    created_by = add_content_request.created_by

    result = await add_content(tb_id, chap_id, sec_id, content, block_id, block_type, created_by)

    if(result == 'error'):
        raise HTTPException(status_code=500, detail=f"Error adding {block_type}")

    return {"message": f"{block_type} Content added"}


class AddQuestionRequest(BaseModel):
    tb_id: int
    chap_id: str
    sec_id: str
    block_id: str
    activity_id: str
    question_id: str
    question_text: str
    option_1: str
    option_1_explanation: str
    option_2: str
    option_2_explanation: str
    option_3: str
    option_3_explanation: str
    option_4: str
    option_4_explanation: str
    answer: int

    
@router.post('/add_question')
async def add_question_request(add_question_request: AddQuestionRequest):
    # Extract data from the request
    tb_id = add_question_request.tb_id
    chap_id = add_question_request.chap_id
    sec_id = add_question_request.sec_id
    block_id = add_question_request.block_id
    activity_id = add_question_request.activity_id
    question_id = add_question_request.question_id
    question_text = add_question_request.question_text
    option_1 = add_question_request.option_1
    option_1_explanation = add_question_request.option_1_explanation
    option_2 = add_question_request.option_2
    option_2_explanation = add_question_request.option_2_explanation
    option_3 = add_question_request.option_3
    option_3_explanation = add_question_request.option_3_explanation
    option_4 = add_question_request.option_4
    option_4_explanation = add_question_request.option_4_explanation
    answer = add_question_request.answer

    # Call the add_question function to handle the logic
    result = await add_question(tb_id, chap_id, sec_id, block_id, activity_id, question_id, question_text,
                                    option_1, option_1_explanation, option_2, option_2_explanation,
                                    option_3, option_3_explanation, option_4, option_4_explanation, answer)
    
    if result == "Question ID already exists for the activity":
        raise HTTPException(status_code=400, detail=result)
    elif result == 'error':
        raise HTTPException(status_code=500, detail="Error adding question")

    return {"message": f"Question id '{question_id}' created for the activity"}

class ModifyTextbookRequest(BaseModel):
    tb_id: int
    user_modifying: str


@router.post("/modify_textbook")
async def modify_textbook_request(modify_textbook_request: ModifyTextbookRequest):
    # Extract values from the request model
    tb_id = modify_textbook_request.tb_id
    user_modifying = modify_textbook_request.user_modifying
    
    # Call the modify_textbook function to check permissions and textbook existence
    result = await modify_textbook(tb_id, user_modifying)
    
    # Handle various outcomes
    if result == "Textbook doesn't exist, so can't modify.":
        raise HTTPException(status_code=404, detail=result)
    elif result == "You are not associated with this course, so can't modify":
        raise HTTPException(status_code=403, detail=result)
    elif result == "error":
        raise HTTPException(status_code=500, detail="Internal Server Error")

    return {"message": result}


class ModifyChapterRequest(BaseModel):
    tb_id: int
    chap_id: str


# Modify Chapter
@router.post("/modify_chapter")
async def modify_chapter_request(modify_chapter_request: ModifyChapterRequest):
    result = await modify_chapter(modify_chapter_request.tb_id, modify_chapter_request.chap_id)

    if result == "Chapter doesn't exist, so can't modify.":
        raise HTTPException(status_code=404, detail="Chapter doesn't exist, so can't modify.")
    if result == "error":
        raise HTTPException(status_code=500, detail="Error modifying chapter.")
    return {"message": result}

class ModifySectionRequest(BaseModel):
    tb_id: int
    chap_id: str
    sec_id: str


# Modify Section
@router.post("/modify_section")
async def modify_section_request(modify_section_request: ModifySectionRequest):
    
    result = await modify_section(modify_section_request.tb_id, modify_section_request.chap_id, modify_section_request.sec_id)

    if result == "Section doesn't exist, so can't modify.":
        raise HTTPException(status_code=404, detail="Section doesn't exist, so can't modify.")
    elif result == "error":
        raise HTTPException(status_code=500, detail="Error modifying section.")
    return {"message": result}


class ModifyBlockRequest(BaseModel):
    tb_id: int
    chap_id: str
    sec_id: str
    block_id: str
    user_modifying: str

@router.post("/modify_block")
async def modify_block_request(modify_block_request: ModifyBlockRequest):
    result = await modify_block(
        modify_block_request.tb_id,
        modify_block_request.chap_id,
        modify_block_request.sec_id,
        modify_block_request.block_id,
        modify_block_request.user_modifying
    )

    if result == "Block doesn't exist, so can't modify":
        raise HTTPException(status_code=404, detail="Block doesn't exist, so can't modify.")
    elif "Don't have permission" in result:
        raise HTTPException(status_code=403, detail=result)
    elif result == "error":
        raise HTTPException(status_code=500, detail="Error modifying block.")

    return {"message": result}


class ModifyContentAddQuestionRequest(BaseModel):
    tb_id: int
    chap_id: str
    sec_id: str
    block_id: str
    activity_id: str
    question_id: str
    question_text: str
    option_1: str
    option_1_explanation: str
    option_2: str
    option_2_explanation: str
    option_3: str
    option_3_explanation: str
    option_4: str
    option_4_explanation: str
    answer: int
    user_modifying: str

@router.post("/modify_content_add_question")
async def modify_content_add_question_request(modify_content_add_question_request: ModifyContentAddQuestionRequest):
    result = await modify_content_add_question(
        modify_content_add_question_request.tb_id, modify_content_add_question_request.chap_id, modify_content_add_question_request.sec_id, 
        modify_content_add_question_request.block_id, modify_content_add_question_request.activity_id, 
        modify_content_add_question_request.question_id, modify_content_add_question_request.question_text, 
        modify_content_add_question_request.option_1, modify_content_add_question_request.option_1_explanation, 
        modify_content_add_question_request.option_2, modify_content_add_question_request.option_2_explanation, 
        modify_content_add_question_request.option_3, modify_content_add_question_request.option_3_explanation, 
        modify_content_add_question_request.option_4, modify_content_add_question_request.option_4_explanation, 
        modify_content_add_question_request.answer, modify_content_add_question_request.user_modifying
    )
    
    if result == "Error" or result == "Previous Activity does not exist.":
        raise HTTPException(status_code=500, detail="error happened")
    
    return {"message": result}


class ModifyActivityAddQuestionRequest(BaseModel):
    tb_id: int
    chap_id: str
    sec_id: str
    block_id: str
    activity_id: str
    question_id: str
    question_text: str
    option_1: str
    option_1_explanation: str
    option_2: str
    option_2_explanation: str
    option_3: str
    option_3_explanation: str
    option_4: str
    option_4_explanation: str
    answer: int
    user_modifying: str

@router.post("/modify_activity_add_question")
async def modify_activity_add_question_request(modify_activity_add_question_request: ModifyActivityAddQuestionRequest):
    result = await modify_activity_add_question(
        modify_activity_add_question_request.tb_id, modify_activity_add_question_request.chap_id, modify_activity_add_question_request.sec_id, 
        modify_activity_add_question_request.block_id, modify_activity_add_question_request.activity_id, 
        modify_activity_add_question_request.question_id, modify_activity_add_question_request.question_text, 
        modify_activity_add_question_request.option_1, modify_activity_add_question_request.option_1_explanation, 
        modify_activity_add_question_request.option_2, modify_activity_add_question_request.option_2_explanation, 
        modify_activity_add_question_request.option_3, modify_activity_add_question_request.option_3_explanation, 
        modify_activity_add_question_request.option_4, modify_activity_add_question_request.option_4_explanation, 
        modify_activity_add_question_request.answer, modify_activity_add_question_request.user_modifying
    )
    
    if result == "Error":
        raise HTTPException(status_code=500, detail="error happened")
    
    return {"message": result}



class DeleteChapterRequest(BaseModel):
    tb_id: int
    chap_id: str
    user_modifying: str

@router.post("/delete_chapter")
async def delete_chapter_request(delete_chapter_request: DeleteChapterRequest):
    result = await delete_chapter(
        delete_chapter_request.tb_id,
        delete_chapter_request.chap_id,
        delete_chapter_request.user_modifying
    )
    
    if "don't have permission" in result or "doesn't exist" in result:
        raise HTTPException(status_code=400, detail=result)
    elif "error" in result.lower():
        raise HTTPException(status_code=500, detail=result)

    return {"message": result}

class DeleteSectionRequest(BaseModel):
    tb_id: int
    chap_id: str
    sec_id: str
    user_modifying: str


@router.post("/delete_section")
async def delete_section_request(delete_section_request: DeleteSectionRequest):
    result = await delete_section(
        delete_section_request.tb_id,
        delete_section_request.chap_id,
        delete_section_request.sec_id,
        delete_section_request.user_modifying
    )
    
    if "don't have permission" in result or "doesn't exist" in result:
        raise HTTPException(status_code=400, detail=result)
    elif "error" in result.lower():
        raise HTTPException(status_code=500, detail=result)

    return {"message": result}



class DeleteBlockRequest(BaseModel):
    tb_id: int
    chap_id: str
    sec_id: str
    block_id: str
    user_modifying: str

@router.post("/delete_block")
async def delete_block_request(delete_block_request: DeleteBlockRequest):
    result = await delete_block(
        delete_block_request.tb_id,
        delete_block_request.chap_id,
        delete_block_request.sec_id,
        delete_block_request.block_id,
        delete_block_request.user_modifying
    )
    print(result)
    if "don't have permission" in result or "doesn't exist" in result:
        raise HTTPException(status_code=400, detail=result)
    elif "error" in result.lower():
        raise HTTPException(status_code=500, detail=result)

    return {"message": result}

    

class GetPendingEnrollmentsRequest(BaseModel):
    unique_course_id: str

@router.post('/get_pending_enrollments')
async def get_pending_enrollments(request: GetPendingEnrollmentsRequest):
    unique_course_id = request.unique_course_id
    
    # Call the function to fetch pending enrollments
    result = await fetch_pending_enrollments(unique_course_id)
    
    if result is None:
        raise HTTPException(status_code=404, detail="No pending enrollments found.")
    
    return {"pending_enrollments": result}, 200


@router.post('/get_enrolled_students')
async def get_enrolled_students(request: GetPendingEnrollmentsRequest):
    unique_course_id = request.unique_course_id
    
    # Call the function to fetch pending enrollments
    result = await fetch_approved_enrollments(unique_course_id)
    
    if result is None:
        raise HTTPException(status_code=404, detail="No enrolled students found.")
    
    return {"enrolled_students": result}, 200


class CourseDetailsRequest(BaseModel):
    input_course_id: str
    current_date: str  # YYYY-MM-DD format
    user_modifying: str

@router.post("/check_course_details")
async def check_course_details_request(request: CourseDetailsRequest):
    result = await check_course_details(
        request.input_course_id,
        request.current_date,
        request.user_modifying
    )

    if result == "You are not associated with this course":
        raise HTTPException(status_code=403, detail="You are not associated with this course")
    elif result == "Beyond the end date - can't change the course!":
        raise HTTPException(status_code=403, detail="Beyond the end date - can't change the course!")
    elif result == "Error":
        raise HTTPException(status_code=500, detail="Error checking course details")
    return {"message": result}


class HideChapterRequest(BaseModel):
    tb_id: int
    chap_id: str

@router.post("/hide_chapter")
async def hide_chapter_request(hide_chapter_request: HideChapterRequest):
    result = await hide_chapter(hide_chapter_request.tb_id, hide_chapter_request.chap_id)
    
    if result == "Error":
        raise HTTPException(status_code=500, detail="Error hiding chapter")
    
    return {"message": result}


class HideSectionRequest(BaseModel):
    tb_id: int
    chap_id: str
    sec_id: str

@router.post("/hide_section")
async def hide_section_request(hide_section_request: HideSectionRequest):
    result = await hide_section(hide_section_request.tb_id, hide_section_request.chap_id, hide_section_request.sec_id)
    
    if result == "Error":
        raise HTTPException(status_code=500, detail="Error hiding section")
    
    return {"message": result}

class HideBlockRequest(BaseModel):
    tb_id: int
    chap_id: str
    sec_id: str
    block_id: str

@router.post("/hide_block")
async def hide_block_request(hide_block_request: HideBlockRequest):
    result = await hide_block(hide_block_request.tb_id, hide_block_request.chap_id, hide_block_request.sec_id, hide_block_request.block_id)
    
    if result == "Error":
        raise HTTPException(status_code=500, detail="Error hiding block")
    
    return {"message": result}

class EnrollStudentRequest(BaseModel):
    course_id: str
    student_id: str

@router.post('/enroll_student')
async def enroll_student_request(request: EnrollStudentRequest):
    course_id = request.course_id
    student_id = request.student_id
    
    # Call the function to handle the enrollment logic
    result = await enroll_student(course_id, student_id)
    
    if result == 'already_enrolled':
        raise HTTPException(status_code=400, detail=f"Student {student_id} is already enrolled in course {course_id}.")
    elif result == 'at_capacity':
        raise HTTPException(status_code=400, detail=f"Course {course_id} is at capacity. Enrollment not possible.")
    elif result == 'error':
        raise HTTPException(status_code=500, detail="An error occurred during enrollment.")
    
    return {"message": f"Student with ID {student_id} has been succesfully enrolled in course {course_id}."}, 200


class EnrollStudentInCourseRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    course_token: str
    password: str


@router.post('/enroll_student_in_course')
async def enroll_student_in_course(request: EnrollStudentInCourseRequest):
    result = await process_enrollment(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        course_token=request.course_token,
        password=request.password
    )
    
    # Handle responses based on status
    if result["status"] == "course_not_found":
        raise HTTPException(status_code=404, detail="Course not found.")
    elif result["status"] == "already_enrolled":
        raise HTTPException(status_code=400, detail="Student is already enrolled/wailisted in the course.")
    elif result["status"] == "error":
        raise HTTPException(status_code=500, detail="An error occurred during enrollment.")
    
    return {
        "message": f"Student {result['user_id']} has been successfully added to waitlist for course {result['course_id']}, awaiting approval from faculty."
    }


# Student : view activity participation summary
class StudentCourseInput(BaseModel):
    student_id: str
    course_ids: List[str]

@router.post("/student/activity_summary")
async def get_student_activity_summary(input_data: StudentCourseInput):
    """Retrieve student activity summary"""
    # Destructure input data
    student_id = input_data.student_id
    course_ids = input_data.course_ids
    
    # Call the utility function to fetch activity summary
    result = await fetch_student_activity_summary(student_id, course_ids)
    
    # Handle responses based on the result from the utility function
    if result == "no_records":
        raise HTTPException(status_code=404, detail="No participation records found for the specified student and course.")
    elif result == "error":
        raise HTTPException(status_code=500, detail="An error occurred while retrieving the activity summary.")
    
    # Return the successful result if no errors
    return result


class FetchContentRequest(BaseModel):
    tb_id: int
    chap_id: str
    sec_id: str

@router.get("/fetch_content")
async def fetch_content_request(tb_id: int, chap_id: str, sec_id: str):
    """Endpoint to fetch block_id and block_type based on the provided IDs."""
    result = await fetch_content(tb_id, chap_id, sec_id)

    if result == "Error retrieving content":
        raise HTTPException(status_code=500, detail="Error retrieving content")
    elif result == "Chapter does not exist.":
        raise HTTPException(status_code=404, detail="Chapter does not exist")
    elif result == "Chapter is hidden.":
        raise HTTPException(status_code=404, detail="Chapter is hidden")
    elif result == "Section does not exist.":
        raise HTTPException(status_code=404, detail="Section does not exist")
    elif result == "Section is hidden.":
        raise HTTPException(status_code=404, detail="Section is hidden")
    elif result == "No visible blocks found in the specified section.":
        raise HTTPException(status_code=404, detail="No visible blocks found in the specified section")

    return result


class ViewContentRequest(BaseModel):
    tb_id: int
    chap_id: str
    sec_id: str
    block_id: str

@router.get("/student/view_content")
async def view_text_picture_block(tb_id: int, chap_id: str, sec_id: str, block_id: str):
    """Endpoint to fetch content for text or picture block types based on the provided IDs."""
    result = await fetch_text_picture_block(tb_id, chap_id, sec_id, block_id)
    
    if result == "Error retrieving content":
        raise HTTPException(status_code=500, detail="Error retrieving content")
    elif result == "No content found for the specified block.":
        raise HTTPException(status_code=404, detail="Content not found for the specified block")

    return {"content": result}


class ViewActivityRequest(BaseModel):
    tb_id: int
    chap_id: str
    sec_id: str
    block_id: str

@router.get("/student/view_activity_block")
async def view_activity_block(tb_id: int, chap_id: str, sec_id: str, block_id: str):
    """Endpoint to fetch questions for activity block types based on the provided IDs."""
    result = await fetch_activity_block(tb_id, chap_id, sec_id, block_id)

    if result == "Error retrieving questions":
        raise HTTPException(status_code=500, detail="Error retrieving questions")
    elif result == "Block content not found.":
        raise HTTPException(status_code=404, detail="Block content not found")
    elif result == "No questions found for the specified block.":
        raise HTTPException(status_code=404, detail="No questions found for the specified block")

    return result

class GetStudentCoursesRequest(BaseModel):
    student_id: str

@router.get('/api/v1/student-courses')
async def _get_student_courses(student_id: str):
    """Fetch a list of course IDs and associated textbook IDs for a given student."""
    
    result = await get_student_courses_and_textbooks(student_id)

    if not result:
        raise HTTPException(status_code=404, detail="No courses found for the specified student.")
    return {'courses': result}

class ParticipationEntry(BaseModel):
    student_id: str
    course_id: str
    textbook_id: int
    section_id: str
    chapter_id: str
    block_id: str
    unique_activity_id: str
    question_id: str
    correct: str

@router.post('/api/v1/participation')
async def add_participation(entry: ParticipationEntry):
    """Insert a participation record."""

    success = await insert_participation_record(entry)
    
    if not success:
        raise HTTPException(status_code=500, detail=f"Failed to mark the question {entry.question_id}")
    
    return {"detail": f"Marks recorded for question {entry.question_id} successfully."}


class ViewNotificationsRequest(BaseModel):
    user_id: str

@router.post("/view_notifications", status_code=200)
async def view_notifications_request(view_notifications_request: ViewNotificationsRequest):
    user_id = view_notifications_request.user_id
    notifications = await fetch_notifications(user_id)

    if notifications:
        return {"status": "success", "notifications": notifications}
    else:
        raise HTTPException(status_code=404, detail="No notifications found for this user.")
    
@router.post("/delete_notifications", status_code=200)
async def delete_notifications_request(delete_notifications_request: ViewNotificationsRequest):
    user_id = delete_notifications_request.user_id

    try:
        await delete_notifications(user_id)
        return {"status": "success", "message": f"All notifications deleted for user ID '{user_id}'."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete notifications: {e}")


"""
Endpoint for additional adhoc queries begin here
"""

# 1. Number of sections in the first chapter of a textbook
class TextbookSectionCountRequest(BaseModel):
    textbook_id: int

@router.post("/sections_in_first_chapter")
async def sections_in_first_chapter(request: TextbookSectionCountRequest):
    query = """
        SELECT COUNT(*) AS number_of_sections
        FROM section
        WHERE chapter_id = '1' AND textbook_id = :textbook_id
    """
    values = {"textbook_id": request.textbook_id}
    result = await database.fetch_one(query=query, values=values)
    if result:
        return {"number_of_sections": result["number_of_sections"]}
    else:
        raise HTTPException(status_code=404, detail="No sections found")


# 2. Names of faculty and TAs of all courses, with roles
@router.get("/faculty_and_tas")
async def get_faculty_and_tas():
    query = """
        SELECT u.first_name, u.last_name, u.role, c.course_id
        FROM user u
        JOIN course c ON u.user_id = c.faculty_id
        UNION
        SELECT u.first_name, u.last_name, 'teaching assistant' AS role, ta.course_id
        FROM user u
        JOIN teaching_assistant ta ON u.user_id = ta.ta_id
    """
    result = await database.fetch_all(query=query)
    if result:
        return {"faculty_and_tas": [dict(row) for row in result]}
    else:
        raise HTTPException(status_code=404, detail="No faculty or TAs found")
    

# 3. Active courses with course ID, faculty member, and total number of students
@router.get("/active_courses_with_students")
async def active_courses_with_students():
    query = """
        SELECT c.course_id, CONCAT(u.first_name, ' ', u.last_name) AS faculty_name, COUNT(e.student_id) AS total_students
        FROM course c
        JOIN user u ON c.faculty_id = u.user_id
        JOIN enrollment e ON c.course_id = e.unique_course_id
        WHERE c.course_type = 'Active'
        GROUP BY c.course_id, faculty_name
    """
    result = await database.fetch_all(query=query)
    if result:
        return {"active_courses": [dict(row) for row in result]}
    else:
        raise HTTPException(status_code=404, detail="No active courses found")


# 4. Course with the largest waiting list
@router.get("/course_with_largest_waitlist")
async def course_with_largest_waitlist():
    query = """
        SELECT e.unique_course_id AS course_id, COUNT(*) AS waiting_list_count
        FROM enrollment e
        WHERE e.status = 'Pending'
        GROUP BY e.unique_course_id
        ORDER BY waiting_list_count DESC
        LIMIT 1
    """
    result = await database.fetch_one(query=query)
    if result:
        return {"course_with_largest_waitlist": dict(result)}
    else:
        raise HTTPException(status_code=404, detail="No courses with waitlists found")


# 5. Contents of Chapter 02 of textbook 101 in sequence
class ChapterContentRequest(BaseModel):
    textbook_id: int
    chapter_id: str

@router.post("/chapter_contents")
async def chapter_contents(request: ChapterContentRequest):
    query = """
        SELECT b.content
        FROM block b
        WHERE b.textbook_id = :textbook_id AND b.chapter_id = :chapter_id
        ORDER BY b.sequence_no
    """
    values = {"textbook_id": request.textbook_id, "chapter_id": request.chapter_id}
    result = await database.fetch_all(query=query, values=values)
    if result:
        return {"chapter_contents": [row["content"] for row in result]}
    else:
        raise HTTPException(status_code=404, detail="No content found for specified chapter")


# 6. Incorrect answers for question 2 of Activity0 and their explanations
class IncorrectAnswersRequest(BaseModel):
    textbook_id: int
    chapter_id: str
    section_id: str
    block_id: str
    correct_answer: str

@router.post("/incorrect_answers")
async def incorrect_answers(request: IncorrectAnswersRequest):
    query = """
        SELECT q.option_1, q.opt_1_explanation, q.option_2, q.opt_2_explanation, 
               q.option_3, q.opt_3_explanation, q.option_4, q.opt_4_explanation
        FROM question q
        WHERE q.textbook_id = :textbook_id 
            AND q.chapter_id = :chapter_id
            AND q.section_id = :section_id
            AND q.block_id = :block_id
            AND q.unique_activity_id = 'Activity0'
            AND q.question_id = 'Q2'
            AND answer <> :correct_answer
    """
    values = {
        "textbook_id": request.textbook_id,
        "chapter_id": request.chapter_id,
        "section_id": request.section_id,
        "block_id": request.block_id,
        "correct_answer": request.correct_answer
    }
    result = await database.fetch_all(query=query, values=values)
    if result:
        return {"incorrect_answers": [dict(row) for row in result]}
    else:
        raise HTTPException(status_code=404, detail="No incorrect answers found")


# 7. Book in active status by one instructor and evaluation status by a different instructor
@router.get("/book_different_status_instructors")
async def book_different_status_instructors():
    query = """
        SELECT c1.textbook_id, c1.faculty_id AS active_faculty, c2.faculty_id AS evaluation_faculty
        FROM course c1
        JOIN course c2 ON c1.textbook_id = c2.textbook_id AND c1.faculty_id <> c2.faculty_id
        WHERE c1.course_type = 'Active' AND c2.course_type = 'Evaluation'
    """
    result = await database.fetch_all(query=query)
    if result:
        return {"books_with_different_status_instructors": [dict(row) for row in result]}
    else:
        raise HTTPException(status_code=404, detail="No books found with different status instructors")


class TextbookRequest(BaseModel):
    tb_id: int

@router.get("/display_textbook")
async def display_textbook_endpoint(tb_id: int):
    """Endpoint to display the textbook hierarchy."""
    hierarchy = await fetch_textbook_hierarchy(tb_id)

    if (hierarchy == "Error retrieving textbook hierarchy."):
        raise HTTPException(status_code=500, detail = "Error retrieving textbook hierarchy")
    return hierarchy

# class NotificationRequest(BaseModel):
#     student_id: str

# @router.post('/view_notifications')
# async def _view_notifications(view_notification_request: NotificationRequest):
#     student_id = view_notification_request.student_id
#     result = await get_notifications(student_id)
#     if not result:
#         raise HTTPException(status_code=404, detail="No unread notifications")
#     return {'notifications': result}