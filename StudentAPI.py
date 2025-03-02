from typing import Any, Optional

from flask import jsonify, request
from flask.views import MethodView

from entities.Entities import Student
from repos.StudentRepo import StudentRepo


class StudentAPI(MethodView):
    def get(self, id: Optional[int] = None) -> Any:
        try:
            studentRepo = StudentRepo()
            if id is None:
                students = studentRepo.get_all()
                return list([student.to_dict()] for student in students)
            else:
                student = studentRepo.get_by_id(id)
                if student is None:
                    return jsonify("Student not found"), 404
                else:
                    return jsonify(student.to_dict())
        except Exception as e:
            return jsonify(str(e))

    def post(self) -> Any:
        try:
            data = request.get_json()
            student = Student(data['id'], data['name'], data['age'], data['grade'])
            studentRepo = StudentRepo()
            exists = studentRepo.get_by_id(data['id'])
            if exists:
                return jsonify("Student already exists"), 400
            st = studentRepo.insert(student)
            return jsonify(st.to_dict())
        except Exception as e:
            return jsonify(str(e))

    def put(self, id: int) -> Any:
        try:
            data = request.get_json()
            studentRepo = StudentRepo()
            student = studentRepo.get_by_id(id)
            if student is None:
                return jsonify("Student not found"), 404
            student.name = data['name']
            student.age = data['age']
            student.grade = data['grade']
            studentRepo.update(id, data)
            return jsonify(student.to_dict())
        except Exception as e:
            return jsonify(str(e))

    def delete(self, id: int) -> Any:
        try:
            studentRepo = StudentRepo()
            student = studentRepo.get_by_id(id)
            if student is None:
                return jsonify("Student not found"), 404
            studentRepo.delete(id)
            return jsonify("Student deleted")
        except Exception as e:
            return jsonify(str(e))
