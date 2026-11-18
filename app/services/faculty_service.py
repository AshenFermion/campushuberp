from app.services.base import CRUD
from app.database.models import FacultyRow
from app.core.validators import validate_faculty_id, validate_email
from app.database.repository import repo
from app.utils.id_generator import faculty_ids

class FacultyService(CRUD):
    model = FacultyRow
    key = "faculty_id"

    def add_faculty(self, name, age, email, department, faculty_id=None):
        if faculty_id:
            fid = validate_faculty_id(faculty_id)
        else:
            fid = faculty_ids()

            while repo.get(self.model, self.key, fid):
                fid = faculty_ids()

        return self.add(
            faculty_id=fid,
            name=name,
            age=age,
            email=validate_email(email),
            department=department,
        )

    def get_faculty(self, faculty_id):
        faculty_id = validate_faculty_id(faculty_id)
        return self.get(faculty_id)

    def update_faculty(self, faculty_id, **data):
        faculty_id = validate_faculty_id(faculty_id)

        if "email" in data and data["email"] is not None:
            data["email"] = validate_email(data["email"])

        return self.update(faculty_id, **data)

    def remove_faculty(self, faculty_id):
        faculty_id = validate_faculty_id(faculty_id)
        return self.remove(faculty_id)

    list_faculty = CRUD.listing