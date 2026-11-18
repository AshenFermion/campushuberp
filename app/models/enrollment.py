from app.core.metaclasses import TimestampMeta, now

class Enrollment(metaclass=TimestampMeta):
    def __init__(self, enrollment_id, student_id, course_code):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_code = course_code
        self.created_at = now()
        self.updated_at = self.created_at

    def to_dict(self):
        return {
            "enrollment_id": self.enrollment_id,
            "student_id": self.student_id,
            "course_code": self.course_code,
        }