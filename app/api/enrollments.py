
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.enrollment_service import EnrollmentService

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])
service = EnrollmentService()

class EnrollmentIn(BaseModel):
    enrollment_id: str | None = None
    student_id: str
    course_code: str

@router.get("")
def list_enrollments():
    return service.list_enrollments()

@router.post("", status_code=201)
def add_enrollment(data: EnrollmentIn):
    try:
        return service.enroll_student(**data.model_dump())
    except LookupError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except ValueError as error:
        raise HTTPException(status_code=409, detail=str(error))

@router.delete("/{ident}")
def delete_enrollment(ident: str):
    try:
        return service.remove_enrollment(ident)
    except LookupError as error:
        raise HTTPException(status_code=404, detail=str(error))