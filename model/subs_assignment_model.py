from model.assignments_model import *
from control.sub_assigment import *
import datetime
import sqlite3

class Submitted_assignments_model:
    conn = sqlite3.connect('ccms.db')
    cursor = conn.cursor()

    def save_assigment(self, object):
        if object.date == None:
            object.date = datetime.datetime()

        self.cursor.execute("INSERT INTO subs_asignment VALUES ('{}', '{}', '{}', '{}').format(object.date, object.grade, object.id_assignment, object.id_user)")
        self.conn.commit()