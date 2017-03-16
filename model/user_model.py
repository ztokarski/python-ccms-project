from model.user import *
from db_connection import DB

class User_model:

    @classmethod
    def get_all_users(cls):
        user_list = []
        database = DB.get_connection()
        db_list = database.execute("SELECT * FROM users")
        for user in db_list:
            name = user[1]
            surname = user[2]
            user_object = User(name, surname)
            user_object.id = user[0]
            user_object.login = user[3]
            user_object.password = user[4]
            user_object.status = user[5]
            user_object.id_role = user[6]
            user_object.id_team = user[7]

            user_list.append(user_object)
        return user_list

    @classmethod
    def get_id_from_login(cls, user_login):
        database = DB.get_connection()
        id_db = database.execute("SELECT ID_user FROM users WHERE login = ?", (user_login,))
        user_id = id_db.fetchone()

        return user_id[0]


    @classmethod
    def get_object_by_id(cls, id):
        database = DB.get_connection()
        users = database.execute("SELECT * FROM users WHERE ID_user = ?", (int(id),))
        for user in users:
            if user[7] == 1:
                user_object =Student(user[1], [user[2]])
            elif user[7] == 2:
                user_object = Mentor(user[1], user[2])
            elif user[7] == 3:
                user_object = Employee(user[1], user[2])
            else:
                user_object = Manager(user[1], user[2])

            user_object.id = user[0]
            user_object.login = user[3]
            user_object.password = user[4]
            user_object.status = user[5]
            user_object.id_team = user[6]
            user_object.id_role = user[7]

            database.close()

            return user_object