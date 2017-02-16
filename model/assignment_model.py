import sqlite3
from tabulate import tabulate
import os

class AssignmentModel:
    '''
    class for Assignment Model
    '''

    def __init__(self):
        self.conn = sqlite3.connect(os.path.realpath('../ccms.db'))
        self.db = self.conn.cursor()

    def get_list_of_assignments(self):
        '''
        returns list of assignments from DB
        '''
        assignments_list = []
        for item in self.db.execute('''SELECT assignments.assignment_name, assignments.max_points, assignments.due_date, users.name || ' ' || users.surname
                                        FROM assignments, users
                                        WHERE assignments.ID_user = users.ID_user
                                        ORDER BY assignments.due_date DESC'''):
            assignments_list.append(item)
        return assignments_list

    def add_assignment(self, *args):
        '''
        add a new assignment to DB
        '''
        self.db.execute(
            '''INSERT INTO assignments(assignment_name, due_date, max_points, ID_user)
            VALUES ('{}','{}','{}','{}')'''.format(*args))
        self.conn.commit()


