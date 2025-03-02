from typing import Any, Optional

from flask import jsonify, request
from flask.views import MethodView

from application.student_service import StudentService


class StudentAPI(MethodView):
    def __init__(self) -> None:
        self.student_service = StudentService()

    def get(self, id: Optional[int] = None) -> Any:
        return self.student_service.get_student(id)

    def post(self) -> Any:
        return self.student_service.create_student(request.get_json())

    def put(self, id: int) -> Any:
        return self.student_service.update_student(id, request.get_json())
        

    def delete(self, id: int) -> Any:
        return self.student_service.delete_student(id)
