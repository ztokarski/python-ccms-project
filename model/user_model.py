import sqlite3
from model.user import *
class User_model:
    conn = sqlite3.connect('ccms.db')
    cursor = conn.cursor()

    @classmethod
    def get_all_users(cls):
        user_list = []
        db_list = cls.conn.execute("SELECT * FROM users")
        for user in db_list:
            name = user[1]
            surname = user[2]
            user_object = User(name, surname)
            user_object.id = user[0]
            user_object.login = user[3]
            user_object.password = user[4]
            user_object.status = user[5]
            user_object.id_team = user[6]
            user_object.id_role = user[7]
            user_list.append(user_object)

        return user_list


    @classmethod
    def get_object_by_id(self, id):
        conn = sqlite3.connect('/home/lukasz/PycharmProjects/ccm/python-ccms-programadores/ccms.db')
        users = conn.execute("SELECT * FROM users WHERE ID_user == %i" % (int(id)))
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

        return user_object