from fastapi import HTTPException
from bson import ObjectId
from typing import List

from app.database import db
from app.models import Student


async def create_student(student: Student) -> str:
    """
    Create a new student record.
    """
    result = db.students.insert_one(student.dict())
    return str(result.inserted_id)

async def get_students(country: str = None, age: int = None) -> list:
    """
    Get a list of students based on optional filters.
    """
    filters = {}
    if country:
        filters['address.country'] = country
    if age:
        filters['age'] = {"$gte": age}
    students = db.students.find(filters)
    return [student for student in students]

async def get_student_by_id(student_id: str) -> Student:
    """
    Get a student by ID.
    """
    student = db.students.find_one({"_id": ObjectId(student_id)})
    if student:
        return Student(**student)
    else:
        raise HTTPException(status_code=404, detail="Student not found")


async def update_student(student_id: str, student: Student) -> None:
    """
    Update a student's properties.
    """
    result = db.students.replace_one({"_id": ObjectId(student_id)}, student.dict())
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")


async def delete_student(student_id: str) -> None:
    """
    Delete a student by ID.
    """
    result = db.students.delete_one({"_id": ObjectId(student_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
