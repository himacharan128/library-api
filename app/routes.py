from fastapi import APIRouter, HTTPException
from typing import List, Dict

from app.models import Student
from app.controllers import (
    create_student,
    get_students,
    get_student_by_id,
    update_student,
    delete_student,
)

router = APIRouter()


@router.post("/students", status_code=201, response_model=dict)
async def create_student_route(student: Student) -> dict:
    """
    Create a new student record.
    """
    student_id = await create_student(student)
    return {"id": student_id}


@router.get("/students", response_model=Dict[str, List[dict]])
async def list_students_route(country: str = None, age: int = None) -> List[Student]:
    """
    List students with optional filters.
    """
    students = await get_students(country, age)
    # return students
    return {"data" : students}


@router.get("/students/{student_id}", response_model=Student)
async def fetch_student_route(student_id: str) -> Student:
    """
    Fetch a student by ID.
    """
    student = await get_student_by_id(student_id)
    return student


@router.patch("/students/{student_id}", status_code=204)
async def update_student_route(student_id: str, student: Student) -> None:
    """
    Update a student's properties.
    """
    await update_student(student_id, student)
    return {}


@router.delete("/students/{student_id}", response_model=dict)
async def delete_student_route(student_id: str) -> dict:
    """
    Delete a student by ID.
    """
    await delete_student(student_id)
    return {}
