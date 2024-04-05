from typing import List

from app.models import Student
from app.database import db


async def create_student(student: Student) -> str:
    """
    Create a new student record.
    """
    result = await db.students.insert_one(student.dict())
    return str(result.inserted_id)


async def get_students(country: str = None, age: int = None) -> List[Student]:
    """
    List students with optional filters.
    """
    query = {}
    if country:
        query["address.country"] = country
    if age is not None:
        query["age"] = {"$gte": age}

    students = await db.students.find(query).to_list(length=None)
    return [Student(**student) for student in students]


async def get_student_by_id(student_id: str) -> Student:
    """
    Fetch a student by ID.
    """
    student = await db.students.find_one({"_id": student_id})
    if student:
        return Student(**student)


async def update_student(student_id: str, student: Student) -> None:
    """
    Update a student's properties.
    """
    await db.students.update_one({"_id": student_id}, {"$set": student.dict()})


async def delete_student(student_id: str) -> None:
    """
    Delete a student by ID.
    """
    await db.students.delete_one({"_id": student_id})
