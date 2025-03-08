from src.application.base_service import BaseService
from src.database.unit_of_work import UnitOfWork
from src.domain.entities import Student
from src.repos.student_repo import StudentRepo


class StudentService(BaseService[Student]):
    def __init__(self) -> None:
        uow = UnitOfWork()
        super().__init__(StudentRepo(), uow)
