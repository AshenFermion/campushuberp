class Field:
    def __init__(self, check, message):
        self.check = check
        self.message = message

    def __set_name__(self, owner, name):
        self.key = "_" + name

    def __get__(self, obj, owner):
        if obj is None:
            return self
        return getattr(obj, self.key, None)

    def __set__(self, obj, value):
        if not self.check(value):
            raise ValueError(self.message)

        if isinstance(value, str):
            value = value.strip()

        setattr(obj, self.key, value)

class Name(Field):
    def __init__(self):
        super().__init__(
            lambda value: isinstance(value, str) and bool(value.strip()),
            "Name cannot be empty"
        )

class Email(Field):
    def __init__(self):
        super().__init__(
            lambda value: isinstance(value, str) and "@" in value,
            "Email must contain @"
        )

class Age(Field):
    def __init__(self):
        super().__init__(
            lambda value: (
                isinstance(value, int)
                and not isinstance(value, bool)
                and 16 <= value <= 80
            ),
            "Age must be between 16 and 80"
        )