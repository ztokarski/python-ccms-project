import sqlite3
from user_model import *


class Assigment:

    def __init__(self, name):
        self.id = 0
        self.name = name
        self.due = 0
        self.max_points = 0



    def __repr__(self):
        return "{} {}".format(self.name, self.due)

    @classmethod
    def get_object_id(cls, id):
        conn = sqlite3.connect('/home/lukasz/PycharmProjects/ccm/python-ccms-programadores/ccms.db')
        assignments = conn.execute("SELECT * FROM assignments WHERE ID_assignment == %i" % (int(id)))
        for assignment in assignments:
            name = assignment[1]
            assignment_object = Assigment(name)
            assignment_object.due = assignment[2]
            assignment_object.max_points = assignment[3]

        return assignment_object

    @classmethod
    def get_all(cls):
        ass_list = []
        conn = sqlite3.connect('/home/lukasz/PycharmProjects/ccm/python-ccms-programadores/ccms.db')
        assignments = conn.execute("SELECT * FROM assignments")
        for assignment in assignments:
            name = assignment[1]

            object = Assigment(name)
            object.due = assignment[2]
            object.max_points = assignment[3]
            object.id = assignment[0]
            ass_list.append(object)

        return ass_list

print(Assigment.get_all())


