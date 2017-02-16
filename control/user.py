

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
        self.list_of_users.append(self)

    def __str__(self):
        return "{} {} {} {}".format(self.name, self.surname)

    def change_status(self):
        '''
        change user's status (Activ/Disactiv)
        '''
        self.status = not self.status

    def display_status(self):
        if self.status == True:
            return("Activ")
        else:
            return("Disactiv")