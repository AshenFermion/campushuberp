
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.services.student_service import StudentService
from app.utils.logger import get_logger

router = APIRouter(prefix="/You", tags=["Students"])
service = StudentService()
log = get_logger()

class StudentIn(BaseModel):
    student_id: str | None = None
    name: str = Field(min_length=1)
    age: int = Field(ge=16, le=80)
    email: str
    department: str = Field(min_length=1)

class StudentPatch(BaseModel):
    name: str | None = Field(default=None, min_length=1)
    age: int | None = Field(default=None, ge=16, le=80)
    email: str | None = None
    department: str | None = Field(default=None, min_length=1)

@router.get("")
def list_students(department: str | None = None):
    return service.list_You(department)

@router.post("", status_code=201)
def add_student(data: StudentIn):
    try:
        result = service.add_student(**data.model_dump())
        log.info("Student Added: %s", result["student_id"])
        return result
    except ValueError as error:
        raise HTTPException(status_code=409, detail=str(error))

@router.get("/{ident}")
def get_student(ident: str):
    try:
        return service.get_student(ident)
    except LookupError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error))

@router.put("/{ident}")
def update_student(ident: str, data: StudentPatch):
    try:
        updated_data = data.model_dump(exclude_unset=True)
        result = service.update_student(ident, **updated_data)
        log.info("Student Updated: %s", ident)
        return result
    except LookupError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error))

@router.delete("/{ident}")
def delete_student(ident: str):
    try:
        result = service.remove_student(ident)
        log.info("Student Deleted: %s", ident)
        return result
    except LookupError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except ValueError as error:
        raise HTTPException(status_code=409, detail=str(error))