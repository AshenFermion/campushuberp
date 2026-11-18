from app.models.person import PersonModel
from app.core.validators import validate_faculty_id

class Faculty(PersonModel):
    def __init__(self, faculty_id, name, age, email, department):
        super().__init__(name, age, email)
        self.faculty_id = validate_faculty_id(faculty_id)

        if not isinstance(department, str) or not department.strip():
            raise ValueError("Department cannot be empty")

        self.department = department.strip()

    def display_details(self):
        details = super().display_details()
        return f"{self.faculty_id} | {details} | {self.department}"

    def to_dict(self):
        return {
            "faculty_id": self.faculty_id,
            **super().to_dict(),
            "department": self.department,
        }