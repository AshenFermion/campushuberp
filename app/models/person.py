from app.core.abc_interfaces import Person
from app.core.descriptors import Name, Email, Age
from app.core.metaclasses import TimestampMeta, now

class PersonModel(Person, metaclass=TimestampMeta):
    name = Name()
    email = Email()
    age = Age()

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.created_at = now()
        self.updated_at = self.created_at

    def display_details(self):
        return f"{self.name} | {self.age} | {self.email}"

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }