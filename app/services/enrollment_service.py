from app.services.base import CRUD
from app.database.models import EnrollmentRow
from app.services.student_service import StudentService
from app.services.course_service import CourseService
from app.database.repository import repo
from app.utils.id_generator import enrollment_ids

class EnrollmentService(CRUD):
    model = EnrollmentRow
    key = "enrollment_id"

    def enroll_student(self, student_id, course_code, enrollment_id=None):
        # Check that the student and course exist before creating enrollment.
        StudentService().get_student(student_id)
        CourseService().get_course(course_code)

        if enrollment_id:
            eid = enrollment_id
        else:
            eid = enrollment_ids()

            while repo.get(self.model, self.key, eid):
                eid = enrollment_ids()

        return self.add(
            enrollment_id=eid,
            student_id=student_id,
            course_code=course_code,
        )

    list_enrollments = CRUD.listing
    remove_enrollment = CRUD.remove