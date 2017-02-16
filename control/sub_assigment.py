from assignment import Assignment


class Sub_assignment(Assignment):

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