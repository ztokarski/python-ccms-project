from control.user import User
from model.student_model import StudentModel
from tabulate import tabulate

class StudentControl:

    @staticmethod
    def add_student(name, surname, login):
        model = StudentModel()
        model.add_student(name, surname, login)

    @staticmethod
    def remove_student(student_id):
        model = StudentModel()
        model.remove_student(student_id)