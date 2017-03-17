
class User:

    '''
    Class for user.
    '''

    def __init__(self, name, surname):
        self.id = 0
        self.name = name
        self.surname = surname
        self.login = None
        self.password = None
        self.status = 1
        self.id_role = 0
        self.id_team = 0

    def __repr__(self):
        return "ID: {} Name: {} Surname {} Status: {}".format(self.id, self.name, self.surname, self.status)


class Student(User):

    '''
    Class for student.
    '''
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.team = None
        self.grades_list = []

    def __str__(self):
        return "{} {} {} {} {}\n".format(self.name, self.surname, self.login, self.password, self.status)



class Mentor(User):

    def __init__(self, name, surname):
        super().__init__(name, surname)

class Manager(User):
    '''
    Class for Manager.
    '''
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return "{}".format("BOSKI JUREK")


class Employee(User):
    def __init__(self, name, surname):
        super().__init__(name, surname)


class Assignment:
    def __init__(self, assignment_name, due_date, max_points):
        self.ID_assignment = 0
        self.assignment_name = assignment_name
        self.due_date = due_date
        self.max_points = max_points
        self.ID_user = 0


