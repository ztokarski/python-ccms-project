from model.user import *

import sqlite3
import os

class AssignmentModel():

    conn = sqlite3.connect(os.path.realpath('ccms.db'))

    cursor = conn.cursor()


    def __init__(self, name, due):
        self.name = name
        self.due = due

    def __repr__(self):

     return "{} {}".format(self.name, self.due)


    @classmethod
    def get_assignments_list(cls):
        assignment_list = []
        assignments = cls.conn.execute("SELECT * FROM assignments")
        for assignment in assignments:
            name = assignment[1]
            object = Assignment(name)
            object.due = assignment[2]
            object.max_points = assignment[3]
            object.id = assignment[0]
            assignment_list.append(object)

        return assignment_list




    def add_assignment(self, *args):
        '''
        add a new assignment to DB
        '''
        self.conn.execute(
            '''INSERT INTO assignments(assignment_name, due_date, max_points, ID_user)
            VALUES ('{}','{}','{}','{}')'''.format(*args))
        self.conn.commit()



    @classmethod
    def get_object_id(cls, id):
        conn = sqlite3.connect('ccms.db')
        assignments = conn.execute("SELECT * FROM assignments WHERE ID_assignment == %i" % (int(id)))
        for assignment in assignments:
            name = assignment[1]
            assignment_object = Assignment(name)
            assignment_object.due = assignment[2]
            assignment_object.max_points = assignment[3]

        return assignment_object


class Sub_assignment(AssignmentModel):


    def __init__(self, name):
        self.name = name
        self.student = ""
        self.due = None
        self.date = None
        self.grade = 0


    def __repr__(self):
        return "{} {} {}".format(self.name, self.due, self.student)
