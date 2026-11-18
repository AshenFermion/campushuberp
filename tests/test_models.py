import pytest
from app.models.student import Student
def test_student_constructs():assert Student("ST001","Asha",20,"asha@example.com","CS").student_id=="ST001"
def test_invalid_age():
    with pytest.raises(ValueError):Student("ST001","Asha",15,"asha@example.com","CS")
def test_invalid_email():
    with pytest.raises(ValueError):Student("ST001","Asha",20,"bad-email","CS")
