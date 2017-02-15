import sqlite3

class Assigment:
    assigments_list = []
    def __init__(self, name, due):
        self.name = name
        self.due = due
        self.assigments_list.append(self)

    def __repr__(self):
        return "{} {}".format(self.name, self.due)


class Sub_assigment(Assigment):
    sub_assigments = []
    def __init__(self, name):
        self.name = name
        self.student = ""
        for i in super().assigments_list:
            if self.name == i.name:
                self.sub_assigments.append(self)
                self.due = i.due

            else:

                pass
        self.date = None

    def __repr__(self):
        return "{} {} {}".format(self.name, self.due, self.student)
