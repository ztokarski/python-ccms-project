from model.user import *
from db_connection import DB
import sqlite3
import os


class AssignmentModel:

    @classmethod
    def get_assignments_list(cls):
        data = DB.get_connection()
        data.cursor()
        list_of_assignments = []
        assignments = data.execute("SELECT * FROM assignments")
        for assignment in assignments:
            assignment_object = Assignment(assignment[1], assignment[2], assignment[3])
            assignment_object.due_date = assignment[2]
            assignment_object.max_points = assignment[3]
            assignment_object.ID_assignment = assignment[0]
            assignment_object.ID_user = assignment[4]
            list_of_assignments.append(assignment_object)
        data.close()
        return list_of_assignments

    @classmethod
    def add_assignment(cls, assignment):
        """add a new assignment to DB"""
        data = DB.get_connection()
        cursor = data.cursor()
        cursor.execute(
            "INSERT INTO `assignments`(`assignment_name`, `due_date`, `max_points`, `ID_user`) VALUES ('{}','{}','{}','{}')".format(
                assignment.name, assignment.due_date, assignment.max_points, assignment.id_user))
        data.commit()
        data.close()

    @classmethod
    def remove_assignment(cls, ID_assignment):
        """remove assignment from DB"""
        data = DB.get_connection()
        cursor = data.cursor()
        cursor.execute("DELETE FROM assignments where ID_assignment = {}".format(ID_assignment))
        data.commit()
        data.close()

    @classmethod
    def edit_assignment(cls, assignment):
        """edit assignment in DB"""
        data = DB.get_connection()
        cursor = data.cursor()
        cursor.execute("UPDATE assignments SET assignment_name = ?, due_date = ?, max_points = ? WHERE ID_assignment = ?", (assignment.name, assignment.due_date, assignment.max_points, assignment.id))
        # cursor.execute("UPDATE assignments SET assignment_name = ? WHERE ID_assignment = ?",
                       # (assignment.name, assignment.id))
        data.commit()
        data.close()


    @classmethod
    def get_object_id(cls, id):
        data = DB.get_connection()
        cursor = data.cursor()
        assignments = cursor.execute("SELECT * FROM assignments WHERE ID_assignment == %i" % (int(id)))
        for assignment in assignments:
            name = assignment[1]
            due_date = assignment[2]
            max_points = assignment[3]
            assignment_object = Assignment(name, due_date, max_points)
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
