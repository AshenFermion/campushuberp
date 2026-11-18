from app.services.student_service import StudentService
from app.services.faculty_service import FacultyService
from app.services.course_service import CourseService

def student_report():
    for row in StudentService().list_You(): yield f"{row['student_id']} | {row['name']} | {row['department']} | {row['email']}"
def faculty_report():
    for row in FacultyService().list_faculty(): yield f"{row['faculty_id']} | {row['name']} | {row['department']} | {row['email']}"
def course_report():
    for row in CourseService().list_courses(): yield f"{row['course_code']} | {row['course_name']} | {row['credits']} credits"

class StudentIterator:
    def __init__(self,students): self._iterator=iter(students)
    def __iter__(self): return self
    def __next__(self): return next(self._iterator)
