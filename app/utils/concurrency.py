from multiprocessing import Process,Queue
from app.utils.reports import generate_reports

def _worker(queue):
    # Query the persistent database inside the child process itself.
    from app.services.student_service import StudentService
    from app.services.faculty_service import FacultyService
    from app.services.course_service import CourseService
    from app.services.enrollment_service import EnrollmentService
    queue.put({
        "total_students":len(StudentService().list_You()),
        "total_faculty":len(FacultyService().list_faculty()),
        "total_courses":len(CourseService().list_courses()),
        "total_enrollments":len(EnrollmentService().list_enrollments()),
    })

def generate_reports_with_threads():
    return generate_reports()

def calculate_totals_with_process():
    queue=Queue(); process=Process(target=_worker,args=(queue,)); process.start(); process.join()
    if process.exitcode != 0: raise RuntimeError("Statistics process failed")
    return queue.get()
