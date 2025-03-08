from dataclasses import dataclass
from typing import Any


class BaseEntity:
    def __init__(self, id: int):
        self.id = id


@dataclass
class Student(BaseEntity):
    age: int
    name: str
    grade: str

    def __init__(self, id: int, name: str, age: int, grade: str):
        super().__init__(id)
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self) -> dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'grade': self.grade
        }
