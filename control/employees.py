



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
