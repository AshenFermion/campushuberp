from app.models.student import Student
from app.models.faculty import Faculty
from app.models.course import Course
class EntityFactory:
    @staticmethod
    def create(kind,**kwargs):
        classes={"student":Student,"faculty":Faculty,"course":Course}
        try:return classes[kind.lower()](**kwargs)
        except KeyError:raise ValueError(f"Unsupported entity type: {kind}")
