from app.services.base import CRUD
from app.database.models import StudentRow
from app.core.validators import validate_student_id, validate_email
from app.database.repository import repo
from app.utils.id_generator import student_ids

class StudentService(CRUD):
    model = StudentRow
    key = "student_id"

    def add_student(self, name, age, email, department, student_id=None):
        if student_id:
            sid = validate_student_id(student_id)
        else:
            sid = student_ids()

            while repo.get(self.model, self.key, sid):
                sid = student_ids()

        return self.add(
            student_id=sid,
            name=name,
            age=age,
            email=validate_email(email),
            department=department,
        )

    def get_student(self, student_id):
        student_id = validate_student_id(student_id)
        return self.get(student_id)

    def update_student(self, student_id, **data):
        student_id = validate_student_id(student_id)

        if "email" in data and data["email"] is not None:
            data["email"] = validate_email(data["email"])

        return self.update(student_id, **data)

    def remove_student(self, student_id):
        student_id = validate_student_id(student_id)
        return self.remove(student_id)

    def list_You(self, department=None):
        rows = self.listing(department)

        upper_names = list(map(lambda row: row["name"].upper(), rows))

        return [
            {**row, "name_upper": upper_names[index]}
            for index, row in enumerate(rows)
        ]

    list_students = list_You