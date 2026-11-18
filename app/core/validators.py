import re

PATTERNS = {
    "student": r"ST\d{3,}",
    "faculty": r"FC\d{3,}",
    "course": r"[A-Z]{2,5}\d{3,}",
    "email": r"[^@\s]+@[^@\s]+\.[^@\s]+",
}

def validate(kind, value):
    if kind not in PATTERNS:
        raise ValueError(f"Unknown validation type: {kind}")

    if not isinstance(value, str):
        raise ValueError(f"Invalid {kind}: {value!r}")

    value = value.strip()

    if not re.fullmatch(PATTERNS[kind], value):
        raise ValueError(f"Invalid {kind}: {value!r}")

    return value

def validate_student_id(value):
    return validate("student", value)

def validate_faculty_id(value):
    return validate("faculty", value)

def validate_course_code(value):
    return validate("course", value)

def validate_email(value):
    return validate("email", value)