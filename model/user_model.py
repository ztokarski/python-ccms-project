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
            user_object.id_role = user[6]
            user_object.id_team = user[7]

            user_list.append(user_object)
        return user_list


    @classmethod
    def get_object_by_id(self, id):
        conn = sqlite3.connect('ccms.db')
        users = conn.execute("SELECT * FROM users WHERE ID_user == %i" % (int(id)))
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


            return user_object