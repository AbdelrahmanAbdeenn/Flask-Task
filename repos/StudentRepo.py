from entities.Entities import Student
from repos.baseRepo import baseRepo


class StudentRepo(baseRepo[Student]):
    def __init__(self) -> None:
        super().__init__(Student, 'students')
