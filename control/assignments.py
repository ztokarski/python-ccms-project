import sqlite3

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
        return cls.assignments_list

    def add_assignment(self):



# ass1 = Assignment("kaszanka", '2017-02-05')
# ass2 = Assignment("pasztet", "2017-02-02")
# print(Assignment.get_assignments_list())


# class Sub_assignment(assignment):
#     sub_assignments = []
#     def __init__(self, name):
#         self.name = name
#         self.student = ""
#         for i in super().assignments_list:
#             if self.name == i.name:
#                 self.sub_assignments.append(self)
#                 self.due = i.due
#
#             else:
#
#                 pass
#         self.date = None
#
#     def __repr__(self):
#         return "{} {} {}".format(self.name, self.due, self.student)
