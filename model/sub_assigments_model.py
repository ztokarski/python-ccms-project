import sqlite3
from Assigments import *
import datetime

class Sub_assigment_model:


    sub_assigments = []

    def __init__(self, name, student):
        self.student = student
        for i in super().assigments_list:
            if self.name == i.name:
                self.sub_assigments.append(self)
                self.due = i.due

            else:

                pass
        self.date = "{}".format(datetime.date.today())

    def __repr__(self):
        return "{} {}".format(self.name, self.student)
    @classmethod
    def get_all_subs(cls):
        conn = sqlite3.connect('ccms.db')
        assigmnets = conn.execute("SELECT * FROM sub_assignments")
        for assigmnet in assigmnets:

    submit_assigment(name)

    @classmethod
    def view_submitted_assigments(cls):

        return cls.sub_assigments

    def submit_assigment(self, name, student):
        submitted_assigment = Sub_assigment(name, student)
        return submitted_assigment

    conn = sqlite3.connect('ccms.db')
    cur = conn.cursor()

    @classmethod
    def sub_assigments_list(cls):
        sub_assigments_db = cls.cur.execute("SELECT * FROM sub_assignments")
        for sub in sub_assigments_db:
            print(sub)
        return sub_assigments_db



CREATE TABLE `sub_assignments` (
	`ID_sub_assignment`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`sub_date`	INTEGER NOT NULL,
	`grade`	INTEGER,
	`ID_assignment`	INTEGER NOT NULL,
	`ID_user`	INTEGER NOT NULL
)