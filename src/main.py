from flask import Flask

from presentation.student_api import StudentAPI

app = Flask("__name__")

if __name__ == "__main__":
    student_view = StudentAPI.as_view('student_api')
    app.add_url_rule('/student', view_func=student_view, methods=['GET', 'POST'])
    app.add_url_rule('/student/<int:id>', view_func=student_view, methods=['GET', 'PUT', 'DELETE'])
    app.run(debug=True)
