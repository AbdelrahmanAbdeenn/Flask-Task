from typing import Any


class BaseEntity:
    def __init__(self, id: int):
        self.id = id


class Student(BaseEntity):
    age: int
    name: str
    grade: str

    def __init__(self, id: int, name: str, age: int, grade: str) -> None:
        super().__init__(id)
        self.age = age
        self.name = name
        self.grade = grade

    def to_dict(self) -> dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'grade': self.grade
        }
