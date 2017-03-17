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
    def get_all_assignment(cls):
        assignment_list = []
        db_list = cls.conn.execute("SELECT * FROM assignments")
        for assignment in db_list:
            assignment_name = assignment[1]
            due_date = assignment[2]
            max_points = assignment[3]
            assignment_object = Assignment(assignment_name, due_date, max_points)
            assignment_object.ID_assignment = assignment[0]
            assignment_object.ID_user = assignment[4]
            assignment_list.append(assignment_object)
        return assignment_list

    @classmethod
    def get_object_by_id(cls, id):
        conn = sqlite3.connect('ccms.db')
        users = conn.execute("SELECT * FROM users WHERE ID_user == %i" % (int(id)))
        user_object = User("a", "b")
        for user in users:
            name = user[1]
            surname = user[2]
            user_object = User(name, surname)
            user_object.id = user[0]
            user_object.login = user[3]
            user_object.password = user[4]
            user_object.status = user[5]
            user_object.id_team = user[6]
            user_object.id_role = user[7]

        return user_object

    @classmethod
    def get_assignment_by_id(cls, assignment_id):
        conn = sqlite3.connect('ccms.db')
        assignments = conn.execute("SELECT * FROM assignments WHERE ID_assignment == %i" % (int(assignment_id)))
        assignment_object = None
        for assignment in assignments:
            assignment_name = assignment[1]
            due_date = assignment[2]
            max_points = assignment[3]
            assignment_object = Assignment(assignment_name, due_date, max_points)
            assignment_object.ID_assignment = assignment[0]
            assignment_object.ID_user = assignment[4]
        return assignment_object
