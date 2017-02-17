import sqlite3
from model.user_model import *
import os



class StudentModel(User_model):
    conn = sqlite3.connect(os.path.realpath('ccms.db'))
    cursor = conn.cursor()

    @classmethod
    def get_all_students(cls):
        list_of_students = []
        students = cls.conn.execute("SELECT * FROM users "
                                    "WHERE ID_role = 1 ")

        for student in students:
            name = student[1]
            surname = student[2]
            student_object = Student(name, surname)
            student_object.id = student[0]
            student_object.login = student[3]
            student_object.password = student[4]
            student_object.status = student[5]
            student_object.id_team = student[6]
            student_object.id_role = student[7]
            list_object= []
            list_object.append(student_object)
            list_of_students.append(list_object)

        return list_of_students


    @classmethod
    def show_student_list(cls):
        students = Mentor.get_mentors_list()
        return tabulate(students, headers=['ID', 'NAME', 'SURNAME'], tablefmt='fancy_grid',stralign='center')



    # @staticmethod
    # def add_student(cls, *args):
    #     model = StudentModel()
    #     model.add_student(args)

    # @classmethod
    # def add_student(self, ID, name, surname, login, password, status, ID_role, ID_team):
    #     values = {'ID_user': ID, 'name': name, 'surname': surname, 'login': login, 'password': password, 'status': status, 'ID_role': ID_role,'ID_team':ID_team}


