from app.models.person import PersonModel
from app.core.validators import validate_student_id

class Student(PersonModel):
    def __init__(self, student_id, name, age, email, department):
        super().__init__(name, age, email)
        self.student_id = validate_student_id(student_id)

        if not isinstance(department, str) or not department.strip():
            raise ValueError("Department cannot be empty")

        self.department = department.strip()

    def display_details(self):
        details = super().display_details()
        return f"{self.student_id} | {details} | {self.department}"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            **super().to_dict(),
            "department": self.department,
        }