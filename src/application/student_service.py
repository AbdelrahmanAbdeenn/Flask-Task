
from typing import Any, List, Optional

from flask import jsonify

from domain.entities import Student
from repos.student_repo import StudentRepo


class StudentService:
    def __init__(self) -> None:
        self.studentRepo = StudentRepo()

    def get_student(self,id: Optional[int])-> Any:
        try:
            if id is None:
                students = self.studentRepo.get_all()
                return list([student.to_dict()] for student in students)
            else:
                student = self.studentRepo.get_by_id(id)
                if student is None:
                    return jsonify("Student not found"), 404
                else:
                    return jsonify(student.to_dict())
        except Exception as e:
            return jsonify(str(e))

    def create_student(self,data: Any) -> Any:
        try:
            student = Student(data['id'], data['name'], data['age'], data['grade'])
            exists = self.studentRepo.get_by_id(data['id'])
            if exists:
                return jsonify("Student already exists"), 400
            st = self.studentRepo.insert(student)
            return jsonify(st.to_dict())
        except Exception as e:
            return jsonify(str(e))


    def update_student(self,id: int, data: dict[str, Any]) -> Any:
        try:
            student = self.studentRepo.get_by_id(id)
            if student is None:
                return jsonify("Student not found"), 404
            student.name = data['name']
            student.age = data['age']
            student.grade = data['grade']
            self.studentRepo.update(id, data)
            return jsonify(student.to_dict())
        except Exception as e:
            return jsonify(str(e))

    def delete_student(self, id: int) -> Any:
        try:
            student = self.studentRepo.get_by_id(id)
            if student is None:
                return jsonify("Student not found"), 404
            self.studentRepo.delete(id)
            return jsonify("Student deleted")
        except Exception as e:
            return jsonify(str(e))