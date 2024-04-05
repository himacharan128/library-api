from fastapi import HTTPException
from bson import ObjectId

from app.database import db
from app.models import Student


async def create_student(student: Student) -> str:
    """
    Create a new student record.
    """
    inserted_student = db.students.insert_one(student.dict())
    student_id = str(inserted_student.inserted_id)
    student_data = student.dict()
    student_data["id"] = student_id
    return student_data


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
    student_list = []
    for student in students:
        student_data = student
        student_data["id"] = str(student["_id"])
        student_list.append(student_data)
    return [Student(**student) for student in student_list]

async def get_student_by_id(student_id: str) -> dict:
    """
    Get a student by ID.
    """
    student = db.students.find_one({"_id": ObjectId(student_id)})
    if student:
        student_data = student
        student_data["_id"] = str(student_data["_id"])
        student_data["id"] = student_data.pop("_id")
        return student_data
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