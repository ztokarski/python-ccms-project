import sqlite3
from tabulate import tabulate
from model.assignment_model import *

class Assignment:
    """
    Class for assignment.
    """
    assignments_list = []
    def __init__(self, name):
        self.name = name
        self.id = id_assignment
        self.due = due_date
        self.points = max_points
        self.mentor = mentor_id

        self.assignments_list.append(self)

    def __repr__(self):
        return "{} {} {}".format(self.name, self.due, self.points)

    @classmethod
    def get_assignments_list(cls):
        """
        Method return assignments_list
        """
        model = AssignmentModel()
        as_list = model.get_list_of_assignments()
        return tabulate(as_list, headers=['Name', 'Max.Points', 'Due Date', 'Created by'], tablefmt='fancy_grid',
                   stralign='center')

    def add_assignment(self):
        """
        Method add assignments to DB
        """
        pass

