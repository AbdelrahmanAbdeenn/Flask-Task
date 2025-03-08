from src.database.schema import students
from src.domain.entities import Student
from src.repos.base_repo import BaseRepo


class StudentRepo(BaseRepo[Student]):
    def __init__(self) -> None:
        super().__init__(Student, 'students', students)
