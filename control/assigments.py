import sqlite3

class Assignment:
    assigments_list = []

    def __init__(self, name, due):
        self.name = name
        self.due = due
        self.assigments_list.append(self)

    def __repr__(self):
        return "{} {}".format(self.name, self.due)


