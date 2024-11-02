# Edugrid

This is a comprehensive educational platform designed to enhance the management and participation in academic courses. It supports various roles, including Admin, Faculty, Student, and Teaching Assistant, each with tailored functionalities (built from scratch and maintained as a part of the CSC 540 - DBMS course at NC State University). 

## Tech Stack
- **Backend**: FastAPI (Python) for API management, MariaDB (MySQL) for the database.
- **Frontend**: TypeScript and modern web technologies.
- **Database**: MySQL with comprehensive schema including courses, students, participation, notifications, and more.

## Architecture Overview
- **Frontend-Backend Interaction**: The frontend interacts with the FastAPI backend via RESTful APIs.
- **Database Structure**: Relational schema designed for handling courses, users, participation, notifications, etc.
- **Authentication and Authorization**: Secure role-based access.
- **Concurrency Support**: The backend is built to handle multiple simultaneous requests efficiently, ensuring seamless user experience during peak usage times.

## Key Features

### Admin
- **User Management**: Create, update, and manage users across the platform.
- **Course Oversight**: View and manage courses and enrollments.
- **Notification Management**: View and send notifications to users.

### Faculty
- **Course Creation and Management**: Create and manage course details, textbooks, and related resources.
- **Student Enrollment**: Approve student enrollments and oversee course capacity.
- **Grade and Feedback**: Manage participation points and give feedback.

### Student
- **Course Enrollment**: Enroll in courses, view status (Pending/Enrolled).
- **Activity Participation**: Attempt activities, answer questions, and track progress.
- **Notification Center**: Receive and view course-related notifications.

### Teaching Assistant (TA)
- **Course Assistance**: Support faculty in managing courses and answering student queries.
- **Participation Review**: Help review student activities and submissions.
- **Resource Sharing**: Share and manage course materials.

## Installation and Setup


## Future Enhancements 
- (Currently on-prem, running on NCSU cluster): migrate to cloud for auto-scale and high availability
- Enhanced UI
- Security layer integration

## Contributors
[Deepak Rajendran](https://www.linkedin.com/in/deep41/)<br/>
[Rishi Singhal](https://www.linkedin.com/in/rishi-singhal1101/)<br/>
[Shashank Madan](https://www.linkedin.com/in/shashank-udyavar-madan/)<br/>
[Aditya Pai Brahmavar](https://www.linkedin.com/in/adityapai16/)<br/>
