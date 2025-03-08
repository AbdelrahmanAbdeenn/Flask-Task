from src.repos.student_repo import StudentRepo
from src.application.base_service import BaseService
from src.domain.entities import Student
from src.database.unit_of_work import UnitOfWork
class StudentService(BaseService[Student]):
    def __init__(self) -> None:
        uow = UnitOfWork()
        super().__init__(StudentRepo(),uow)
