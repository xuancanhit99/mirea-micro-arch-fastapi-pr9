from pydantic import BaseModel


class CreateStudentModel(BaseModel):
    name: str
    age: str
    math: str
    literature: str
    english: str


class Student:
    def __init__(self, id_, name, age, math, literature, english) -> None:
        self.id = id_
        self.name = name
        self.age = age
        self.math = math
        self.literature = literature
        self.english = english
