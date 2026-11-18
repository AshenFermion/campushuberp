from app.core.validators import validate_course_code
from app.core.metaclasses import TimestampMeta, now

class Course(metaclass=TimestampMeta):
    def __init__(self, course_code, course_name, credits):
        self.course_code = validate_course_code(course_code)

        if not isinstance(course_name, str) or not course_name.strip():
            raise ValueError("Course name cannot be empty")

        if (
            not isinstance(credits, int)
            or isinstance(credits, bool)
            or credits < 1
        ):
            raise ValueError("Credits must be a positive integer")

        self.course_name = course_name.strip()
        self.credits = credits
        self.created_at = now()
        self.updated_at = self.created_at

    def display_details(self):
        return f"{self.course_code} | {self.course_name} | {self.credits} credits"

    def to_dict(self):
        return {
            "course_code": self.course_code,
            "course_name": self.course_name,
            "credits": self.credits,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }