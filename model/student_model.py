from model.user_model import *
import sqlite3


class Student_model(User_model):

    @classmethod
    def get_all_students(cls):
        list_of_students = []
        students = cls.conn.execute("SELECT * FROM users WHERE ID_role = `1`")

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
            list_of_students.append(student_object)

        return list_of_students


    # def show_grades(self):
    #     '''
    #     Method which return student's grades.
    #     '''
    #     from_grades = Open().open_users("CSV/sub_assignments.csv")
    #     grades = {}
    #     for assigment in subs_assigment:
    #         if assigment.grade != None:
    #             grades[assigment.name] = assigment.grade
    #
    #     return grades