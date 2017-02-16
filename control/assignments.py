import sqlite3
from tabulate import tabulate
from model.assignment_model import *

class Assignment:
    """
    Class for assignment.
    """
    assignments_list = []
    def __init__(self, name, due_date):
        self.name = name
        self.due = due_date
        self.assignments_list.append(self)

    def __repr__(self):
        return "{} {}".format(self.name, self.due)

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





# ass1 = Assignment("kaszanka", '2017-02-05')
# ass2 = Assignment("pasztet", "2017-02-02")
# print(Assignment.get_assignments_list())

print(Assignment.get_assignments_list())