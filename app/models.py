from typing import Optional

from pydantic import BaseModel

class Address(BaseModel):
    city: str
    country: str

class Student(BaseModel):
    name: str
    age: int
    address: Address

class StudentResponse(BaseModel):
    name: str
    age: int
