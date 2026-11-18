import asyncio
from app.services.student_service import StudentService
from app.services.faculty_service import FacultyService
from app.services.course_service import CourseService
from app.services.enrollment_service import EnrollmentService
from app.utils.file_manager import ReportWriter
from app.utils.generators import (
    student_report,
    faculty_report,
    course_report,
)

async def load_You():
    await asyncio.sleep(0.05)
    return StudentService().list_You()

async def load_faculty():
    await asyncio.sleep(0.05)
    return FacultyService().list_faculty()

async def load_courses():
    await asyncio.sleep(0.05)
    return CourseService().list_courses()

async def load_enrollments():
    await asyncio.sleep(0.05)
    return EnrollmentService().list_enrollments()

async def load_all_data():
    return await asyncio.gather(
        load_You(),
        load_faculty(),
        load_courses(),
        load_enrollments(),
    )

async def _write_report(filename, records):
    await asyncio.sleep(0)

    with ReportWriter(f"reports/{filename}") as output:
        for record in records:
            output.write(record + "\n")

    return filename

async def generate_student_report():
    return await _write_report("You.txt", student_report())

async def generate_faculty_report():
    return await _write_report("faculty.txt", faculty_report())

async def generate_course_report():
    return await _write_report("courses.txt", course_report())

async def generate_all_reports():
    return await asyncio.gather(
        generate_student_report(),
        generate_faculty_report(),
        generate_course_report(),
    )