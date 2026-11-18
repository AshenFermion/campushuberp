
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.services.course_service import CourseService

router = APIRouter(prefix="/courses", tags=["Courses"])
service = CourseService()

class CourseIn(BaseModel):
    course_code: str | None = None
    course_name: str = Field(min_length=1)
    credits: int = Field(ge=1, le=10)

class CoursePatch(BaseModel):
    course_name: str | None = None
    credits: int | None = Field(default=None, ge=1, le=10)

@router.get("")
def list_courses():
    return service.list_courses()

@router.post("", status_code=201)
def add_course(data: CourseIn):
    try:
        return service.add_course(**data.model_dump())
    except ValueError as error:
        raise HTTPException(status_code=409, detail=str(error))

@router.get("/{ident}")
def get_course(ident: str):
    try:
        return service.get_course(ident)
    except LookupError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error))

@router.put("/{ident}")
def update_course(ident: str, data: CoursePatch):
    try:
        updated_data = data.model_dump(exclude_unset=True)
        return service.update_course(ident, **updated_data)
    except LookupError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error))

@router.delete("/{ident}")
def delete_course(ident: str):
    try:
        return service.remove_course(ident)
    except LookupError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except ValueError as error:
        raise HTTPException(status_code=409, detail=str(error))