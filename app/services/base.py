from app.database.repository import repo
from app.utils.decorators import service_operation
from app.utils.logger import get_logger

log = get_logger()

class CRUD:
    model = None
    key = None

    @service_operation
    def add(self, **data):
        required_fields = {
            column.name
            for column in self.model.__table__.columns
            if column.name in data
            or (
                column.default is None
                and column.server_default is None
                and column.nullable is False
            )
        }

        missing_fields = required_fields - set(data)
        if missing_fields:
            missing = ", ".join(sorted(missing_fields))
            raise ValueError(f"Missing fields: {missing}")

        identifier = data[self.key]

        if repo.get(self.model, self.key, identifier):
            raise ValueError(f"Duplicate {self.key}: {identifier}")

        record = self.model(**{
            field: data[field]
            for field in required_fields
        })

        result = repo.add(self.model, record)
        log.info("Added %s", identifier)
        return result

    @service_operation
    def get(self, ident):
        result = repo.get(self.model, self.key, ident)

        if result is None:
            raise LookupError(f"{self.key} '{ident}' not found")

        return result

    @service_operation
    def listing(self, department=None):
        rows = repo.list(self.model)

        if department and "department" in self.model.__table__.columns:
            rows = [
                row for row in rows
                if row["department"].casefold() == department.casefold()
            ]

        columns = self.model.__table__.columns

        if "name" in columns:
            sort_field = "name"
        elif "course_name" in columns:
            sort_field = "course_name"
        else:
            sort_field = "enrollment_id"

        return sorted(rows, key=lambda row: row[sort_field].casefold())

    @service_operation
    def update(self, ident, **data):
        result = repo.update(self.model, self.key, ident, data)

        if result is None:
            raise LookupError(f"{self.key} '{ident}' not found")

        return result

    @service_operation
    def remove(self, ident):
        deleted = repo.delete(self.model, self.key, ident)

        if not deleted:
            raise LookupError(f"{self.key} '{ident}' not found")

        return {"message": "Deleted successfully"}