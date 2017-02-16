import sqlite3
import datetime
from assignments_model import *
from user_model import *

class Sub_assigment_model:

    def __init__(self, assigment_id, student_id):
        self.assiment_id = assigment_id
        self.student_id = student_id
        self.student = User_model.get_object_by_id(student_id)
        self.task = Assigment.get_object_id(assigment_id)
        self.due = ""
        self.date = "{}".format(datetime.date.today())


    def __repr__(self):
        return "{} {}".format(self.task, self.student)

    @classmethod
    def view_my_subs_assignments(cls, student_id):
        conn = sqlite3.connect('/home/lukasz/PycharmProjects/ccm/python-ccms-programadores/ccms.db')
        db_list = conn.execute("SELECT id_assignment, id_user FROM sub_assignments")
        return_list = []
        for ass in db_list:
            if ass[1] == student_id:
                pos = Sub_assigment_model(ass[0], ass[1])
                return_list.append(pos)

        return return_list




    def submit_assigment(self):
        conn = sqlite3.connect('/home/lukasz/PycharmProjects/ccm/python-ccms-programadores/ccms.db')
        conn.execute("INSERT INTO sub_assignments (sub_date, grade, ID_assignment, ID_user) VALUES (%i, %i, %i, %i)" % (0, 0, self.student.id, self.task.id))




print(Sub_assigment_model.view_my_subs_assignments(2))
