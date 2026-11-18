from app.services.base import CRUD
from app.database.models import CourseRow
from app.core.validators import validate_course_code
from app.utils.id_generator import course_ids
from app.database.repository import repo

class CourseService(CRUD):
    model = CourseRow
    key = "course_code"

    def add_course(self, course_name, credits, course_code=None):
        if course_code:
            code = validate_course_code(course_code)
        else:
            code = course_ids()

            while repo.get(self.model, self.key, code):
                code = course_ids()

        return self.add(
            course_code=code,
            course_name=course_name,
            credits=credits,
        )

    def get_course(self, course_code):
        course_code = validate_course_code(course_code)
        return self.get(course_code)

    def update_course(self, course_code, **data):
        course_code = validate_course_code(course_code)
        return self.update(course_code, **data)

    def remove_course(self, course_code):
        course_code = validate_course_code(course_code)
        return self.remove(course_code)

    list_courses = CRUD.listing