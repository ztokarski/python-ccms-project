import sqlite3
class User_model:
    list_of_users = []
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

    @classmethod
    def get_all_users(cls):
        conn = sqlite3.connect('ccms.db')
        users = conn.execute("SELECT * FROM users")
        for user in users:
            name = user[1]
            surname = user[2]
            user_object = User_model(name, surname)
            user_object.id = user[0]
            user_object.login = user[3]
            user_object.password = user[4]
            user_object.status = user[5]
            user_object.id_team = user[6]
            user_object.id_role = user[7]
            cls.list_of_users.append(user_object)
    @classmethod
    def get_name_by_id(self, id):
        conn = sqlite3.connect('ccms.db')
        users = conn.execute("SELECT ID_User, name, surname FROM users WHERE ID_User == %s" % (id))
        return users



    def change_status(self):
        '''
        change user's status (Activ/Disactiv)
        '''
        self.status = not self.status

    def display_status(self):
        if self.status == True:
            return ("Activ")
        else:
            return ("Disactiv")

print(User_model.get_name_by_id(1))
