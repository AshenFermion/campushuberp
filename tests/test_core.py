import pytest
from app.models.student import Student
from app.models.course import Course
from app.models.student_iterator import StudentIterator
from app.utils.id_generator import make_id_generator
from app.utils.factory import EntityFactory

def test_descriptors_and_domain_model():
    with pytest.raises(ValueError): Student("ST001","",20,"a@b.com","CS")
    with pytest.raises(ValueError): Student("ST001","Valid",15,"a@b.com","CS")
    s=Student("ST001","Valid",20,"a@b.com","CS")
    assert s.to_dict()["student_id"]=="ST001" and s.created_at is not None

def test_closure_factory_iterator():
    ids=make_id_generator("ST"); assert [ids(),ids(),ids()]==["ST001","ST002","ST003"]
    assert EntityFactory.create("course",course_code="CS101",course_name="Networks",credits=3).credits==3
    people=[Student("ST101","A",20,"a@example.com","CS"),Student("ST102","B",21,"b@example.com","IT")]
    assert [x.name for x in StudentIterator(people)]==["A","B"]
