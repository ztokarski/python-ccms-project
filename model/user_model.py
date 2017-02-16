import sqlite3
class User_model:
    conn = sqlite3.connect('ccms.db')
    users = conn.execute("SELECT * FROM users")

    @classmethod
    def get_student_and_mentors(cls):
        s_and_m_list = []
        s_and_m = cls.users.execute('SELECT * FROM users WHERE ID_role = 1 OR ID_role = 2')

        for user in s_and_m:
            s_and_m_list.append([user[0], user[1], user[2], user[3], user[7]])

        return s_and_m_list