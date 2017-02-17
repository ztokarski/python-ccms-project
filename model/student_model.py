import sqlite3
from model.user_model import *
import os
from tabulate import tabulate
from sqlite3 import OperationalError


class StudentModel(User_model):
    conn = sqlite3.connect(os.path.realpath('ccms.db'))





class StudentModel(User_model):
    conn = sqlite3.connect('ccms.db')
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

    def add_student(self, name, surname, login):
        self.conn.execute("INSERT INTO `users`(`name`,`surname`,`login`) VALUES ('{}','{}','{}');".format(name, surname, login))
        self.conn.commit()

    def remove_student(self, student_id):
        try:
            self.conn.execute("DELETE FROM users where ID_user = {} and ID_role = 1".format(student_id))
            self.conn.commit()
        except OperationalError:
            print("Cannot remove")
