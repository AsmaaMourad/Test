# API docs

#### Get all Courses
GET /rest/1/courses

#### Create a new Course
POST /rest/1/courses

#### Get single Course
GET /rest/1/courses/{ID}

#### Update single Course
PATCH /rest/1/courses/{ID}

#### Delete single Course
DELETE /rest/1/courses/{ID}

#### Get all enrolled Students in a single Course
GET /rest/1/courses/{ID}/child/StudentsView

#### Get all Students
GET /rest/1/students

#### Create a new Student
POST /rest/1/students

#### Get single Student
GET /rest/1/students/{ID}

#### Update single Student
PATCH /rest/1/students/{ID}

#### Delete single Student
DELETE /rest/1/students/{ID}

#### Get all selected Courses by a Student
GET /rest/1/students/{ID}/child/CoursesView

#### Enroll a Student in a Course
POST /rest/1/course_student


