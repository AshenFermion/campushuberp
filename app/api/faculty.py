
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.services.faculty_service import FacultyService

router = APIRouter(prefix="/faculty", tags=["Faculty"])
service = FacultyService()

class FacultyIn(BaseModel):
    faculty_id: str | None = None
    name: str = Field(min_length=1)
    age: int = Field(ge=16, le=80)
    email: str
    department: str = Field(min_length=1)

class FacultyPatch(BaseModel):
    name: str | None = Field(default=None, min_length=1)
    age: int | None = Field(default=None, ge=16, le=80)
    email: str | None = None
    department: str | None = Field(default=None, min_length=1)

@router.get("")
def list_faculty(department: str | None = None):
    return service.list_faculty(department)

@router.post("", status_code=201)
def add_faculty(data: FacultyIn):
    try:
        return service.add_faculty(**data.model_dump())
    except ValueError as error:
        raise HTTPException(status_code=409, detail=str(error))

@router.get("/{ident}")
def get_faculty(ident: str):
    try:
        return service.get_faculty(ident)
    except LookupError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error))

@router.put("/{ident}")
def update_faculty(ident: str, data: FacultyPatch):
    try:
        updated_data = data.model_dump(exclude_unset=True)
        return service.update_faculty(ident, **updated_data)
    except LookupError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error))

@router.delete("/{ident}")
def delete_faculty(ident: str):
    try:
        return service.remove_faculty(ident)
    except LookupError as error:
        raise HTTPException(status_code=404, detail=str(error))