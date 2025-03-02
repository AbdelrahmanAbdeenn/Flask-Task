from domain.entities import Student
from repos.base_repo import baseRepo


class StudentRepo(baseRepo[Student]):
    def __init__(self) -> None:
        super().__init__(Student, 'students')
