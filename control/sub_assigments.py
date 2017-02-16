import datetime
from Assigments import *

class Sub_assigment(Assigment):

    def __init__(self, name):
        self.student = student
        self.name == i.name:
        self.sub_assigments.append(self)
        self.due = i.due
        self.date = "{}".format(datetime.date.today())

    def __repr__(self):
        return "{} {}".format(self.name, self.student)

    @classmethod
    def view_submitted_assigments(cls):
        return cls.sub_assigments


    def submit_assigment(self, name, student):
        submitted_assigment = Sub_assigment(name, student)
        return submitted_assigment


dupa = Sub_assigment("dupa", "janusz")
print(str(dupa.date))

